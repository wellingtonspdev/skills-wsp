# Handoff to the new orchestrator

1. Archive the previous Traycer orchestrator agent.
2. Start a fresh Codex session in the same project and Epic.
3. Load `model-orchestrator` v3.0.0 from zero.
4. Read current project state and preserved Task/Spec/Ticket/Story/Review plus JSON/Markdown artifacts.
5. Do not repeat completed work or reuse architectural interpretations that conflict with v3.
6. Run preflight and runtime capability discovery before project reads or delegation.
7. Perform a separate controlled real child-agent test before declaring external delegation operational.
8. Keep OpenCode as every external worker harness; treat OpenRouter only as the DeepSeek/Laguna provider.