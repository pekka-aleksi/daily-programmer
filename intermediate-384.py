# https://www.reddit.com/r/dailyprogrammer/comments/g1xrun/20200415_challenge_384_intermediate_necklace/

"""
For the purpose of this challenge, a k-ary necklace of length n is a sequence of n letters chosen from k options,
e.g. ABBEACEEA is a 5-ary necklace of length 9. Note that not every letter needs to appear in the necklace.
Two necklaces are equal if you can move some letters from the beginning to the end to make the other one,
otherwise maintaining the order. For instance, ABCDE is equal to DEABC.

For more detail, see challenge #383 Easy: Necklace matching.

Today's challenge is, given k and n, find the number of distinct k-ary necklaces of length n.
That is, the size of the largest set of k-ary necklaces of length n such that no two of them are equal to each other.
You do not need to actually generate the necklaces, just count them.

For example, there are 24 distinct 3-ary necklaces of length 4, so necklaces(3, 4) is 24. Here they are:

AAAA  BBBB  CCCC
AAAB  BBBC  CCCA
AAAC  BBBA  CCCB
AABB  BBCC  CCAA
ABAB  BCBC  CACA
AABC  BBCA  CCAB
AACB  BBAC  CCBA
ABAC  BCBA  CACB

You only need to handle inputs such that k**n < 10,000.

necklaces(2, 12) => 352
necklaces(3, 7) => 315
necklaces(9, 4) => 1665
necklaces(21, 3) => 3101
necklaces(99, 2) => 4950

The most straightforward way to count necklaces is to generate all kn patterns,
and deduplicate them (potentially using your code from Easy #383).

This is an acceptable approach for this challenge, as long as you can actually run your program through to completion
for the above examples.

"""

from sympy.ntheory import totient, divisors


def necklaces(k, n):
    list_of_a = divisors(n)

    S = 0

    for a in list_of_a:
        b = n // a
        PHI_A = totient(a)
        S += PHI_A * k ** b

    return S // n


print(necklaces(2, 12))
print(necklaces(3, 7))
print(necklaces(9, 4))
print(necklaces(21, 3))
print(necklaces(99, 2))
print(necklaces(3, 10))
print("-" * 12)
print(necklaces(3, 90))
print(necklaces(123, 18))
print(necklaces(1234567, 6))
print(necklaces(12345678910, 3))
