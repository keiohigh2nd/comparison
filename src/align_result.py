import sys, datetime, random

d = datetime.datetime.today()
argvs = sys.argv

del argvs[0]
num_file = len(argvs)

inputs = []
for input in argvs:
  filename = input
  f = open(filename, 'r')
  lines = f.readlines()
  f.close()
  inputs.append(lines)



f_out = open('visualization/viz_%s_%s_%s_%s' % (str(d.year), str(d.month), str(d.day),  str(random.randint(1,100))) , 'w')

max_line = len(inputs[0])
for i in xrange(max_line):
  f_out.write(inputs[0][i].split('\t')[0].strip('\n'))
  for j in xrange(len(inputs)):
    f_out.write('\t')
    f_out.write(inputs[j][i].split('\t')[3].strip('\n'))
  f_out.write('\n')

f_out.close()


