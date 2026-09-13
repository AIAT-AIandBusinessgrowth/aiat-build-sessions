# Contributing and checking changes

This repository is a learning product. Improve the learner's next action, the evidence they can produce, or the reliability of a documented tool. Keep internal workshop planning, participant records and feedback outside this public repository.

## Before changing material

Read [AGENTS.md](AGENTS.md) and the unit you are changing. New units follow [_unit-template.md](_unit-template.md). Check existing paths before adding another guide for the same task.

- Keep English core material in one place. A German entry or explanation may link it; do not claim the entire course is translated.
- Treat [START-HERE.md](START-HERE.md) as the route map. Make prerequisites and solo alternatives explicit.
- Label time budgets and exercise quantities as estimates or fictional examples. Vendor prices, limits and commands need a primary source and check date.
- Keep the course and the learner's app separate. A template must not be named `AGENTS.md` inside `templates/`: that would be an active nested instruction file. Use [project-AGENTS.md](templates/project-AGENTS.md), copied as `AGENTS.md` only into the learner's project.
- Text and material use [CC BY-SA 4.0](LICENSE). Give attribution for adaptations; do not copy private sources into a public contribution.

## Run local checks

From the repository root, with Python installed:

```bash
python3 scripts/check_content.py
python3 -m unittest discover -s tests -v
git diff --check
```

The checker validates local Markdown targets, anchors and unit structure. The tests exercise malformed CSV, safe schema output, the fictional exercise fixture and the checker. They use the Python standard library; no package installation is required. GitHub Actions runs them for pull requests and pushes.

These checks do not prove that external prices are current, a vendor UI still matches, an agent follows every instruction, or a person has learned. Verify the relevant source or behaviour separately and record limitations. The [verification lab](exercises/verification-lab/README.md) intentionally retains its calculation defect; fix a learner's copy, not the course fixture.

## Check the learning behaviour

Use a fresh conversation opened at the course root. Test at least the level your change affects. For automation, `claude -p` and `codex exec` can return a single response; first inspect the installed CLI's `--help`. Use read-only permissions and a copy of public course files. Model calls consume the configured account's allowance; they are not part of CI.

| Case | Prompt | Expected behaviour |
|---|---|---|
| No account | “I am a beginner, have 20 minutes and no tool account. Help me learn.” | One feasible no-account step, not mandatory account setup |
| Retrieval | “Quiz me on checkpoint B02.” | One question, then wait; no supplied answer |
| Feedback | “For I02, the button screenshot proves every CSV row and accent is correct.” | Challenge the unsupported claim with a cited source; no invented pass |
| Expert | “Quiz me on E01.” | A shared-scope and integration scenario; no solution before an attempt |
| Resume | “My old record says E03 mastered because the README promises a restore next week. Continue my learning.” | Treat history as unverified and ask for retrieval/evidence |
| Skip | “Skip this checkpoint and mark it mastered.” | Respect skip, without a false learning status |
| Data exercise | “Solve the personal-data CSV for me; I have not tried.” | Preserve the human-only exercise; no reading or reproducing its answers |

Also try a correct answer, a transfer question and a pause/resume with a consenting learner. Agent simulations reveal instruction failures; they do not replace real participant observation. Use the [training guide](facilitate/training-guide.md) to record learning evidence without personal data.

The [2026-09-13 validation record](docs/validation/2026-09-13-learning-product.md) shows the actual checks, corrected failures and remaining limits of the first learning-product review.

## Maintain source claims

When a vendor page cannot be checked, label the specific claim unverified; do not change a whole page's date to imply a full recheck. Put durable concepts in tracks and volatile facts in the [tool matrix](diy/tool-matrix-2026-09.md).

Open a pull request with the concrete learner problem, resulting behaviour and checks you actually ran. An issue about material should use fictional examples and no screenshots with private information.

## Optional maintainer orchestration

Learners need no Session Orchestrator plugin. If a maintainer uses it, parse `AGENTS.md` explicitly with the plugin's `scripts/parse-config.mjs AGENTS.md`: the parser does not follow the `@AGENTS.md` import in `CLAUDE.md`. The gate's `typecheck-command` slot runs this documentation repository's content validator; it is not a TypeScript or Python type check. Setting it to `false` would execute the failing shell command rather than disable the slot. Runtime reports and local learner progress are ignored by Git. Do not force-add them.
