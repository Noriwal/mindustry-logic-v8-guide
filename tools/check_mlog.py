#!/usr/bin/env python3
"""Conservative static check for raw Mindustry processor code.

This does not execute MLog or claim compatibility with a game build.
"""
import argparse
from pathlib import Path
import re
import sys

INTEGER = re.compile(r"^[+-]?\d+$")
LABEL = re.compile(r"^[A-Za-z_][A-Za-z_0-9]*:$")


def tokenize(line):
    """Split whitespace outside strings; keep quotes and escapes untouched."""
    return re.findall(r'"(?:\\.|[^"\\])*"|\S+', line)


def has_unquoted_hash(line):
    quoted = False
    escaped = False
    for character in line:
        if escaped:
            escaped = False
        elif character == "\\" and quoted:
            escaped = True
        elif character == '"':
            quoted = not quoted
        elif character == "#" and not quoted:
            return True
    return False


def check(path):
    errors = []
    warnings = []
    instructions = []
    physical = []
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        stripped = raw.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            warnings.append(f"{path}:{number}: comentário '#' fora de código colável")
            continue
        if LABEL.fullmatch(stripped):
            errors.append(f"{path}:{number}: rótulo '{stripped}' não é instrução MLog")
            continue
        if has_unquoted_hash(stripped):
            errors.append(f"{path}:{number}: comentário inline; remova antes de colar")
        tokens = tokenize(stripped)
        instructions.append(tokens)
        physical.append(number)
    for index, tokens in enumerate(instructions):
        command = tokens[0]
        line = physical[index]
        if command == "jump":
            if len(tokens) != 5:
                errors.append(f"{path}:{line}: jump requer destino, condição e dois operandos")
            elif INTEGER.fullmatch(tokens[1]):
                target = int(tokens[1])
                if not 0 <= target < len(instructions):
                    errors.append(f"{path}:{line}: jump {target} fora das linhas 0..{len(instructions)-1}")
            else:
                warnings.append(f"{path}:{line}: destino dinâmico '{tokens[1]}' não verificável estaticamente")
        if command == "getlink" and len(tokens) != 3:
            errors.append(f"{path}:{line}: getlink requer resultado e índice")
        if command in {"ubind", "sensor"} and len(tokens) != {"ubind": 2, "sensor": 4}[command]:
            errors.append(f"{path}:{line}: quantidade de parâmetros de {command} inesperada")
        if command == "unit" and len(tokens) > 1 and tokens[1] in {"bind", "control", "radar", "locate"}:
            errors.append(f"{path}:{line}: use instrução MLog única (ubind/ucontrol/uradar/ulocate)")
    return errors, warnings, len(instructions)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path, help="arquivos .mlog completos")
    args = parser.parse_args()
    all_errors = []
    for path in args.files:
        if not path.is_file():
            all_errors.append(f"{path}: arquivo não encontrado")
            continue
        errors, warnings, total = check(path)
        print(f"{path}: {total} instruções")
        for issue in warnings + errors:
            print(issue)
        all_errors.extend(errors)
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
