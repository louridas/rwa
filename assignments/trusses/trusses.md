Title: Finding Trusses
Category: assignments
Author: Panos Louridas
Date: 31 July 2017
Template: assignment
publications_src: content/assignments/trusses/trusses.bib

Thanks to
[Edward Snowden](https://en.wikipedia.org/wiki/Edward_Snowden) we
know much more than we used to about
the way intelligence services work. So,
[one of the documents he leaked](
https://www.documentcloud.org/documents/2702948-Problem-Book-Redacted.html)
concerns the research activities of
[GCHQ (Government Communications Headquarters)](https://en.wikipedia.org/wiki/Government_Communications_Headquarters).
Reading the document, we can see that they are interested in detecting
specific structures in graphs. The nodes in these graphs are people
and the edges are links between them. The links may be communication
channels such as phone calls, e-mails, etc. A structure that seems of
particular interest to GCHQ is the *k-truss*, an idea that seems to
come from the
[National Security Agency](https://en.wikipedia.org/wiki/National_Security_Agency), see
[@cohen:2008] and [@cohen:2009].


A k-truss in a graph is a subset of the graph such that every edge in
the subject is supported by at least $k - 2$ other edges that form
triangles with that particular edge. In other words, every edge in the
truss must be part of $k - 2$ triangles made up of nodes that are part
of the truss. For example, in the following figures you can see two
3-trusses in a graph. By definition, 3-trusses are the triangles of a
graph.

<img src="{attach}truss_3_1.png" width="300">
<img src="{attach}truss_3_2.png" width="300">

Similarly, in the following figure you can see a 4-truss of a graph.
4-trusses are sets of such that every edge is part of two triangles
composed of nodes in the truss.

<img src="{attach}truss_4.png" width="400">

A k-truss is *maximal* when it is not a subgraph of another k-truss.
Here we want to find the maximal k-trusses of a graph.

### Maximal Truss Finding Algorithm

How do we find the maximal k-trusses of a graph? One way is with the
following algorithm:

```
find_maximal_k_trusses(g, k):
    until no change do
        for each edge e = (a,b) in g:
            if (size(intersection(neighbours(a), neighbours(b)) < k - 2:
                remove e from g
    return the connected components of the remaining graph
```

In the above algorithm, `g` is the graph and `k` is the truss size.
The function `neighbours(a)` gives us the neighbours of node `a`, the
function `intersection(s1, s2)` finds the intersection of two sets
`s1` and `s2`, and the function `size(s)` finds the size of the set
`s`. The idea behind the algorithm is to reduce the graph so that in
the end the connected components of the graph are maximal k-trusses.
This algorithm is not very efficient, better ones do exist, but it
will do for this assignment.

### Requirements

1. You will write a program named `trusses.py` that finds the
   maximal k-trusses of a graph.
2. You will represent the graph with adjacency lists, not with an
   adjacency matrix.
3. You will not use ready-made graph libraries.
4. Your program must be called as follows:
```bash
python trusses.py graph_file size_of_truss
```

The `graph_file` argument specifies the name of the file where the
graph is stored (that does not mean that the name of the file is
`graph_file`, it is just a stand-in). The file will have the
following format:
```
0 2
1 3 
2 4
...
```
that is, it contains lines each one of which has two numbers. If
the two numbers are `x` and `y`, the graph will have an edge between
the nodes `x` and `y`. The graph is undirected, so we assume that
there always exists the reverse edge from `y` to `x`. The nodes
will be always consecutive integers starting from 0, i.e.,
0, 1, 2, ... You cannot assume that the file contents are ordered
in any way.

The argument `size_of_truss` is the truss dimension, i.e., the $k$ in
k-truss.

### Output

The program will print out the k-trusses of the graph, if they exist,
in the form:
```bash
[0, 1, 9]
[8, 10, 16]
```
That is, each line
will contain a truss inside square brackets, with the nodes separated by
commas and whitespace. Every k-truss will be output only once, and
the k-trusses will be output in order.

### Examples

If the user gives:
```bash
python trusses.py graph_1.txt 3
```
with the file [graph_1.txt]({attach}graph_1.txt), which actually corresponds
to the graph of the first two figures with the 3-trusses above, the
output will be the one we gave just above:
```bash
[0, 1, 9]
[8, 10, 16]
```

If the user gives:
```
python trusses.py graph_2.txt 4
```
with the file [graph_2.txt]({attach}graph_2.txt), the output will be:
```bash
[3, 8, 9, 18]
[7, 11, 15, 21]
```

If the user gives:
```
python trusses.py graph_3.txt 5
```
with the file [graph_3.txt]({attach}graph_3.txt), the output will be:
```bash
[2, 5, 8, 9, 13, 14]
```

If the user gives:
```
python trusses.py graph_4.txt 3
```
with the file [graph_4.txt]({attach}graph_4.txt), the output will be:
```bash
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
```
that is, all the nodes in the graph, whereas if the user gives:
```
python trusses.py graph_4.txt 4
```
with the same file, the output will be:
```bash
[0, 1, 3, 4, 5, 6, 9, 11]
```
which corresponds to the 4-truss figure we gave at the beginning.

If you want to try a bigger example, if the user gives:
```
python trusses.py barabasi_albert_graph_1500.txt 4
```
using the file
[graph_5.txt]({attach}graph_5.txt), which contains 1500 nodes,
the output will be:
```bash
[0, 3, 4, 5, 7, 9, 11, 15, 26]
```
