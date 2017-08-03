Title: Musical Rhythms
Category: assignments
Author: Panos Louridas
Date: 2 August 2017
Template: assignment
publications_src: content/assignments/musical_rhythms/musical_rhythms.bib

Consider the following problem. You want to create a binary sequence
of $n$ bits, out of which $k$ are one (and the rest are of course
zero). You also want the ones to be as evenly spread as possible among
the zeroes. If $k$ divides $n$, then the solution is straighforward;
we just divide the ones among the zeros. For example, for $n = 16$ and
$k = 4$ we get the sequence:
```
[1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0]
```

The problem gets more interesting when $n$ and $k$ are relatively
prime, that is, when the only common divisor of $n$ and $k$ is the
number 1.

So suppose that we have $n = 13$ and $k = 5$. As we have $13 - 5 = 8$,
we start by creating a sequence with 5 ones and 8 zeroes:
```
[ 1 1 1 1 1 0 0 0 0 0 0 0 0]
```
We can treat this sequence as 13 sequences of one bit each:
```
[ [1] [1] [1] [1] [1] [0] [0] [0] [0] [0] [0] [0] [0] ]
```
We distribute the zeroes so that we get five sequences of two bits
each, and three sequences of one bit:
```
[ [1 0] [1 0] [1 0] [1 0] [1 0] [0] [0] [0] ]
```
Then we distribute the remaining zeroes in the same way, so that we
get:
```
[ [1 0 0] [1 0 0] [1 0 0] [1 0] [1 0] ]
```
Now we distribute the `[1 0]` sequences, which leads to:
```
[ [1 0 0 1 0] [1 0 0 1 0] [1 0 0] ]
```
The process ends when the remainder (that is, the sequences with the
smallest number of bits) is exactly one, or we do not have any more
zeroes to distribute. Then we concatenate the result. In our example,
we get:
```
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
  is a popular arabic rhythm called Agsag Samai. If started on the second
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
say that we have a *Euclidean string*. For example, $E(4, 9) =
[\ 1\ 0\ 1\ 0\ 1\ 0\ 1\ 0\ 0\ ] = (2223)$. If we increase the first
digit by one and we decrease the last digit by one, we get $(3222)$,
which we can get by rotating the first string, so the rhythm is also a
Euclidean string.

If we take the reverse string from an interval vector, that is, if we
read it from the end to the start, and we the reverse string is also a
Euclidean string, then we say that we have a *reverse Euclidean
string*. For example, $E(4, 11) = [\ 1\ 0\ 0\ 1\ 0\ 0\ 1\ 0\ 0\ 1\ 0\ ]
= (3332)$. The reverse string of the interval vector is $(2333)$,
which is a Euclidean string, so $(3332)$ is a reverse Euclidean
string.

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

### 
