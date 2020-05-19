#Open file and declare variables
filer = open("/home/ishansri/PycharmProjects/ROSALIND/rosalind_ini5.txt.py", "r")
reader = filer.read().splitlines()
string1 = reader[0]
string2 = reader[1]
count = 0
#If the strings are read one-to-one, count the number of mismatched pairs
for i in range(len(string1)):
    if string1[i] != string2[i]:
        count += 1
print(count)
