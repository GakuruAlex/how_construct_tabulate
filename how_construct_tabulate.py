from typing import List
def how_construct_tabulate(target_word: str, words: List[str]) -> List[List[str]]:
    how_construct: List[List[str]] = [False for _ in range(len(target_word) + 1)]
    how_construct[0] = [[]]


