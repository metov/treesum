# Parsimonious Tree Summary
Do you like looking at trees, but hate scrolling?

`treesum` takes a complex tree, and tries to show the most information without printing too many lines.

The tree is expected to consist of nodes, each of which has a weight. `treesum` will expand branches with highest weight and collapse those with lowest. The weights are a measure of how much you care about different nodes of the tree: They can be file sizes, diff deltas, how much you like each item, whatever you want. If you don't provide weights, all nodes will be assumed to have a weight of 1.

## Usage
Summarize list of paths:
```shell script
find . | treesum paths
```

Summarize `rsync` changelist:
```shell script
rsync -raihP --dry-run /source/dir /dest/dir > rsync.txt
treesum rsync < rsync.txt
```

You can, of course, also use `treesum` as a library. The basic method is `treesum.summarize.summarize_tree` which takes a tree constructed from `treesum.summarize.Node` instances. If you don't want to do this by hand, `treesum.convert` contains methods for constructing a tree from various text representations. Try looking at the implementation of `treesum.cli` for an example of how to do this.

## Install
Run: `pip install treesum`
