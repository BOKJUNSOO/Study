from pyspark import SparkConf , SparkContext
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
        .getOrCreat()
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
      StructField("type", StringType(), True)
  ])

df = spark.read.json(file_path , schema = schema)


# 어떤 컬럼내의 json데이터를 위한 schema 정의(nested data)
actor_schema = StructType(
    [
        StructField('login', StringType(),True),
        StructField('url',StringType(), True)
    ]
)

payload_schema = StructType(
    [
    StructField('repository_id', LongType(), True),
    StructField('size', LongType(), True),
    StructField('distinct_size', LongType(), True),
    StructField('message', StringType(), True),
    StructField('comment', StructType([StructField('body', StringType(), True)]))
    ]
)

repo_schema = StructType(
    [
    StructField('name', StringType(), True),
    StructField('url', StringType(), True)
    ]
)

gitdata = df.withColumn('actor_json', F.from_json('actor', schema = actor_schema)) \
               .select('created_at','id', 'payload', 'type', 'actor_json.*', 'repo')
gitdata = gitdata.withColumn('payload_json', F.from_json('payload', schema = payload_schema)) \
               .select('login', 'url', 'created_at', 'id', 'payload_json.*', 'type', 'repo')
gitdata = gitdata.withColumn('repo_json', F.from_json('repo', schema = repo_schema)) \
               .select('login', 'url', 'created_at', 'id', 'repository_id', 'size', 'distinct_size', 'message', 'type', 'repo_json.*')


gitdata = gitdata.filter(col("login") != "github-actions[bot]")         # created_at col 을 datetime 데이터로 변환하기
gitdata = gitdata.withColumn('created_at', F.trim(F.regexp_replace(gitdata.created_at, "[TZ]", " ")))
gitdata = gitdata.withColumn('created_dt', F.to_timestamp(gitdata.created_at, 'yyyy-MM-dd HH:mm:ss'))

udf_check_repo_name = F.udf(lambda name : name.split("/")[1], StringType())     # name 컬럼에서 repo만 가져오기
gitdata = gitdata.withColumn('repo_name', udf_check_repo_name(F.col('name')))

gitdata.show(10, False)

spark.stop()

#docker exec -it de_2024-spark-master-1 spark-submit --master spark://spark-master:7077 jobs/1w-pysparkschema.py data/2024-06-01-17.json




