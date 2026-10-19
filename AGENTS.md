# Guide for agents

This file explains how to change Humanize AI Slop without breaking the package or the prompt.

## What this repository contains

Humanize AI Slop is an agent skill written in Markdown that merges two English skills, [Humanizer](https://github.com/blader/humanizer) and [No AI Slop](https://github.com/petergyang/no-ai-slop), following the structure of [Humanize BR](https://github.com/Esl1h/humanize-br). There is no build step for the skill itself.

Keep the skill portable. Do not write instructions that limit it to one or two specific agent tools.

## Main files

- `SKILL.md` is the source of truth and the only skill file in the repository. It contains portable YAML metadata, the modes, the editing principles, the word lists, a one-line index of the 41 patterns, and the rewrite process.
- `references/patterns.md` is the full pattern catalog: phrases to watch, the problem, and a before and after example for each pattern. The skill reads it on demand.
- `eval.md` contains the self-check list the skill runs on its own work before returning the result.
- `scripts/slop_scan.py` scans text for the machine-checkable patterns, as `fix` or `watch` findings, and reads its word lists from `SKILL.md` and `references/patterns.md`.
- `scripts/check-sync.py` checks that this repository and [Humanize BR](https://github.com/Esl1h/humanize-br) have not drifted apart.
- `tests/` holds unit tests for the scanner.
- `evals/` holds fixtures with planted patterns and negative controls, golden rewrites, the expected findings (`checks.json`), a grader (`run_evals.py`), agent eval prompts (`evals.json`), and an agent eval runner (`run_agent_evals.py`).
- `README.md` explains installation, usage, patterns, and version history.
- `.claude-plugin/plugin.json` describes the Claude Code plugin and points the skill loader at the root `SKILL.md`.
- `.claude-plugin/marketplace.json` lets users add this repository as a Claude marketplace.
- `.codex-plugin/plugin.json` describes the plugin for ChatGPT and Codex.
- `agents/openai.yaml` holds interface metadata for agents that read the OpenAI format.
- `scripts/validate-package.py` checks the package files and their consistency.
- `NOTICE.md` documents the origin and license of the projects this skill builds on.

## Rules for changes

Keep `SKILL.md`, `eval.md`, and `README.md` in sync.

- **Patterns:** the skill has 41 numbered patterns in seven categories. When you add, remove, or renumber a pattern, update the catalog in `references/patterns.md`, the README table, the pattern index in SKILL.md, the validator, the pattern numbers reported by `scripts/slop_scan.py`, and every reference to the pattern number.
- **Version:** keep the same version in `SKILL.md` under `metadata.version`, in the first version entry of the README, in `.claude-plugin/plugin.json`, and in `.codex-plugin/plugin.json`. Do not add a top-level `version` field to the skill.
- **Compatibility:** keep installation and usage instructions neutral across agents. Names such as Claude Code, ChatGPT, and Codex are examples, not limits.
- **History:** add a short version note to the README for every behavior change or non-obvious fix.
- **Merging:** when a Humanizer pattern and a No AI Slop pattern describe the same habit, keep one numbered pattern and fold the second source's example or wording into it. Do not add a near-duplicate pattern.
- **Shared files:** `scripts/slop_scan.py`, `scripts/check-sync.py`, `evals/run_evals.py`, and `evals/run_agent_evals.py` are identical in Humanize BR. Keep language-specific behavior in the scanner's `CONFIG` and in `evals/checks.json`, and copy any change to both repositories.
- **Parity:** a structural change here (a section, a numbered step, a list item in SKILL.md or eval.md, an eval prompt) needs the same change in Humanize BR. `scripts/check-sync.py` catches the drift.
- **Size:** keep SKILL.md short. Detail that the skill does not need on every run belongs in `references/`.
- **Checks:** before publishing, run `python3 scripts/validate-package.py`, `python3 evals/run_evals.py`, `python3 -m unittest discover -s tests`, and `python3 scripts/check-sync.py`.

## Writing style

Use plain, direct language in code comments, prompts, documentation, descriptions, validation messages, and progress reports.

- Lead with the main point.
- Use common words and active voice.
- Keep sentences and paragraphs short.
- Use one term for the same thing.
- Use "must" or "need" for requirements, not vague wording.
- Use headings, lists, and tables when they help the reader.
- Remove repeated or unnecessary words.
- Avoid double negatives.
- Keep identifiers, commands, paths, schema fields, quotes, watched phrases, and behavior-carrying examples exactly as they are.
- Preserve the full technical meaning.

## Editing the skill

- Keep the YAML metadata valid.
- Treat the prompt below the metadata as the product itself.
- Prefer one short, clear instruction over another exception or repeated explanation.
- Do not use em dashes or en dashes in the prose of this repository outside the examples that discuss them. The skill bans them, so its own files must not lean on them.
