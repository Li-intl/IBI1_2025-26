import os

STOP_CODONS = {'TAA', 'TAG', 'TGA'}

def find_in_frame_stops(seq):
    """
    Finds all in-frame stop codons in a given DNA sequence.
    In-frame means the stop codon is encoded by an ORF that begins with 'ATG'[cite: 50].
    Returns a list of unique stop codons found.
    """
    found_stops = set()
    seq_length = len(seq)
    
    for i in range(seq_length - 2):
        if seq[i:i+3] == 'ATG':
            for j in range(i + 3, seq_length - 2, 3):
                codon = seq[j:j+3]
                if codon in STOP_CODONS:
                    found_stops.add(codon)
                    break
                    
    return list(found_stops)

def process_fasta(input_path, output_path):
    """
    Reads the fasta file, processes sequences, and writes valid ones to the new file.
    """
    with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
        header = ""
        seq = ""

        # Read the file line by line
        for line in infile:
            line = line.strip()
            # '>' indicates the start of a new sequence header
            if line.startswith(">"):
                # If header is not empty, process the previously accumulated sequence
                if header and seq:
                    stops = find_in_frame_stops(seq)
                    # Only proceed if at least one in-frame stop codon is found 
                    if stops:
                        # Extract gene name (split by space, take the first item, remove the '>') [cite: 56]
                        gene_name = header.split()[0][1:]
                        # Join the found stop codons into a string (e.g., "TGA, TAA")
                        stops_str = ", ".join(stops)
                        
                        # Write the new header containing only gene name and stop codons [cite: 56]
                        outfile.write(f">{gene_name}, {stops_str}\n")
                        
                        # Write the sequence, wrapping at 80 characters per line to maintain FASTA format
                        for i in range(0, len(seq), 80):
                            outfile.write(seq[i:i+80] + "\n")

                # Update the header and reset the sequence string for the next gene
                header = line
                seq = ""
            else:
                # Concatenate multi-line sequences [cite: 58]
                seq += line 

        # Process the very last sequence remaining in the buffer after the loop finishes
        if header and seq:
            stops = find_in_frame_stops(seq)
            if stops:
                gene_name = header.split()[0][1:]
                stops_str = ", ".join(stops)
                outfile.write(f">{gene_name}, {stops_str}\n")
                for i in range(0, len(seq), 80):
                    outfile.write(seq[i:i+80] + "\n")

if __name__ == "__main__":
    # Define file names
    input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa" # 
    output_file = "stop_genes.fa" # 
    
    print(f"Processing {input_file} ...")
    
    # Check if the input file exists in the current directory
    if os.path.exists(input_file):
        process_fasta(input_file, output_file)
        print(f"Done! Sequences with in-frame stop codons have been saved to: {output_file}")
    else:
        print(f"Error: Cannot find input file '{input_file}'.")
        print("Please ensure you have downloaded the .fa file and placed it in the exact same folder as this Python script.")
