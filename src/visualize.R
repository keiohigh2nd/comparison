filename <- commandArgs(trailingOnly=TRUE)[1] #

library(ggplot2)
library(reshape2)
library(ggthemes)

data <- read.table(filename, header = TRUE, row.names = 1, nrows = 100)
data <- as.matrix(data)
data2=melt(data,id.var="PValue")

(p<-ggplot(data2,aes(as.factor(Var1),as.factor(Var2)))+geom_tile(aes(fill=value))+scale_fill_gradient(low="white",high="red"))

png("res_pic/plot.png", width = 1000, height = 1000)

plot(p + labs(x = "",y = "") + scale_x_discrete(expand = c(0, 0)) + scale_y_discrete(expand = c(0, 0)) +  theme(legend.position = "none",axis.ticks = element_blank(), axis.text.x = element_text(size = 7, angle = 280, hjust = 0, colour = "grey50")))

dev.off() 

