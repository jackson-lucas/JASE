#!/usr/bin/env python
# -*- coding: utf-8 -*-
from query import Query
from stemming.porter2 import stem
import string


def apply_stemming(query_list):
    clean_queries = []
    for query in query_list:
        query.text = [stem(w) for w in query.text]
        clean_queries.append(query)
    return clean_queries


def remove_punctuation(query_list):
    "Remove pontuações presentes no queryo."
    clean_queries = []
    exclude = string.punctuation

    for query in query_list:
        query.text = ''.join([l for l in query.text if l not in exclude])
        clean_queries.append(query)
    return clean_queries


def remove_stopwords(query_list):
    "Remove stopwords inglesas obtidas a partir do NLTK."
    def remove_from_query(query):
        query.text = [w for w in query.text.split() if w not in stopwords]
        return query
    stopwords = []

    with open('./aux/stopwords.txt') as f:
        for el in f:
            stopwords.append(el.strip())

    clean_queries = []

    for query in query_list:
        clean_queries.append(remove_from_query(query))
    return clean_queries


def clear_query_list(query_list):
    query_list = remove_punctuation(query_list)
    query_list = remove_stopwords(query_list)
    query_list = apply_stemming(query_list)
    return query_list


def main():
    new_query = Query(
        1,
        """
        What are the effects of calcium on the physical properties of mucus
        from CF patients?
        """,
        []
    )
    x = remove_punctuation([new_query])
    print(x[0].__dict__)
    x = remove_stopwords(x)
    print(x[0].__dict__)
    x = apply_stemming(x)
    print(x[0].__dict__)


if __name__ == '__main__':
    main()
