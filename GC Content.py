'''
seq = ""
header_list = []
seq_list = []
GC_list = []
gc_dic = {}
count = 0
with open("/home/ishansri/PycharmProjects/Module01/rosalind_ini5.txt", "r") as fh:
    for line in fh:
        if line.startswith('>'):
            splitter = line.split(">")[1].rstrip("\n")
            header_list.append(splitter)
            if len(seq) != 0:
                seq_list.append(seq)
                seq = ""
        else:
            seq += line.rstrip()
    if len(seq) != 0:
        seq_list.append(seq)
        seq = ""

for seq in seq_list:
    count = 0
    for i in seq:
        if i == 'G' or i == "C":
            count += 1
    GC_total = (count/len(seq)) * 100
    GC_list.append(GC_total)

for key in header_list:
    for value in GC_list:
        gc_dic[key] = value

print(gc_dic)
print(max(gc_dic.items()))
'''
def getGC(nt):
    '''
    Find the amount of guanines and cytosines in the sequence in a percentage
    '''
    #Make sure there is a sequence
    if len(nt) != 0:
        ctr_g = nt.count("G")
        ctr_c = nt.count("C")
        #Do calculation to find GC content
        try:
            gc_percent = ((ctr_g + ctr_c) / len(nt)) * 100
        except ZeroDivisionError:
            print("Zero Divisor")
            exit(-1)
    return gc_percent

def getItems():
    '''
    Makes a dictionary with the id as the key and GC content as the value
    '''
    #Open file and declare variables
    f = open("/home/ishansri/PycharmProjects/Module01/rosalind_ini5.txt", "r")
    fasta_dict = {}
    nu_key_=""
    val_ = ""
    #Differentiate between header and sequence lines and update dictionary
    for x in f:
        if x.startswith('>'):
            if len(val_) > 0:
                gc_percent = getGC(val_)
                old_key_ = nu_key_
                nu_key_ = x.split('>')[1].rstrip("\n")
                fasta_dict[old_key_] = gc_percent
                val_ = ""
            else:
                nu_key_ = x.split('>')[1].rstrip("\n")
        else :
            val_ += x.rstrip("\n")
    #Make sure the last value is also appended
    if nu_key_ not in fasta_dict.keys():
        if len(val_) > 0:
            gc_percent = getGC(val_)
            fasta_dict[nu_key_] = gc_percent

    return fasta_dict

#Find the max value
fasta_dict = getItems()


key, value = max(fasta_dict.items(), key=lambda x:x[1])

print(str(key) + "\n" + str(value))