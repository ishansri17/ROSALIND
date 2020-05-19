#Import modules
import Bio
from Bio.Seq import Seq

RNA_Dict = {
    'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

str1 = "AUGUCCGGCCUCAUCAAUACCUAUUGUCGGGAUGCCUUCUCUACCCCACCGCCCUUAACGGCUACGUGCACAAGAGGGGGAUAUAUUCCAGCGGCCAAUCUCCUCUCUCCUAGCUUCAGGACUUCAUUUGGGGGAGAAUCGCUGAAUGGCCUUCUGGUCGGAGGGAGAAUAGUUCCGAAUGCUUCCGUCCGUCGGUCGCAGCAAGGUAGAGACGGCCUUUGCGUUGGCGUGUCUCUGUCUUGUUGGACGUACGCCGAAUUUCUGAUACGACACGACCAGAUCCGGUCUCUCUGCGAAAGGCUGAACUCCUUUGUACCAGACUCCAUAAGAGUCAGGUCAAUGAGCGACGCCGCAGCUGAAUAUACCAUACUAAGUGAGCAAGUUCCAGACACGAAGAUUGCGUCCCGGUGCGACUGGGUAGCAAACACAAAUUUUCACAAUCGUUGUACGCCUCACGAGUCCAUGCACUGGACGUGUCCCCCUAGUUUCUAUUCGCCUACCGUAACUCUUUCACCGAUCAGUAUCAGGUAUGGCCAGAAAUCCAGGCUAGCGAUGAUACUGUAUGUGAUAAAAUUACGAAGCGUACGCGUCCUUGUAUCAAUGCAAGCAAGCCCGGCAUCAGGACCUCGACGCCUUUUCACUAGCCCCGGCCCGCGAUCGUCCGGAUAUCGACAUAGCUCUCUCCGCCACCGGGAGUUGUACAUCGUGUUGUCAUGCACUAGGUGCUCUGACCUACGACUUGAGAUCAAGCGCUCGCCUUUAUUUCGCUCUUCCCCUGACGUUCGCCGUAGCCGCCAGAUCUCCUGGUCUAGGGGGAUUGGAACGGAGGCUGGUGCCUUUUCAGGGCGAUUGCGUGCGGUGAACCGCCAAGUCGACUUACUGAAGGAGUCAGUUAGUGUCAGGUUGUAUAAGGUGGGAGCUUGGGGUGGUUUGCGCAUUACGUUUCACAUCAUAUCGCCGGAUUAUACCGAGUGGCGUGGGUGGGAUGUUCCCAUUCUAAGUUCAUUGACUCAUCGACGCGGCAGCGACCUGACGAGGCGCAUAAAAAUUCGGGCUAGGUUGCAAACUUAUGGUCAUGCUGGCUGGCGCUGUCUACACGUAAGCUACCCGGCCCUGGUCCGUCGCAGAGCAGGACGGGCUAGUGACUUACGUCGCUUCCGUCAGAAGUUCCAUCUUAAAAAGCGGAUACUGCACGUUCAGACGGUAGGGCUAUGCAGGCCACCGAUUCGAACUCGUGUUAGAUGCGACCGACUUAUAGAAAGGUUCUUAACAAGAAGGCCUAUCGGCCCCCUGAUAAAAUCCCUCUCUAUUCAGUCCCUUUGGACAGGACGCCGCGGUACGGCUACGCAAGCAUCCCCAAAACUUGAUGCCAAAUCCAUGUAUUCAUUGAUAGGUAGGCGAGCGACCCGGGAGUCCGCGCUUAUAUACUUUCCUACCGCAUCCUGGAAUAAGGUCACUCUCAUUAUAGUGGCGGGGCGUCCUGUAGUUGUUUCCGGUCGCCCUCUCUCUACCAUAACCCUCGACGAGGGAGCGAUUCUAGCCAAGGGCGCAACUCCCCGAGAGACUCAGGUUCUUAACUACUCUGUUCAUGCGUAUUUUCAGACCCCCUCGCCGGAGGGUGGGUACAAAACACUGCCGGACCUCCAGAACGCGAGCCUCAAAGGACCUUUCAAGGCAGUCAGUCACGCGCUUCUCGCACCCGCAGUGCGGUGCGUCCUGCUUGUUUAUCGACUCUUUGCGACCAGCGGUAUACACGUGUACAAAUACCAUUAUAUUGUAUAUUGCGUCAAUAGAGUAGAGUGUACUGCCGAUAAACAUCCUCUAAUUGGAGGGCCCAGGAGUUGCUGGACUAACGCGCAACAAUUGGGCGAACGCGUAGGAAGUCGGCAAAGCAUACUAUACAGUGAUGGUCACCAACUUUGCGUUCAUGGGGAGCACUUACGUAGCCCCCUUUGUCCGAAACGCGCGCUAGCGAGGGACGCACGUUAUGCGAGUACAACGUCGAUUCAACCCCGGGGCAACGAAUGGUGGGGCAUCGAUUCCGAGACUCGGCAGCGGACCUAUCGGACUCAAGCCCCUUUAAAAACUUGGAUGCCGGACACAGAAUUGCUAUCGAAGGGGCCAACCUGUUGCUCCCACCGAGACCCUGCGCGGCAUUAUACCGUCCCUAGUUGCCAGGAACGUUGGGUAGAGCAACUCCUCCAACGUUCUGGCCACCCCCUUCAACAUUGCAUUGUGGCGGUAGGGGAUGACUGGUCUAGCAAAUGCAUGUUCCAUAUGAUCCACUUGUCGCUCCGGGGGAUCGAGAAGAGCACAGCUAAUAUACGAAAUAACAACAUGCGCGUCGCGCAUGGAAGAAGAACCUCGCCCCUCGGGACUUGCUUACUUCCGAUCUCAUCUGUCCCCUUCCGACUAUGCUGUUGGUCGCUAAUGUCAGACUACCCGCCAGCUGGCCACACCAAUCACAAUCGUGAAGCUCAUAAAGACAAGGUAAAAACGCGAAGAAUCUGUCUGCCUUGCCCCGCACCGAUUGGGCCCCAGGCCGUUGCUAGCCUGGUUAUCAGGGGUCUCACACAUGGAGGCUCCCUAAUGGCGCCCAACACAAUAACGGUAGCGAUGAUGCACGUCCAUACGCAUGUCUAUCCUGACAUAUACAUCUCUCAACACCUAUCUGAGGCGACGGUUUCUGCGUCUCGCCAGAUAUGGACUGGUGUGCAGACUUUUGCGCGGCUUAGACGGACCUCUAACAGCAUGAUUUCUAUUGAUGCUGACUUCACACUGGGAGUUUCCCCUACCGGAACUACGUUCGACGCUGCCCCUUCUAAUGUACCUUCCCUCAGGUUUGGAGGGAGGUGCUGUCAACAUUACCGGCACAACGCGGACGGUAGUUUUCCUGCGAGAAAAAAGCCGAGUAGGCUACAUAGAACCCCAGCUGAAAGCACAUUAGUUUUAAUUAGCGGGACAGGAUCUCAAAAAGCAAUUCGACGUCUCAUAAACAUUAGGCGUCGACCUGCCAGGAGUGAACAUGGUCGUAUUAUGAAAGCCCGAAACCCUCAUCAAUGGAUAUUAUUUCGAAUAUUCGUGAGUUGGCAGUUUUGCCAUACCACACCAGCCAACUGCUGUUUAAUCGGGGGUCAAUUCCUCGGAGACGUUUCGGGUCAUACGGUCGGCGGCAAUGAAAGCGAUAAAACUAAGCACACGCCAGCUAUCUCUUCAGGGAACCCUAUUAUAGCCUCCCUAGCUGCUUCCGUAUUUCUUGUUGAUUGCUGUUGGUCACAAUACCCCUUCCUUAUAACCUGCCUUAAAGGUGAAUCCAGUGAGAGGGGAGAUUCUACUUCCGCCAAACCAGAGAACUAUUCCAGUGCCGCCAAAAUCAGCGUGAAGUUCUUUACGACCUCAAAUGUUAGAUGUUAUCACGACGUUCUCCCAUUCUUGAUUCCUCGGAUUCAUCUAAGUCAUAUGAAAGCCCGACUACACCUGUUAUUAUGUGGAACCGGUAUAAGGUCCCGACUAGACAAGUUUUUUACAACCCGUGCUAACGAGCUCACAUUAAGGAUUCCGUACGAAAUGAGAGCUUGCCAAGUAAGGCGGCGCAGUUUAGACGCAAGAUACAAGGAUCGACAUGCAGUCGUCAUGAAAUUCAGGUUUAUCGCUCCGCGCUGCUACCCAAUCACCGUGAUUCAGUGUCCUCGCGCGAUGGUUCCACGGACUCCUAAUCGGUCGAGGACUCAUGACUGUGCACUCUAUACUCGUAAAAGUAGCUCUAUGGAAAAAGUACGCGCUGCGGCCGUUGGAGUAGCUUCAGGUUCUGCAAAUCAGGGCCUCCUUAGAUUGCGCUGCCGUUUUGUUAUAAUGAGCCUAGACGUUCCCCCCCCCGCGUCAAAGGACAGCCCGUGGUUAUUUGACACAGGCGGCCAACGGAGCAGUCAUGUGAAGACGUCUCAAGUGCGACGCGGAUUACCAACUAAAAAAUGGGCUCAGAGCGUGAUCCUGGGAAUGAACCGUAAUGGAGGCCGUACUUGUGGAGAAACAAGCUUGAAGCACUUCUACCACCUUUUCCUGGAGAUUUAUCCCGGUAAUCGAUGGCGGCGGGCUAGUUGUCAAUGGAGAAUUAAAUUGGGUCAGUCUAAUCUUUGCCCAACAUUGAGUGUUAAUGGCCCCCCAUUUAGGUCUACGUUCCGGCAACCGAAACUUCCGCACCAGUGUCCACCUGGGGGAUUACUACUCACCGUGAGCCGUGCGCCUUGGCUGGAAUCAUCGCCUCAAACACGGGGUAACCUUGACCCCCUGUCGAGCAUCCUUUCCGUGCUGUUGACACUUGACAGGCUAGCUCUUGGAGGGGAAAACCAGAGGAGACCCCGAUUGGUCAACGAAACAGCCGUGGGUGUGCAGUGUAUCAGGACACGUGCUCUACCAACGCCGGAUACCCCCCUCUGGGGCACUCUUGCUGGAAGAGCCUUAGUCGGCACCCAGGCGGCACCACAGAAACUUAGCAGCCGGCGAAUUGGGUUCCGUGCCAAUAGCAAAGCGGUGUCUGGGCCCCAUCGAGACUCAAUUCCAGGCCGUAAUCACCAGGGUCACCUAGAGCGUUAUUUUAAGUGCUCUGCAAAUUUGCGGCCGUCGCAGCGCAGUCCACGCAGGGUGCCACGACCCACAAGCGGCCAGUGUGUCUUUUCUCCUAACCAGUUGUGGUGUCUGUAUUUGCUUUGGCUUGCGCCGUGCCAUGCCACACACGCUUUUGGUAGGUUCGCCGUAAGGCGAGCCUGCAUGUUAUUUAUUGUCAAUCCGGAGCGUCUCCGCAUCGGAUGGAAAUCCACCAAGACAUCCCAAUAUCAGCUCGAAACAGUACCCGCUACUUAUACAUGUAGCAGAUCCACAGUAGCUGCGGUGGUCAUACACGGCAAAGCAUAUGUCGUCGGCGUCAAAGAGUUCACUGGUAUGCACUUUGCGCGUGAUUUAGACCGGCGCAGGAGUAACUCCGGGUACGUCGGAGCAUUAGAACCUGUGAGGGCCGGUGGGCUGAAGGCCAUCGAAGCCAUAGUCCAUUUGUGUUCGAAGACAGUGCUGUCAAGGUCGUGGUCUGGUACUCACCCGUUUCCAAUCGCAAGAAAGAAGAAGAAACGUUGUACUGACCCUGAGGUAAGAGUCAGGUGUCGGACCGGGGGCGGGAACUACAUAAGUAGGCACCUGAGUCUAUGCGCGACUUGUCGCCAAAAAUGGCGCAAGAUAUACGAAUUUCUAUACAAGUUGUACUCACCAAGUGAUACAUCGAGUCAAACAGAAAUGGCUCUCGUUGGACAGGAAUGUUCAAUCAGCGGGAUUCGUGCCAGUAAGCAUCGUCAUAGGGAAACCGAGGAAUCACCAUGGGAUUCGGGCCCGAGUUGGAGCGAAUCGACAAACGCAAUCGGCCUUGGCCUUUUGGCUAGUCAACACGCUCCACACCUAGUUGGCAUCUGGUUUCACUGUCCACUCCCAAAACUUACCAGAAACGACACGAGCCUUAGCACGACCGGUUAUUCGACAAGUGGUCAAAAUGAGCGCUCUGCAUACUGCAGUUUACGCGCCCCGGACCCCGGGAACGGACCUGGACAUAUCCACCAGGGCACGGCCUCUAGACAAAUCGGGACCGACAGUACGUCAAAACUCGGUGAGCCACAUGCCAGGGGGUCUAUGAUGCGACAUUUGAUCCACGUAGAACUUGUCGCGUAUACGACCGCCCUAUUCCUAUUGCUAGCAACAACAGGGGGUGCACUACUGUGCAUGACGCGACACUUCACCUUGGACGUCCGAUCGAAGCUUGGUUCGUUCGUUCUAGGAGCCGGCCAGGAGGGCUGCCCUCGUGUAGGUUAUCUAUCGCAUUUGGGCCUAUGUCUUAGACGGAUCACAAAAGCAUGUGCAAUCAGACGCGCUGAUAUACCCCACUGCGCGACUGUGCCAUUGACGACUCACCUUGUUGCCCUAGACGCAAUCCAACAUGGAGACCGUUCCUAUGCGUUCUGUCUUAUUGUUGGACUCAGUGGACUUAUGGAUUGUUACGUGGAAAUCAACGUUAUAUAUCCUAUAAUUUACAUUCGACGCCCCAGACAGCAUACUGGGCGUGCAAUGGGGGAGUGGAUCCGCUCGAUACAUGCAGCUGAGGACUAUCAGAGAGAACAGCAUCAUUUUGCAAGUAUUCGCUGGCACUCACAUGCUACCGGCAGAUCCUUCCUUGCAGUCCGUCGUUUUGUUGGAGUUAAAGUUGCGUGGCCCUUAGUUGCUCUUGAGUCCCUGACGCUAGAAAGAGAUCGCUCCGUACAAAUGCCUCUCUGGUCCCUGCUAGAGCAAGCGUACACGAGGGUUGUAUUUUUCACCCCAAGAAAUGGGUUAUGUGUUCUAGACCAACAUUGCAGGUGGGCUGCGGCGACGCCAUCCAAGUCAUCGCGUAUGGAUCUUUUCUACGGCGAGCCAGUUUCUUGUGAAUGGGUCGCCGUCAGGCCUUCCAGAUAUGCUCAAGUAAGAAUAGGGAACGAUCACAGGGUCUCAUAUGGUACGAUUAGCGACUGGACCUCGCAUGAGUUAGUCAAUUACCUCCAAAACAAUCGGGAGGCGUACCUACCUUCCAUUCUACCCUCCAGCCUGGUAGCAGAUCCCACGGGUAGCGACCGGGAAACAUCUAUUAAACUUUGCACAAGCCGCGCAUACUCCGCGCACUUGAAGGAUUCGUGUCCCUCUGUUUGCCCUCUUAUACCAGAGCGUUCGCCGCGACCCGACAUUAAGUUUCAGCCGAAGAUGCCACGUGUACACGACAUGGCAUUCUGCGAUGUACUUCCGGUCGUCUGCCUAAUAUUGACCUCGACCCUGCCCGCCAAUAGGACCUCCGUGAAGAGUGCUCAAAAGGCGGGCCCCGCUUCUAAGGAGGAACCUACUCAGGACCCGAUGCGAGUCGUGGCUUCCGGGGAUGCGCUCGUAAGUACUAUUUCGUGCCCUAUUAUCGAUAUUUGGAGCAAAUACAAACAUCCUAAGGAAAGCGCUCGAAAAAACGUUAAACAGCAUCCAAGCCGCUGGUCGCGCGGAAAUGAAUGUCAACAGUCCGCGGGGUAUUAUGAUGAUAGGGACGGCCGCUGUGUUAAUUAUACCGGUCAUCUCCGAUACUUCCCGCUGCCGGGAGUGACUCGAUUUGUUAACGGCGAUUAUAUACUGCAAACCAACAUCACUAAGAGAACUGUGUCUUUGAUAAUUGGGCGCGCCAGAACCGCGCUAGCUAUAUUUACCCCGAGAAUUACUUGCGAUGGAAGUCGUAAUUUAAAGCCAAUAAUUGAAAAAAGCGGCCCAGGAAAGAGUCCUUUCGCACCAGGUUGGACCCGCAUGUCGUUGCCUCAACCACAGUGCAGGUUGUGCCCAACCGAAGCCCCGUGUUGUGCAGCCGAAUGGCCGUCAAUGCCACCCCUCGUCGUGUGGCCCCACUCCUUAGCUUUUUGGCCUCACGAAAGCUUGGAUGUCGUAUACAUUUUUAUCAUGACUUCAACCCCAGGCGUCUCCCGCAAUCUAUCGGGAUAUUUUAGUUGCCCAGUAGUUGCACGAGGACACGGUACGCACGCUAUGGCUCGUACCGUAAAACGACGUUUACAUAAGUUUCUGUCGUUUAGCGGUCACACAAAACGAUUUGAUGAACUAACUGCCACGGUCUGGCUUAUCAAGAUUAUAGCCCGAGUCUCCGUCACAGGUUCACUGGAGCGGGCUAGUCGCUCGAAUUUCGUAAGGGAGUGCUUCAGAUGUGUAGGCCGUCGCUCCGGGCGAUGGAUGACGUCUCGGUGGUCAAAUAUGACGCGAGAAUGGCCGCAUACAGGCCGAAGAUUUUGGAUUCCCUAUGAGCGUAUAGGUUGUCAAGUCAAGUGGAGGGUCACACAUUUUAGGUGGGUAACGGAAUGGGACUCAAAAACUGCCAUUCACGCGUCCUUACCGCCGUUAACCGACCUUCGAGGAUACGGCGUAUCGUACCCGCAACCAACUUGCUUGACACUCAGUUGGCUUAGGCGCUGCCUACGGCGGACGGUGGUGAAAAGUGGUGAUGCUUACCCCUAUGCAUGCAUUGAUCUCGCGUACGUUAAUAAUGUAUGUAAUGCCUGGCGGCGGGUGAUUUGCUCACUGUGGACGCUAGCUAACGGUCCUAUGUCCGGUUAUAACUAUCAGAGGGCACUGGGCAGAGGGUCAAAUAGGAUUGUCAUGACCAAUUCUUCCACGUGCUGGCGAAGCCCGAUGUUUAUAAUACAUGUCUCAGAAGGCGAAGUUCGAUUAUCCGUGAGGCAAGGACAUCGCACAAUUCUGCUAUGCAACCCUGGGGCCUAUUCCCAAAGUCAUCGCUCUUUUUACGCUGAUGACCAAAACGGAAUUAACACGUGCUGUACGAUCGCGGAUUCGAAAACACAAGCUGAAGGUCUUGUGUUAGUGCGCUUCGAUUGCAAGCAAAUUGUCAAACUCACACGGCAGCGUCAGACUAGGAACACUUGGGACUACACUACAAUGGGAAGCGCCGAGAAAAGGUUCCAUGCGCGCCCCCGCACCAACAUAUCUCUACUGAAUGUAUACGACGCGACACCAUACAAUGGGCAUGGAGUGCAUGGGCCCAGUACGUUCCAAACGAACCUUGGACCGAACCGACGCUACCCGGUUCCCUGUCGAUUGCCCCCUCUAACUGCGAUAUUAACCAUAGGUCCGGGGCGGGUUGGAGAAUCCGCGCUCGGAAUAUUACGGAUCGUGGAUGAUGUGAUGUUGAAUAUAACGGGCCAUAAAGUAUUGACUACCCAUAUCAAGACAGGUGGGUAUGUCUCUGGUCGCGGGUUUCUGAUUGGUCGUCUUCAGGCGGACGGGUAUACGUUAAUUGCUAUUUUUCGGCCUACAUGGUACGACUGCUUCCCUCGAGUCUGUUUUCUGAUUCCAGUUAGGGCUUCCCCUCCAAUUAAGGGACUAGUCUGCUCUCCGGACACAGCCACCGAAUUCGCAACAAUGUCGGGUCUAUCAAAGCAGGACGCAGGAAACUCCGUGUCCACGUUAUCGACCCCACUCUCGCCGCCGGUGCUACGCAGGCACGGCCUCAACAAGCGGUGUCCAGAGACUGGAGUCUCAUUCAGCACCGGCCUACUAAGUCAAGUAAAUGAUAGCCAAGCUAGCGUAUCAAUAUACGUAGCUAAUCCAAAUACAAAGUGGUUCAGUCGAGGUGAGAACGUAAGUGGGUCACUCAUUGCAUGUGUCCGAUACAUUCGGACCGCCGCGAUGGGCUUAUGGUCAUGGUCAAUGUUUUUGGCGAUCGUAUUCAUCACUGACAGGAUCUUAACUUUACAGUUGAUGGGGGUAAAGUACGCCUCUGCUGUUAUGACGGCACCGAGAGGGCGCCAAAUGCCCCACAACCUUUCCUGUACUCAGAAUUGGACGCUUGUGCGUAAAGUUACUCCGGCUGUUACUGGCUCUCGAAUACCUCAGAGGACAGCAGGCUGUCUCAGGAAUCUAUACUGGUGUUCGUCCGAUAGCCCGACACUUUUCCGUGGAGGCCAGAUAAUGCCAAACUUUUACCGUAGGUCCUCACUCGUGCCUCGUCCAAUAGCGCGGAGUCACCGGCGGAUUGUACUGUCGGAACAAAUGAUCAACAUCGAUUGGGAGAGCAUCUGUUCACUACGGCACACGACAUGCUCGCAAAGGGCUUUAUGUCAUGAGUGGGCGAGGGGCUACGCUCAAGCGGCUACGUUAGCUAUCUUAAUUCACAGUGCGAUCCAAGACUUGUUCUAUCAGCUACUCAGCGCAGUGAUAUUUUUUUUUCCCAUUACGAUCGGACCUCGUAGAUUUGUCAAAUACGUUCCAAGAUCACCGCUAUGUCACUUGCGAUUAGUACUACGGCAUUGCUUUGAGCGUGAAGCUUUUGGCGGUCAUCCGAAUAGACCUGUUGUCAACACUCAUGCUCGUCAAUGUAUGGGUACGAAGACAGAGUGA"

#Use translate method to translate RNA to protein using the hardcoded sequence
str1 = Seq(str1)
protein = str1.translate(to_stop=True)
print(protein)

new = ""
for i in range(0, len(str1), 3):
    symbol = RNA_Dict[i:i+3]
    if symbol == "Stop":
        break
    new += symbol

out = []
protein = ""
start = str1.find('AUG')
tr = str1[start:]
for n in range(0, len(tr), 3):
    if tr[n:n+3] in RNA_Dict:
        if RNA_Dict[tr[n:n+3]] =="Stop":
            out.append(protein)
            protein = ""
        else:
            protein += RNA_Dict[tr[n:n+3]]