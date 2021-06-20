# `treesum`: Parsimonious Tree Summary
Do you like looking at trees, but hate scrolling?

`treesum` takes a complex tree, and tries to show the most information without printing too many lines.

# Usage
`treesum` can be used in multiple ways:
* Construct a suitable tree and call `treesum.summarize.summarize_tree` directly. (allows you to set weights)
* Construct a list of string paths and call `treesum.summarize_paths.summarize_paths` (reads from pipe and prints to console)

The input is a list of every node with a weight. `treesum` will expand branches with highest weight and collapse those with lowest. The idea is that weights are a measure of how much you care about those nodes of the tree: They can be file sizes, diff deltas, how much you like each item, whatever you want. If you don't provide weights, all nodes will be assumed to have a weight of 1.

Summarize rsync changelist: `summarize_rsync < rsync.txt`

# Install
Clone the repo and run `pip install .` in the repo root.
