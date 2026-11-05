# Lessons learned

| Situation | What happened | Lesson |
|---|---|---|
| Fresh issues in repos where maintainers fix their own (rea, 8f4e, cryo) | The maintainer fixed each within hours of my claim | Do not race for brand-new issues in those repos |
| repowise #4850 and several others | Another contributor claimed or had a PR within a day | Check the logged-in timeline before building |
| pabot #734 | I built a fix; the maintainer wanted a different design (run Rebot as a subprocess) | Ask which approach is wanted before opening a PR |
| pabot #737 | The reporter solved it with an existing feature | Read the whole thread; some issues need no code |
| New rule packs that never fired | Dot-directories and `.properties` files were never scanned | When rules never fire, check file discovery first |
| A test that passed with or without my change | The sample line matched no generic rule | Prove a test bites by removing the protection |
| Several PRs touching one rule file | Merge-conflict risk | Put new rules in a separate file, or in the middle of a shared one |
| Unsigned commits blocked a merge (pabot) | The repo required verified signatures | Enable commit signing early; web commits are signed automatically |
