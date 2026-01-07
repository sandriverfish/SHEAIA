---
description: Systematic debugging - find root cause before attempting fixes
---

# Systematic Debugging Workflow

Use when encountering any bug, test failure, or unexpected behavior.

## The Iron Law

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

## The Four Phases

### Phase 1: Root Cause Investigation

**BEFORE attempting ANY fix:**

1. **Read Error Messages Carefully**
   - Don't skip past errors or warnings
   - Read stack traces completely
   - Note line numbers, file paths, error codes

2. **Reproduce Consistently**
   - Can you trigger it reliably?
   - What are the exact steps?

3. **Check Recent Changes**
   - Git diff, recent commits
   - New dependencies, config changes

4. **Trace Data Flow**
   - Where does bad value originate?
   - What called this with bad value?
   - Fix at source, not at symptom

### Phase 2: Pattern Analysis
- Find similar working code in codebase
- Compare working vs broken
- Identify ALL differences

### Phase 3: Hypothesis and Testing
1. Form single hypothesis: "I think X is the root cause because Y"
2. Make SMALLEST possible change to test
3. One variable at a time

### Phase 4: Implementation
1. Create failing test case first
2. Implement SINGLE fix for root cause
3. Verify fix and no regressions

## Red Flags - STOP and Return to Phase 1
- "Quick fix for now, investigate later"
- "Just try changing X and see if it works"
- Proposing solutions before tracing data flow
- If 3+ fixes failed: Question the architecture
