#!/usr/bin/env python
# Copyright (c) 2014 Cisco Systems, Inc.
import subprocess
from itertools import chain
import os
import fnmatch
import sys


def _get_script_dirname():
    return os.path.dirname(os.path.abspath(__file__))


def _expand_path(*args):
    return os.path.join(_get_script_dirname(), *args)


def get_python_files():
    tests = []

    paths = ('infra/modules/ipsla', 'tests')
    for root, _, files in chain.from_iterable(
            os.walk(_expand_path(path)) for path in paths):
        for items in fnmatch.filter(files, '*.py'):
            tests.append('%s/%s' % (root, items))
    return tests


def _get_command(test):
    return ['pylint', test, '--rcfile=infra/modules/pylint.conf', '-f', 'html']


def run_pylint(tests):
    """
    Run pylint on the the given files.
    """
    return all(list(run_pylint_file(t) for t in tests))


def run_pylint_file(test):
    """
    Run pylint on given file.
    """
    cmd = _get_command(test)
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)

    sys.stdout.write(proc.communicate()[0])
    sys.stdout.flush()
    return proc.returncode == 0


def main():
    """
    Entry point.
    """
    tests = get_python_files()
    exit(0 if run_pylint(tests) else 1)

main()
