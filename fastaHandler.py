#!usr/bin/env python3

def get_dict_from_fasta (fileLocation, key_index):
    with open(fileLocation, "r") as f:
        key = ""
        seq = ""
        fasta_dict = {}
        for line in f:
            if line.startswith(">"):

                if len(seq) != 0 and len(key)!=0:
                    fasta_dict[key] = seq
                    seq = ""
                key = line.split(">")[key_index].rstrip("\n")

            else:
                seq += line.rstrip("\n")

        # In below the code is to deal when there is no next line or header but we have a sequence ready to be added
        if len(seq) != 0:
            fasta_dict[key] = seq

    return fasta_dict


