#Watch out our query gene character. Capital, small letter

import sys, os, datetime, random
import pandas as pd
import numpy as np

argvs = sys.argv

target_data = argvs[1]
reduct_data = argvs[2]
other1_data = argvs[3]
other2_data = argvs[4]

col_names = ['gene','logFC','logCPM','LR','PValue','FDR']

d = datetime.datetime.today()
f_diff = open('find_common/find_common_%s_%s_%s_%s_%s.txt' % (str(target_data.split('/')[-1]), str(reduct_data.split('/')[-1]), str(other1_data.split('/')[-1]), str(d.day),  str(random.randint(1,1000))) , 'w')

t_data = pd.read_csv(target_data, delimiter='\t', names=col_names,header=0)
r_data = pd.read_csv(reduct_data, delimiter='\t', names=col_names,header=0)
o1_data = pd.read_csv(other1_data, delimiter='\t', names=col_names,header=0)
o2_data = pd.read_csv(other2_data, delimiter='\t', names=col_names,header=0)

t_data = t_data.sort('gene')
r_data = r_data.sort('gene')
o1_data = o1_data.sort('gene')
o2_data = o2_data.sort('gene')

t_data['PValue'] = t_data['PValue'].astype(np.float64)
r_data['PValue'] = r_data['PValue'].astype(np.float64)
o1_data['PValue'] = o1_data['PValue'].astype(np.float64)
o2_data['PValue'] = o2_data['PValue'].astype(np.float64)

for t_d  in t_data.T :
  if int(t_data.iloc[t_d]['gene'].find('LOC')) != -1:
    continue
  if int(t_data.iloc[t_d]['gene'].find('ZNF')) != -1:
    continue
  if int(t_data.iloc[t_d]['gene'].find('XAGE')) != -1:
    continue
  if t_data.iloc[t_d]['PValue'] >= float(0.05):
    continue
  else:
    if r_data.iloc[t_d]['PValue'] >= float(0.05):
      continue
    else:
      if o1_data.iloc[t_d]['PValue'] <= float(0.05):
        if o2_data.iloc[t_d]['PValue'] <= float(0.05):
          f_diff.write(t_data.iloc[t_d]['gene'])  
          f_diff.write('\t')  
          f_diff.write(str(t_data.iloc[t_d]['logFC']))  
          f_diff.write('\n') 

f_diff.close()
