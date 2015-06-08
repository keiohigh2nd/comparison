filename <- commandArgs(trailingOnly=TRUE)[1] #

library(edgeR)
count <- read.table(filename, sep = "\t", header = T, row.names = 1)
count <- as.matrix(count)

cell = factor(c("N", "N", "T", "T"))
patient = factor(c("A", "B", "A", "B"))
design <- model.matrix(~ patient + cell)

d <- DGEList(counts = count, group = cell)
d <- calcNormFactors(d)
d <- estimateGLMCommonDisp(d, design)
d <- estimateGLMTrendedDisp(d, design)
d <- estimateGLMTagwiseDisp(d, design)

fit <- glmFit(d, design)
lrt <- glmLRT(fit, coef = 3)
topTags(lrt)

table <- as.data.frame(topTags(lrt, n = nrow(count)))
write.table(table, file = "result.txt", col.names = T, row.names = T, sep = "\t")
