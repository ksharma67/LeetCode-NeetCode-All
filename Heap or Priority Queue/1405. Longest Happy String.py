class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # use a heap to keep the most frequent first
        max_heap = []
        if a != 0:
            heappush(max_heap, (-a, 'a'))
        if b != 0:
            heappush(max_heap, (-b, 'b'))
        if c != 0:
            heappush(max_heap, (-c, 'c'))

        # append to a list instead of string, because O(1) in Python
        # while appending to strings are O(N)
        string_list = []

        while max_heap:
            freq, letter = heapq.heappop(max_heap)

            if len(string_list) >= 2 and string_list[-2] == string_list[-1] == letter:
                if not max_heap:
                    # no more letters left
                    return ''.join(string_list)
                else:
                    # try the next most frequent letter
                    next_freq, next_letter = heapq.heappop(max_heap)
                    next_freq += 1
                    string_list.append(next_letter)
                    if next_freq != 0:
                        heapq.heappush(max_heap, (next_freq, next_letter))
                    # still need to push the first letter back into heap
                    heapq.heappush(max_heap, (freq, letter))
            else:
                # need to do + because negative max_heap
                freq += 1
                string_list.append(letter)
                if freq != 0:
                    heapq.heappush(max_heap, (freq, letter))

        return ''.join(string_list)
