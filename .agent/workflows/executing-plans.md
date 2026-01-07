---
description: Execute implementation plans in batches with human checkpoints
---

# Executing Plans Workflow

Use with an approved implementation plan.

## The Process

### 1. Setup
- Verify all tests pass (clean baseline)
- Have implementation plan ready
- Confirm with human: "Ready to start execution?"

### 2. Execute in Batches
Work through tasks in order, pausing for checkpoints:

**For each task:**
1. Read the task from the plan
2. Implement exactly as specified
3. Run the verification step
4. Mark task complete
5. Commit with descriptive message

**Batch checkpoints:**
- After every 3-5 tasks, pause for human review
- Report: what was done, what's next, any issues
- Wait for go-ahead before continuing

### 3. Handle Issues
If a task fails:
1. STOP - don't continue to next task
2. Report the failure clearly
3. Use systematic-debugging workflow if needed
4. May need to revise plan

### 4. Completion
When all tasks done:
- Run full test suite
- Report summary of changes
- List any deviations from plan

## Key Principles
- **Follow the plan** - Don't improvise
- **Verify each task** - Never skip verification
- **Communicate issues early** - Don't hide problems
- **Batch checkpoints** - Keep human in the loop

## Quick Commands
- "Continue to next batch"
- "Show progress"
- "Stop and investigate [issue]"
