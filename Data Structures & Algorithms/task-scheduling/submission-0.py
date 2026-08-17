class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts=Counter(tasks)
        maxHeap=[-i for i in counts.values()]
        heapq.heapify(maxHeap)
        queue=deque()
        time=0
        while maxHeap or queue:
            time+=1
            if maxHeap:
                count=heapq.heappop(maxHeap)
                count+=1
                if count<0:
                    queue.append((count,time+n))
            if queue and queue[0][1]==time:
                count,ready=queue.popleft()
                heapq.heappush(maxHeap,count)
        return time