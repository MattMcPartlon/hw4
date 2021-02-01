import os
from collections import defaultdict
from typing import List, DefaultDict, Tuple

import numpy as np

from hw4 import DataStructure

PLAYER, SCORE = 0, 1


def parse_golfer_names() -> np.ndarray:
    root = os.getcwd()
    if not root.endswith('tests'):
        if not root.endswith('hw4'):
            print('please run test scripts from the root (hw4) directory')
            exit(1)
        root = os.path.join(root, 'tests')
    golfer_name_path = os.path.join(root, 'golfer_names.txt')
    return np.loadtxt(golfer_name_path, dtype=str, delimiter='\n')


def get_random_players_and_scores(n: int) -> List[Tuple[str, int]]:
    golfer_names = parse_golfer_names()
    selection = np.random.randint(0, len(golfer_names), n).astype(int)
    golfer_names = golfer_names[selection]
    scores = np.round(np.random.normal(72, 2.75, n)).astype(int)
    return list(zip(golfer_names, scores))


def get_lowest_score_dict(S: List[Tuple[str, int]]) -> DefaultDict:
    n = len(S)
    lowest_tuples = defaultdict(set)
    for i in range(n):
        lowest_ij = defaultdict(list)
        lowest_score = S[i][SCORE]
        for j in range(i, n):
            if lowest_score >= S[j][SCORE]:
                lowest_ij[S[j][SCORE]].append(S[j][PLAYER])
            lowest_score = min(lowest_score, S[j][SCORE])
            lowest_tuples[(i, j)] = set(lowest_ij[lowest_score])
    return lowest_tuples


def get_intervals(n: int, m: int) -> List[Tuple[int, int]]:
    intervals = np.random.randint(0, n, 2 * m)
    return [(min(i, j), max(i, j)) for i, j in zip(intervals[0::2], intervals[1::2])]


def test_lowest_player(data_structure: DataStructure):
    ns = [0, 2, 4, 10, 100, 1000]
    ms = [0, 3, 5, 8, 50, 100]
    for n, m in zip(ns, ms):
        S = get_random_players_and_scores(n)
        lowest_score_dict = get_lowest_score_dict(S)
        intervals = get_intervals(n, m)
        data_struct = data_structure(S)
        for (s, e) in intervals:
            assert s <= e
            expected_lowest_players = lowest_score_dict[(s, e)]
            actual_lowest_player = data_struct.lowest_player(s, e)
            if actual_lowest_player not in expected_lowest_players:
                print(f'processing interval {s}..{e}, n={n}')
                print(f'player "{actual_lowest_player}" not one of the players in {expected_lowest_players}')
                print(f'players/scores for this interval {S[s:e + 1]}')
                exit(1)
    print('all tests passed!')
