#!/usr/bin/env python3
"""
Just a little experiment, it is not used
"""


def create_efficient_grep_regex(words) -> str:
    print('create_efficient_grep_regex()')
    root = Node('')
    for word in words:
        node = root
        for c in word:
            node = node.add_child(c)
            print(root)
    print(root)
    print(root.to_grep_regex())

    # grep_regex = '\\({}\\)'.format('\\|'.join(list_of_strings))
    # print(grep_regex)
    return 'todo'


class Node:
    def __init__(self, data):
        self.data = data
        self.children = set()

    def __eq__(self, other):
        print(self.data == other.data)
        return self.data == other.data

    def __lt__(self, other):
        return self.data < other.data

    def __hash__(self):
        print('__hash__ of', self.data, 'is ', hash(self.data))
        return hash(self.data)

    def __str__(self):
        s = '(' + self.data
        for child in sorted(self.children):
            s += str(child)
        s += ')'
        return s

    def to_grep_regex(self) -> str:
        s = self.data
        if self.children:
            s += '['
            for child in sorted(self.children):
                s += child.to_grep_regex()
            s += ']'
        else:
            for child in sorted(self.children):
                s += child.to_grep_regex()
        return s

    def add_child(self, obj):
        if isinstance(obj, Node):
            node = obj
        else:
            node = Node(obj)
        self.children.add(node)
        for child in self.children:
            if child == node:
                return child
        return None


create_efficient_grep_regex([i[2] for i in migration_v4_and_v5_data()])  # Using list comprehension
