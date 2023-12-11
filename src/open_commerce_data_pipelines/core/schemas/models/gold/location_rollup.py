from enum import Enum

from pyspark.sql.types import StructType


class LocationRollupTimeframes(Enum):
    DAILY = "daily"
    MONTHLY = "monthly"
    WEEKLY = "weekly"


LOCATIONS_ROLLUP_GOLD_STAGE_1_SCHEMA = (StructType()
                                        .add("day_id", "date")
                                        .add("location_id", "string")
                                        .add("timeframe", "string")
                                        .add("transaction_count", "long")
                                        .add("fuel_transaction_count", "long")
                                        .add("non_fuel_transaction_count", "long")
                                        .add("average_fuel_transaction_amount", "double")
                                        .add("total_fuel_transaction_amount", "double")
                                        .add("average_fuel_gallons", "double")
                                        .add("total_fuel_gallons", "double")
                                        .add("average_non_fuel_transaction_amount", "double")
                                        .add("total_non_fuel_transaction_amount", "double")
                                        .add("average_transaction_amount", "double")
                                        .add("total_transaction_amount", "double")
                                        .add("average_basket_size", "double")
                                        .add("total_basket_size", "long")
                                        .add("total_new_members", "long")
                                        .add("total_home_store_members", "long")
                                        .add("timestamp", "timestamp"))
