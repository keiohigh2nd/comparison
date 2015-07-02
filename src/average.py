import sys, datetime, random

d = datetime.datetime.today()
argvs = sys.argv

del argvs[0]
num_file = len(argvs)

filename = argvs[0]
f = open(filename, 'r')
lines1 = f.readlines()
f.close()

filename = argvs[1]
f = open(filename, 'r')
lines2 = f.readlines()
f.close()


f_out = open('ave/input_%s_%s_%s_%s' % (str(d.year), str(d.month), str(d.day),  str(random.randint(1,100))) , 'w')

for line1 in lines1:
  for line2 in lines2:
    if line1.split('\t')[0].find(line2.split('\t')[0]) == 0:
      f_out.write(line1.split('\t')[0])
      try:
        tmp = float(line1.split('\t')[3]) + float(line2.split('\t')[3])
      except:
        break
      f_out.write('\t')
      f_out.write(str(tmp))
      f_out.write('\n')
      break


