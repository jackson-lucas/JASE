class Document(object):
    def __init__(self, rn, title, major_sub, minor_sub, abstract):
        self.id_number = rn
        self.title = title
        self.major_subjects = major_sub
        self.minor_subjects = minor_sub
        self.abstract = abstract
