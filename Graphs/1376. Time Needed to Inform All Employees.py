class Solution:
	def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

		graph = defaultdict(list)

		for node in range(n):

			graph[manager[node]].append(node)

		def DFS(manager):

			manager_time = informTime[manager]

			employee_time = 0

			for employee in graph[manager]:

				employee_time = max(employee_time, DFS(employee))

			return manager_time + employee_time

		result = DFS(headID)

		return result
