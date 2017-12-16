# Contributing to the ACM Website
Contributions are welcome!

The two most important rules are

1. **Make your intentions and reasoning clear.**
2. **Don't be a jerk.**

In general, code contributions follow this pattern:

1. Ask one of the ACM officers for access to the repository.
2. Make some changes (being careful to follow the
   [Coding Style](#coding-style)).
3. [Submit a PR](#submitting-a-pr)!
4. [Make requested changes](#making-requested-changes).
5. Get your PR accepted!

Always follow [Good Repository Etiquette](#general-repository-etiquette).

You can also [Create an Issue](#creating-an-issue) requesting a feature,
reporting a bug fix, or suggesting an improvement.

If you have never worked on a TurboGears 2 project, see the
[Resources](#resources-for-learning-turbogears-2) section below.

## Creating an Issue
You can create an issue to request a feature, report a bug fix, suggest an
improvement, etc. When creating an issue, the most important thing is to make
sure you include enough information for a developer to act on the issue.  In
general, this means that the following guidelines are followed:

- The issue title is descriptive
- If reporting a bug, describe:
  - What steps are required to reproduce the bug
  - What you expected to see
  - What you saw instead
- If requesting a feature, describe:
  - What the desired new functionality is
  - How the UI or API should behave
  - Any technical or security considerations that need to be addressed
- Any other information that would be useful to someone looking at this issue in
  a week (or a month, or a year).

Be prepared to actively participate in getting the issue resolved. This can
include answering questions and adapting the issue as necessary.

## Coding Style
The most important thing is to make sure the purpose of the code is clearly
conveyed. If you are having a hard time following the style guide, reconsider
how you are approaching the problem.

### Python
[PEP-8](https://www.python.org/dev/peps/pep-0008/) is to be followed
__strictly__; however lines with lengths of up to 90 or 100 columns are OK if
the purpose of the line is still cleanly conveyed.

### (X)HTML/CSS/JS
Items marked with "(R)" are requirements that cannot be broken except in *very*
rare circumstances.

- (R) Indentation should be 2 **spaces** in XHTML and CSS.
- (R) Indentation should be 4 **spaces** in JavaScript.
- (R) Try to match the style of the rest of the codebase. If there are
  inconsistencies in the codebase, go with whichever option one is the most
  common.
- Use single quotes in JavaScript, use double quotes in (X)HTML. But most
  importantly, be consistent.
- In Kajiki templates, use the `py:*` Kajiki directives when possible. For
  example, use `py:content="x"` when you can, rather than using
  `<tag>${x}</tag>`.
- Use your best judgement on when to split long tags to a new line.
- Use Bootstrap's default classes for styling when possible.
- Use of JavaScript should be minimized. The site should be fully functional
  with JavaScript disabled.
- Use semantic markup. For example, use `strong` and `em` when emphasis is
  required if the words were spoken, and use `b` and `i` if the distinction is
  merely for display purposes.

## Submitting a PR
Please submit a PR on GitHub from your branch to master. Please ensure that:

1. The branch name is concise but descriptive.
2. The PR title is descriptive and explains the point of the PR.
3. In the description of the PR (the comment box), please include the following
   information:

    - If applicable, at the top of the description, include

        Resolves #{issue_number}

      where `{issue_number}` is the issue number that the PR resolves.

    - Describe at a high level the changes that were made in the PR.
    - Include screenshots of any visual changes.
    - Include anything else that you think will be helpful/important for the
      reviewer to know when reviewing your changes.

## Making Requested Changes
We will likely want you to make a couple of changes on your PR before accepting
it. When you make changes, **do not rebase**, we want to preserve the commit
history, even if it contains back-and-forth commits.

There will likely be a few of rounds of this process, that's normal. We want
only the best code in our codebase, and nobody writes perfect code the first
time.

## General Repository Etiquette
Don't be a jerk with the repository. Other people are working on this project.
The `master` branch is protected, but you should also understand that other
people could be working on your branch too.

### Commit Messages
Make descriptive commit messages. "did stuff" is not a descriptive commit
message.

If you are working on an issue, it is recommended that you include the issue
number at the beginning of the commit to make it clear which issue it belongs to
(for example "#18 table with sorting to view survey responses"). This lets
GitHub link the commit to the issue.

### Branching
Create a branch for every feature/bugfix. Make the branch name consise but
descriptive. Two examples of what *not* to do are: "my-branch" (not descriptive)
and "my-cool-feature-which-adds-foo-to-bar" (not consise).

### Rebasing
**If it's not on the internet yet, rebase away. If you have to force push,
reconsider.**

Make sure there is a good reason to rebase and force push if you end up doing
so. Some examples of good reasons include:

- Work-in-Progress (WIP) commits which are overriden almost immediately.
- Removing binaries that were committed on accident.

Some possibly good reasons to rebase and force push include:

- Fixing a typo in the latest commit on a branch. (But catch your mistake
  before pushing next time.)
- Making a commit more descriptive. (But you should have done this before
  pushing.)

Use good judgement to discern whether or not this is applies to your situation.
If in doubt, ask @jackrosenthal.

Some examples of bad reasons to rebase include:

- Rebasing to make the tree cleaner. It's OK to have lots of commits, even ones
  that go back and forth on a PR (see [Making Requested
  Changes](#making-requested-changes)). We want to preserve *all* of the commit
  history.
- Any other reason not mentioned. By default, any reason not mentioned is a bad
  reason to rebase. If you think your situation is special, elevate to the
  project owner (@jackrosenthal) first.

## Resources for Learning TurboGears 2
["Make a Wiki in 20 Minutes" TurboGears
tutorial](http://turbogears.readthedocs.io/en/latest/turbogears/wiki20.html)

You can also look at some other codebases in TG2 to learn a bit about
the structure of an application.

- [`jackrosenthal/puzzle-challenge-website`](https://github.com/jackrosenthal/puzzle-challenge-website)
