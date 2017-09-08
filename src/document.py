#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Document(object):
    def __init__(self, rn, title, major_sub, minor_sub, abstract):
        self.id_number = rn
        self.title = title.lower()
        self.major_subjects = major_sub.lower()
        self.minor_subjects = minor_sub.lower()
        self.abstract = abstract.lower()
