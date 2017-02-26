from pyspark import SparkContext, SparkConf

##Constants
APP_NAME = "Word Cont App"
MASTER ="local[*]"

##Functions


##Main
def main(sc):
    """
     This app counts the words in an example file 'WordCountExampleFile'. Locally I am using wget from the hortonworks wiki as my example file.
    """

    myLines =  sc.textFile('hdfs://sandbox.hortonworks.com/tmp/WordCountExampleFile')
    words = myLines.flatMap(lambda text: text.split())
    wc = words.map(lambda word: (word, 1))
    counts = wc.reduceByKey(lambda v1,v2: v1+v2) 
    list = counts.collect()
    print repr(list)

if __name__ == "__main__":
    #setup spark
    conf = SparkConf().setMaster(MASTER).setAppName(APP_NAME)
    sc = SparkContext(conf=conf)

    #execute
    main(sc)
    print "============================= Made it to the end==================================="

