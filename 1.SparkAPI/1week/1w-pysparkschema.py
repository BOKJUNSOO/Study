from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType , DateType, TimestampType, LongType ,BooleanType
import sys

# spark 객체 생성
spark = (
    SparkSession.builder
        .appName("hello-world")
        .master("local")
        .getOrCreate()
)
# 파일로드 docker-compose 에서 파일경로를 파라미터로 지정함
file_path = sys.argv[1]   #파라미터 // data 디렉토리에 넣은파일

df = spark.read.json(file_path) #option when cvs
                                #df = spark.read.option("header", "true").option("inferSchema", "true").csv()

df.printSchema()


# schema 객체생성
schema = StructType([
      StructField("actor", StringType(), True),
      StructField("created_at", DateType(), True),
      StructField("id", LongType(), False),
      StructField("org", StringType(), True),
      StructField("payload", StringType(), True),
      StructField("public", BooleanType(), True),
      StructField("repo", StringType(), True),
      StructField("type", StringType(), True)
  ])

# 직접생성한 schema

df2 = spark.read.json(      # json 파일은 header 을 파라미터로 갖을수 없다
    file_path, 
    schema=schema, # 명시적으로 정의한 스키마 사용
)

## csv 파일 로드        #csv option
#sales_df = spark.read.csv(
#    csv_file_path, 
#    header=True, 
#     inferSchema=True,
#    schema=schema, # 명시적으로 정의한 스키마 사용
#)


# spark-summit 종료
spark.stop()
#docker exec -it de_2024-spark-master-1 spark-submit --master spark://spark-master:7077 jobs/1w-pysparkschema.py data/2024-06-01-17.json