def f(x):
    y = x * 3
    return y - x

def larger_of_smallest(L1, L2):
    '''(list of int, list of int) -> int

    Return the larger of the smallest value in L1 and the smallest value in
    L2.

    Precondition: L1 and L2 are not empty.

    >>> larger_of_smallest([1, 4, 0], [3, 2])
    2
    >>> larger_of_smallest([4], [9, 6, 3])
    4
    '''

    return max(min(L1),min(L2))

#print(larger_of_smallest([1, 4, 0], [3, 2]))
#print(larger_of_smallest([4], [9, 6, 3]))

def both_start_with(s1, s2, prefix):
    '''(str, str, str) -> bool

    Return True if and only if s1 and s2 both start with the letters in prefix.
    '''
    '''
    return s1.startswith(prefix) and s2.startswith(prefix):
        return True
    else:
        return False
    '''
    return s1.startswith(prefix) and s2.startswith(prefix)

s1='canada'
s2='cat'
prefix='ca'
#print(both_start_with(s1, s2, prefix))


s1='canada'
s2='cement'
prefix='ca'
#print(both_start_with(s1, s2, prefix))


def moogah(a, b):
    '''(str, int) -> str'''
    pass

def frooble(L):
    '''(list of str) -> int
    Precondition: L has at least one element.'''
    pass

def gather_every_nth(L, n):
    '''(list, int) -> list

    Return a new list containing every n'th element in L, starting at index 0.

    Precondition: n >= 1

    >>> gather_every_nth([0, 1, 2, 3, 4, 5], 3)
    [0, 3]
    >>> gather_every_nth(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 2)
    ['a', 'c', 'e', 'g', 'i']
    '''

    result = []
    i = 0
    while i < len(L):
        result.append(L[i])
        i = i+n# CODE MISSING HERE

    return result

#print (gather_every_nth([0, 1, 2, 3, 4, 5], 3))
#print (gather_every_nth(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 2))



def get_keys(L, d):
    '''(list, dict) -> list

    Return a new list containing all the items in L that are keys in d.

    >>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
    ['a', 1]
    '''

    result = []
    for k in d:
        if k in L:
            result.append(k)

    return result

#print (get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'}))

def are_lengths_of_strs(L1, L2):
    '''(list of int, list of str) -> bool

    Return True if and only if all the ints in L1 are the lengths of the strings
    in L2 at the corresponding positions.

    Precondition: len(L1) == len(L2)

    >>> are_lengths_of_strs([4, 0, 2], ['abcd', '', 'ef'])
    True
    '''

    result = True
    for i in range(len(L1)):
        if L1[i]!=len(L2[i]):
            result = False

    return result


#print(are_lengths_of_strs([4, 0, 2], ['abcd', '', 'ef']))


def double_last_value(L):
    '''(list of int) -> NoneType

    Double the value at L[-1].  For example, if L[-1] is 3,
    replace it with 6.

    Precondition: len(L) >= 1.
    '''
    L[-1] = L[-1]*2

L1 = [1, 3, 5]
double_last_value(L1)
#print(L1[-1])




def get_negative_nonnegative_lists(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the negative ints in the
    inner lists of L and the second item is a list of the non-negative ints
    in those inner lists.

    Precondition: the number of rows in L is the same as the number of
    columns.

    >>> get_negative_nonnegative_lists([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]])
    ([-1, -4], [3, 5, 2, 5, 4, 0, 8])
    '''

    nonneg = []
    neg = []
    for row in range(len(L)):
        for col in range(len(L)):
            val = L[row][col]
            if val < 0:
                neg.append(val)
            else:
                nonneg.append(val)

    return (neg, nonneg)

#print(get_negative_nonnegative_lists([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]]))


def count_chars(s):
    '''(str) -> dict of {str: int}

    Return a dictionary where the keys are the characters in s and the values
    are how many times those characters appear in s.

    >>> count_chars('abracadabra')
    {'a': 5, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
    '''
    d = {}

    for c in s:
        if not (c in d):
            # CODE MISSING HERE
            d[c]=1
        else:
            d[c] = d[c] + 1

    return d

#print (count_chars('abracadabra'))
