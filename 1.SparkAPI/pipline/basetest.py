from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType , DateType, TimestampType, LongType ,BooleanType
import sys
import pyspark.sql.functions as F
from pyspark.sql.functions import col
#spark 객체 생성
spark = (
        SparkSession.builder
        .appName("my-Project")
        .master("local")
        .getOrCreate()
)

# 데이터 로드
file_path = sys.argv[1]

schema = StructType([
      StructField("actor", StringType(), True),
      StructField("created_at", DateType(), True),
      StructField("id", LongType(), False),
      StructField("org", StringType(), True),
      StructField("payload", StringType(), True),
      StructField("public", BooleanType(), True),
      StructField("repo", StringType(), True),
      StructField("type", StringType(), True),
  ])

# 어떤 컬럼내의 json데이터를 위한 schema 정의(nested data)
actor_schema = StructType([
    StructField('login', StringType(), True),
    StructField('url', StringType(), True)
])

payload_schema = StructType([
    StructField('repository_id', LongType(), True),
    StructField('size', LongType(), True),
    StructField('distinct_size', LongType(), True),
    StructField('comment', StructType([StructField('body', StringType(), True)]), True),
    StructField(                                                                            #nested1
        'pull_request' , StructType([StructField(
            'repo' , StructType([StructField(
                'language' , StringType(), True
            )]), True
        )]), True
    )
])
repo_schema = StructType([
    StructField('name', StringType(), True),
    StructField('url', StringType(), True)
])

df = spark.read.json(file_path) # parameter : schema = schema
df.show(1, False)

# 사용할 컬럼 불러오기
df = df.select('created_at', 'id' , 'payload' , 'type' ,
                df.actor.login.alias('login'),
                df.actor.url.alias('url'), 
               'repo')

df = df.select('created_at', 'id' , 'type', 
               df.payload.repository_id.alias('repository_id'),
               df.payload.size.alias('size'),
               df.payload.distinct_size.alias('distinct_size'),
               df.payload.comment.alias('comment'),
               df.payload.pull_request.base.repo.language.alias('language'),
             'login', 'url', 'repo')

df = df.select('created_at', 'id' , 'type', 
               'repository_id','size','distinct_size','comment', 'language',
               'login', 'url',
               F.col('repo.name').alias('name'), 
               df.repo.url.alias('repo_url'))

n_cols = ['created_at', 'id', 'type',
              'repository_id', 'size', 'distinct_size', 'comment','language',
              'login', 'url', 'name', 'repo_url'
             ]

df = df.toDF(*n_cols)   # n_cols로 toDF() dataframe 을 만들겠다.

df = df.filter(df.language.isNotNull()) # collect() ==> RDD list 변환되어 48번줄 filter() 는 list를 attribute로 받을수 없음

# created_at col 을 datetime 데이터로 변환하기
df = df.filter(col("login") != "github-actions[bot]")
df = df.withColumn('created_at', F.trim(F.regexp_replace(df.created_at, "[TZ]", " ")))
df = df.withColumn('created_dt', F.to_timestamp(df.created_at, 'yyyy-MM-dd HH:mm:ss'))

# name 컬럼에서 repo만 가져오기
udf_check_repo_name = F.udf(lambda name : name.split("/")[1], StringType())
df = df.withColumn('repo_name', udf_check_repo_name(F.col('name')))
df = df.drop('name')

df.show(10)
df.printSchema()
spark.stop()

# docker exec -it de_2024-spark-master-1 spark-submit --master spark://spark-master:7077 jobs/base1.py data/2024-06-01-17.json




