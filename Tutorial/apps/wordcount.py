
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType


def init_spark():
  sql = SparkSession.builder\
    .appName("firstSession")\
    .getOrCreate()
  sc = sql.sparkContext
  sql
  return sql,sc

def main():
    sql,sc = init_spark()
    columnas = ['id','nombre','x']

    lista = [
            (1,'Sarvf','a'),
            (2,'Sully','b'),
            (3,'Dendrobates','c'),
            (4,'Monosaurio','d')
    ]

    lista
    df_1 = sql.createDataFrame(lista, schema=columnas)
    df_1.count()
    df_1.show()
    df_1.columns
    df_1.printSchema()
    df_1.describe().show()
    
    
    schema_1 = StructType(
            [
                StructField('Id',IntegerType(),True),
                StructField('Nombre',StringType(),True),
                StructField('Y',StringType(),True),
            ]
    )
    df_2 = sql.createDataFrame(lista,schema=schema_1)
    df_2.show()
    df_2.printSchema()
if __name__ == '__main__':
    main()