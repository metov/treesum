"""
Parses an rsync changelist, assuming a weight of 1 for every path,
and summarizes the tree. The tree is read from standard input.

For more information, see:

Run without installing:
    cat rsync.txt | python -m treesum.summarize_rsync

Usage:
    summarize_rsync [options]

Options:
    -n <lines>  Number of lines to output [default: 10].
"""
import sys

from docopt import docopt

from treesum.summarize_paths import summarize_paths


def main():
    args = docopt(__doc__)
    lines = sys.stdin.read().splitlines()
    paths = rsync_to_paths(lines)

    n_lines = int(args["-n"]) or 10
    summarize_paths(paths, n_lines)


if __name__ == "__main__":
    main()


def rsync_to_paths(rsync_lines):
    paths = []

    for s in rsync_lines:
        if s == '':
            continue

        # Remove the transfer type indicators
        _, p = s.split(' ', maxsplit=1)
        paths.append(p)

    return paths