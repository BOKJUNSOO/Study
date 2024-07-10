from abc import ABC , abstractmethod
from pyspark.sql.types import StructType, StructField, StringType, LongType
import pyspark.sql.functions as F

# 스키마 지정
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


class BaseFilter(ABC):
    def __init__(self, args):
        self.args = args
        self.spark = args.spark

    def pre(self, df):
        df = df.withColumn('actor_json', F.from_json('actor', schema = actor_schema)) \
               .select('created_at','id', 'payload', 'type', 'actor_json.*', 'repo')
        df = df.withColumn('payload_json', F.from_json('payload', schema = payload_schema)) \
               .select('login', 'url', 'created_at', 'id', 'payload_json.*', 'type', 'repo')
        df = df.withColumn('repo_json', F.from_json('repo', schema = repo_schema)) \
               .select('login', 'url', 'created_at', 'id', 'repository_id', 'size', 'distinct_size', 'message', 'type', 'repo_json.*')


        df = df.filter(F.col("login") != "github-actions[bot]")         # created_at col 을 datetime 데이터로 변환하기
        df = df.withColumn('created_at', F.trim(F.regexp_replace(df.created_at, "[TZ]", " ")))
        df = df.withColumn('created_dt', F.to_timestamp(df.created_at, 'yyyy-MM-dd HH:mm:ss'))

        udf_check_repo_name = F.udf(lambda name : name.split("/")[1], StringType())     # name 컬럼에서 repo만 가져오기
        df = df.withColumn('repo_name', udf_check_repo_name(F.col('name')))
        df = df.drop('name')
        return df

    def filter(self, df):
        pass

    