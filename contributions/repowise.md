# repowise

Codebase-intelligence tool with code health scoring. Contribution: [PR #4802](https://github.com/repowise-dev/repowise/pull/4802), closing issue #4790. **Merged; credited in the v0.60.0 release notes.**

## The problem
In C and C++, both arms of an `#if` / `#else` block were walked and their branches summed into one function's cyclomatic complexity, so a function with two alternative builds read as if every configuration ran at once (the issue's example: CCN 5 where either build alone is CCN 3).

## The change
| Decision | Choice |
|---|---|
| CCN and cognitive complexity | Take the **largest arm** of a `#if` chain, compared by (ccn, cognitive); an `#if` without an alternative is unchanged; nested blocks and `#elif` chains follow the same rule |
| NLOC | Still counts every arm (the lines exist); documented in the complexity README |
| Complex-condition findings | Still reported from every arm |

3 files, +140 -1. 8 new tests for `c` and `cpp` (6 of 8 fail without the change). The repo's own health gate passed with two warnings, which I called out in the PR.

## Process notes
- The upstream branch moved 18 commits while I worked; I rebuilt the patch on the latest `main` instead of pushing an old one.
- The repository's review bot raised two nits; I answered one with evidence (the new tests do run) and applied the other (dispatch from the top of `_recurse`: complexity 34 to 33, 64 to 61 lines).
- I also prepared a larger refactor and offered it to the maintainers instead of pushing it unasked.
