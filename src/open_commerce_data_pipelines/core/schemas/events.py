from pyspark.sql.types import MapType, StringType, StructType

CHANGE_EVENT_SCHEMA = (StructType()
                       .add("data", "string")
                       .add("metadata",
                            MapType(StringType(),
                                    StringType())))
