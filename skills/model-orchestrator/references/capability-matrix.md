# Runtime capability matrix

Generate the matrix with `scripts/capability_discovery.py`. Record Traycer version, executed argv probes, harness availability, models, surfaces, A2A per surface, agent creation, transcript, worktree creation, identity sources, and Epic sources. A documented feature without runtime evidence is `unverified`, not available.

Use structured subprocess argument arrays, `shell=False`, bounded output, and no secret values. Mocks are permitted only in automated skill tests and never prove live integration.