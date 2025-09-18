import heapq


def dijkstra(graph, start):
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0

    heap = [(0, start)]

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("A", 1), ("C", 2), ("D", 5)],
    "C": [("A", 4), ("B", 2), ("D", 1)],
    "D": [("B", 5), ("C", 1)],
}

start_vertex = "A"
shortest_paths = dijkstra(graph, start_vertex)
print(f"Shortest distances from the top {start_vertex}:")
for vertex, distance in shortest_paths.items():
    print(f"{vertex}: {distance}")
