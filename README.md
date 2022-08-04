[dotbot_repo]: https://github.com/anishathalye/dotbot
[ed_repo]: https://github.com/wonderbeyond/dotbot-ed.git

## Dotbot `ED` Plugin

A [Dotbot][dotbot_repo] plugin that helps ensure expected lines in a file.

## Installation

1. Simply add this repo as a submodule of your dotfiles repository:

```
git submodule add https://github.com/wonderbeyond/dotbot-ed.git
```

2. Pass the path of `ed.py` to [Dotbot][dotbot_repo] script:

  - `-p dotbot-ed/ed.py`

## Usage

Example config:

```yaml
- sudo:
  - ensure_lines:
    - file: /etc/hosts
      lines:
        - pattern: '^127\.0\.0\.1\s+localhost\b'
          content: '127.0.0.1  localhost'
        - pattern: '^10\.10\.10\.88(\s+)wonder-dev-001\b'
          content: '10.10.10.88  wonder-dev-001'
```

## Directives

* `ensure_lines`: Ensure a file has specified lines, given a (regex) pattern to check
  if the line exists and the content to append if check fails.
* `drop_lines`: Coming...
