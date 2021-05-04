import collections
import hashlib

block1 = {'b': 2, 'a': 1}
block2 = {'a': 1, 'b': 2}


def sorted_dict_by_key(unsorted_dict):
    return collections.OrderedDict(
        sorted(unsorted_dict.items(), key=lambda d:d[0]))
