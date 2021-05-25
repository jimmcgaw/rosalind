from Bio.SeqIO.FastaIO import SimpleFastaParser

from Bio.Seq import Seq



# with open('./rosalind_subs.txt', 'r') as f:
#     lines = f.readlines()

# strand = lines[0]
# strand = strand.replace('\n', '')


with open('./rosalind_revp.txt', 'r') as f:
    for values in SimpleFastaParser(f):
        strand = values[1]


def is_reverse_palindrome(subseq):
    return Seq(subseq).reverse_complement() == subseq

# strand = 'TCAATGCATGCGGGTCTATATGCAT'

answers = []
for index, char in enumerate(strand):
    # print(index, char)
    # continue
    for length in range(4, 13):
        subseq = strand[index:index+length]
        if len(subseq) < 4:
            continue
        if is_reverse_palindrome(subseq):
            print(index+1, len(subseq), subseq)
            answer = (index+1, len(subseq))
            if answer not in answers:
                answers.append(answer)

for answer in answers:
    print(' '.join([str(i) for i in answer]))