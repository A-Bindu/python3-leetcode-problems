class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        #word1=
        #word2=
        return all(starmap(eq, zip_longest(chain.from_iterable(word1), chain.from_iterable(word2))))

