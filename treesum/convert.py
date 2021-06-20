from treesum.Node import Node


def rsync_to_paths(rsync_lines):
    paths = []

    for s in rsync_lines:
        if s == "":
            continue

        # Remove the transfer type indicators
        _, p = s.split(" ", maxsplit=1)
        paths.append(p)

    return paths


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
