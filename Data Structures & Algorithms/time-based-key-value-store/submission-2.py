class TimeMap:

    def __init__(self):
        self.store={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=[]
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res=""
        vals = self.store.get(key, [])
        left=0
        right=len(vals)-1
        mid=(left+right)//2
        while (left<=right):
            if vals[mid][1]<=timestamp:
                res=vals[mid][0]
                left=mid+1
            else:
                right=mid-1
            mid=(left+right)//2
        return res
