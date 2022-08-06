import re
import os

import dotbot


def _readlines(filepath):
    with open(filepath, 'r') as f:
        return f.readlines()


def _writelines(filepath, lines):
    with open(filepath, 'w') as f:
        lines = (
            line if line.endswith('\n') else line + '\n' for line in lines
        )
        f.writelines(lines)


class ED(dotbot.Plugin):
    _directives = [
        'ensure_lines',
    ]

    def can_handle(self, directive):
        return directive in self._directives

    def handle(self, directive, data):
        if directive not in self._directives:
            raise ValueError(f'Cannot handle this directive {directive}')

        if directive == 'ensure_lines':
            return self._handle_ensure_lines(directive, data)

        return False

    def _handle_ensure_lines(self, directive, data):
        for ensurance in data:
            filepath = ensurance["file"]
            filelines = (
                _readlines(filepath) if os.path.exists(filepath) else []
            )
            self._log.debug(f'Checking {filepath}')

            for line_spec in ensurance['lines']:
                self._log.debug(f'Ensure line `{line_spec["content"]}`')

                pattern = re.compile(line_spec['pattern'])
                content = line_spec['content']

                if not any(pattern.match(line) for line in filelines):
                    self._log.info(f'Adding line `{content}` to {filepath}')
                    filelines.append(content)

            _writelines(filepath, filelines)

        return True
