palindrome
==========

Effectively find palindromes from a list of words using a smart hash to split input up to different search trees.

Method
======
A hash splits a word and it's palindrome to the same bucket where 
a simple search list is located. Could easily be extended to use a search tree
but if the bucketing is sparse enough it will be faster to just do linear search.

F is the symmetric hash and f is atomic hash for the object. ' is an operation
such that a'' = a. (+) is a commutative binary operation.

F(a) = {def} = f(a) (+) f(a') = f(a'') (+) f(a') = f(a') (+) f(a'') = F(a')

