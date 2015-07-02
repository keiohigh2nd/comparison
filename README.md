# comparison

1st step: Merge expression file into one 
 python src/extract.py data/brain_3-3-2.counts.txt data/brain_2-4-5.counts.txt data/brain_1-2-4.counts.txt data/brain_1-2-2.counts.txt

2nd step: Statistic Analysis
 R --file=src/comparison_edgeR.R --args input/input_2015_6_8_25 

 # Be careful with your experimental labell
   it is in R file

#Put R result into one file
python src/average.py result/HER2-60_BM_2-3_and_HER2-90_BM_3-1.txt result/HER2-60-brain_and_HER2-90-brain.txt


#visualization
1st step: merge results
  python src/align_result.py result/two_brain_3-3-2_and_fatpad.txt result/two_brain_2-4-5_and_fatpad.txt 
2nd step: make map
  R --file=src/visualize.R --args visualization/viz_2015_6_10_98 

#Search p-value experiment
python2.7 src/search_experiment.py mouse_result/ Grm3

#Find commons of p-value results
python2.7 src/find_common_4.py [1] [2] [3] [4]

#Search TCGA
python2.7 src/ref_tcga.py tcga/breast_invasive/Level_3/ 'SSPO','TPH2','PTPRT'

