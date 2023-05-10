class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        
        # sort the servers in order of weight, keeping index 
        server_avail = [(w,i) for i,w in enumerate(servers)]
        heapify(server_avail)
        tasks_in_progress = []
        res = []
        st=0
        for j,task in enumerate(tasks):
            #starting time of task
            st = max(st,j)
            
            # if any server is not free then we can take start-time equal to end-time of task
            if not server_avail:
                st = tasks_in_progress[0][0]
            
            # pop the completed task's server and push inside the server avail
            while tasks_in_progress and tasks_in_progress[0][0]<=st:
                heapq.heappush(server_avail,heappop(tasks_in_progress)[1])
                
            # append index of used server in res
            res.append(server_avail[0][1])
            
            # push the first available server in "server_avail" heap to "tasks_in_progress" heap
            heapq.heappush(tasks_in_progress,(st+task,heappop(server_avail)))
        
        return res
