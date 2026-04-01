import re
import matplotlib.pyplot as plt
seq='AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
inputstop=input("input a stop condon(choose one from TAA \ TAG \ TGA):  ").strip().upper()
correct_input=["TAA","TGA","TAG"]
if inputstop not in correct_input:
    print("your input is wrong!")
else:
    RNA_stop=inputstop.replace("T","U")
    pattern=fr"AUG(?:.{{3}})*?{RNA_stop}"
    orflist=[]
    for orf in re.finditer(pattern,seq,re.IGNORECASE):
        orflist.append(orf.group())
    if not orflist:
        print(f"there is no ORF that end with {inputstop}")
    else:
        longest=max(orflist,key=len)
        coding_region=longest[:-3]
        codons=[]
        for i in range(0,len(coding_region),3):
            codon=coding_region[i:i+3]
            if len(codon)==3:
                codons.append(codon)
        codon_count={}
        for c in codons:
            if c in codon_count:
                codon_count[c]=codon_count.get(c,0)+1
        labels=list(codon_count.keys())
        sizes=list(codon_count.values())
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.title(f'Codon Distribution (Upstream of {inputstop})')
        plt.axis('equal') 
        plt.savefig('codon_pie_chart.png', dpi=300, bbox_inches='tight')
        print("-" * 50)
        print(f"input stop codon: {inputstop}")
        print(f"longest ORF: {longest}")
        print(f"all codon number: {len(codons)}")
        print("-" * 50)
        print("result:")
        for codon, count in codon_count.items():
            print(f"{codon}: {count} times")
        print("-" * 50)
        print("pie chart: codon_pie_chart.png")
