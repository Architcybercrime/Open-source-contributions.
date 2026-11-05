# How I find, build and ship a contribution

## 1. Find an issue worth doing
| Step | What I do |
|---|---|
| Search | `is:issue is:open no:assignee comments:0 label:"help wanted"` plus a language filter; repository search with `pushed:>DATE help-wanted-issues:>3` to find active projects |
| Prefer | Projects whose maintainers merge outside PRs (check the last few merged PRs and who wrote them) |
| Avoid | Brand-new issues in repos where maintainers fix their own; programme-farm labels; issues that need a design discussion first |

## 2. Check it is really free
1. Search for PRs that mention the issue number (`repo:X is:pr NUMBER in:body` and `in:title`).
2. Read the timeline for "linked a pull request" and for "Taking this!" comments (logged-out HTML can hide these, so confirm on the logged-in page).
3. Read the issue text itself: some say "an open PR already fixes this".

## 3. Claim with a plan
A short comment: what I will change, the files involved, the tests, and the noise check I will run. Then build.

## 4. Build
| Practice | Why |
|---|---|
| Reproduce the problem first | A fix without a failing case proves nothing |
| Tests with vulnerable and safe examples, plus a language-isolation test | Rules must not fire where they should not |
| A test that fails when the protection is removed | Guards against tests that pass for the wrong reason |
| Run the project's own CI commands locally (lint, type-check, tests) | CI should not be the first place a failure appears |
| Measure before and after on real projects | False-positive counts are the evidence a reviewer wants |

## 5. Submit
Follow the PR template, state limitations honestly (do not tick checkboxes I did not verify), link the issue with `Closes #N`, and keep the PR focused.

## 6. Follow up
Check CI once, answer reviewers within a day, nudge once after about a week, then move on.
