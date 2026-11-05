# Open-source contributions

A structured record of the pull requests I have shipped to open-source projects: what I changed, how I verified it, and what I learned. Statuses are refreshed from GitHub with `scripts/update_status.py`.

**Archit** - B.Tech (CSE, AI/ML), GLA University. GitHub: [@Architcybercrime](https://github.com/Architcybercrime)

## At a glance

<!-- STATS:START -->
| Merged PRs | Projects | Tests added (merged) | Open PRs |
|---|---|---|---|
| **8** | **3** | **224** | **3** |
<!-- STATS:END -->

## Contributions

<!-- CONTRIBUTIONS:START -->
| Project | PR | What | Closes | Tests | Status |
|---|---|---|---|---|---|
| noCap | [#19](https://github.com/fatihserhatturan/noCap/pull/19) | docs: add keyboard shortcuts section to README | #18 | - | Merged (2026-10-21) |
| repowise | [#4802](https://github.com/repowise-dev/repowise/pull/4802) | fix(health): take the largest arm of C/C++ #if blocks | #4790 | 8 | Merged (2026-10) |
| argus-codescan-mcp | [#122](https://github.com/argus-code-scanning/argus-codescan-mcp/pull/122) | feat(rules): Python access-control rules (DRF, Django CSRF, Flask-Login) | #114 | 34 | Merged (2026-10-30) |
| argus-codescan-mcp | [#123](https://github.com/argus-code-scanning/argus-codescan-mcp/pull/123) | feat(rules): detect JWTs decoded without signature verification | #117 | 27 | Merged (2026-10-30) |
| argus-codescan-mcp | [#128](https://github.com/argus-code-scanning/argus-codescan-mcp/pull/128) | feat(rules): Spring Security and ASP.NET Core access-control opt-outs | #115 | 27 | Merged (2026-11-03) |
| argus-codescan-mcp | [#129](https://github.com/argus-code-scanning/argus-codescan-mcp/pull/129) | feat(rules): Rails, Laravel and Node access-control opt-outs | #116 | 34 | Merged (2026-11-03) |
| argus-codescan-mcp | [#130](https://github.com/argus-code-scanning/argus-codescan-mcp/pull/130) | fix(rules): flag SQL built from variables only, per language | #108 | 49 | Merged (2026-11-03) |
| argus-codescan-mcp | [#131](https://github.com/argus-code-scanning/argus-codescan-mcp/pull/131) | feat(rules): detect exposed admin, debug and management endpoints | #118 | 45 | Merged (2026-11-03) |
| argus-codescan-mcp | [#156](https://github.com/argus-code-scanning/argus-codescan-mcp/pull/156) | feat(rules): GitHub Actions rules for unpinned actions and script injection | #143, #144 | 51 | Open |
| argus-codescan-mcp | [#157](https://github.com/argus-code-scanning/argus-codescan-mcp/pull/157) | feat(malware): detect obfuscated JavaScript and crypto-wallet hijacking | #145 | 24 | Open |
| pabot | [#744](https://github.com/mkorpela/pabot/pull/744) | Pass --pabotlibhost/--pabotlibport to workers when using an external PabotLib server | #743 | 2 | Open |
| Java-Template | [#81](https://github.com/Frc5572/Java-Template/pull/81) | Fix forward tilt limit clamp in SwerveRateLimiter | #68 | - | Closed |
<!-- CONTRIBUTIONS:END -->

Per-project write-ups: [argus-codescan-mcp](contributions/argus-codescan-mcp.md) | [repowise](contributions/repowise.md) | [pabot](contributions/pabot.md) | [noCap](contributions/noCap.md) | [attempts that were not merged](contributions/attempts-not-merged.md)

## Highlights

| What | Where |
|---|---|
| Credited as a first-time contributor in a release (repowise **v0.60.0**) | [repowise #5211](https://github.com/repowise-dev/repowise/pull/5211) |
| Cut false positives from **2,834 to 7** (WebGoat) and **1,973 to 13** (juice-shop) with one rule rewrite | [argus #130](https://github.com/argus-code-scanning/argus-codescan-mcp/pull/130) |
| Added new file types end to end (discovery, scanner tables, rules, tests) so config and CI files are scanned for the first time | [argus #131](https://github.com/argus-code-scanning/argus-codescan-mcp/pull/131), [#156](https://github.com/argus-code-scanning/argus-codescan-mcp/pull/156) |
| Reproduced and fixed a CLI bug end to end against a real server | [pabot #744](https://github.com/mkorpela/pabot/pull/744) |

## How I work

Pick an issue nobody has, verify it is really free, claim it with a plan, build it with tests, measure before and after on real projects, then submit. Details and the search queries are in [workflow.md](workflow.md); mistakes and what they taught me are in [lessons-learned.md](lessons-learned.md).

## Update the tables

```bash
python scripts/update_status.py            # refresh from GitHub
python scripts/update_status.py --offline  # rebuild from data/contributions.json only
```
