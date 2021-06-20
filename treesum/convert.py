from treesum.Node import Node


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


def rsync_to_paths(rsync_lines):
    paths = []

    for s in rsync_lines:
        if s == "":
            continue

        # Remove the transfer type indicators
        _, p = s.split(" ", maxsplit=1)
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
