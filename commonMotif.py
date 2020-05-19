#!/usr/bin/env python3
#categories.py
import fastaHandler
from fastaHandler import get_dict_from_fasta


def main():

    fasta_dict = get_dict_from_fasta("rosalind_lcsm-1.txt", 1)

    list_str = fasta_dict.values()
    short_str = min(list_str, key =len)
    matched = ""


    result_dict = {}
    for index in range(len(short_str)):
        strCtr = 2

        while strCtr < len(short_str) and index < (len(short_str) - 1):
            lookup_str = short_str[index: index + strCtr]

            counter = 0
            # now find if the short_str match is in the values of fasts_dict
            for val in list_str:
                counter += 1
                if val != lookup_str:
                    if lookup_str in val:
                        if counter == len(list_str):
                            matched = lookup_str

                            if len(matched) != 0:
                                result_dict[lookup_str] = matched
                    else:
                        break

            strCtr += 1

    #print(result_dict)
    if len(result_dict) != 0:
        print(max(result_dict.values(), key=len))




    # find the shortest string in dictionary values

if __name__ == "__main__":
    main()