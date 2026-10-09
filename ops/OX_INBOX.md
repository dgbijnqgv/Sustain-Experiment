# Ox inbox

`ops/ox-inbox.json` holds tasks for Ox, the agent app on the owner's phone, which is
logged into the owner's Reddit account. An Ox scheduled skill reads the file at
https://raw.githubusercontent.com/dgbijnqgv/Sustain-Experiment/claude/ai-revenue-generation-ume6vn/ops/ox-inbox.json
once a day. It runs every task whose `not_before` has passed and whose `id` it hasn't
done yet, then notifies the owner with the resulting links.

iOS decides when background runs happen, so expect a task within about a day of its
`not_before`, not at an exact minute.

## Adding a task (Claude sessions)

Append to `tasks`. Never edit or reuse the `id` of a task that already ran.

```json
{
  "id": "2026-10-27-indiegames",
  "not_before": "2026-10-27T04:30:00-07:00",
  "action": "reddit_post",
  "subreddit": "indiegames",
  "kind": "link",
  "url": "https://shiteven.fun",
  "title": "...",
  "body": "",
  "first_comment": "..."
}
```

- `kind` is `link` (uses `url`), `text` (uses `body`) or `video` (uses `video_url`).
  Video tasks wait until the clip exists: Ox skips them, without marking them done,
  while `video_url` returns 404. Use `reddit_comment` with a
  `thread_url` to comment in a thread.
- Rules: one post per subreddit per month, spaced at least two days apart. Check the
  subreddit's self-promotion rules in the task notes. Never ask for upvotes.

## Clips

The owner's Codex clipping agent commits finished clips to `ops/clips/` on this branch.
Video tasks point at the clip's raw URL there, so a task can be queued before its clip
exists. Keep clips under 25 MB, 15–30 s, MP4.

Waiting on: `ops/clips/septic-lord.mp4` (Septic Lord fight with resurrect and pickup
healing) for task `2026-10-15-indiegames-video`.
