def calculate_protein_mass(amino_acid_sequence):
    # 20 amino acid mass
    mass_table = {
        'G':57.02,
        'A':71.04,
        'S':87.03,
        'P':97.05,
        'V':99.07,
        'T':101.05,
        'C':103.01,
        'I':113.08,
        'L':113.08,
        'N':114.04,
        'D':115.03,
        'Q':128.06,
        'K':128.09,
        'E':129.04,
        'M':131.04,
        'H':137.06,
        'F':147.07,
        'R':156.10,
        'Y':163.06,
        'W':186.08
    }

    total_mass=0.0

# add all amino mass in caculate function
    for aa in amino_acid_sequence:
        if aa not in mass_table:
            raise ValueError(f"wrong, there are wrong amino name in sequence. wrong part: '{aa}'")
        total_mass += mass_table[aa]

    return total_mass

if __name__ == "__main__":
    seq=str(input("input the sequence, for example:GASPV.  input the sequence:    "))
    mass=calculate_protein_mass(seq)
    print(f"sequence{seq} 's protein mass = {mass} amu")
