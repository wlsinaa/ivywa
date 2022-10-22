class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length = len(strs)
        common_pre = ""
        smallest_index,smallest_len = self.checkSmallestIndex(strs)
        if len(strs) > 1:
            char_order = 0
            for char in strs[smallest_index]:
                number = 0
                for str in strs:
                    if str[char_order] == char:
                        number += 1
                
                
                if number == length:
                    common_pre += char
                if number != length:
                    break
                char_order += 1
        elif len(strs) == 1:
            return strs[0]
        return common_pre
    def checkSmallestIndex(self,strs):
        smallest_index = 0
        smallest_len = 201
        index = 0
        for i in strs:
            if len(i) < smallest_len:
                smallest_index = index
                smallest_len = len(i)
            index += 1
        return smallest_index,smallest_len