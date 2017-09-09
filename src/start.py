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


def main():
    '''
    Código para inicialização e utilização da máquina vetorial.
    O arquivo deve ser dado como parâmetro para ser indexado.
    '''
    docs = []
    k = sys.argv[1]
    queries = extractor.extract_queries(sys.argv[2])
    queries = clearqueries.clear_query_list(queries)

    for argument in sys.argv[3:]:
        docs += extractor.extract_documents(argument)
    clean_docs = cleardocs.clear_document_list(docs)

    inverted_index = tfidf.build_inverted_index(clean_docs)

    avg_precision = 0.
    import pdb; pdb.set_trace()
    ndcg_values = []
    for query in queries:
        query_weight, query_norm = similarity.query_values(inverted_index, query.text)
        accumulators, norms = similarity.accumulate(inverted_index, query.text, query_weight)
        similarities = similarity.similarity(accumulators, norms, query_norm)
        # TODO: get top k docs
        top_k = similarities
        # import pdb; pdb.set_trace()
        avg_precision += metrics.average_precision(top_k, query.relevant_docs)
        ndcg_values.append(metrics.ndcg(top_k, query.relevant_docs, k))

    map_value = avg_precision / len(queries)




if __name__ == '__main__':
    main()
