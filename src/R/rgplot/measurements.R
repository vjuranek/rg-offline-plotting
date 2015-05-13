loadMeasurements <- function(file) {
    measurements <- read.csv(file, sep = ";")
}

m <- loadMeasurements("../data/nc_lazy_GET1k.csv")
head(m)

plot(m$BasicOperations.Get.ResponseTimeMean)
