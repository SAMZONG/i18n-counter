# i18n-counter

[![Release](https://img.shields.io/github/v/release/samzong/i18n-counter)](https://img.shields.io/github/v/release/samzong/i18n-counter)
[![Build](https://github.com/SAMZONG/i18n-counter/actions/workflows/run_builds.yaml/badge.svg)](https://github.com/SAMZONG/i18n-counter/actions/workflows/run_builds.yaml)
[![Commit activity](https://img.shields.io/github/commit-activity/m/samzong/i18n-counter)](https://img.shields.io/github/commit-activity/m/samzong/i18n-counter)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


## introduce

i18n-counter is a tool to count the number of translated strings in a project.

please make sure that the language has exists before using this tool.

- **Github repository**: <https://github.com/samzong/i18n-counter/>

## Usage

i18n-counter locales_path source_language target_language

```bash
i18n-counter locales zh-CN en-US
```

### Good Example

```bash
~ ./i18n-counter ~/Git/daocloud/frontend/kairship-ui/src/locales en-US zh-CN

project:  /Users/samzonglu/Git/daocloud/frontend/kairship-ui/src/locales
en-US files:  82
en-US strings:  883

zh-CN files:  82
zh-CN strings:  881

zh-CN -> en-US file translation rate:  100.00%
zh-CN -> en-US string translation rate:  99.77%

{'source_files': 82, 'source_counter': 883, 'target_files': 82, 'target_counter': 881}
```

```bash
~ ./i18n-counter /app/src/locales zh-CN en-US

project:  /Users/samzonglu/Git/daocloud/frontend/kairship-ui/src/locales
zh-CN files:  82
zh-CN strings:  881

en-US files:  82
en-US strings:  883

en-US -> zh-CN file translation rate:  100.00%
en-US -> zh-CN string translation rate:  100.23%

{'source_files': 82, 'source_counter': 881, 'target_files': 82, 'target_counter': 883}

```

### Bad Example

```bash
~ ./i18n-counter /app/src/locales en-US
{'tips': 'Usage: i18n-counter locales_path source_language target_language'}
```

```bash
~ ./i18n-counter /app/src/locales en-US zh-CN a
{'tips': 'Usage: i18n-counter locales_path source_language target_language'}
```

```bash
~ ./i18n-counter /notfound/path en-US zh-CN
/Users/samzonglu/Git/samzong/i18n-counter/.venv/bin/python /Users/samzonglu/Git/samzong/i18n-counter/i18n_counter/i18n-counter.py locales zh-CN en-US 
[Errno 2] No such file or directory: 'locales/zh-CN/'
{'tips': 'No translation files found.'}
```
