import heapq

def dijkstra_heapq(start, edges):
    INF = 10 ** 10  
    num_of_nodes = len(edges) + 1
    result = [INF] * num_of_nodes;result[start] = 0
    visited = [False] * num_of_nodes
    heap = [(0, start)] 
    while heap:
        cur_cost, cur_node = heapq.heappop(heap)
        if visited[cur_node]:
            continue
        visited[cur_node] = True
        for next_cost, next_node in edges[cur_node]:
            if not visited[next_node]:
                if result[next_node] > result[cur_node] + next_cost:
                    result[next_node] = result[cur_node] + next_cost
                    heapq.heappush(heap, (result[next_node], next_node))
    return result


"""if __name__ == "__main__":
    # Step 1: Get input values
    n, m = map(int, input().split())
    edges = [[] for i in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        edges[a].append((c, b))
        edges[b].append((c, a))

    # Step 2: Calculate distance and output results
    dist = dijkstra_heapq(1, edges)
    for i in range(1,n+1):
        print(dist[i] if dist[i] != 10**10 else -1)"""