class Node:
    def __init__(self, name):
        self.name = name
        self.weight = 0
        self.children = {}
        self.parent = None
        self.path = ""

    def __repr__(self):
        return f"{self.path}: {self.weight}"


def summarize_tree(root, max_branches):
    """
    Takes a tree, and builds a summary tree with the given number of branches.

    The input tree is specified with its root. All nodes must provide the
    following methods:
     - .name (name of the node)
     - .children (a dict mapping node name to node instance)
     - .weight (cumulative weight of the node and its subtree)
     - .path (string path leading to the node)

    Explanation of algorithm:
    1. Start with just root node in list of branches and empty list of leaves.
    2. Find best split node (highest weight/only 1 child) and pop it.
    3. Pop out its highest-weight children.
    4. If child has no children, append it to leaves.
    5. If child has children, append it to branches.
    6. If node still has children remaining, add it to branches again.
    7. Repeat steps 2-6 until desired number of branches.

    Steps 2 and 3 would be more natural to implement with PriorityQueue,
    but I found the Python implementation less readable for this use than
    simple sorting.
    """

    leaves = set()
    branches = set()

    def get_clump(node):
        new_branch = Node(node.name)
        new_branch.path = node.path
        new_branch.weight = node.weight
        new_branch.children = sorted(
            list(node.children.values()), key=lambda n: n.weight
        )
        return new_branch

    def pop_child(clump):
        assert len(clump.children) > 0

        child = clump.children.pop()
        clump.weight -= child.weight

        if len(child.children) == 0:
            leaves.add(child)
        else:
            new_clump = get_clump(child)
            branches.add(new_clump)

        if len(clump.children) == 1:
            pop_child(clump)
        elif len(clump.children) > 1:
            branches.add(clump)

    pop_child(get_clump(root))

    while len(branches) + len(leaves) < max_branches and len(branches) > 0:
        # Sort by:
        #  - Whether the branch has a single child (expanding these is free
        #    and should always be done)
        #  - Weight of children (excluding already revealed children)
        best_node = max(branches, key=lambda n: (len(n.children) == 1, n.weight))
        branches.remove(best_node)
        pop_child(best_node)

    return leaves | branches
