#!/usr/bin/env python
# -*- coding: utf-8 -*-
from query import Query
from math import log

def getKey(doc):
    return doc[1]

def precision(retrieved_docs, relevant_docs, k=-1):
    relevant_retrieved_docs = 0.
    if k == -1:
        k = len(relevant_docs)

    for doc in retrieved_docs:
        if doc in relevant_docs:
            relevant_retrieved_docs += 1
    return relevant_retrieved_docs / k

# source: https://en.wikipedia.org/wiki/Information_retrieval#Average_precision
def average_precision(retrieved_docs, relevant_docs):
    avg_precision = 0.
    for index in range(len(retrieved_docs)):
        if retrieved_docs[index] in relevant_docs:
            avg_precision += precision(retrieved_docs, relevant_docs, index + 1)
    return avg_precision / len(relevant_docs)

# source: https://en.wikipedia.org/wiki/Information_retrieval#Mean_average_precision
def mean_average_precision(queries, retrieved_docs):
    queries_avg_precision = 0.
    for query in queries:
        queries_avg_precision += average_precision(retrieved_docs, query.relevant_docs)
    return queries_avg_precision / len(queries)

def dcg(retrieved_docs, relevant_docs, k):
    cumulative_gain = 0.

    if k > len(relevant_docs):
        k = len(relevant_docs)

    for index in range(1, k):
        if retrieved_docs[index] in relevant_docs:
            cumulative_gain += 1. / log(index+1, 2)

    if retrieved_docs[0] in relevant_docs:
        cumulative_gain += 1

    return cumulative_gain

def idcg(retrieved_docs_n_scores, relevant_docs, k):
    cumulative_gain = 0.
    docs_n_scores = sorted(retrieved_docs_n_scores, reverse=True, key=getKey)

    if k > len(relevant_docs):
        k = len(relevant_docs)

    for index in range(1, k):
        if docs_n_scores[index][0] in relevant_docs:
            cumulative_gain += 1. / log(index+1, 2)

    if docs_n_scores[index][0] in relevant_docs:
        cumulative_gain += 1

    return cumulative_gain

def ndcg(retrieved_docs_n_scores, relevant_docs, k):
    retrieved_docs = [item[0] for item in retrieved_docs_n_scores]

    dcg_value = dcg(retrieved_docs, relevant_docs, k)
    idcg_value = idcg(retrieved_docs_n_scores, relevant_docs, k)
    try:
        return dcg_value / idcg_value
    except ZeroDivisionError:
        import pdb; pdb.set_trace()

def main():
    p_value = precision([1,2,3], [2,3,4,5,6], 3)
    print(p_value)

    avgp_value = average_precision([1,2,3,7], [2,3,4,5,6])
    print(avgp_value)

    queries = []
    queries.append(Query(1, 'Ohayo', [2,3,4,5,6]))
    queries.append(Query(2, 'Track', [2,5,7]))
    map_value = mean_average_precision(queries, [1,2,3,7])
    print(map_value)

    docs_n_scores = [[1,0.5],[5,0.9],[7,0.6]]
    docs_n_scores = sorted(docs_n_scores, reverse=True, key=getKey)
    ndcg_value = ndcg(docs_n_scores, [1,2,3,7], 3)
    print(ndcg_value)


if __name__ == '__main__':
    main()
