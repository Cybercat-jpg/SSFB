#!/usr/bin/env python3

### Simple script for dropping sequences below a specific length
### I just created this script to drop reads below a specific length from my ONT data.

### Still not working how I want it.

from Bio import SeqIO

input_file = '/home/yvonne/Documents/HaliclonaReads/ONT.fasta'
output_file = open('/home/yvonne/Documents/HaliclonaReads/Filtered/filtered.faa', 'w')

long_sequences = []
#dropped = []
for seq_record in SeqIO.parse(input_file, "fasta"):
    print(len(seq_record.seq))
    if len(seq_record.seq) >= 300:
        
        output_file.write(seq_record.seq)
    #else:
        #dropped.append(seq_record)

output_file.close()
#SeqIO.write(long_sequences, output_file, "fasta")
#SeqIO.write(dropped, "/home/yvonne/Desktop/dropped.faa", "fasta")
