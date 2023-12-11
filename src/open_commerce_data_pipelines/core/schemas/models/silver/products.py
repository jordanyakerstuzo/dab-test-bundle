from pyspark.sql.types import ArrayType, StringType, StructType

PRODUCT_GROUPS_SILVER_STAGE_1_SCHEMA = (StructType()
                                        .add("id", "string")
                                        .add("name", "string")
                                        .add("description", "string")
                                        .add("key", "string")
                                        .add("values", ArrayType(StringType()))
                                        .add("created_at", "timestamp")
                                        .add("updated_at", "timestamp")
                                        .add("deleted_at", "timestamp")
                                        .add("timestamp", "timestamp"))
