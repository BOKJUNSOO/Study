from pyspark.sql import SparkSession
from pyspark import SparkContext , SparkConf
from pyspark.sql.types import StructField
import sys
spark = (
    SparkSession.builder
    .appName('my-project')
    .master('local')
    .getOrCreate()
)

# 데이터 로드
file_path = sys.argv[1]

df = spark.read.csv(file_path , header = True , inferSchema = True)

column_descriptions = {
    "Data" : "거래일",
    "Open" : "시초가",
    "Low" : "최저가",
    "Close" : "종가",
    "Adj Close" : "수정종가",
    "Volume" : "거래량"
}

df.printSchema()
df.show(10, False)
# spark submit : 
# docker exec -it de_2024-spark-master-1 spark-submit --master spark://spark-master:7077 jobs/1printSchema.py data/msftFinance.csv

