import pybedtools

a = pybedtools.BedTool('data/input_a.bed')
b = pybedtools.BedTool('data/input_b.bed')

print("bed file a")
print(a)

print("bed file b")
print(b)

c = a.coverage(b, s=True)
print("a coverage b")
print(c)

d = b.coverage(a, s=True)
print("b coverage a")
print(d)
