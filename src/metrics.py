#!/usr/bin/env python
# -*- coding: utf-8 -*-
from query import Query

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

if __name__ == '__main__':
    main()
