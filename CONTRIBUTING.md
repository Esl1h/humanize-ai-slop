# Contributing to Humanize AI Slop

Thanks for your interest in improving the skill.

## Before opening a pull request

1. Read [`AGENTS.md`](AGENTS.md). It explains the package layout and the rules for changing `SKILL.md` without breaking the pattern numbering or the sync between files.
2. Run the local validation:

   ```bash
   python3 scripts/validate-package.py
   ```

3. If you changed something in `SKILL.md`, update the matching table in `README.md` and, for a behavior change, add a note under **Version history**.

## Welcome contributions

- **A new AI writing pattern** you keep seeing that the skill does not cover yet.
- **A more natural example** for an existing pattern, especially when the current one is thin.
- **A false positive**: a pattern flagging something it should not.
- **Wording fixes** that make an instruction shorter or clearer.

To suggest a new pattern, open an issue with a real excerpt (anonymized if needed) that shows the problem before sending the pull request. That avoids wasted work when the pattern is already covered under another number.

## What to avoid

- Do not add a pattern that duplicates an existing one under a new name. Fold the example into the existing pattern instead.
- Do not open pull requests that mix behavior changes with reformatting. One topic at a time.
