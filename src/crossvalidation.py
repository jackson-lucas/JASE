#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict


def get_most_frequent(queries, qnt=0.2):
    word_dict = defaultdict(int)
    for query in queries:
        query = query.text
        for word in query:
            word_dict[word] += 1
    most_frequent_words = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    quantity = int(qnt * len(most_frequent_words))
    return [el[0] for el in most_frequent_words[:quantity]]
