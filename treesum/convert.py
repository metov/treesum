from metovlogs import get_log

from treesum.summarize import Node

log = get_log(__name__)


def paths_to_tree(paths, w=1):
    """
    Convert a list of /-delimited string paths to a tree. Terminal /-es are
    ignored.
    """

    # Strings to tree
    root = Node("<root>")
    for s in paths:
        path = s.split("/")

        # Ignore terminal slashes
        if s.endswith("/"):
            path.pop()

        # Adjust tree weights
        root.weight += w
        n = root
        for p in path:
            if p not in n.children:
                n.children[p] = Node(p)
                n.children[p].parent = n

            c = n.children[p]
            c.weight += w
            c.path = f"{n.path}/{p}"
            n = c

    return root


import re

RE_RSYNC_SEP = re.compile("([<>ch.*][<>.*+?\w]{10})|(\*deleting ) ")


def rsync_to_paths(rsync_lines):
    paths = []

    # Trim header lines & find column offset
    head = None
    filename_start_col = None
    for i, s in enumerate(rsync_lines):
        if m := RE_RSYNC_SEP.search(s):
            filename_start_col = m.end() + 1
            head = i
            log.debug(f"{head=}\n{m}\n{s}")
            break

    head_trimmed = rsync_lines[head:]

    # Check column offset & trim footer lines
    foot = None
    for i, s in enumerate(head_trimmed):
        if m := RE_RSYNC_SEP.search(s):
            assert filename_start_col - 1 == m.end()
        else:
            foot = i
            log.debug(f"{foot=}\n{s}")
            break

    assert len(head_trimmed) - foot < 100, "Seems like too many lines in footer?"
    both_trimmed = head_trimmed[:foot]

    # Find likely column offset
    for s in both_trimmed:
        # Remove the transfer type indicators
        p = s[filename_start_col:]
        paths.append(p)

    return paths


def summary_to_strings(summary_tree):
    """Convert summary tree to a list of human-readable strings."""
    sum_lines = []
    for i in summary_tree:
        s = f"{i.weight} {i.path}"
        if len(i.children) > 0:
            # Mini-BFS to find all children
            n_leaves = 0
            q = list(i.children)
            while len(q) > 0:
                n = q.pop()
                if len(n.children) > 0:
                    q.extend(n.children.values())
                else:
                    n_leaves += 1

            s += f"/... [ {len(i.children)} branches, " f"{n_leaves} leaves not shown ]"

        sum_lines.append(s)

    # Print in lexicographic order
    sum_lines = sorted(sum_lines, key=lambda s: s.split(" ", maxsplit=1)[1])

    return sum_lines
