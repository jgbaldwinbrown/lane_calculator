#!/usr/bin/env python3

import math
import argparse

def exactlanesneeded(runpairs, readlen, gensize, indivs, covperindiv):
    lanes = covperindiv * gensize * indivs / (runpairs * readlen * 2)
    return lanes

def lanesneeded(runpairs, readlen, gensize, indivs, covperindiv):
    lanes = int(math.ceil(exactlanesneeded(runpairs, readlen, gensize, indivs, covperindiv)))
    return lanes

def basepairsneeded(gensize, indivs, covperindiv):
    bases = gensize * indivs * covperindiv
    return bases

def bp_per_lane(runpairs, readlen):
    bpperlane = runpairs * readlen
    return bpperlane

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Calculate sequencing lanes needed for different sequencing regimes")

    parser.add_argument("-l", "--length", help="Length of sequencing reads (default = 150).")
    parser.add_argument("-p", "--pairs", help="Number of read pairs per sequencing run (default = 100 million).")
    parser.add_argument("-g", "--genomesize", help="Genome size (default = 200 million).")
    parser.add_argument("-i", "--indivs", help="Individuals to sequence (default = 200).")
    parser.add_argument("-c", "--cov", help="Coverage per individual (default = 16x).")

    args=parser.parse_args()

    if args.length:
        length = int(args.length)
    else:
        length = 150

    if args.pairs:
        pairs = int(float(args.pairs))
    else:
        pairs = 100e6

    if args.genomesize:
        genomesize = int(float(args.genomesize))
    else:
        genomesize = 200e6

    if args.indivs:
        indivs = int(args.indivs)
    else:
        indivs = 200

    if args.cov:
        cov = float(args.cov)
    else:
        cov = 16.0

    exactlanes = exactlanesneeded(pairs, length, genomesize, indivs, cov)
    lanes = lanesneeded(pairs, length, genomesize, indivs, cov)
    small = indivs // lanes
    big = math.ceil(float(indivs) / float(lanes))
    numbig = indivs % lanes
    numsmall = lanes - numbig

    print("Read length:", length)
    print("Number of read pairs:", pairs)
    print("Genome size:", genomesize)
    print("Number of individuals:", indivs)
    print("Coverage per individual:", cov)
    print("")
    print("Exact number of lanes needed:", exactlanes)
    print("Integer number of lanes needed:", lanes)
    print("")
    print("Number of small lanes:", numsmall)
    print("Individuals per small lane:", small)
    print("")
    print("Number of big lanes:", numbig)
    print("Individuals per big lane:", big)

