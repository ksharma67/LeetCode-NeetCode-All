class FreqStack:

    def __init__(self):
        self.freq_levels = [[]]
        self.freq_counter = Counter()

    def push(self, val: int) -> None:
        if val not in self.freq_counter:
            self.freq_counter[val] = 0
            self.freq_levels[0].append(val)
        else:
            self.freq_counter[val] += 1
            if self.freq_counter[val] == len(self.freq_levels):
                self.freq_levels.append([])
            self.freq_levels[self.freq_counter[val]].append(val)

    def pop(self) -> int:
        res = self.freq_levels[-1].pop()
        self.freq_counter[res] -= 1
        if self.freq_counter[res] < 0:
            del self.freq_counter[res]
        if len(self.freq_levels[-1]) == 0:
            self.freq_levels.pop()
        return res
        
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
