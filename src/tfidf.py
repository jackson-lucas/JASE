#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict
import math


def get_idf(doc_list):
    """
    Verifica em quantos documentos cada palavra aparece
    e realiza o cálculo de IDF = log(qnt_documentos / qnt_ocorrencias).

    """
    word_dict = defaultdict(set)
    wd_frequency = defaultdict(int)
    for index, doc in enumerate(doc_list):
        all_words = doc.title + doc.abstract + doc.major_subjects + doc.minor_subjects
        for word in all_words:
            word_dict[word].add(index)
    for key, value in word_dict.items():
        wd_frequency[key] = math.log(len(doc_list) / len(value))
    return wd_frequency


def get_tf(doc_list):
    """
    Verifica quantas vezes uma palavra aparece em um documento e executa
    a operação do TF = quantidade_de_aparições / quantidade_palavras_no_doc.
    """
    tf = defaultdict(list)
    for index, doc in enumerate(doc_list):
        all_words = doc.title + doc.abstract + doc.major_subjects + doc.minor_subjects
        word_dict = defaultdict(int)
        for word in all_words:
            word_dict[word] += 1
        for key, value in word_dict.items():
            tf[key].append([index, value / len(all_words)])
    return tf


def build_inverted_index(doc_list):
    """
    Utiliza os resultados do TF e IDF para formar um dicionário utilizando
    palavras como chave e uma lista de ocorrências, sendo o primeiro elemento
    da lista o IDF de cada palavra e para cada documento na qual a palavra aparece,
    está o valor do TF e o índice do documento. (Índice da lista de documentos original).
    """
    inverted_index = defaultdict(list)
    tf = get_tf(doc_list)
    idf = get_idf(doc_list)

    for key, value in idf.items():
        inverted_index[key].append(value)
        for element in tf[key]:
            inverted_index[key].append(element)
    return inverted_index
