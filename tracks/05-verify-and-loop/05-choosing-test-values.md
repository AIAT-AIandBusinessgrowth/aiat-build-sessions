# Choose test values

| | |
|---|---|
| **Prerequisites** | [Check an agent's work](01-verification-ladder.md) |
| **Time** | ~20 min |
| **Outcome** | A short list of test values with predictions that finds a mistake your first try missed. |
| **Last verified** | 2026-09-13 |

## Why this matters

Open the [notebook calculator](https://build-sessions.apps.aiat-poc.at/notebook-calculator.html) and enter 8. The answer is right. So are 10, 11 and 12. Enter 9 and it is wrong.

A check is only as good as the numbers you try. Four correct answers in a row tell you nothing about the fifth. The usual advice, try an empty field or a very large number, misses this one completely: the mistake sits between the ordinary numbers, not far away from them. Here you learn to pick the few values that find a mistake.

## Do it

The example below is the notebook calculator: one notebook per person, notebooks come in packs of four, buy enough for everyone without buying a spare pack. If you have not tried it yet, try it now. The next paragraph names the rule the calculator uses, and that is easier to think about after your own attempt.

The calculator divides the number of people by four and rounds to the nearest whole number. Seven questions turn that rule into a short list of values.

### 1. Write the rule in one sentence (2 min)

Say what should happen, in your own words, in one sentence:

```text
Every four people need one pack, and anyone left over needs a pack of their own.
```

If you cannot write the sentence, you cannot test the tool, only look at it. Ask the agent to state the rule it built, in one sentence, and test that sentence.

### 2. Start at zero (1 min)

Zero people, zero packs. Empty list, empty basket, nobody signed up. This case is skipped often because it feels pointless, and it is the one that shows a blank screen or a suggestion to buy one pack for nobody.

### 3. Take both sides of every step (5 min)

The rule has steps. Every fourth person the number of packs goes up by one. A step is where the answer changes, and that is where a mistake hides.

For each step, try three values: just below, the step itself, just above. The first step is at four people, so try 3, 4, 5. The next is at eight, so try 7, 8, 9.

| people | packs you need |
|---|---|
| 3 | 1 |
| 4 | 1 |
| 5 | 2 |
| 7 | 2 |
| 8 | 2 |
| 9 | 3 |

Six values, and two of them, 5 and 9, sit right next to values that work. That is why "try a different number" is not enough on its own. The numbers have to be chosen.

### 4. Keep one value that was right before (2 min)

Note one value the tool already gets right, for example 8 or 12. After any change you or an agent makes, try it again. A fix that repairs 9 and breaks 8 is not a fix, and nobody notices unless someone tries 8 a second time.

### 5. Try one impossible input (3 min)

An empty field, -1, 1.5, or the word "twelve". Decide what should happen **before** you try it:

- A message that says what to enter.
- No answer on screen that belongs to the previous input. An old result standing under a new question is a wrong answer, and it looks exactly like a right one.

Write your expectation down. Otherwise whatever the tool does will look like the intended behaviour.

### 6. One big but realistic number (2 min)

Pick a number your real case could reach, for example 249 people at a conference, not ten million. A very large number mostly finds a display or speed problem. A thinking mistake sits at a step in the rule, so choose a big number that also sits beside a step: 249 rather than 250.

### 7. Write the values down first, and predict each one (5 min)

Before you open the tool, make a table and fill in the first two columns. A prediction made after seeing the answer is not a prediction.

| input | I expect | tool shows | ok? |
|---|---|---|---|
| 0 | 0 packs | | |
| 5 | 2 packs | | |
| 8 | 2 packs | | |
| 9 | 3 packs | | |
| empty | a message saying what to enter | | |
| 249 | 63 packs | | |

Then try them in order and fill in the rest. Where the two middle columns disagree, one of you is wrong, and you now have a specific example to hand to whoever fixes it: "For 9 people I need 3 packs. The calculator says 2."

You can ask an agent for candidate values:

```text
Here is the rule in one sentence: [your sentence].
List the values you would try to find a mistake in it: the zero case,
both sides of every step in the rule, one impossible input, and one large
but realistic number. Give the correct answer for each value.
Do not change anything yet.
```

Read the list as a starting point, not as an answer. An agent that built the tool shares the blind spot that produced the mistake, so add the values it left out.

### Run it on your own thing

Take one rule from your own tool and put the same seven questions to it:

| Rule | Values worth trying |
|---|---|
| Orders of 25 items or more get the lower price | 24, 25, 26, and 0 |
| A date counts as this month | the first day, the last day, and the day before each |
| Three free exports per month | the third, the fourth, and the first after the month turns |

Then try the [harder calculator tasks](../../exercises/verification-lab/README.md#harder-tasks): a price that changes above a set number of packs while the field counts people, and a calculator whose two mistakes hide each other. Both add rules, so the values worth trying sit at new numbers. Write your values and predictions before you ask an agent to make the change.

## Check your understanding

Notebooks now come in packs of six instead of four. Which numbers of people would you try first, and what do you expect each one to show?

## Done when

- [ ] You wrote down at least five test values with a predicted answer for each, before trying them.
- [ ] Your list contains the zero case and both sides of at least one step in the rule.
- [ ] You tried the values and can name one where the tool disagreed with your prediction, or say that all of them matched.
- [ ] After a change, you tried again a value that was correct before, and it is still correct.

## Data note

Test values are invented numbers. Do not use real order values, real customer counts or a real price list to check a tool, and do not paste a real export in to "have realistic data". Made-up numbers find the same mistakes. See [Rule one: no real data](../00-orientation/01-rule-one-no-real-data.md).

## Next

[Keep your work safe](../06-keep-and-ship/01-keep-your-work-safe.md): make sure what you just finished exists twice.

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
