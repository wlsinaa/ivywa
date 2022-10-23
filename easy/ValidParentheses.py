class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return False
        search_dict = {")":"(", "]": "[", "}": "{"}
        stack = []
        for str in s:
            if str in search_dict.values():
                stack.append(str)
                continue
            if len(stack) == 0 and str in search_dict.keys():
                return False
            if stack and search_dict.get(str) != stack[-1]:
                return False
            if stack and search_dict.get(str) == stack[-1]:
                stack.pop()
        return len(stack) == 0
            