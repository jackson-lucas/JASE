import sys
import pprint
from document import Document


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


if __name__ == '__main__':
    main()
