# Try the notebook calculator

You are planning a workshop. Each person needs one notebook. Notebooks come in packs of four. An AI has built a calculator to tell you how many packs to buy, but it makes a mistake with some numbers.

Can you find one? Give yourself about five minutes for a first try. You can spend longer fixing it afterwards.

## Open the calculator

On GitHub, choose **Code → Download ZIP** at the top of the repository. Unzip the download and open `exercises/verification-lab/index.html` in your browser. It starts in German; choose **English** at the top to switch languages.

GitHub shows the HTML as code. Download it first to use the calculator. It needs no account, installation or server and saves nothing.

## Try one number

1. Choose how many people are coming to your pretend workshop.
2. Work out how many whole packs you need. Get enough for everyone, without buying an extra pack.
3. Enter your number in the calculator and compare its answer with yours.

If nobody comes, you need no packs. For other numbers, count the notebooks in the suggested packs. The calculator has a hint you can open if you get stuck.

When you find a mistake, finish this sentence:

> For ___ people, I need ___ packs. The calculator says ___.

That is a useful first result. You can now tell an AI what went wrong with a specific example.

<details>
<summary>Do it on paper instead</summary>

Use the same workshop example. The calculator divides the number of people by four and rounds to the nearest whole number. Try its rule on paper and compare the answer with the packs you would actually need.

</details>

<details>
<summary>Fix it with Codex or Claude</summary>

Copy `index.html` into your own practice folder and open that folder in the agent. Keep the course example as it is so the next person can try it. Use the [project instructions](../../templates/project-AGENTS.md) if you are starting a new project.

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
