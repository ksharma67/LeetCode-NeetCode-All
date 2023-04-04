import heapq as hp
class SeatManager:

    def __init__(self, n: int):
        self.i=0
        self.n=n
        self.seats=[]
    def reserve(self) -> int:
        if(self.seats):
            return hp.heappop(self.seats)
        else:
            if self.i<self.n:
                self.i=self.i+1
                return self.i;
            else:
                return -1

    def unreserve(self, seatNumber: int) -> None:
        hp.heappush(self.seats,seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
