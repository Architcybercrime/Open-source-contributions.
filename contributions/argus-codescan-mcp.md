# argus-codescan-mcp

Open-source security scanner (SAST, secrets, malware heuristics, SARIF, MCP) driven by YAML rule packs in `packages/languages/src/argus_languages/bundled_rules/`. Each rule needs `fix_guidance`, tests with vulnerable and safe examples, and a noise check on real projects.

| PR | Issue | Rules | Tests | Verification | Status |
|---|---|---|---|---|---|
| [#122](https://github.com/argus-code-scanning/argus-codescan-mcp/pull/122) Python access control | #114 | 5 | 34 | 0 findings on a plain Django app; the 4 hits on a DRF app are intentional public views | Merged 2026-10-30 |
| [#123](https://github.com/argus-code-scanning/argus-codescan-mcp/pull/123) JWT verification | #117 | 8 | 27 | 0 findings on 4 real applications; libraries only trip on their own tests | Merged 2026-10-30 |
| [#128](https://github.com/argus-code-scanning/argus-codescan-mcp/pull/128) Spring and ASP.NET Core | #115 | 5 | 27 | 0 on CleanArchitecture and a Spring demo; eShop and eShopOnWeb hits are login endpoints | Merged 2026-11-03 |
| [#129](https://github.com/argus-code-scanning/argus-codescan-mcp/pull/129) Rails, Laravel, Node | #116 | 7 | 34 | 0 on juice-shop, monica and an Express app; Mastodon and Forem hits are public-by-design endpoints | Merged 2026-11-03 |
| [#130](https://github.com/argus-code-scanning/argus-codescan-mcp/pull/130) SQL string-build | #108 | 5 + 1 narrowed | 49 | WebGoat 2,834 to 7; juice-shop 1,973 to 13; four other projects to 0 | Merged 2026-11-03 |
| [#131](https://github.com/argus-code-scanning/argus-codescan-mcp/pull/131) Exposed endpoints | #118 | 5 | 45 | 46 Spring config files in spring-security-samples scanned with 0 findings; Petclinic `exposure.include=*` caught | Merged 2026-11-03 |
| [#156](https://github.com/argus-code-scanning/argus-codescan-mcp/pull/156) GitHub Actions | #143, #144 | 8 | 51 | flask and requests: 0; argus itself: 0 injection; ultralytics: 84 | Open |
| [#157](https://github.com/argus-code-scanning/argus-codescan-mcp/pull/157) Obfuscated JS and wallet hijack | #145 | 6 + 3 file-level | 24 | Real javascript-obfuscator output detected; 0 findings on 3,900+ JS/TS files | Open |

## Design decisions worth knowing
- **Statement shape, not keywords (#130).** A SQL rule fires only on `SELECT ... FROM`, `INSERT INTO`, `UPDATE ... SET` or `DELETE FROM` with a variable in a value position. Parameterised queries and table names built from variables are not flagged.
- **Config files get their own rules (#131, #156).** New file types (`spring-config`, `github-actions`) are added to `CONFIG_LANGUAGES` so generic code rules cannot misfire on `KEY=value` lines.
- **Severity follows intent.** Definite bypasses are high; "is this meant to be public?" findings are medium or low and say "review".
- **Maintainer feedback (paraphrased).** The maintainer called the first PR a great first PR for its precise patterns, tests and honest noise check, assigned follow-up issues to me, and adjusted one severity himself after merging.
