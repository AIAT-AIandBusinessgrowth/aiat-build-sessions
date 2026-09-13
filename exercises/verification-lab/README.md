# Try the notebook calculator

AI results can look right and still be wrong. Here you practise checking them with your own example and describing a mistake clearly.

You are planning a workshop. Each person needs one notebook. Notebooks come in packs of four. An AI has built a calculator to tell you how many packs to buy, but it makes a mistake with some numbers.

Can you find one? Give yourself about five minutes for a first try. You can spend longer fixing it afterwards.

## Open the calculator

**[Open the exercise](https://build-sessions.apps.aiat-poc.at/)** and try it right in your browser. It starts in German; choose **English** at the top to switch languages. No account, installation or download is needed. The calculator saves no inputs and makes no purchases.

Using Codex, Claude or another agent? Share the link and the [agent guide](https://build-sessions.apps.aiat-poc.at/agent-guide.md). Ask it to let you try before giving hints or the answer.

<details>
<summary>Use it offline or change the code</summary>

On the exercise page, open **Fix it with Codex or Claude** and download the HTML file into your own folder. You can open that file in your browser later. The live page stays ready for the next person.

You can also download the whole course from GitHub: **Code → Download ZIP**, unzip it, then open `exercises/verification-lab/index.html`. GitHub itself displays HTML as code.

</details>

## Try one number

1. Choose how many people are coming to your pretend workshop.
2. Work out how many whole packs you need. Get enough for everyone, without buying an extra pack.
3. Enter your number in the calculator and compare its answer with yours.

If nobody comes, you need no packs. For other numbers, count the notebooks in the suggested packs. The calculator has a hint you can open if you get stuck.

When you find a mistake, finish this sentence:

> For ___ people, I need ___ packs. The calculator says ___.

Your example gives the AI something specific to fix. Use the same check on your own tool: a visible Export button does not show whether the file contains the right information. Look at the result yourself.

Try another number too. One correct answer does not tell you whether the rest works.

<details>
<summary>Do it on paper instead (this one names the calculator's rule)</summary>

Use the same workshop example. The calculator divides the number of people by four and rounds to the nearest whole number. Try its rule on paper and compare the answer with the packs you would actually need.

</details>

<details>
<summary>Fix it with Codex or Claude</summary>

Open the folder containing your downloaded `notebook-calculator.html` in the agent. If you downloaded the whole course instead, copy `exercises/verification-lab/index.html` into your own practice folder and open that folder. Keep the course example as it is so the next person can try it. Use the [project instructions](../../templates/project-AGENTS.md) if you are starting a new project.

Tell the AI the number you tried, what you expected and what the calculator showed. Ask it to change only the calculation. Then try your example again and check a number that worked before. Read the result yourself.

No agent available? Write down the change you would make. You can try it later.

</details>

<details>
<summary>Want a harder task?</summary>

Give another agent the original task and your updated file. Ask it to check the result independently and report only problems it can show. A review may find no problems. For this small task, two agents editing at once would add unnecessary work.

Then imagine notebooks come in packs of six. Choose examples that would tell you whether the updated calculator works. Explain why you chose them before asking the agent to make the change.

For a larger task split between several agents, see [Parallel agents](../../tracks/08-advanced/03-parallel-agents.md).

</details>

## Keep going

Try the same habit on [something an agent built for you](../../tracks/05-verify-and-loop/01-verification-ladder.md), or return to the [learning guide](../../learning/README.md).

This is a practice calculator with an intentional bug. Use made-up numbers. The separate [personal-data exercise](../find-the-personal-data/README.md) is done without AI.
