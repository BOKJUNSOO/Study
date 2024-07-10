from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
        .appName("word-count")
        .master("local")
        .getOrCreate()
)
sc = spark.sparkContext

text = "Hello Spark Hello Python Hello Docker Hello World"
words = sc.parallelize(text.split(" "))     #local data set / RDD 생성
wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)  # 같은 key_word 에 대하여 모두 다 더한다

for wc in wordCounts.collect():
    print(wc[0], wc[1])

# docker exec -it dataengineering-spark-master-1 spark-submit --master spark://spark-master:7077 jobs/worldcount.py data/2024-06-01-17.json