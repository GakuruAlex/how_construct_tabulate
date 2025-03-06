from copy import deepcopy
import pprint
from typing import List

def how_construct_tabulate(target_word: str, words: List[str]) -> List[List[str]]:
    how_construct: List[List[str]] = [False for _ in range(len(target_word) + 1)]
    how_construct[0] = []

    for index in range(len(target_word)):
        for word in words:
            if word == target_word[index: index + len(word)] and how_construct[index] != False:

                if not how_construct[index + len(word)]:
                    how_construct[index + len(word)] = how_construct[index][:]
                    how_construct[index +  len(word)].append(word)
                else:
                    in_index: List[str] = deepcopy(how_construct[index])
                    in_index.append(word)
                    how_construct[index + len(word)].extend([in_index])
    return how_construct[len(target_word)]



def main()-> None:
    target_word: str = 'abcdef'
    words: List[str] = ['ab', 'cd', 'ef', 'abc', 'abcd']
    how_construct = how_construct_tabulate(target_word=target_word, words=words)
    pprint.pprint(how_construct)

if __name__ == "__main__":
    main()
