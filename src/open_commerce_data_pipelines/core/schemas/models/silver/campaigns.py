from pyspark.sql.types import StructType

CAMPAIGNS_SILVER_STAGE_1_SCHEMA = (StructType()
                                   .add("id", "string")
                                   .add("category", "string")
                                   .add("chain_id", "string")
                                   .add("description", "string")
                                   .add("deleted_at", "timestamp")
                                   .add("name", "string")
                                   .add("created_at", "timestamp")
                                   .add("updated_at", "timestamp")
                                   .add("external_id", "string")
                                   .add("timestamp", "timestamp"))
