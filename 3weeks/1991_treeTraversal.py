from dataclasses import dataclass
@dataclass
class Node:
    value:int
    left: 'Node' = None
    right: 'Node' = None

def build_tree(relations):

    build_frame = {} #연결을 위한 딕셔너리
    for parent, left, right in relations:
        if parent not in build_frame:
            build_frame[parent] = Node(parent)
        if left != '.':
            if left not in build_frame:
                build_frame[left] = Node(left)
            build_frame[parent].left = build_frame[left]
        if right != '.':
            if right not in build_frame:
                build_frame[right] = Node(right)
            build_frame[parent].right = build_frame[right]
    return build_frame[relations[0][0]]

def preorder(node):
    if node:
        print(node.value, end='')
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end='')
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end='')

relations = []
n = int(input())
for _ in range(n):
    parent, left, right = map(str, input().split())
    relations.append([parent, left, right])

root = build_tree(relations)

preorder(root)
print()
inorder(root)
print()
postorder(root)
print()

