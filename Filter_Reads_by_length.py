#python3
### Simple script for dropping sequences below a specific length

from Bio import SeqIO

input_file = "/home/yvonne/Desktop/ls_orchid.fasta"
output_file = "/home/yvonne/Desktop/filtered.faa"

long_sequences = []
dropped = []
for seq_record in SeqIO.parse(input_file, "fasta"):
    print(len(seq_record.seq))
    if len(seq_record.seq) >= 300:
        long_sequences.append(seq_record)
    else:
        dropped.append(seq_record)

SeqIO.write(long_sequences, output_file, "fasta")
SeqIO.write(dropped, "/home/yvonne/Desktop/dropped.faa", "fasta")
