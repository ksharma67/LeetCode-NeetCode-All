class Solution:
    def convert(self, s: str, numRows: int) -> str:
        list_of_items = [[] for i in range(numRows)]
        DOWN = -1
        i = 0
        if numRows == 1:
            return s
        for char in s:
            list_of_items[i].append(char)
            if i == 0 or i == numRows - 1:
                DOWN *= -1
            i += DOWN
        list_of_items = list(chain(*list_of_items))
        return ''.join(list_of_items)
