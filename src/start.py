#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import pprint
import cleardocs
import clearqueries
import extractor
import tfidf
import similarity
import metrics
import crossvalidation


def main():
    '''
    Código para inicialização e utilização da máquina vetorial.
    O arquivo deve ser dado como parâmetro para ser indexado.
    '''
    docs = []
    k = int(sys.argv[1])
    queries = extractor.extract_queries(sys.argv[2])
    queries = clearqueries.clear_query_list(queries)

    #####
    # qnt = int(0.2 * len(queries))
    # training_data, queries = queries[:qnt], queries[qnt:]
    # frequent_words = crossvalidation.get_most_frequent(training_data)
    # n_queries = []
    # for x in range(len(queries)):
    #     new_query = []
    #     for word in queries[x].text:
    #         if word in frequent_words:
    #             new_query.append(word)
    #             new_query.append(word)
    #         else:
    #             new_query.append(word)
    #     queries[x].text = new_query
    #####

    for argument in sys.argv[3:]:
        docs += extractor.extract_documents(argument)
    clean_docs = cleardocs.clear_document_list(docs)

    inverted_index = tfidf.build_inverted_index(clean_docs)

    avg_precision = 0.

    ndcg_values = []
    for query in queries:
        query_weight, query_norm = similarity.query_values(inverted_index, query.text)
        accumulators, norms = similarity.accumulate(inverted_index, query.text, query_weight)

        similarities = similarity.similarity(accumulators, norms, query_norm, k)

        avg_precision += metrics.average_precision(
            [item[0] for item in similarities],
            query.relevant_docs
        )
        ndcg_values.append(metrics.ndcg(similarities, query.relevant_docs, k))

    mean = metrics.mean(ndcg_values)

    mse = metrics.mse(mean, ndcg_values)

    print('ndcg mean', mean)
    print('ndcg mse', mse)

    map_value = avg_precision / len(queries)
    print('map', map_value)


if __name__ == '__main__':
    main()
