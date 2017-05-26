#!/home/sasha/anaconda3/bin/python
lst = [1, [2, 3], 4,[[6, 7]]]
from collections import Iterable

def flatten (lst):
    for x in lst:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x

lst_flatten = (list(flatten(lst)))
print(lst_flatten)

