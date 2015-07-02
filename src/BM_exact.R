filename <- commandArgs(trailingOnly=TRUE)[1] #

library(edgeR)
count <- read.table(filename, sep = "\t", header = T, row.names = 1)
count <- as.matrix(count)

dim(count)

group <- factor(c("A", "B", "B", "B", "B", "B"))


d <- DGEList(counts = count, group = group)
d <- calcNormFactors(d)
d <- estimateCommonDisp(d)
d <- estimateTagwiseDisp(d)

result <- exactTest(d)
topTags(result)

table <- as.data.frame(topTags(result, n = nrow(count)))
write.table(table, file = "exact_result.txt", col.names = T, row.names = T, sep = "\t")

is.DEG <- as.logical(table$FDR < 0.01)
DEG.names <- rownames(table)[is.DEG]

png("res_pic/plot.png", width = 1000, height = 1000)
plotSmear(result, de.tags = DEG.names)
dev.off()

