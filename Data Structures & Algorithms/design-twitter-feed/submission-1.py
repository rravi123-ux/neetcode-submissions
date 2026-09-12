class Twitter:

    def __init__(self):
        self.time=0
        self.followMap=defaultdict(set)
        self.tweetMap=defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.tweetMap[userId].append((self.time,tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        users=self.followMap[userId] | {userId}
        heap=[]
        for user in users:
            if self.tweetMap[user]:
                ind=len(self.tweetMap[user])-1
                time,tweet=self.tweetMap[user][ind]
                heapq.heappush(heap,(-time,tweet,user,ind))
        feed=[]
        while heap and len(feed)<10:
            negtime,tweet,user,ind=heapq.heappop(heap)
            feed.append(tweet)
            ind-=1
            if ind>=0:
                time,tweet=self.tweetMap[user][ind]
                heapq.heappush(heap,(-time,tweet,user,ind))
        return feed




    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
