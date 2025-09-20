#일단 첫번째, 입력값이 주어지면 이게 언제 끝나는지를 알아야하지 않나
#무조건, 이것이 계속 인자값이 들어오는데 그걸 끝내는 조건이 있어야할것이다.
#그런거 없다 내가 끊어야한다. ctrl + D!!

#🧠 알고리즘 요약
# 주어진 preorder, inorder로 BST 복원하는 방식:
# preorder[0] → 루트
# 이 루트 값을 inorder에서 찾아
# 왼쪽 서브트리 길이 = 루트 왼쪽에 있는 값 개수
# 그걸 기준으로 preorder / inorder 둘 다 분할
# 재귀 호출

import sys
from dataclasses import dataclass

sys.setrecursionlimit(10**6)
@dataclass
class Node:
    value: int
    left: 'Node' = None
    right: 'Node' = None

# 🔍 왜 분할정복이냐?
# ✔ Divide (분할):
# 전위 순회에서 루트 노드를 뽑고
# 중위 순회에서 루트 위치 기준으로 왼쪽/오른쪽 서브트리를 나눈다
# ✔ Conquer (정복):
# 나눠진 왼쪽/오른쪽 서브트리에 대해 재귀적으로 같은 작업 수행
# ✔ Combine (통합):
# 리턴된 서브트리들을 하나의 트리로 연결 → 최종 BST 완성

#내가 이해한바, pre에서 루트를 알면 order에서 왼쪽 오른쪽 서브트리를 나눌수있다.
#그리고 그 order 주소값을 idx로 담아준다. -> 처음같은 경우는 5
#왜 이 값을 받나 싶었는데 서브트리의 개수를 알려준다.
#pre는 루트노드 빼고 1 + idx전까지 서브노드, in은 idx를 기준으로 좌우로 서브 노드
#그래서 값을 넘길때 1:1+idx까지는 왼쪽 노드,(i+idx 미포함)
# def make_bst(preorder, inorder):
#     #분할 정복 탈출 조건
#     if not preorder or not inorder:
#         return None

#     root_val = preorder[0]
#     root = Node(root_val)

#     idx = inorder.index(root_val)
#     root.left = make_bst(preorder[1:1+idx], inorder[:idx])
#     root.right = make_bst(preorder[1+idx:], inorder[idx+1:])

#     return root

def make_bst(preorder, inorder):
    idx_map = {val: i for i, val in enumerate(inorder)}  # inorder 인덱스 빠르게 찾기
    n = len(preorder)
    
    def helper(pre_l, pre_r, in_l, in_r):
        if pre_l > pre_r or in_l > in_r:
            return None

        root_val = preorder[pre_l]
        root = Node(root_val)

        idx = idx_map[root_val]
        left_size = idx - in_l

        root.left = helper(pre_l + 1, pre_l + left_size, in_l, idx - 1)
        root.right = helper(pre_l + left_size + 1, pre_r, idx + 1, in_r)

        return root

    return helper(0, n - 1, 0, n - 1)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value)

preorder = [int(line) for line in sys.stdin]
#이진 탐색트리의 중위 순회 결과는 오름차순이다
inorder = sorted(preorder)
#두개가 있으면 할수있다.
root = make_bst(preorder,inorder)
postorder(root)