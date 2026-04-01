import re
seq='AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
pattern=r'AUG(?:.{3})*?(UAA|UAG|UGA)'
#AUG  :an ORF should start with AUG
#(?:.{3})*?  :an ORF including many group(and each group contains 3 string)
#(UAA|UAG|UGA)  :it will end with these 3 stop condon
#pattern help set a model of an ORF so that we can use "re" to help us search string!
#honestly, AI help me to wirte line 3. And i learned it and have taken some notes.
allorf=re.findall(pattern,seq)
orflist=[]
for orf in re.finditer(pattern,seq):
    orflist.append(orf.group())
#search all ORF and make them in a list
maxlength=max(len(orf_lenth) for orf_lenth in orflist) if orflist else 0
#find the largest
print(f"The length of largest ORF is {maxlength} nucleotides")


#orf_start = re.search("AUG", seq)
#orf_start.span()
#orf_start.end()
#orf_start.start()
#maybe it is better to use these codes professor taught me 
#I will shift my code if i have time