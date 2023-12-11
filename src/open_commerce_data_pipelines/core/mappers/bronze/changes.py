from pyspark.sql import DataFrame
from pyspark.sql.functions import from_json, regexp_replace
from pyspark.sql.types import StructType, BooleanType

from open_commerce_data_pipelines.core.schemas.models.bronze import CHANGES_BRONZE_STAGE_2_DATA_SCHEMA


class ChangesBronzeStage1Mapper:
    @staticmethod
    def map_to_changes_bronze_stage_2(src: DataFrame):
        return (src
                .select("partitionKey",
                        from_json(src.data.cast("string"),
                                  CHANGES_BRONZE_STAGE_2_DATA_SCHEMA)
                        .alias("data"),
                        "stream",
                        "shardId",
                        "sequenceNumber",
                        "approximateArrivalTimestamp",
                        "day_id",
                        "timestamp"))
