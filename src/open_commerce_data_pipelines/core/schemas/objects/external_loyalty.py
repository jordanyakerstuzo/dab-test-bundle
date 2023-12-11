from pyspark.sql.types import StructType

OFFER_ACTIVITY_LOG_SCHEMA = (StructType()
                             .add("id", "string")
                             .add("membershipId", "string")
                             .add("activityType", "string")
                             .add("channel", "string")
                             .add("externalChainId", "string")
                             .add("adId", "string")
                             .add("activityState", "string")
                             .add("marketingTransactionLogId", "string")
                             .add("activityAt", "timestamp")
                             .add("createdAt", "timestamp")
                             .add("updatedAt", "timestamp"))
