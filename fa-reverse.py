#!/usr/bin/env python3
# Reverse complement

# Usage
import argparse
from argparse import RawTextHelpFormatter
from io import StringIO
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

parser = argparse.ArgumentParser(
	formatter_class=RawTextHelpFormatter,
	description='Reverse complement a FASTA file\n',
	usage='\n  %(prog)s [OPTIONS] FASTA > reverse.fa')
parser.add_argument('fasta', metavar='FASTA', help='input FASTA file', nargs='+')
parser.add_argument('--version', action='version', version='v0.2')
args = parser.parse_args()

sample = args.fasta[0]

newSEQS = []
for s in SeqIO.parse(sample, 'fasta'):
	newseq = s.seq.reverse_complement()
	newdesc = s.description + ' reverse_complement'
	newseqREC = SeqRecord(newseq, id=s.id, description=newdesc)
	newSEQS.append(newseqREC)

seqFILE = StringIO()
SeqIO.write(newseqREC, seqFILE, 'fasta')
output = seqFILE.getvalue().rstrip()
print(output)
