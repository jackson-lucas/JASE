#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import pprint
import cleardocs
import extractor
import tfidf


def main():
    '''
    Código para inicialização e utilização da máquina vetorial.
    O arquivo deve ser dado como parâmetro para ser indexado.
    '''
    docs = []
    for argument in sys.argv[1:]:
        docs += extractor.extract_documents(argument)
    clean_docs = cleardocs.clear_document_list(docs)
    x = tfidf.build_inverted_index(clean_docs)
    pprint.pprint(x)


if __name__ == '__main__':
    main()
