---
name: get-shit-done
description: A meta-prompting, context engineering and spec-driven development system for Gemini CLI. Provides advanced workflows for planning, execution, and verification of complex tasks.
---

# Get Shit Done (GSD)

GSD is a framework designed to streamline software development through spec-driven workflows and autonomous agents.

## Core Commands

- \/gsd:new-project\: Initialize a new GSD project in the current directory.
- \/gsd:plan-phase\: Create a detailed plan for the current phase.
- \/gsd:execute-phase\: Execute the current phase according to the plan.
- \/gsd:verify-work\: Verify the work completed in the current phase.
- \/gsd:progress\: Show the current progress of the project.
- \/gsd:status\: Display the status of the current workstream.

## How it works

GSD uses a set of specialized agents located in \~/.gemini/agents/\ and command definitions in \~/.gemini/commands/gsd/\. It manages project state through \.planning/\ directories, keeping track of milestones, phases, and tasks.

## Key Files

- \README.md\: Project overview.
- \CONTEXT.md\: Machine-readable project context.
- \AGENTS.md\: Guidelines for agent behavior.
- \STATE.md\: Current project state and progress.
