class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # initialize a dictionary to store the frequency of each 10-letter-long substring
        freq = {}
        # iterate over each 10-letter-long substring in the DNA sequence
        for i in range(len(s) - 9):
            # extract the current 10-letter-long substring
            substring = s[i:i+10]
            # update the frequency count of the current substring in the dictionary
            freq[substring] = freq.get(substring, 0) + 1
        # filter out the substrings that occur less than twice and return the list of the remaining substrings
        return [substring for substring in freq if freq[substring] > 1]
