#!/usr/bin/python
# coding=utf-8

from __future__ import print_function
import argparse
import subprocess
import sys

class Processor(object):
    """
    :type str markup
    :type str working_directory
    """

    def __init__(self, working_directory='.', markup='@tsincluder'):
        self.markup = markup
        self.working_directory = working_directory

    def process(self, line):
        markup = self.markup.strip() + ' '
        if markup in line:
            prefix = line[0:line.rfind(markup)]

            shell_command = line.replace(prefix, '').replace(markup, '')
            text = subprocess.Popen(shell_command, shell=True, stdout=subprocess.PIPE).stdout.read()
            rows = text.split('\n')
            line = ''
            for row in rows:
                if len(row.strip()) != 0:
                    line += prefix + row.strip() + '\n'

        return line

def main(arguments):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="input file", type=argparse.FileType('r'))
    args = parser.parse_args(arguments)

if __name__ == "__main__":
    main(sys.argv)
