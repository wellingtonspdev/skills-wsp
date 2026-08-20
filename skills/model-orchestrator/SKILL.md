---
name: model-orchestrator
description: "Operate Traycer-led Codex orchestration with mandatory worktree, privacy, budget, capability-discovery, OpenCode worker, artifact-handoff, conflict, and independent-review gates. Use when planning, routing, delegating, reviewing, or integrating work across Codex, OpenCode, MiMo, DeepSeek, or Laguna."
---

# Model orchestrator v3.0.0

Act as the control plane. Treat Traycer as coordinator, Codex plus GPT models as orchestrator/reviewer/integrator, OpenCode as the only external development-worker harness, and OpenRouter only as provider for DeepSeek and Laguna.

## Mandatory order

1. Validate the absolute active `config/orchestrator.json` and run `preflight.py` before project reads or commands.
2. Run `capability_discovery.py` against the installed Traycer runtime. Never infer CLI features from documentation alone.
3. Read GSD planning, decompose into Task/Spec/Ticket/Story objects, and classify risk, complexity, sensitivity, reversibility, scope, external access, and review need.
4. Run `detect_conflicts.py`. Do not parallelize tasks sharing any allowed file or conflicting area.
5. Run `choose_route.py`. Keep architecture, authentication, authorization, security, migration, sensitive-data, deadline-calculation, concurrency, idempotency, cross-cutting, high/critical-risk, or unsanitizable work in Codex.
6. For an external route, force `harness=opencode`. Select MiMo for simple sanitized low-risk local work; DeepSeek as the paid default for bounded implementation; Laguna for terminal/tool/navigation/test-loop intensive work. OpenRouter is never a harness or agent.
7. Run `select_protocol.py` with the capability matrix. Use `gui_chat` for iterative communication and `terminal_tui` for launch-once autonomous work. Block A2A after TUI launch.
8. Sanitize, validate scope/worktree, validate budget, create the complete contract, then create/request the child through Traycer. Do not create children without verified parent and Epic identities.
9. Require durable artifacts. TUI requires `HANDOFF.md` and `STATUS.json`; collect transcript, artifacts, and Git diff. Conversation history alone is insufficient.
10. Require independent Codex review and objective validation before integration. Never let an executor approve itself.

## Authority

Apply priority: `model-orchestrator` > GSD > Context7 > Context7 Auto Research. This skill owns security, privacy, worktree, agents, models, budget, delegation, parallelization, review, and approval. GSD organizes phases; Context7 supplies current technical documentation. Auxiliary skills cannot relax gates.

## Identity

Record `agent_id`, `display_name`, `parent_agent_id`, `epic_id`, `harness`, `surface`, `requested_model`, `effective_model`, `identity_status`, `worktree`, `task_id`, and `reviewer_agent_id` separately. Never derive an ID from a display name. Use `null` plus `unverified` when proof is absent, and block hierarchy-dependent steps.

## Resources

Read `references/definitive-architecture.md` for roles and worker selection, `references/surface-protocols.md` for GUI/TUI behavior, `references/capability-matrix.md` for discovery fields, and `references/new-orchestrator-handoff.md` when rotating the orchestrator session. Continue applying all privacy, risk, provider, escalation, compatibility, and pipeline references already bundled.