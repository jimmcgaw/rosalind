from Bio.SeqIO.FastaIO import SimpleFastaParser

from Bio.Seq import Seq

from collections import Counter


with open('./rosalind_gc.txt', 'r') as f:
    for values in SimpleFastaParser(f):
        strand_name = values[0]
        strand = values[1]
        counter = Counter(strand)
        g_count = counter.get('G')
        c_count = counter.get('C')
        gc_count = g_count + c_count
        print(strand_name)
        print(gc_count / len(strand) * 100)

