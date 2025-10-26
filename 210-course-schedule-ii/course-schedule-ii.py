from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: Build adjacency list
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = [0] * numCourses   # 0 = unvisited, 1 = visiting, 2 = done
        result = []
        self.has_cycle = False

        def dfs(node):
            if visited[node] == 1:   # back edge -> cycle
                self.has_cycle = True
                return
            if visited[node] == 2:   # already processed
                return

            visited[node] = 1        # mark as visiting

            for nei in graph[node]:
                dfs(nei)
                if self.has_cycle:
                    return

            visited[node] = 2        # mark as done
            result.append(node)      # add after exploring all dependencies

        # Step 2: Run DFS on all nodes
        for i in range(numCourses):
            if visited[i] == 0:
                dfs(i)
                if self.has_cycle:
                    return []

        # Step 3: Reverse to get correct topological order
        return result[::-1]
