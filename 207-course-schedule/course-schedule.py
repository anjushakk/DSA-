class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build adjacency list
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)  # b -> a (must take b before a)

        # Step 2: State array: 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses

        # Step 3: DFS function
        def dfs(course):
            if state[course] == 1:
                return False  # cycle found
            if state[course] == 2:
                return True   # already checked, no cycle from here

            # mark as visiting
            state[course] = 1

            # visit all neighbors
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            # mark as fully processed
            state[course] = 2
            return True

        # Step 4: Start DFS for each unvisited node
        for c in range(numCourses):
            if state[c] == 0:
                if not dfs(c):
                    return False
        return True
