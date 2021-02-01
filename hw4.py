from typing import List, Tuple

PLAYER, SCORE = 0, 1
from abc import ABC, abstractmethod


class DataStructure(ABC):
    def __init__(self, S: List[Tuple[str, int]]):
        self.S = S
        if S:
            self.fill_dp_table()

    @abstractmethod
    def lowest_player(self, start, end) -> str:
        """
        Return the lowest scoring player in S[start..end] (inclusive)
        :param start:
        :param end:
        :return:
        """
        pass

    @abstractmethod
    def fill_dp_table(self):
        pass


class Datastructure1(DataStructure):
    """
    TODO : answer parts 1-4
    """

    def __init__(self, S):
        super().__init__(S)

    def lowest_player(self, start: int, end: int) -> str:
        pass  # TODO

    def fill_dp_table(self):
        self.T = {}
        pass #TODO : fill T

    def set_table_entry(self, x: int, i: int, value: Tuple[str, int]):
        self.T[(x, i)] = value


class Datastructure2(DataStructure):
    """
    TODO : answer parts 1-4
    """

    def __init__(self, S):
        super().__init__(S)

    def lowest_player(self, start: int, end: int) -> str:
        pass  # TODO

    def fill_dp_table(self):
        self.T1, self.T2 = {}, {}
        pass # TODO: fill T1 and T2

    def set_T1_entry(self, x: int, i: int, value: Tuple[str, int]):
        self.T1[(x, i)] = value

    def set_T2_entry(self, x: int, i: int, value: Tuple[str, int]):
        self.T2[(x, i)] = value
