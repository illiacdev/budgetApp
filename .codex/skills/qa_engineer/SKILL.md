# qa_engineer Skill

## Purpose
- Perform quality review for the Python CLI budget app before commit.

## When to use
- After a feature implementation is ready for review.
- Before commit and push.

## Checklist
- Tests were written before implementation.
- `pytest` passes.
- `radon cc` stays within the complexity limit.
- Type hints exist on public functions.
- Functions remain under 50 lines.
- Edge cases are covered.

## Response style
- Report findings first.
- Keep comments concrete and brief.
- Include residual risk if nothing is found.

