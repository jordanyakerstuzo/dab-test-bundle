from pyspark.sql.types import StructType

LOCATION_HOURS_OF_OPERATION = (StructType()
                               .add("close_time", "string")
                               .add("day_of_week", "string")
                               .add("open_time", "string"))
