import sys
import pprint
import cleardocs
import extractor


def main():
    """
    Código para inicialização e utilização da máquina vetorial.
    """
    docs = extractor.extract_documents(sys.argv[1])
    clean_docs = cleardocs.clear_document_list(docs)
    for doc in clean_docs:
        pprint.pprint(doc.__dict__)


if __name__ == '__main__':
    main()
