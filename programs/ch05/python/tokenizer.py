import sys
import re

import regex


def tokenize(text):
    """uses the nonletters to break the text into words
    returns a list of words"""
    # words = re.split("[\s\-,;:!?.’\'«»()–...&‘’“”*—]+", text)
    # words = re.split("[^a-zåàâäæçéèêëîïôöœßùûüÿA-ZÅÀÂÄÆÇÉÈÊËÎÏÔÖŒÙÛÜŸ’\-]+", text)
    # words = re.split("\W+", text)
    words = regex.split("\P{L}+", text)
    words.remove('')
    return words


def tokenize2(text):
    """uses the letters to break the text into words
    returns a list of words"""
    # words = re.findall("[a-zåàâäæçéèêëîïôöœßùûüÿA-ZÅÀÂÄÆÇÉÈÊËÎÏÔÖŒÙÛÜŸ’\-]+", text)
    # words = re.findall("\w+", text)
    words = regex.findall("\p{L}+", text)
    return words


def tokenize3(text):
    """uses the punctuation and nonletters to break the text into words
    returns a list of words"""
    text = re.sub("[^a-zåàâäæçéèêëîïôöœßùûüÿA-ZÅÀÂÄÆÇÉÈÊËÎÏÔÖŒÙÛÜŸ’'()\-,.?!:;]+", "\n", text)
    text = re.sub("([,.?!:;)('-])", r"\n\1\n", text)
    text = re.sub(r"\n+", "\n", text)
    return text


if __name__ == '__main__':
    text = sys.stdin.read()
    words = tokenize(text)
    for word in words:
        print(word)
    text = tokenize2(text)
    print(text)
