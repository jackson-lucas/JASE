#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import pow, sqrt


# tf(document, term) x idf(term)

# na pesquisa termo a termo para cada termo e irei passar pelos documentos
# a cada documento no termo que passo, tenho idf, termo, documento e tf

# norms = {"docs_id": value}

def query_values(inverted_index, terms):
    weight = {}
    norm = 0
    tf = 1. / len(terms)

    for term in terms:
        if term in inverted_index:
            weight[term] = tf * inverted_index[term][0]
            norm += pow(tf * inverted_index[term][0], 2)

    return weight, sqrt(norm)


def accumulate(inverted_index, terms, terms_weight):
    accumulators = {}
    norms = {}

    for term in terms:
        if term in inverted_index:
            term_values = inverted_index[term]
            idf = term_values[0]

            for document in term_values[1]:
                document_index = document[0]
                document_weight = idf * document[1]

                if document_index in norms:
                    norms[document_index] += pow(document_weight, 2)
                else:
                    norms[document_index] = pow(document_weight, 2)

                if document_index in accumulators:
                    accumulators[document_index] += document_weight * terms_weight[term]
                else:
                    accumulators[document_index] = document_weight * terms_weight[term]

    return accumulators, normalize(norms)

def normalize(norms):
    for key, value in norms.items():
        norms[key] = sqrt(value)
    return norms
# def similarity(query, document):
#     for term in terms:
#         idf = inverted_index[term][0]
#         for element in inverted_index[term][1:]
#             accumulator[element[0]] = w(d,t) * query_weight


    # stemming + stopwords?
def similarity(accumulators, norms, query_norm):
    similarities = []
    for doc in accumulators:
        similarities.append([doc, accumulators[doc] / (norms[doc] * query_norm)])
    return similarities

def main():
    inverted_index = {
        'hey': [0.67, [[600, 0.009259259259259259], [610, 0.037037037037037035]]],
        'yoshi': [0.44, [
            [659, 0.015151515151515152],
            [669, 0.017241379310344827],
            [610, 0.013513513513513514]
        ]]
    }
    terms = ['hey', 'yoshi', 'me']
    query_weight, query_norm = query_values(inverted_index, terms)
    print(query_weight)
    print(query_norm)

    accumulators, norms = accumulate(inverted_index, terms, query_weight)
    print(accumulators)
    print(norms)

    similarities = similarity(accumulators, norms, query_norm)
    print(similarities)

if __name__ == '__main__':
    main()
