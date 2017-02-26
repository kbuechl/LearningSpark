from pyspark import SparkContext, SparkConf

##Constants
APP_NAME = ""
MASTER ="local[*]"
##Functions


##Main
def main(sc):
    
if __name__ == "__main__":
    #setup spark
    conf = SparkConf().setMaster(MASTER).setAppName(APP_NAME)
    sc = SparkContext(conf=conf)

    #execute
    main(sc)