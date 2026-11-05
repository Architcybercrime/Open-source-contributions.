# pabot

Parallel executor for Robot Framework.

## [PR #744](https://github.com/mkorpela/pabot/pull/744) - closes #743 (open)
With `--pabotlibhost`, `_start_remote_library` returned early before updating `_PABOTLIBURI`, so workers always received `127.0.0.1:8270`. I reproduced it with a pre-started PabotLib server on port 18279 (the worker received 8270 before and 18279 after), added two unit tests and a README note. The commit is signed because the repository requires verified signatures.

## Not submitted
- **#734** (result lines split across lines with Robot Framework 7.5): I built and tested a line-buffering writer (output unchanged on RF 7.2.2, fixed on 7.5). The maintainer preferred running Rebot as a subprocess, so I shelved my patch and asked first instead of opening a PR.
- **#737**: resolved by the reporter using an existing PabotLib feature; no code needed.
