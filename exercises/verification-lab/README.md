# Try the notebook calculator

AI results can look right and still be wrong. Here you practise deciding the answer yourself first, then comparing it with the tool and saying clearly where they differ.

You are planning a workshop. Each person needs one notebook. Notebooks come in packs of four. An AI has built a calculator that says how many packs to buy — and for some numbers it is wrong.

Give yourself about ten minutes for the five rounds. Repairing the calculator afterwards takes longer.

## Open the calculator

**[Open the exercise](https://build-sessions.apps.aiat-poc.at/)** and try it in your browser. It starts in German; choose **English** at the top to switch. No account, installation or download is needed. The page saves no inputs and makes no purchases.

Using Codex, Claude or another agent? Share the link and the [agent guide](https://build-sessions.apps.aiat-poc.at/agent-guide.md). Ask it to let you answer each round before it gives hints or the answer.

<details>
<summary>Use it offline or change the code</summary>

The page has a download link for `notebook-calculator.html`, a plain copy of the calculator with the same mistake and none of the course text. Save it in a folder of your own; you can open it in your browser any time, and it is the file you repair.

You can also download the whole course from GitHub: **Code → Download ZIP**, unzip it, then open `exercises/verification-lab/index.html`. Opened from a folder this way the page hides its download link, but `notebook-calculator.html` is already in that same folder. GitHub itself displays HTML as code.

</details>

## How the five rounds work

The rounds bring 8, 9, 12, 5 and 15 people. In each round:

1. Work out how many whole packs you would buy: enough for everyone, as few spares as possible. If nobody comes, you buy nothing.
2. Enter your number. It is fixed before the calculator's answer appears — that is the whole point of the exercise.
3. Compare. The page shows the people, the packs, the notebooks and who is left standing without one.

The calculator is right in three of the five rounds and wrong in two. Points count up as you go. They are feedback on your predictions, not a grade, and being right where the calculator is wrong is worth the most.

After round five you get a summary and a free field for any number from 0 to 1000. Use it. Try 1, 5, 9 and 13, then 8, 12 and 16, and see which ones go wrong. One correct answer never proves the next one.

## The sentence you take to the AI

Every round the calculator gets wrong produces a sentence you can copy, for example:

> For 9 people I need 3 packs. The calculator buys 2, so one notebook is missing.

That sentence gives an agent something specific to act on. "It is broken" does not.

To repair the calculator, download `notebook-calculator.html` from the page into a folder of your own and open that folder in Codex or Claude Code. Leave the course example as it is, so the next person can still try it. If you are starting a new project, use the [project instructions](../../templates/project-AGENTS.md).

Paste your sentence and ask the agent to **change only the calculation**. Then check two numbers yourself: the one that failed, and one that was right before. Read the results yourself — a confident "fixed" is not a result.

No agent available? Write down the change you would make and try it later.

## Do it on paper instead

No browser needed. One notebook per person, four notebooks per pack. Work out the packs for 8, 9, 12, 5 and 15 people, and note for each how many notebooks that is and whether anyone is left out.

<details>
<summary>The rule the calculator follows (this gives the answer away)</summary>

It divides the number of people by four and rounds to the nearest whole number. Apply that rule to your five numbers on paper and compare it with the packs you would actually buy.

</details>

## Harder tasks

Two longer exercises for when the notebook rounds feel easy. In both, you ask an agent to build the calculator described, and then check whether it does what the task says. All prices are invented for this exercise.

### 1. The limit is not in the input field

About 25 minutes. Do the five rounds first.

You order notebooks from a supplier. Packs of four, one notebook per person, and the supplier charges by order size:

| Order size | Price per pack |
|---|---|
| 1 to 24 packs | EUR 12.00 |
| 25 to 59 packs | EUR 10.50 |
| 60 packs or more | EUR 9.20 |

The price for the tier applies to the whole order, not only to the packs above the limit. Ask an agent to build a calculator for this: you type a number of people, and it shows packs, notebooks and the total price. Then find out whether it follows the price list.

The catch: the price list counts packs, the input field counts people. Convert each limit into a number of people before you test it. 24 packs cover 96 people, so the 25-pack limit starts at 97 people; the 60-pack limit starts at 237. For each limit, enter three numbers: exactly on it, one person below, one person above. Then read the price per pack back out of the answer — the total divided by the packs — and compare it with the table.

Done when you can say:

> I entered 96, 97, 100, 101, 236, 237 and 240 people and wrote down the packs, the total and the price per pack I calculated back from it. For ___ people the calculator charged ___ per pack instead of ___. After the change all seven cases match the price list, and 237 people still get the EUR 9.20 price.

The last half of that sentence is not decoration. A limit that worked before the change has to still work after it.

<details>
<summary>Solution notes</summary>

The step is usually written as "more than 25 packs" where the table says "25 packs or more". Then 97 to 100 people get 25 packs at EUR 12.00 instead of EUR 10.50: EUR 300.00 instead of EUR 262.50. That is four of the 1001 possible inputs. Round numbers such as 10, 20 and 50 look fine, the second limit at 237 people is fine, and typing 25 into a field that counts people tests a different limit entirely — which is why a quick check finds nothing.

The pack calculation itself is correct in this task. When the agent repairs the price step, watch that it does not tidy up the 60-pack limit as well: that one already works, and 237 people is the case that proves it still does.

</details>

### 2. Two mistakes, one right answer

About 35 minutes. Do task 1 first.

This calculator has three fields: participants, trainers (pre-filled with 4) and spare notebooks (pre-filled with 0). The rule is:

1. Everyone in the room gets one notebook. The trainers count too.
2. Spare notebooks are added on top.
3. The total is rounded up to whole packs of four.

A colleague has already checked it. They entered 40 different participant numbers — 0, 1, 2, 3, 8, 9, 13, 17, 50, 100, 250, 500 and more — and every answer was right, so they signed it off. Do not sign it off yet. They checked one thing 40 times, not 40 things once.

What to enter:

- The case whose right answer you know without calculating: 0 participants, 0 trainers, 0 spares. That has to be 0 packs.
- Then hold the participants at 20 and walk the trainers from 0 up to 8. A pre-filled field is an input, not a constant.
- For each case, work out the middle step by hand first: how many people are in the room, and how many notebooks that is. Only then look at the packs, and compare notebooks with notebooks.

Done when you can say:

> With 0 participants, 0 trainers and 0 spares the calculator ordered ___ packs instead of 0. With 20 participants and 5 trainers, 25 people are in the room; the calculator bought ___ packs, which is ___ notebooks. After the change both cases are right, and the numbers that were right before — 8, 9, 20 and 500 participants with 4 trainers — still give 3, 4, 6 and 126 packs.

<details>
<summary>Solution notes</summary>

There are two mistakes, not one: the trainers are left out of the sum, and one whole pack is added to every order. With exactly 4 trainers the two cancel each other out, which is why every answer the colleague saw was right. With 0 trainers every order is one pack too large; with 5 trainers notebooks are actually missing. The spare-notebook field is a decoy: it is built correctly, so changing it never reveals anything.

Repairing only one of the two makes the calculator worse than it was. That is why the last part of the sentence above — the numbers that were right before — is not optional.

</details>

Choosing which numbers to enter is a skill of its own: [Choose test values](../../tracks/05-verify-and-loop/05-choosing-test-values.md).

For a larger task split between several agents, see [Parallel agents](../../tracks/08-advanced/03-parallel-agents.md).

## Keep going

Try the same habit on [something an agent built for you](../../tracks/05-verify-and-loop/01-verification-ladder.md), or return to the [learning guide](../../learning/README.md).

This is a practice calculator with an intentional mistake. Use made-up numbers. The separate [personal-data exercise](../find-the-personal-data/README.md) is done without AI.
