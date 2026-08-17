class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap=[-x for x in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap)>1:
            if maxHeap[0]==maxHeap[1]:
                heapq.heappop(maxHeap)
                heapq.heappop(maxHeap)
            else:
                first=heapq.heappop(maxHeap)
                second=heapq.heappop(maxHeap)
                if(first>second):
                    heapq.heappush(maxHeap,second-first)
                else:
                    heapq.heappush(maxHeap,first-second)
        if len(maxHeap)==0:
            return 0
        return -maxHeap[0]
        