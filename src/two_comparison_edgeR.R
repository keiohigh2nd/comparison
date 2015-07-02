filename <- commandArgs(trailingOnly=TRUE)[1] #

library(edgeR)
count <- read.table(filename, sep = "\t", header = T, row.names = 1)
count <- as.matrix(count)

group= factor(c("A", "B"))
design <- model.matrix(~ group)


d <- DGEList(counts = count, group = group)
d <- calcNormFactors(d)
d <- estimateGLMCommonDisp(d, method = "deviance", robust = T, subset = NULL)
fit <- glmFit(d, design)
lrt <- glmLRT(fit, coef = 2)
topTags(lrt)

table <- as.data.frame(topTags(lrt, n = nrow(count)))
write.table(table, file = "two_result.txt", col.names = T, row.names = T, sep = "\t")
