#Declare variables
s = "GATATATGCATATACTT"
t = "ATAT"
end = len(s) - len(t) + 1
result=""
#Iterate over string to get position of first letter in t
for i in range(0, end):
    line = s[i:i+len(t)]
    if line == t:
       result += str(i + 1) + " "
print(result)


