# OpenCode surface protocols

## GUI or Chat

Use for iterative Codex-worker communication. Require runtime-confirmed surface availability and A2A support. Enable transcripts and artifacts. Flow: create agent, send contract, execute, receive handoff, independent Codex review.

## Terminal or TUI

Use only when the complete contract can be supplied at launch. Never send later A2A messages. Supply context through initial prompt, Ticket, or contract file. Require `HANDOFF.md` and `STATUS.json`; retrieve transcript, artifacts, and Git diff.

Fail before launch if the selected protocol requires an unsupported capability. Fail any post-launch A2A attempt on TUI.