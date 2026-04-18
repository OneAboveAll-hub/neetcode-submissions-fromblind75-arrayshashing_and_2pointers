from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self,strs):
        group_arr=defaultdict(list)
        for word in strs:
            key=''.join(sorted(word))
            group_arr[key].append(word)
        return list(group_arr.values())