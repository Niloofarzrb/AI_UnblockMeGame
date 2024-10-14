from Board import Board
from Problem import Problem
from State import State
from Search import Search
import ast

if __name__ == '__main__':
    test_path = './tests/test1.txt'
    file = open(test_path, 'r')
    p = ''
    for i in file.readlines():
        a = i.replace('\n', '')
        a = a.replace(' ', '')
        p += a
    lst = ast.literal_eval(p)
    s = Search.bfs(Problem(State(Board(len(lst), len(lst[0]), lst), None, 0)))
    s.print_path()
