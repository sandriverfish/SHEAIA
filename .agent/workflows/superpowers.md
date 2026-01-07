---
description: Using superpowers skills library - core workflows for AI-assisted development
---

# Superpowers Skills Integration

The superpowers skills are located in `.superpowers/skills/`. Each skill is a markdown file that provides detailed workflows and best practices.

## Available Skills

### Core Development Workflow
1. **brainstorming** - Use before any creative work to explore ideas and create designs
2. **writing-plans** - Create detailed implementation plans after design approval
3. **executing-plans** - Execute plans in batches with checkpoints
4. **subagent-driven-development** - Fast iteration with two-stage review

### Testing & Quality
5. **test-driven-development** - RED-GREEN-REFACTOR cycle for all implementations
6. **systematic-debugging** - 4-phase root cause process for any bug
7. **verification-before-completion** - Ensure fixes are actually complete

### Collaboration & Review
8. **requesting-code-review** - Pre-review checklist and process
9. **receiving-code-review** - How to respond to review feedback
10. **dispatching-parallel-agents** - Run concurrent subagent workflows

### Git & Branch Management
11. **using-git-worktrees** - Create isolated workspaces on new branches
12. **finishing-a-development-branch** - Merge/PR decision workflow

### Meta
13. **writing-skills** - Create new skills following best practices
14. **using-superpowers** - Introduction to the skills system

## How to Use

To use a skill, read the corresponding file:
```
.superpowers/skills/<skill-name>/SKILL.md
```

### Example: Start a New Feature
1. Read `.superpowers/skills/brainstorming/SKILL.md` - Design the feature
2. Read `.superpowers/skills/writing-plans/SKILL.md` - Create implementation plan
3. Read `.superpowers/skills/test-driven-development/SKILL.md` - TDD implementation
4. Read `.superpowers/skills/executing-plans/SKILL.md` - Execute the plan

### Example: Debug an Issue
1. Read `.superpowers/skills/systematic-debugging/SKILL.md` - Find root cause
2. Read `.superpowers/skills/test-driven-development/SKILL.md` - Write failing test
3. Read `.superpowers/skills/verification-before-completion/SKILL.md` - Verify fix

## Quick Commands

To invoke a specific workflow, ask:
- "Use the brainstorming workflow to design [feature]"
- "Follow the TDD skill to implement [feature]"
- "Use systematic debugging to fix [issue]"
