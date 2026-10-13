# bfs.py

"""
BFS (Breadth First Search)
"""
# 동작방식
# 1. 방문(탐색)할 노드를 담을 큐(Queue) 자료형 생성
# 2. 각 노드가 방문한 노드인지를 구분할 수 있는 리스트 생성
# 3. 탐색 시작 노드(첫 번째 노드)를 큐에 삽입
# 4. 방문할 노드를 큐에서 하나씩 꺼내기 (삽입된 순서대로)
# 5. 큐에서 꺼낸 노드가 방문한 노드가 아니면, 
# 그 인접 노드를 큐에 삽입하고 방문 처리
# 6. 큐에 방문할 노드가 남지 않을 때까지 4~5의 과정을 계속 반복

myGraph = {'A': ['B', 'C', 'D'], 
          'B': ['A', 'E'], 
          'C': ['A', 'F', 'G'],
          'D': ['A', 'H'],
          'E': ['B', 'I'],
          'F': ['C', 'J'],
          'G': ['C'],
          'H': ['D'],
          'I': ['E'],
          'J': ['F']
          }

def my_bfs(graph, start_node):
    # 1. 방문(탐색)할 노드를 담을 큐(Queue) 자료형 생성
    queue = list()
    # 2. 각 노드가 방문한 노드인지를 구분할 수 있는 리스트 생성
    visited = list()
    # 3. 탐색 시작 노드(첫 번째 노드)를 큐에 삽입
    queue.append(start_node)
    # 6. 큐에 방문할 노드가 남지 않을 때까지 4~5의 과정을 계속 반복
    while queue:
        # 4. 방문할 노드를 큐에서 하나씩 꺼내기 (삽입된 순서대로)
        node = queue.pop(0)
        # 5. 큐에서 꺼낸 노드가 방문한 노드가 아니면, 
        if node not in visited:
            # 그 인접 노드를 큐에 삽입하고
            queue.extend(graph[node])
            # 방문 처리
            visited.append(node)
    return visited

if __name__ == "__main__":
    print(f"bfs - {my_bfs(myGraph, 'A')}")

    print('-------------')

