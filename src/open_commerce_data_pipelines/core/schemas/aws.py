from pyspark.sql.types import StructType

KINESIS_MESSAGE_SCHEMA = (StructType()
                          .add("partitionKey", "string")
                          .add("data", "binary")
                          .add("stream", "string")
                          .add("shardId", "string")
                          .add("sequenceNumber", "string")
                          .add("approximateArrivalTimestamp", "timestamp"))
