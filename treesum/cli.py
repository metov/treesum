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

from treesum.convert import rsync_to_paths, paths_to_tree, summary_to_strings
from treesum.summarize import summarize_tree


def main():
    args = docopt(__doc__)
    n_lines = int(args["-n"]) or 10

    tree = None
    if args["rsync"]:
        lines = sys.stdin.read().splitlines()
        paths = rsync_to_paths(lines)
        tree = paths_to_tree(paths)

    summary = summarize_tree(tree, n_lines)

    strings = summary_to_strings(summary)
    for s in strings:
        print(s)


if __name__ == "__main__":
    main()
