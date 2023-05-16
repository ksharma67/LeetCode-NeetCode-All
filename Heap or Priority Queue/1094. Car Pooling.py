class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # let's define a minHeap to track the ending time - top of the heap is the trip that ends soonest
        import heapq
        minHeapEndingTime = []

        # let's sort the trips based on their start date in an ascending order, i.e., trips starting earlier show up first
        trips.sort(key = lambda x:x[1])

        for cap, start, end in trips:

            # let's first removing from the heap the ALL the trips that have ended earlier than the start of new trip
            # i.e., process the trips that have already finished
            while minHeapEndingTime and minHeapEndingTime[0][0] <= start:
                capacity += minHeapEndingTime[0][1]
                heapq.heappop(minHeapEndingTime)

            # if the current capacity is not enough for processing the current trip, return False
            if cap>capacity:
                return False
            # otherwise, let's process the current trip
            ## put that passenger on the car, i.e., reduce the capacity
            ## and also add its ending time to the minHeap
            else:
                capacity -= cap
                heapq.heappush(minHeapEndingTime, (end,cap))

        return True
