import re


def create_import(code):
    if 'from pdb import set_trace' in code:
        return code
    return ["from pdb import set_trace"] + code


def remove_import(code):
    for row in code:
        if re.match('set_trace()', row):
            return code
    return [row for row in code if row != 'from pdb import set_trace']


def remove_set_trace(code):
    return [row for row in code if re.search('set_trace', row) is None]


def remove_breakpoints(code):
    return remove_import(remove_set_trace(code))