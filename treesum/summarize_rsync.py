"""
Parses an rsync changelist, assuming a weight of 1 for every path,
and summarizes the tree. The tree is read from standard input.

For more information, see:

Run without installing:
    cat rsync.txt | python -m treesum.summarize_rsync

Usage:
    summarize_rsync [<n_lines>]

Options:
    <n_lines>   Number of lines to output [default: 10].
"""
import sys

from docopt import docopt

from treesum.rsync_to_paths import rsync_to_paths
from treesum.summarize_paths import summarize_paths


def main():
    lines = sys.stdin.read().splitlines()
    paths = rsync_to_paths(lines)

    n_lines = 10
    if args['<n_lines>'] is not None:
        n_lines = int(args['<n_lines>'])

    summarize_paths(paths, n_lines)


if __name__ == "__main__":
    args = docopt(__doc__)
    main()
