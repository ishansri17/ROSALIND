# All code below woks - gives different ways to accomplish ReverseComplement

with open("/home/ishansri/PycharmProjects/Module01/rosalind_ini5.txt", "r") as f:
    dna = f.read().strip()


'''
dict_dna = {'A':"T", "T":"A", "C":"G", "G":"C"}

for x in range(len(dna)) [::-1]:
    reverse += "".join(str(dict_dna[dna[x]]))

print(reverse)

'''

'''
translate = {"A": "T", "C": "G", "T": "A", "G":"C"}

reversed = ("".join([str(translate[dna[x]]) for x in range(len(dna))]))[::-1]

print(reversed)
'''


response= ""
translate = {"A": "T", "C": "G", "T": "A", "G":"C"}


for s in dna:
    if s in translate:
        response = response + translate[s]

print(response)

'''
How to do this in Linux

Bash Shell:  
1. cat rosalind_ini5.txt | tr [ACGT] [TGCA] | rev
Using Sed
2. cat rosalind_ini5.txt | tr [ACGT] [TGCA] | rev

For multi-line sequences:

for FASTA files
3. grep -v "^>" ss.fasta | tr -d "\n" | rev | tr ATCG TAGC > ss_reversed_fasta.txt


'''
