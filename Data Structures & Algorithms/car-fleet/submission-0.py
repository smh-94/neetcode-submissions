class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
            res = []
            z = sorted(zip(position,speed))
            for i in range(len(z)-1,-1,-1):
                position,speed = z[i]
                time = (target - position) / speed
                if len(res) == 0:
                    res.append(time)
                    continue
                
                #we want to ignore any cars that overlap
                #if we approach the list backwards we can 
                #calculate any that may overlap
                if time > res[-1]:
                    res.append(time)
            return len(res)