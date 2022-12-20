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
            else:
                if stack and search_dict.get(str) == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack
            