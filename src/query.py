#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Query(object):
    def __init__(self, qn, text, relevant_docs):
        self.id_number = qn
        self.text = text.lower()
        self.relevant_docs = relevant_docs
