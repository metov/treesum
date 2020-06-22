class Node:
    def __init__(self, name):
        self.name = name
        self.weight = 0
        self.children = {}
        self.parent = None
        self.path = ''

    def __repr__(self):
        return f'{self.path}: {self.weight}'
