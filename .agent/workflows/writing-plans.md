---
description: Create detailed implementation plans from approved designs
---

# Writing Implementation Plans Workflow

Use after design is approved, before implementation begins.

## Plan Structure

Break work into bite-sized tasks (2-5 minutes each). Every task must have:
- Exact file paths
- Complete code snippets
- Verification steps

## Plan Format

```markdown
# Implementation Plan: [Feature Name]

## Overview
[Brief description of what we're implementing]

## Prerequisites
- [ ] Design document approved
- [ ] Test baseline verified (all tests pass)

## Tasks

### Task 1: [Descriptive Name]
**File:** `path/to/file.ts`
**Action:** Create/Modify/Delete

**Code:**
```[language]
// Exact code to write
```

**Verification:**
- [ ] Run tests: `npm test path/to/test`
- [ ] Expected result: [what should happen]

### Task 2: [Next Task]
...
```

## Key Principles

1. **Granular Tasks** - Each task 2-5 minutes, single focus
2. **Complete Code** - No placeholders or "implement logic here"
3. **Verification Steps** - Every task has testable completion criteria
4. **Order Matters** - Tasks in dependency order
5. **Test First** - Include test-writing tasks before implementation

## After Planning
- Review plan with human partner
- On approval, use executing-plans workflow
