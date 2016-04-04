#! /usr/bin/env python3
import sys
import utils
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', action='store_true',
                        help='print versions')
    parser.add_argument('sequencefile',
                        help='a FASTQ file full of sequences')
    args = parser.parse_args()
    
    if args.version:
        print('Using version', utils.version, 'of utils.py')

    seqs = utils.load_sequences(args.sequencefile)

    tracking = []
    for seq in seqs:
        n_bases, n_ns = utils.count_Ns(seq)
        tracking.append(n_ns)

    num_with_zero = 0
    num_with_one = 0
    num_with_more = 0

    for count in tracking:
        if count == 0:
            num_with_zero += 1
        elif count == 1:
            num_with_one += 1
        else:
            num_with_more += 1

    print(num_with_zero, num_with_one, num_with_more)
    print(sum(tracking))

    
if __name__ == '__main__':
    main()
