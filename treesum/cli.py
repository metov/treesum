"""
Summarize trees from the command line.

Parses a tree in one of the following formats and summarizes it:
* rsync -- rsync changeset, assumes a weight of 1 for every path

The tree is read from standard input, results will go to standard output. See
https://github.com/metov/treesum for more information.

Usage:
    treesum (-h | --help)
    treesum rsync [options]

Options:
    -n <lines>  Number of lines to output [default: 10].
"""
import sys

from docopt import docopt

from treesum.summarize_paths import summarize_paths
from treesum.convert import rsync_to_paths


def main():
    args = docopt(__doc__)
    n_lines = int(args["-n"]) or 10

    if args["rsync"]:
        lines = sys.stdin.read().splitlines()
        paths = rsync_to_paths(lines)

        summarize_paths(paths, n_lines)


if __name__ == "__main__":
    main()
