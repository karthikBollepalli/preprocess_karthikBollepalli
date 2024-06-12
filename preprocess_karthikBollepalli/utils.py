import re
import os
import sys
#import pandas as pd
import numpy as np
import spacy
from spacy.lang.en.stop_words import STOP_WORDS as stopwords

#1 word counts
def _get_wordcounts(x):
	length=len(str(x).split())
	return length


#char counts
def _get_charcounts(x):
	s= x.split()
	x=''.join(s)
	return len(x)


#avg word len

def _get_avg_wordlength(x):
	count=_get_charcounts(x)/_get_wordcounts(x)
	return count

#stopwords

def _get_stopwords_counts(x):
	l=len([t for t in x.split() if t in stopwords])
	return


def _get_hastag_counts(x):
	l=len([t for t in x.split() if t.startswith('#')])
	return l

def _get_hastag_counts(x):
	l=len([t for t in x.split() if t.startswith('@')])
	return l
def _get_digit_counts(x):
	return len([t for t in x.split() if t.isdigit()])

def _get_uppercase_counts(x):
	return len([t for t in x.split() if t.isupper()])

def _get_cont_exp(x):
	contractions={
	"can't": "cannot",
	"won't": "will not",
	"I'm": "I am",
	"you're": "you are",
	"he's": "he is",
	"she's": "she is",
	"it's":"it is",
	"we're":"we are",
	"they're":"they are",
	"I've":"I have",
	"you've":"you have",
	"we've":"we have",
	"they've":"they have",
	"don't":"do not",
	"didn't":"did not"}
	if type(x) is str:
		for key in contractions:
			value=contractions[key]
			x=x.replace(key, value)
		return x
	else:
		return x



