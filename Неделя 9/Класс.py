from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, list):
        self.list = deepcopy(list)

    def __str__(self):
        rows = []
        for row in self.list:
            rows.append('\t'.join(map(str, row)))
        return '\n'.join(rows)

    def size(self):
        return len(self.list), len(self.list[0])


exec(stdin.read())
