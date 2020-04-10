# https://www.reddit.com/r/dailyprogrammer/comments/cmd1hb/20190805_challenge_380_easy_smooshed_morse_code_1/
import string
from collections import defaultdict
import pandas as pd


def create_data():
    morse = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..".split()

    letter_map = {a: b for a, b in zip(string.ascii_lowercase, morse)}
    wordlist = open("data/enable1.txt", 'rt').read().splitlines()

    word_to_encoding = dict()
    encoding_to_words = defaultdict(list)

    for word in wordlist[:]:
        encoded_word = "".join([letter_map[char] for char in word])
        word_to_encoding[word] = encoded_word
        encoding_to_words[encoded_word].append(word)

    w2e = pd.DataFrame(word_to_encoding.values(), index=word_to_encoding.keys())
    e2w = pd.DataFrame(encoding_to_words.values(), index=encoding_to_words.keys()).stack().droplevel(1)

    w2e.to_csv('easy-380/w2e.csv', header=False)
    e2w.to_csv('easy-380/e2w.csv', header=False)


def load_data():
    w2e = pd.read_csv('easy-380/w2e.csv', index_col=0, header=None)
    e2w = pd.read_csv('easy-380/e2w.csv', index_col=0, header=None)
    return w2e, e2w


def get_13_words(e2w):
    encoding_groups = e2w.groupby(level=0)

    for groupname, groupdf in encoding_groups:
        if len(groupdf) == 13:
            print("GROUPNAME", groupname)
            print(groupdf)
            break


def find_15_dashes(w2e):
    print(w2e.loc[w2e[1].str.contains('-' * 15)])


def find_21_letter_balanced(w2e):
    corr_length = w2e[w2e.index.str.len() == 21]
    corr_length['BALANCED'] = corr_length[1].str.count('-') == corr_length[1].str.count('\.')
    print(corr_length[corr_length.BALANCED])


def find_13_letter_palindrome(w2e):
    corr_len = w2e[w2e.index.str.len() == 13]
    corr_len.loc[:, 2] = corr_len.apply(lambda r: "".join([ch for ch in reversed(r[1])]), axis=1)
    print(corr_len[corr_len[1] == corr_len[2]])


if __name__ == '__main__':
    # create_data()

    w2e, e2w = load_data()

    # get_13_words(e2w)
    # find_15_dashes(w2e)
    # find_21_letter_balanced(w2e)
    #find_13_letter_palindrome(w2e)


    def find_13_character_encoding_that_isnt_a_word(bruh):
        #corr_encs = e2w[e2w.index.str.len() == 13]

        print(bruh)

        # I'd start by removing characters from the length of 13 and see how many different ways you can
        # 'approach' 13 - that gives you the 13s to test whether they are WORDS







    find_13_character_encoding_that_isnt_a_word(e2w)