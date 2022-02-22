# Problem: Substring with Concatenation of All Words
# URL: https://leetcode.com/problems/substring-with-concatenation-of-all-words/
#
# Problem outline:
# You are given a string s and an array of strings words of the same length.
# Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once,
# in any order, and without any intervening characters.

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        s_length = len(s)
        num_of_words = len(words)
        word_length = len(words[0])
        concat_string_length = num_of_words * word_length

        res = []

        # dictionary with count for each word in word list
        word_dict = {i: words.count(i) for i in words}

        # construct sliding window of length (num of words * wordLength), slide by 1 character in each itern
        for x in range(0, s_length - concat_string_length + 1):
            window = s[x:x + concat_string_length]

            # count occurrence of each word in window
            window_dict = dict.fromkeys(word_dict.keys(), 0)
            for i in range(0, len(window), word_length):
                word = window[i:i + word_length]
                window_dict[word] = window_dict.get(word, 0) + 1

            # if window dict matches word dict, add idx of starting char to result
            if window_dict == word_dict: res.append(x)

        return res