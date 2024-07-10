import sys
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
        .appName("hello-world")
        .master("local")
        .getOrCreate()
)
sc = spark.sparkContext
logFile = sys.argv[1]   #파라미터로 데이터
logData = sc.textFile(logFile).cache()

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print("Lines with a: {}, lines with b: {}".format(numAs, numBs))
spark.stop()



#docker exec -it de_2024-spark-master-1 spark-submit --master spark://spark-master:7077 jobs/hello-world.py data/2024-06-01-17.json