"""Offline tests for mc.py (Metaculus client mocked)."""
import io
import json
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from datetime import datetime, timezone
from types import SimpleNamespace
from unittest import mock

os.environ.setdefault("METACULUS_TOKEN", "test-token")
import mc  # noqa: E402
from forecasting_tools import BinaryQuestion, DateQuestion, MultipleChoiceQuestion, NumericQuestion  # noqa: E402


def write(obj) -> str:
    f = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False)
    json.dump(obj, f)
    f.close()
    return f.name


BIN = BinaryQuestion(question_text="b?", id_of_post=1, id_of_question=11, page_url="u1")
MCQ = MultipleChoiceQuestion(question_text="m?", id_of_post=2, id_of_question=22, page_url="u2", options=["A", "B", "C"])
NUM = NumericQuestion(question_text="n?", id_of_post=3, id_of_question=33, page_url="u3", lower_bound=0, upper_bound=100,
                      open_lower_bound=False, open_upper_bound=True)
DATE = DateQuestion(question_text="d?", id_of_post=4, id_of_question=44, page_url="u4",
                    lower_bound=datetime(2026, 10, 1, tzinfo=timezone.utc), upper_bound=datetime(2027, 6, 1, tzinfo=timezone.utc),
                    open_lower_bound=False, open_upper_bound=True)


class AggregateTest(unittest.TestCase):
    def test_binary_median_and_clip(self):
        fs = [{"post_id": 1, "question_id": 11, "type": "binary", "probability": p, "comment": "c"} for p in (0.01, 0.02, 0.5)]
        out = mc.normalize(mc.aggregate(fs))
        self.assertAlmostEqual(out["probability"], 0.03)
        self.assertIn("median of 3", out["comment"])

    def test_mc_mean_floor_and_renormalize(self):
        fs = [{"post_id": 2, "question_id": 22, "type": "multiple_choice", "probabilities": {"A": 1.0, "B": 0.0, "C": 0.0}, "comment": "c"}] * 2
        out = mc.normalize(mc.aggregate(fs))
        self.assertAlmostEqual(sum(out["probabilities"].values()), 1.0)
        self.assertGreater(out["probabilities"]["B"], 0.0)

    def test_numeric_percentile_median(self):
        fs = [{"post_id": 3, "question_id": 33, "type": "numeric", "percentiles": {"10": a, "50": b, "90": c}, "comment": "c"}
              for a, b, c in ((10, 20, 30), (12, 25, 40), (8, 22, 35))]
        self.assertEqual(mc.aggregate(fs)["percentiles"], {"10": 10.0, "50": 22.0, "90": 35.0})

    def test_mixed_questions_rejected(self):
        with self.assertRaises(ValueError):
            mc.aggregate([{"post_id": 1, "type": "binary", "question_id": 1}, {"post_id": 2, "type": "binary", "question_id": 2}])

    def test_validation(self):
        with self.assertRaises(ValueError):
            mc.normalize({"type": "binary", "probability": 0.5, "comment": " "})
        with self.assertRaises(ValueError):
            mc.normalize({"type": "numeric", "percentiles": {"10": 5, "50": 5, "90": 9}, "comment": "c"})


class CoverageTest(unittest.TestCase):
    def test_counts_only(self):
        t = lambda d: datetime(2026, 10, d, tzinfo=timezone.utc)
        qs = [SimpleNamespace(already_forecasted=f, state=SimpleNamespace(value=st), open_time=t(d))
              for f, st, d in ((False, "resolved", 1), (True, "open", 12), (False, "closed", 11),
                               (True, "resolved", 10), (True, "closed", 13))]
        client = mock.MagicMock()
        client.get_questions_matching_filter = mock.AsyncMock(return_value=qs)
        with mock.patch("forecasting_tools.MetaculusClient", return_value=client), redirect_stdout(io.StringIO()) as out:
            mc.cmd_coverage(SimpleNamespace(tournament="main"))
        result = json.loads(out.getvalue())
        # The question from before the bot's first answer (Oct 1) is excluded.
        self.assertEqual((result["questions"], result["answered"], result["coverage"]), (4, 3, 0.75))
        self.assertEqual(result["by_state"]["closed:missed"], 1)
        self.assertNotIn("probability", out.getvalue())


class SubmitTest(unittest.TestCase):
    def submit(self, question, forecast, dry_run=False):
        client = mock.MagicMock()
        client.get_question_by_post_id.return_value = question
        with mock.patch("forecasting_tools.MetaculusClient", return_value=client), redirect_stdout(io.StringIO()) as out:
            mc.cmd_submit(SimpleNamespace(file=write(forecast), dry_run=dry_run))
        return client, out.getvalue()

    def test_binary_posts_prediction_and_comment(self):
        client, out = self.submit(BIN, {"post_id": 1, "question_id": 11, "type": "binary", "probability": 0.999, "comment": "why"})
        client.post_binary_question_prediction.assert_called_once_with(11, 0.97)
        client.post_question_comment.assert_called_once_with(1, "why")
        self.assertIn("SUBMITTED", out)

    def test_dry_run_posts_nothing(self):
        client, out = self.submit(BIN, {"post_id": 1, "question_id": 11, "type": "binary", "probability": 0.4, "comment": "why"}, dry_run=True)
        client.post_binary_question_prediction.assert_not_called()
        client.post_question_comment.assert_not_called()

    def test_mc_requires_all_options(self):
        with self.assertRaises(ValueError):
            self.submit(MCQ, {"post_id": 2, "question_id": 22, "type": "multiple_choice", "probabilities": {"A": 0.5, "B": 0.5}, "comment": "c"})

    def test_numeric_cdf_is_valid(self):
        client, _ = self.submit(NUM, {"post_id": 3, "question_id": 33, "type": "numeric",
                                      "percentiles": {"5": 10, "25": 30, "50": 45, "75": 60, "95": 85}, "comment": "c"})
        cdf = client.post_numeric_question_prediction.call_args[0][1]
        self.assertEqual(len(cdf), 201)
        self.assertTrue(all(a <= b for a, b in zip(cdf, cdf[1:])))
        self.assertEqual(cdf[0], 0.0)  # closed lower bound

    def test_date_cdf_is_valid(self):
        client, _ = self.submit(DATE, {"post_id": 4, "question_id": 44, "type": "date",
                                       "percentiles": {"10": "2026-11-15", "50": "2027-01-20", "90": "2027-05-01"}, "comment": "c"})
        cdf = client.post_numeric_question_prediction.call_args[0][1]
        self.assertEqual(len(cdf), 201)

    def test_mismatched_file_rejected(self):
        with self.assertRaises(ValueError):
            self.submit(BIN, {"post_id": 1, "question_id": 99, "type": "binary", "probability": 0.4, "comment": "c"})


if __name__ == "__main__":
    unittest.main()
