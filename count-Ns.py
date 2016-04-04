import sys
import utils
    
def main():
    print('Loading sequences from', sys.argv[1])
    seqs = utils.load_sequences(sys.argv[1])

    count = 0
    total_bases = 0
    total_ns = 0
    for seq in seqs:
        (n_bases, n_ns) = utils.count_Ns(seq)
        total_bases += n_bases
        total_ns += n_ns
        count += 1

    print("total sequences", count)
    print("fraction of bases that are ns:", total_ns / total_bases)

main()