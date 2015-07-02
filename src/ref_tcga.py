# -*- coding:utf-8 -*-
#Watch out our query gene character. Capital, small letter

import sys, os, datetime, random, csv
import pandas as pd
import numpy as np

d = datetime.datetime.today()

argvs = sys.argv

tcga_dir = argvs[1]
target_genes = argvs[2].split(',')

for t in target_genes:
  print t

files = os.listdir(tcga_dir)

f = open('tcga/result/%s_%s_%s_%s.txt' % (tcga_dir.split('/')[1], target_genes[0], str(d.day),  str(random.randint(1,1000))), 'w')

f.write(tcga_dir)
f.write('\t')
f.write(argvs[2])
f.write('\n')

f.write('\t')
for t_gene in target_genes:
  f.write(t_gene)
  f.write('\t')
f.write('\n')

for file in files:
  f.write(file)
  f.write('\t')
  for line in open(os.path.join(tcga_dir, file ), 'r'):
    for t_gene in target_genes:
      if int(line.strip('\n').split('\t')[0].find(t_gene)) != -1:
        f.write(line.strip('\n').split('\t')[1])
        f.write('\t')
  f.write('\n')
      

f.close()
