# Topological Sorting

- Topological sorting is an important concept in computer science, particularly in the field of graph theory. It is used to order the vertices of a directed acyclic graph (DAG) in such a way that for every directed edge 
u→v, vertex u comes before vertex v in the ordering.

# When 

1. **Task Scheduling**: If you have a set of tasks and some tasks must be completed before others, topological sorting can help determine a valid order to perform the tasks.
2. **Course Prerequisites**: Determining a sequence in which courses can be taken based on prerequisites.
3. **Build Systems**: Determining the order of file compilation where some files depend on others.

# Kahn’s Algorithm (Breadth-First Search Based) BFS

1. Calculate in-degrees of all vertices & build graph.
2. Create a queue to store all vertices with in-degree 0.
3. While the queue is not empty, extract a vertex from the queue.
4. Append the extracted vertex to the topological order.
5. For each adjacent vertex, decrease its in-degree by 1.
6. If in-degree of an adjacent vertex becomes 0, add it to the queue.

7. If all vertices are processed, the topological sort is complete.
8. If the graph has a cycle, it won’t be possible to get a valid topological order.

## NOT RECOMMENDED DFS (if from to, reverse result)

1. build graph from to, or in reverse order to from.
2. create visited array & initiate 0.
3. iterate each node, if not visited, call dfs function.
4. in dfs function, if has cycle(== -1) or already visited(== 1), return.
5. mark the current node -1.
6. for each adjacent node, call dfs function.
7. mark the current node 1 and add current node into result.

## Leetcode

- [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/description/)
- [2192. All Ancestors of a Node in a Directed Acyclic Graph](https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/description/)