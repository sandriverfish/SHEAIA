---
description: Test-Driven Development - write failing tests before implementation code
---

# Test-Driven Development (TDD) Workflow

Use when implementing any feature or bugfix.

## The Iron Law

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

Write code before the test? Delete it. Start over.

## Red-Green-Refactor Cycle

### 1. RED - Write Failing Test
- Write ONE minimal test showing what should happen
- Clear name describing behavior
- Test real code (no mocks unless unavoidable)

### 2. Verify RED - Watch It Fail
**MANDATORY. Never skip.**
```bash
npm test path/to/test.test.ts  # or equivalent
```
- Confirm test fails (not errors)
- Failure message is expected
- Fails because feature missing

### 3. GREEN - Minimal Code
Write SIMPLEST code to pass the test. No over-engineering.

### 4. Verify GREEN - Watch It Pass
**MANDATORY.**
- Test passes
- Other tests still pass
- Output pristine

### 5. REFACTOR - Clean Up
After green only:
- Remove duplication
- Improve names
- Extract helpers
Keep tests green. Don't add behavior.

## Red Flags - STOP and Start Over
- Code before test
- Test passes immediately
- Can't explain why test failed
- Rationalizing "just this once"

## Verification Checklist
- [ ] Every new function/method has a test
- [ ] Watched each test fail before implementing
- [ ] Wrote minimal code to pass each test
- [ ] All tests pass
