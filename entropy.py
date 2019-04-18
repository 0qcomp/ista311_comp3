'''
File: comp3.py
Author: Justin Nichols
Instructor: Dylan Murphy
Assignment: Computational Hw 3

Purpose: computes the entropy-per-character of a source text using ngrams

Abbreviations:
rv <- random variable
pmf <- probability mass function
epc <- entropy per character
'''

import numpy as np
import math
from testing_dicts import *


def entropy(outcomes2probs):
    '''
    computes the entropy of an rv

    @param dict outcomes2probs. Each key is one of the rv's outcomes, and the
    value is the normalized frequency of that outcome

    @return np.float64 entropy. The entropy of the rv
    '''
    entropy = 0
    for outcome in outcomes2probs:
        prob = outcomes2probs[outcome]
        info = -np.log2(prob)
        entropy += info * prob

    return entropy


def ngram_dist(fname, n):
    '''
    computes the normalized frequencies of all ngrams in a source-text

    @param Str fname. The file-name for the source-text

    @param int n. The size of the ngrams

    @return dict<Str, float> ngrams2probs. Each key is an ngram in the source-
    text, and the value is the normlized frequency of that ngram
    '''    
    ngrams2probs = {}
    text = open(fname).read()
    
    for i in range(len(text) - n):
        ngram = text[i:i + n]
        ngrams2probs[ngram] = 1 if (ngram not in ngrams2probs) else \
                              ngrams2probs[ngram] + 1
        
    normalize(ngrams2probs)
    return ngrams2probs


def normalize(outcomes2probs):
    '''
    normalizes a pmf

    Param: outcomes2probs, a dict. Each key is an outcome, and its
               corresponding value is the probability of that outcome.
               In other words, a pmf

    Return: None    
    '''
    # calcuating the normalizing constant
    total_pre_normal_prob = 0
    for outcome in outcomes2probs:
        pre_normal_prob = outcomes2probs[outcome]
        total_pre_normal_prob += pre_normal_prob

    # dividing each probability by the normalizing constant
    for outcome in outcomes2probs:
        pre_normal_prob = outcomes2probs[outcome]
        normal_prob = pre_normal_prob / total_pre_normal_prob
        outcomes2probs[outcome] = normal_prob


def epc(fname, n):
    '''
    uses ngrams to approximate the epc in a source-text

    @param Str fname. The file-name for the source-text

    @param int n. The size of the ngrams

    @return float. The epc of the source-text
    '''
    assert n > 0
    return entropy(ngram_dist(fname, n)) - entropy(ngram_dist(fname, n-1))


def main():
    for i in range(1,4):
        print(epc("hp6.txt", i))
