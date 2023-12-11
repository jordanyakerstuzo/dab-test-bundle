from pyspark.sql.types import StructType


COMMUNICATION_PREFERENCES_SCHEMA = (StructType()
                                    .add("createdAt", "timestamp")
                                    .add("updatedAt", "timestamp")
                                    .add("id", "integer")
                                    .add("customerUuid", "string")
                                    .add("smsOptInAt", "timestamp")
                                    .add("smsOptOutAt", "timestamp")
                                    .add("emailOptInAt", "timestamp")
                                    .add("emailOptOutAt", "timestamp")
                                    .add("pushOptOutAt", "timestamp"))

SMS_OPT_OUT_SCHEMA = (StructType()
                      .add("createdAt", "timestamp")
                      .add("updatedAt", "timestamp")
                      .add("id", "integer")
                      .add("phoneNumber", "string"))
