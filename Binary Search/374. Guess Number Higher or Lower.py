# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        mid=n//2
        start=0
        end=n
        x=guess(mid)
        while(x!=0 and start<end):
            print(mid)
            if(x==1):
                start = mid+1
                mid = (start+end)//2
                x = guess(mid)
            else:
                end = mid-1
                mid = (start+end)//2
                x = guess(mid)
        return mid
