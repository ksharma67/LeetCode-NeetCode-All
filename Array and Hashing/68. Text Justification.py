class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        list1 = [[words[0]]]
        length = [len(words[0])]

        for i in range(1, len(words)):
            if length[-1] + len(list1[-1]) + len(words[i]) > maxWidth:
                list1.append([words[i]])
                length.append(len(words[i]))
            else :
                list1[-1].append(words[i])
                length[-1] += len(words[i])

        for i in range(len(list1) - 1):
            space = len(list1[i]) - 1
            
            if space == 0:
                list1[i] = list1[i][0].ljust(maxWidth, " ")
            else :
                odd_space = (maxWidth-length[i]) % space
                for k in range(odd_space):
                    list1[i][k] += " " 
                sp = " " * ((maxWidth-length[i]) // space)
                list1[i] = sp.join(list1[i])

        list1[-1] = (" ".join(list1[-1])).ljust(maxWidth, " ")

        return list1
