class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        for u, v in edges:
            if u not in graph:
                graph[u] = []
            graph[u].append(v)
            if v not in graph:
                graph[v] = []
            graph[v].append(u)

            visited = set()

        def dfs(curr):
             if curr == destination:
                return True
             visited.add(curr)
             if curr in graph:
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        if dfs(neighbor):
                            return True
                return False    

        return dfs(source)
        print()

