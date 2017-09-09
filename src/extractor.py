#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import pprint
from document import Document
from query import Query

def is_relevant_data(data):
    if '' == data.strip():
        return False
    return True

def extract_queries(file_path):
    data = []
    with open(file_path) as f:
        data = f.readlines()

    queries = []
    for index in range(len(data)):

        if data[index].startswith('QU'):
            text = data[index].split(' ', 1)[1]
        elif data[index].startswith('RD'):
            documents = []
            relevances = ' '.join(data[index].split()).split()[1:]
            for rv_index in range(len(relevances)):
                if rv_index % 2 == 0:
                    documents.append(relevances[rv_index])

            index += 1
            should_continue = is_relevant_data(data[index]);
            while(should_continue):
                line = ' '.join(data[index].split()).split()
                for rv_index in range(len(line)):
                    if rv_index % 2 == 0:
                        documents.append(line[rv_index])

                index += 1
                if index >= len(data):
                    break
                should_continue = is_relevant_data(data[index])

            queries.append(Query(len(queries), text, documents))

    return queries

def extract_documents(file_path):
    """
    Função utilizada para extrair dados dos documentos passados. Retorna
    uma lista de elementos da classe documento contendo as informações dos
    documentos, removendo siglas e ajustando whitespaces e convertendo palavras
    para letras minúsculas.
    """
    def remove_whitespaces(title, major_sub, minor_sub, abstract):
        title = " ".join(title.split()).lower()
        major_sub = " ".join(major_sub.split()).lower()
        minor_sub = " ".join(minor_sub.split()).lower()
        abstract = " ".join(abstract.split()).lower()
        return title, major_sub, minor_sub, abstract

    data = []
    with open(file_path) as f:
        data = f.readlines()

    i = 0
    rn = 1

    size = len(data)

    document_list = []

    title = major_sub = minor_sub = abstract = ""

    genenerate_doc = False

    while i < size:
        if data[i].startswith("TI"):
            title += data[i][2:]
            i += 1
            while data[i].startswith(" "):
                title += data[i]
                i += 1
        elif data[i].startswith("MJ"):
            major_sub += data[i][2:]
            i += 1
            while data[i].startswith(" "):
                major_sub += data[i]
                i += 1
        elif data[i].startswith("MN"):
            minor_sub += data[i][2:]
            i += 1
            while data[i].startswith(" "):
                minor_sub += data[i]
                i += 1
        elif data[i].startswith("AB"):
            abstract += data[i][2:]
            i += 1
            while data[i].startswith(" "):
                abstract += data[i]
                i += 1
            genenerate_doc = True
        elif genenerate_doc:
            new_document = Document(rn, *remove_whitespaces(title, major_sub,
                                    minor_sub, abstract))
            document_list.append(new_document)
            title = major_sub = minor_sub = abstract = ""
            genenerate_doc = False
            rn += 1
        else:
            i += 1
    return document_list


def main():
    document_list = extract_documents(sys.argv[1])
    for document in document_list:
        pprint.pprint(document.__dict__)

    queries = extract_queries('cfc/cfquery')
    import pprint
    for query in queries[-7:]:
        pprint.pprint(query.text)
        pprint.pprint(query.relevant_docs)

if __name__ == '__main__':
    main()
