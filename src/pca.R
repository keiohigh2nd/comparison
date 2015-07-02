filename <- commandArgs(trailingOnly=TRUE)[1] #

count <- read.table(filename, sep = "\t", header = T, row.names = 1)
okamoto <- as.matrix(count)

dim(okamoto)


colnames(okamoto)<-c("A", "B", "C", "D", "E",'F','G','H')
oka.pc<-prcomp(okamoto, scale=TRUE)
summary(oka.pc)
table <- oka.pc$rotation
table
plot(oka.pc$rotation[,2],oka.pc$rotation[,3],type="n")
text(oka.pc$rotation[,2],oka.pc$rotation[,3],colnames(okamoto))
dev.off()

write.table(table, file = "pca_result.txt", col.names = T, row.names = T, sep = "\t")
