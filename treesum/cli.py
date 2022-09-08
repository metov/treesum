"""
Summarize trees from the command line.

Parses a tree in one of the following formats and summarizes it:
* paths -- list of paths; as produced by eg. ls. Assumes weight of 1.
* rsync -- rsync changeset, assumes a weight of 1 for every path

The tree is read from standard input, results will go to standard output. See
https://github.com/metov/treesum for more information.

Usage:
    treesum (-h | --help)
    treesum paths [options]
    treesum rsync [options]

Options:
    -n <lines>  Number of lines to output [default: 10].
"""
import sys

from docopt import docopt

from treesum.convert import paths_to_tree, rsync_to_paths, summary_to_strings
from treesum.summarize import summarize_tree


def main():
    args = docopt(__doc__)
    n_lines = int(args["-n"]) or 10

    lines = sys.stdin.read().splitlines()
    if args["paths"]:
        tree = paths_to_tree(lines)
    elif args["rsync"]:
        paths = rsync_to_paths(lines)
        tree = paths_to_tree(paths)
    else:
        # We should never end up here because docopt validates arguments
        tree = None

    summary = summarize_tree(tree, n_lines)

    strings = summary_to_strings(summary)
    for s in strings:
        print(s)


if __name__ == "__main__":
    main()
