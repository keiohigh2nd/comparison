#Watch out our query gene character. Capital, small letter

import sys, os, datetime, random
import pandas as pd
import numpy as np

argvs = sys.argv

res_dir = argvs[1]
t_gene = argvs[2]

col_names = ['gene','logFC','logCPM','LR','PValue','FDR']

d = datetime.datetime.today()
f_diff = open('diff/diff_%s_%s_%s_%s.txt' % (str(t_gene), str(res_dir.split('/')[0]), str(d.day),  str(random.randint(1,1000))) , 'w')
f_diff.write(t_gene)
f_diff.write('\n')

for file  in os.listdir(res_dir) : 
    data = pd.read_csv(os.path.join(res_dir,file), delimiter='\t', names=col_names,header=0)
    data['PValue'] = data['PValue'].astype(np.float64)
    if data[data['gene'] == t_gene]['PValue']:
      if data[data['gene'] == t_gene]['PValue'] < float(0.05):
        f_diff.write(file)
        f_diff.write('\t')
        f_diff.write('Diff')
        f_diff.write('\n')
      else:
        f_diff.write(file)
        f_diff.write('\t')
        f_diff.write('No')
        f_diff.write('\n') 
    elif data[data['gene'] == t_gene.upper()]['PValue']:
      if data[data['gene'] == t_gene.upper()]['PValue'] < float(0.05):
        f_diff.write(file)
        f_diff.write('\t')
        f_diff.write('Diff')
        f_diff.write('\n')
      else:
        f_diff.write(file)
        f_diff.write('\t')
        f_diff.write('No')
        f_diff.write('\n')
    else:
      print 'Gene Not found'
      break

f_diff.close()
