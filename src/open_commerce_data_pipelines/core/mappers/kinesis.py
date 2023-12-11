from pyspark.sql import DataFrame
from pyspark.sql.functions import current_date


class KinesisMapper:
    @staticmethod
    def map_to_changes_bronze_stage_1(src: DataFrame):
        """Map the data from the Kinesis message format to the Bronze-tier Changes stage-1 model format."""

        return src.withColumn("day_id", current_date())
