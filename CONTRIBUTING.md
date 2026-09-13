# Contributing and checking changes

Help someone try a useful task, notice whether it worked and apply what they learned to another example. Keep internal workshop planning, participant records and feedback outside this public repository.

## Before changing material

Read [AGENTS.md](AGENTS.md) and the unit you are changing. New units follow [_unit-template.md](_unit-template.md). Check existing paths before adding another guide for the same task.

## Write for the person trying it

Every lesson must answer these near the top:

- **What will I try?** Name the first action and its object, such as opening an exported CSV.
- **Why is that useful?** Name the problem it helps with, such as finding rows missing from an export.
- **What can I do afterwards?** Name something the learner can do or check, such as comparing the export with the original table.

The outcome table and opening paragraph can answer these together; do not add a second form or repeat the same promise under three headings. Use adult everyday language. ELI5 here means explaining the actual task simply, without childish analogies or lost facts.

Put the next action before the explanation of your teaching method. Use a familiar example: “four notebooks in a pack” is easier to picture than “sealed kits”. A newcomer should see what to try without first learning words such as “artefact”, “evidence”, “transfer” or “checkpoint”. Introduce a technical term when it helps with the task.

Give one question at a time. Put extra explanations and harder tasks after the first attempt, or behind a clearly named optional section. Keep detailed grading and recordkeeping in the coach material. A brief note for next time should be enough for someone studying alone.

Read the text aloud. Remove generic praise, slogans, repeated cautions and sentences that only announce the next paragraph. Keep the concrete facts and the checks that help someone notice a mistake. Simplifying the language must not turn an untested result into a pass.

Keep exact commands, file paths, prerequisites, data rules, sources and check dates. Explain a technical term beside the first step that needs it. Preserve existing heading anchors when renaming a heading. Reviews may find no problems; never require an invented finding, an unnecessary edit or a new rule just to finish an exercise.

## Keep the material consistent

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

Also try a correct answer, a different example using the same idea and a pause/resume with a consenting learner. Agent simulations reveal instruction failures; they do not replace watching real participants. Use the [training guide](facilitate/training-guide.md) to check learning without collecting personal data.

A learning-product review keeps this kind of evidence — the checks actually run, failures found and fixed, and remaining limits — in the pull request that introduces the change, not in a separate validation file in this repository.

## Maintain source claims

When a vendor page cannot be checked, label the specific claim unverified; do not change a whole page's date to imply a full recheck. Put durable concepts in tracks and volatile facts in the [tool matrix](diy/tool-matrix-2026-09.md).

Open a pull request with the concrete learner problem, resulting behaviour and checks you actually ran. An issue about material should use fictional examples and no screenshots with private information.

## Optional maintainer orchestration

Learners need no Session Orchestrator plugin. If a maintainer uses it, parse `AGENTS.md` explicitly with the plugin's `scripts/parse-config.mjs AGENTS.md`: the parser does not follow the `@AGENTS.md` import in `CLAUDE.md`. The gate's `typecheck-command` slot runs this documentation repository's content validator; it is not a TypeScript or Python type check. Setting it to `false` would execute the failing shell command rather than disable the slot. Runtime reports and local learner progress are ignored by Git. Do not force-add them.
