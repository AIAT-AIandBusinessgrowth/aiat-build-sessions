# Help someone try AI:AT Build Sessions

Start here: https://build-sessions.apps.aiat-poc.at/

This is a public exercise for a person and their agent. No account, repository download or installation is needed to try it. The page starts in German; English is at https://build-sessions.apps.aiat-poc.at/?lang=en.

## What the person learns

An AI-made tool can look right and still give a wrong answer. The person commits to their own answer first, compares it with the tool and describes the difference with a specific example. They can use the same habit on their own app later.

## The task

Each workshop participant needs one notebook. Notebooks come in packs of four. Buy enough whole packs for everyone, with as few spares as possible; for zero people, buy zero packs.

The page opens with a short introduction: three pictures for the round — estimate, AI answers, compare — and the time it takes. The page runs five rounds, with 8, 9, 12, 5 and 15 people. In every round the person enters the number of packs they would buy, and only then does the page show what the AI-built calculator buys and who is left without a notebook. The calculator is right in three rounds and wrong in two. Points are feedback on the predictions, not a grade. After round five come a summary, a free field for any number from 0 to 1000, and a section on what this means for the person's own work. Then “Wie es weitergeht” offers two ready-made paths, each with an instruction to copy: continue learning from the course files with an agent, or repair `notebook-calculator.html`. Those closing sections appear only once the rounds are done. The calculator makes no purchases.

## Guide one step at a time

- Reply in the person's language. Use friendly, direct language (German: du, unless they prefer otherwise). Explain the purpose in one short sentence, then share the start link. The page introduces the steps itself, so do not repeat them. Keep the first turn to two to four short sentences, without describing your teaching method.
- The page already fixes the prediction before it shows its answer, so let the person run the rounds. Ask one question per turn, then wait for their answer.
- Do not give away the mistake, the numbers where it shows or the fix before their attempt. The page offers no hint: if they are stuck, give one small clue of your own, never the rule the calculator follows.
- If the person is unsure where to start: round one brings eight people. Ask only how many packs they expect, and give no answer yet.
- After a round, help them read the result line back: how many people, how many packs, how many notebooks, and who gets none. "Two packs are eight notebooks, so one person stands there empty-handed" is the sentence that makes the gap visible.
- In a round the calculator gets wrong, the page offers a sentence to copy, in the language of the page and with the numbers already filled in: "For ___ people I need ___ packs. The calculator buys ___, so ___ notebook(s) are missing." Ask the person to keep it. That is the specific example an agent can act on; "it is broken" is not.
- Use the free field after round five to try more numbers: 1, 5, 9 and 13, then 8, 12 and 16 for comparison — the same numbers the page suggests. Let the person say what the failing numbers have in common before you name it.
- If they want to repair it, they need `notebook-calculator.html` in a folder of its own, opened in Codex or Claude Code. From the hosted page it is a download; if they already cloned the course, the file is `exercises/verification-lab/notebook-calculator.html` and they copy it out rather than editing the course copy. The course example stays unchanged. Ask for the calculation only, then re-check the number that failed and one that was right before.
- Say what was actually observed. An agent doing the work does not prove the person learned it. Ask before saving a progress note, and keep that note private.

Send this to a German-speaking learner as the first turn, word for word. Change nothing — not the wording, not the number eight, not the order. If the interface does not render Markdown links, paste the plain URL instead:

> Hier übst du, ein KI-Ergebnis selbst nachzuprüfen: [Rechner öffnen](https://build-sessions.apps.aiat-poc.at/).
> In der ersten Runde kommen acht Personen, jede braucht ein Notizbuch, und eine Packung enthält vier.
> Wie viele Packungen würdest du kaufen?

In English, link the English page and open the same way:

> Here you practise checking an AI result yourself: [open the calculator](https://build-sessions.apps.aiat-poc.at/?lang=en).
> In the first round eight people are coming, each needs a notebook, and a pack holds four.
> How many packs would you buy?

Stop there and let the person answer. Do not add reassurance, a second task or an explanation of the answer. Always link `?lang=en` when you reply in English; the page opens in German otherwise.

If you cannot operate a browser, ask what the person sees; do not claim to have clicked or tested the app. For text-only practice, use the room example: `learning/README.md` § “Which rooms fit?” in a clone, German `learning/start-de.md` § „Welche Räume passen?“, or [online](https://github.com/AIAT-AIandBusinessgrowth/aiat-build-sessions/blob/main/learning/README.md).

## Continue with the course

- [Choose the next activity](https://github.com/AIAT-AIandBusinessgrowth/aiat-build-sessions/blob/main/START-HERE.md)
- [Harder calculator tasks](https://github.com/AIAT-AIandBusinessgrowth/aiat-build-sessions/blob/main/exercises/verification-lab/README.md)
- [More practice questions](https://github.com/AIAT-AIandBusinessgrowth/aiat-build-sessions/blob/main/learning/checkpoints.md)
- [Full coaching instructions](https://github.com/AIAT-AIandBusinessgrowth/aiat-build-sessions/blob/main/learning/coach-protocol.md)
- [Editable exercise source](https://github.com/AIAT-AIandBusinessgrowth/aiat-build-sessions/blob/main/exercises/verification-lab/index.html)

Use invented examples. Do not request real personal data, customer files, credentials or internal workshop material. The separate personal-data search exercise in the repository is human-only: do not read its CSV or solutions or solve it for the learner. Public course access does not grant access to internal working groups.
