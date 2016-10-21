#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import listdir
from tika import parser
import magic


def is_containerid(containerID):
    """
    :param containerID:
    :return: [True if container ID is valid, True if container ID is freight, True if container ID is ISO]
    """
    containerID = str(containerID)
    containerID = containerID.strip()
    containerID = containerID.upper()
    result = [True, True, True]

    if len(containerID) != 7:
        return [not i for i in result]
    elif containerID[0:4].isalpha() and \
            containerID[4:12].isdigit() and\
            containerID[3] in 'JRUZ':
        if containerID[3] is not 'U':
            result[1] = False
        if not __is_iso6346(containerID):
            result[3] = False

    return result


def __is_iso6346(containerID):
    char2num = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
        '9': 9, 'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17,
        'H': 18, 'I': 19, 'J': 20, 'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26,
        'P': 27, 'Q': 28, 'R': 29, 'S': 30, 'T': 31, 'U': 32, 'V': 34, 'W': 35,
        'X': 36, 'Y': 37, 'Z': 38,
    }
    total = sum(char2num[c] * 2 ** x for x, c in enumerate(containerID[0:-1]))
    return (total % 11) % 10 == char2num[containerID[-1]]


def main():
    container = []
    path = 'C:/docs_pdf/'
    files = [path + f for f in listdir(path)]
    for doc in files:
        if magic.from_file(doc, mime=True) is 'application/pdf':
            text = parser.from_file(doc)
            with open("Output.txt", "w") as text_file:
                # text_file.write("Purchase Amount: {0}".format(TotalAmount))
                text_file.writelines(text['content'])
        #     print(text['content'])
                print(doc)


if __name__ == '__main__':
    main()