class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        The equivalent is:
                rows = []
                for i in range(n):   # I don't actually use i
                    rows.append([])
        Use _ when the variable is required syntactically but I don’t need it.
        """
        rows = [[] for _ in range(numRows)]
        i = 0
        rowNums = []
        rowNums.append(i)
        isInc = True
        for _ in s:
            if i < numRows - 1 and isInc:
                i = i + 1
                rowNums.append(i)
                if i == numRows - 1:
                    isInc = False
            elif i == numRows - 1 and not isInc:
                i = i - 1
                rowNums.append(i)
                if i == 0:
                    isInc = True
            elif i < numRows - 1 and not isInc:
                i = i - 1
                rowNums.append(i)
                if i == 0:
                    isInc = True
        i = 0
        for l in s:
            rows[rowNums[i]].append(l)
            if(i < len(rowNums) - 1):
                i = i + 1

        result = ""
        for row in rows:
            for l in row:
                result += l

        return result
