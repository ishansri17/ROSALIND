k = 2
m = 2
n = 2

total = k + m + n
sec_total = total - 1
KK = (k/total) * ((k-1)/sec_total)
nn = (n/total) * ((n-1)/sec_total)
km = (k/total) * (m/sec_total) + (m/total) * (k/sec_total)
kn = (k/total) * (n/sec_total) + (n/total) * (k/sec_total)
mn = (m/total) * (n/sec_total) + (n/total) * (m/sec_total)
final = KK * 1/4 + nn + km * 1/2 + kn + mn
actual = 1 - final
print(final)