Title: Perfect Strangers
Category: assignments
Author: Panos Louridas
Date: 18 September 2017
Template: assignment
publications_src: content/assignments/perfect-strangers/perfect_strangers.bib

Sometimes we want to break apart a set of entities to subsets such
that the entities in each subset have no relationship between them. If
we use a graph to represent the entities and their relationships, the
problem we have to solve is to find subsets of the graph so that the
members of each subset are not neighbours with any other member of the
same subset. This is an instance of an
[independent set](https://en.wikipedia.org/wiki/Independent_set_(graph_theory)):
a set of nodes such that no node is a neighbour of any other node in
the set. An independent set is called a
[maximal independent set](https://en.wikipedia.org/wiki/Maximal_independent_set)
when it is not a subset of any other independent set. In other words,
there is no node outside the set that can be added to the set with the
set remaining independent.

Below you can see the two maximal independent sets of a star graph:

<img src="{attach}star_1.png" width="300">
<img src="{attach}star_2.png" width="300">

Similarly, below you can see the six maximal independent sets of a
cube graph:

<img src="{attach}cube_1.png" width="300">
<img src="{attach}cube_2.png" width="300">

<img src="{attach}cube_3.png" width="300">
<img src="{attach}cube_4.png" width="300">

<img src="{attach}cube_5.png" width="300">
<img src="{attach}cube_6.png" width="300">

Finally, here are four maximal independent sets of the
[Petersen graph](https://en.wikipedia.org/wiki/Petersen_graph) (there
are more):

<img src="{attach}petersen_1.png" width="300">
<img src="{attach}petersen_2.png" width="300">

<img src="{attach}petersen_3.png" width="300">
<img src="{attach}petersen_4.png" width="300">

In this assignment you will implement a program that finds the maximal
independent subsets of a graph.

## Requirements

1. You will write a program called `mis.py` that finds the maximal
   independent subsets of a graph using the algorithm of Johnson,
   Yannakakis and Papadimitriou, described in [@johnson:1988].
2. You can use the [networkx](https://networkx.github.io/) library for
   graph input, output, manipulation, and drawing.
3. You can use anything you want from the
   [Python library](https://docs.python.org/3/library/). 
4. The program must be called as follows:
```
python mis.py [-h] [-d] [-n NAME] [-f FIGURE] input
```

The `input` parameter corresponds to the name of the file containing
the graph. The file will contain the graph in
[networkx adjacency list format](https://networkx.github.io/documentation/stable/reference/readwrite.adjlist.html).

If the user provides the parameter `-d`, the program will display on
screen the graph and each maximal independent subset, similarly to the
way we have presented them here. The actual images produced need not
be exactly the same as the one we have shown, as graph layout depends
on many parameters.

If the user provides the parameter `-n NAME` and `-f FIGURE` each
images will be stored in a file with name `NAME_x.FIGURE`, where `x`
is a positive number. For example, if the user enters `-n cube -f
png`, the program will store the images in the files `cube_1.png`,
`cube_2.png`, and so on.

The parameter `-h` can be used to display a short description of the
program and its parameters.

In all cases, the program output will be the maximal independend
subsets in lexicographic order. So, if we are dealing with the star
graph, the output will be:

```bash
['0']
['1', '10', '2', '3', '4', '5', '6', '7', '8', '9']
```

While if we are dealing with the cube graph, the output will be:

```bash
['(0, 0, 0)', '(0, 1, 1)', '(1, 0, 1)', '(1, 1, 0)']
['(0, 0, 0)', '(1, 1, 1)']
['(0, 0, 1)', '(0, 1, 0)', '(1, 0, 0)', '(1, 1, 1)']
['(0, 0, 1)', '(1, 1, 0)']
['(0, 1, 0)', '(1, 0, 1)']
['(0, 1, 1)', '(1, 0, 0)']
```

## Graph Examples

You can check your program with the following files:

* [Star graph with 10 nodes]({attach}star_graph_10.txt).
* [Cube graph]({attach}cube_graph.txt).
* [Petersen graph]({attach}petersen_graph.txt).
* [Barabási-Albert graph with 15 nodes]({attach}barabasi_albert_graph_15.txt).
* [Powerlaw cluster graph with 20 nodes]({attach}powerlaw_cluster_graph_20.txt).
* [Erdős-Rényi graph with 20 nodes]({attach}erdos_renyi_graph_20.txt).
* [Erdős-Rényi graph with 25 nodes]({attach}erdos_renyi_graph_25.txt).
