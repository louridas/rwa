Title: Musical Rhythms
Category: assignments
Author: Panos Louridas
Date: 2 August 2017
Template: assignment
publications_src: content/assignments/musical-rhythms/musical_rhythms.bib

Consider the following problem. You want to create a binary sequence
of $n$ bits, out of which $k$ are one (and the rest are of course
zero). You also want the ones to be as evenly spread as possible among
the zeroes. If $k$ divides $n$, then the solution is straightforward;
we just divide the ones among the zeros. For example, for $n = 16$ and
$k = 4$ we get the sequence:
```text
[ 1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 ]
```

The problem gets more interesting when $n$ and $k$ are relatively
prime, that is, when the only common divisor of $n$ and $k$ is the
number 1.

So suppose that we have $n = 13$ and $k = 5$. As we have $13 - 5 = 8$,
we start by creating a sequence with 5 ones and 8 zeroes:
```text
[ 1 1 1 1 1 0 0 0 0 0 0 0 0 ]
```
We can treat this sequence as 13 sequences of one bit each:
```text
[ [1] [1] [1] [1] [1] [0] [0] [0] [0] [0] [0] [0] [0] ]
```
We distribute the zeroes so that we get five sequences of two bits
each, and three sequences of one bit:
```text
[ [1 0] [1 0] [1 0] [1 0] [1 0] [0] [0] [0] ]
```
Then we distribute the remaining zeroes in the same way, so that we
get:
```text
[ [1 0 0] [1 0 0] [1 0 0] [1 0] [1 0] ]
```
Now we distribute the `[1 0]` sequences, which leads to:
```text
[ [1 0 0 1 0] [1 0 0 1 0] [1 0 0] ]
```
The process ends when the remainder (that is, the sequences with the
smallest number of bits) is exactly one, or we do not have any more
zeroes to distribute. Then we concatenate the result. In our example,
we get:
```text
[ 1 0 0 1 0 1 0 0 1 0 1 0 0 ]
```

We can interpret the above sequence as a rhythm, where each digit is a
unit of time and each `0` shows a silence (or unaccented note), while
each `1` shows an attack, or an onset of a note. Then, for different
relatively prime $n$ and $k$ we get a wealth of rhythms that are used
in world music. Two examples:

