#!/usr/bin/env python

from __future__ import print_function

# Usage
import argparse
from argparse import RawTextHelpFormatter
import StringIO
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

parser = argparse.ArgumentParser(
	formatter_class=RawTextHelpFormatter,
	description='Reverse complement a FASTA file\n',
	usage='\n  %(prog)s [OPTIONS] FASTA')
parser.add_argument('fasta', metavar='FASTA', help='input FASTA file', nargs='+')
parser.add_argument('--version', action='version', version=
		'=====================================\n'
		'%(prog)s v0.1\n'
		'Author: Jason Kwong\n'
		'Updated 18-Jun-2016\n'
		'Dependencies: Python 2.7.x, BioPython\n'
		'=====================================\n')
args = parser.parse_args()

sample = args.fasta[0]

newSEQS = []
for s in SeqIO.parse(sample, 'fasta'):
	newseq = s.seq.reverse_complement()
	newdesc = s.description + ' reverse complement'
	newseqREC = SeqRecord(newseq, id=s.id, description=newdesc)
	newSEQS.append(newseqREC)

seqFILE = StringIO.StringIO()
SeqIO.write(newseqREC, seqFILE, 'fasta')
output = seqFILE.getvalue().rstrip()
print(output)
