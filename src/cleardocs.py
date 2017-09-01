from document import Document
from stemming.porter2 import stem
import string


def apply_stemming(document_list):
    "Aplica stemming em cada palavra dos campos do documento."
    clean_docs = []
    for doc in document_list:
        doc.title = [stem(w) for w in doc.title]
        doc.major_subjects = [stem(w) for w in doc.major_subjects]
        doc.minor_subjects = [stem(w) for w in doc.minor_subjects]
        doc.abstract = [stem(w) for w in doc.abstract]
        clean_docs.append(doc)
    return clean_docs


def remove_punctuation(document_list):
    "Remove pontuações presentes no documento."
    clean_docs = []
    exclude = string.punctuation

    for doc in document_list:
        doc.title = ''.join([l for l in doc.title if l not in exclude])
        doc.major_subjects = ''.join([l for l in doc.major_subjects if l not in exclude])
        doc.minor_subjects = ''.join([l for l in doc.minor_subjects if l not in exclude])
        doc.abstract = ''.join([l for l in doc.abstract if l not in exclude])
        clean_docs.append(doc)
    return clean_docs


def remove_stopwords(document_list):
    "Remove stopwords inglesas obtidas a partir do NLTK."
    def remove_from_doc(doc):
        doc.title = [w for w in doc.title.split() if w not in stopwords]
        doc.major_subjects = [w for w in doc.major_subjects.split() if w not in stopwords]
        doc.minor_subjects = [w for w in doc.minor_subjects.split() if w not in stopwords]
        doc.abstract = [w for w in doc.abstract.split() if w not in stopwords]
        return doc
    stopwords = []

    with open('../aux/stopwords.txt') as f:
        for el in f:
            stopwords.append(el.strip())

    clean_docs = []

    for document in document_list:
        clean_docs.append(remove_from_doc(document))
    return clean_docs


def clear_document_list(doc_list):
    "Filtra documento para remoção de dados indesejados."
    doc_list = remove_punctuation(doc_list)
    doc_list = remove_stopwords(doc_list)
    doc_list = apply_stemming(doc_list)
    return doc_list


def main():
    new_doc = Document(1, "each of them hello, darkness my old friend", "a", "a", "a")
    x = remove_punctuation([new_doc])
    print(x[0].__dict__)
    x = remove_stopwords(x)
    print(x[0].__dict__)
    x = apply_stemming(x)
    print(x[0].__dict__)


if __name__ == '__main__':
    main()