* The rhythm with $k = 3$ and $n = 7$, $[\ 1\ 0\ 1\ 0\ 1\ 0\ 0\ ]$, is
  the Ruchenitza (Rachenitsa, Ръченица, Rŭchenitsa, Râčenica) rhythm
  that is used in Bulgarian folk musing and in the
  [Pink Floyd](https://en.wikipedia.org/wiki/Pink_Floyd) song
  [Money](https://en.wikipedia.org/wiki/Money_(Pink_Floyd_song)).
* The rhythm with $k = 5$ and $n = 9$,
  $[\ 1\ 0\ 1\ 0\ 1\ 0\ 1\ 0\ 1\ ]$,
  is a popular Arabic rhythm called Agsag Samai. If started on the second
  onset, it is drum pattern used by the
  [Venda people](https://en.wikipedia.org/wiki/Venda_people) in South
  Africa, as well as a Romanian folk dance. It is also the rhythm
  pattern of the Greek Sigaktistos.
  [ This is according to the bibliography. The author, being Greek,
  does not know any rhythm by that name. A student, Marios Pitsalidis,
  suggested that perhaps the correct name is Sigkathistos, Συγκαθιστός,
  meaning "sitting together," which probably makes sense. If somebody
  knows more, please contact the author. ] The Turkish Samai Aktsak
  follows the same pattern as well. If started on the third onset, it
  is the rhythmical pattern of the Turkish Nawahiid rhythm.

### Euclidean Rhythms and Euclidean Strings

The way we outlined for constructing these rhythmical sequences for
different $k$ and $n$ follows Euclid's algorithm for finding the
greatest common divisor of two numbers. Indeed, if `euclid(n, k)` is a
function implementing the algorithm, we would have `euclid(8,5) =
euclid(5,3) = euclid(3,2) = euclid(2,1) = euclid(1,0) = 1`, which
corresponds to the steps we made. For that reason, these rhythms are
called
[Euclidean rhythms](https://en.wikipedia.org/wiki/Euclidean_rhythm). 

To describe a Euclidean rhythm we use the $E(k, n)$ notation, where
$k$ is the number of onsets and $n$ is the length of the rhythm, for
example $E(5, 9)$. We can also use another notation, in which we count
the intervals until the next onset, so we have $E(5, 9) = (22221)$,
because there are two between the first and the second onset in
$[\ 1\ 0\ 1\ 0\ 1\ 0\ 1\ 0\ 1\ ]$, and so on. Another rhythm is $E(5, 12)$,
which corresponds to $[\ 1\ 0\ 0\ 1\ 0\ 1\ 0\ 0\ 1\ 0\ 1\ 0\ ]$ and
can also be written $(32322)$, as you may check. The second notation
is called *adjacent-inter-onset-interval vector*, or *interval vector*
for short. In essence, an interval vector is a sequence of positive
integers.

If we have a rhythm written in interval vector notation, say, `P =
(p[0], p[1] , ... , p[n−1])`, then if we increase `p[0]` by one and
decrease `p[n-1]` by one, we will get a new interval vector. If this
new interval vector can also result by rotating the first one, then we
say that we have a *Euclidean string*. For example, $E(4, 9)$ is
$[\ 1\ 0\ 1\ 0\ 1\ 0\ 1\ 0\ 0\ ]$ and $(2223)$. If we increase the first
digit by one and we decrease the last digit by one, we get $(3222)$,
which we can get by rotating the first string, so the rhythm is also a
Euclidean string.

If we take the reverse string from an interval vector, that is, if we
read it from the end to the start, and we the reverse string is also a
Euclidean string, then we say that we have a *reverse Euclidean
string*. For example, $E(4, 11)$ is
$[\ 1\ 0\ 0\ 1\ 0\ 0\ 1\ 0\ 0\ 1\ 0\ ]$ and $(3332)$. The reverse
string of the interval vector is $(2333)$, which is a Euclidean
string, so $(3332)$ is a reverse Euclidean string.

For more information on Euclidean rhythms check [@toussaint:2005];
[Godfried Toussaint](https://en.wikipedia.org/wiki/Godfried_Toussaint)
was the one that introduced the concept and has written a whole book
on the geometry of musical rhythm [@toussaint:2013]. See also
[@demaine:2009] for a well-developed overview. For more information on
Euclidean strings, see [@ellis:2003].

### Distance between Rhythms

How different are two rhythms? If we take two rhythms are binary
sequences, then one metric that we can use to gauge the distance
between two strings of equal length is the number of positions in
which the corresponding elements of the sequences are different. This
is called
[Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance). If
`s1` and `s2` are two sequences, the following function (adapted for
Python 3 from
the Wikipedia article), calculates the Hamming distance:

```python
def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(bool(ord(ch1) - ord(ch2)) for ch1, ch2 in zip(s1, s2))
```

For example, the rhythm $E(4, 9) = [\ 1\ 0\ 1\ 0\ 1\ 0\ 1\ 0\ 0\ ]$
has a Hamming distance of one from the rhythm $E(5, 9) =
[\ 1\ 0\ 1\ 0\ 1\ 0\ 1\ 0\ 1\ ]$ and a Hamming distance of three from
the rhythm $E(7, 9) = [\ 1\ 0\ 1\ 1\ 1\ 0\ 1\ 1\ 1\ ]$.

That said, the Hamming distance is not the best way to measure the
similarity of rhythms. There are better metrics for that purpose
[@toussaint:2004] [@toussaint:2013], but we'll stick to the Hamming
distance for now.

In this assignment you will develop a program that handles and
manipulates Euclidean rhythms.

### Requirements

1. You will write a program called `musical_rhythms.py`, which will
   work with Euclidean rhythms.
2. The program will read, upon start, the dictionary of rhythms that
   is stored in the file
   [musical_rhythms.json]({attach}musical_rhythms.json). The file
   should be stored in the same directory as the program itself. The
   contents of the file are in
   [JSON (JavaScript Object Notation)](http://www.json.org/), so you
   should use the
   [Python `json` library](https://docs.python.org/3/library/json.html).
3. Your program must be called as follows:
```bash
python musical_rhythms.py [-s SLOTS] [-p PULSES] [-r RECOGNIZE] [-l LIST_RHYTHMS]
```

### Output

#### Create a Rhythm

If the user gives the parameters `-s SLOTS` and `-p PULSES`, then
`SLOTS` and `PULSES` will be positive integers. The program will then
return information on the rhythm that corresponds to these parameters, where
`PULSES` is the number of onsets and `SLOTS` is the length of the
rhythm. To do that, the program will look up the rhythm in the rhythm
dictionary. If it finds it there, it will display the information
stored for that rhythm; otherwise, it will just display the rhythm. In
the next line, if the rhythm corresponds to a Euclidean string or to a
reverse Euclidean string, it will display an appropriate message.

Examples:

```bash
python musical_rhythms.py -s 12 -p 6
E(6,12) = [101010101010] = (222222)
```

```bash
python musical_rhythms.py -s 12 -p 7
E(7,12) = [101101011010] = (2122122) It is a common West African bell pattern. For example, it is used in the Mpre rhythm of the Ashanti people of Ghana. Started on the seventh (last) onset, it is a Yoruba bell pattern of Nigeria, a Babenzele pattern of Central Africa, and a Mende pattern of Sierra Leone.
```

```bash
python musical_rhythms.py -s 16 -p 5
E(5,16) = [1001001001001000] = (33334) It is the Bossa-Nova rhythm necklace of Brazil. The actual Bossa-Nova rhythm usually starts on the third onset as follows: [1001001000100100]. However, other starting places are also documented in world music practices, such as [1001001001000100].
It is a Euclidean string.
```

```bash
python musical_rhythms.py -s 9 -p 5
E(5,9) = [101010101] = (22221) It is a popular Arabic rhythm called Agsag-Samai. Started on the second onset, it is a drum pattern used by the Venda in South Africa, as well as a Rumanian folk-dance rhythm. It is also the rhythmic pattern of the Sigaktistos rhythm of Greece, and the Samai aktsak rhythm of Turkey. Started on the third onset, it is the rhythmic pattern of the Nawahiid rhythm of Turkey.
It is a reverse Euclidean string.
```

As you can see, the first thing to appear will be rhythm in the form
$E(k, n)$; then as a binary string inside square brackets; then as
interval vector inside parentheses; and then any description found in
the rhythms dictionary. The final line will contain a message if it is
a Euclidean or a reverse Euclidean string.

#### Rhythm Recognition

If the user gives the parameter `-r RECOGNIZE`, then `RECOGNIZE` will
be a rhythm represented as a binary string and the program should
identify it, if it is a Euclidean rhythm, and print out any
information available. If it is not a Euclidean rhythm, it should
print an appropriate message.

Examples:

```bash
python musical_rhythms.py -r 101101011010
E(7,12) = [101101011010] = (2122122) It is a common West African bell pattern. For example, it is used in the Mpre rhythm of the Ashanti people of Ghana. Started on the seventh (last) onset, it is a Yoruba bell pattern of Nigeria, a Babenzele pattern of Central Africa, and a Mende pattern of Sierra Leone.
```

```bash
python musical_rhythms.py -r 10010010010
E(4,11) = [10010010010] = (3332) It is the metric pattern used by Frank Zappa in his piece titled Outside Now.
It is a reverse Euclidean string.
```

```bash
python musical_rhythms.py -r 10010010011
Not a Euclidean rhythm.
```

#### Show Similar Rhythms

If the user gives the parameter `-l LIST_RHYTHMS`, then `LIST_RHYTHMS`
will be a rhythm given as a binary string and the program will display
all rhythms of the same length, ordered in increasing Hamming distance
and number of onsets.

Examples:

```bash
python musical_rythms.py -l 101010100
Distance = 0
E(4,9) = [101010100] = (2223) It is the Aksak rhythm of Turkey. It is also the metric pattern used by Dave Brubeck in his piece Rondo a la Turk.
It is a Euclidean string.
Distance = 1
E(5,9) = [101010101] = (22221) It is a popular Arabic rhythm called Agsag-Samai. Started on the second onset, it is a drum pattern used by the Venda in South Africa, as well as a Rumanian folk-dance rhythm. It is also the rhythmic pattern of the Sigaktistos rhythm of Greece, and the Samai aktsak rhythm of Turkey. Started on the third onset, it is the rhythmic pattern of the Nawahiid rhythm of Turkey.
It is a reverse Euclidean string.
Distance = 2
E(2,9) = [100010000] = (45)
It is a Euclidean string.
Distance = 3
E(1,9) = [100000000] = (9)
Distance = 3
E(3,9) = [100100100] = (333)
Distance = 3
E(7,9) = [101110111] = (2112111) It is the Bazaragana rhythmic pattern of Greece.
It is a reverse Euclidean string.
Distance = 4
E(6,9) = [101101101] = (212121)
Distance = 4
E(8,9) = [101111111] = (21111111)
It is a reverse Euclidean string.
```

```bash
python musical_rythms.py -l 1001001001000
Distance = 0
E(4,13) = [1001001001000] = (3334)
It is a Euclidean string.
Distance = 2
E(2,13) = [1000001000000] = (67)
It is a Euclidean string.
Distance = 3
E(1,13) = [1000000000000] = (13)
Distance = 5
E(3,13) = [1000100010000] = (445)
It is a Euclidean string.
Distance = 5
E(5,13) = [1001010010100] = (32323) It is a rhythm from the FYROM which is also played by starting it on the fourth onset as follows: [1010010010100].
Distance = 5
E(9,13) = [1011011011011] = (212121211)
It is a reverse Euclidean string.
Distance = 6
E(6,13) = [1010101010100] = (222223) It is the rhythm of the dance Mama Cone pita from the FYROM. Started on the third onset, it is the rhythm of the dance Postupano Oro from the FYROM, as well as the Krivo Plovdivsko Horo of Bulgaria.
It is a Euclidean string.
Distance = 7
E(7,13) = [1010101010101] = (2222221)
It is a reverse Euclidean string.
Distance = 7
E(11,13) = [1011111011111] = (21111211111)
It is a reverse Euclidean string.
Distance = 8
E(8,13) = [1011010110101] = (21221221)
Distance = 8
E(10,13) = [1011101110111] = (2112112111)
It is a reverse Euclidean string.
Distance = 8
E(12,13) = [1011111111111] = (211111111111)
It is a reverse Euclidean string.
```

### Notes on Implementation

The rhythms can be constructed using an algorithm with repeated
division, following the logic of Euclid's algorithm. That algorithm is
called the Bjorklund algorithm, after the name of the researcher that
noticed such patterns in neutron experiments in the
[Spallation Neutron Source](https://en.wikipedia.org/wiki/Spallation_Neutron_Source)
[@bjorklund:1999].

*Do not use the Bjorklund algorithm to solve the assignment. Develop
 your solutions manipulating lists, as is described here.*

If you want to verify your results, you may wish to check the
Euclidean rhythms in [@toussaint:2005] and [@demaine:2009].
