# dfs.py

"""
DFS (Depth First Search)
"""

# 동작 방식
# 1. 방문(탐색)할 노드를 담을 스택(Stack) 자료형 생성
# 2. 각 노드가 방문한 노드인지를 구분할 수 있는 리스트 생성
# 3. 탐색 시작 노드(첫 번째 노드)를 스택에 삽입
# 4. 방문할 노드를 스택에서 하나씩 꺼내기
# 5. 스택에서 꺼낸 노드가 방문한 노드가 아니면,
# 그 인접 노드를 스택에 삽입하고 방문 처리
# 6. 스택에 방문할 노드가 남지 않을 때까지 4~5의 과정을 반복

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

def my_dfs(graph, start_node):
    # 1. 방문(탐색)할 노드를 담을 스택(Stack) 자료형 생성
    stack = list()      # stack = []
    # 2. 각 노드가 방문한 노드인지를 구분할 수 있는 리스트 생성
    visited = list()    # visited = []
    # 3. 탐색 시작 노드(첫 번째 노드)를 스택에 삽입
    stack.append(start_node)
    # 6. 스택에 방문할 노드가 남지 않을 때까지 4~5의 과정을 반복
    while stack:    # while len(stack) == 0 / stack == []
        # 4. 방문할 노드를 스택에서 하나씩 꺼내기
        # print(f" visited: {visited}")
        # print(f" stack: {stack}")
        node = stack.pop()
        # print(node)
        # 5. 스택에서 꺼낸 노드가 방문한 노드가 아니면,
        if node not in visited:
            # 그 인접 노드(갈 수 있는 후보지)를 스택에 삽입하고 
            stack.extend(reversed(graph[node]))
            # stack.extend(graph[node])
            # 방문 처리
            visited.append(node)
    return visited

if __name__ == "__main__":
    print(f"dfs - {my_dfs(myGraph, 'A')}")

    # print(f"dfs - {my_dfs(myGraph, 'I')}")
    # dfs - ['I', 'E', 'B', 'A', 'C', 'F', 'J', 'G', 'D', 'H']

    # reversed() : 시퀀스 데이터를 거꾸로 한 이터레이터 반환
    print(list(reversed(myGraph['A'])))
    # dfs - ['A', 'B', 'E', 'I', 'C', 'F', 'J', 'G', 'D', 'H']
    print(myGraph['A'])
    # dfs - ['A', 'D', 'H', 'C', 'G', 'F', 'J', 'B', 'E', 'I']
    print(list('abc'))  # ['a', 'b', 'c']
    print(bool([]))     # False
    print(bool(['A']))  # True
    print('------------')
