from pyspark.sql.types import ArrayType, StructType, MapType, StringType

from open_commerce_data_pipelines.core.schemas.models.silver.transactions import \
    TRANSACTION_LINE_ITEMS_SILVER_SCHEMA, TRANSACTIONS_SILVER_DISCOUNT_SCHEMA

LOYALTY_TRANSACTIONS_SILVER_STAGE_1_SCHEMA = (StructType()
                                              .add("id", "string")
                                              .add("day_id", "date")
                                              .add("loyalty_member_id", "string")
                                              .add("loyalty_transaction_id", "string")
                                              .add("location_id", "string")
                                              .add("external_id", "string")
                                              .add("transaction_type", "string")
                                              .add("transaction_pos_timestamp", "timestamp")
                                              .add("transaction_pos_timestamp_local", "timestamp")
                                              .add("transaction_till_id", "string")
                                              .add("transaction_cashier_id", "string")
                                              .add("transaction_register_id", "string")
                                              .add("is_forecourt_transaction", "boolean")
                                              .add("payment_amount", "double")
                                              .add("payment_method", "string")
                                              .add("payment_method_card_type", "string")
                                              .add("tax_amount", "double")
                                              .add("points_quantity", "integer")
                                              .add("loyalty_transaction_created_at", "timestamp")
                                              .add("loyalty_transaction_processed_at", "timestamp")
                                              .add("loyalty_transaction_time_at", "timestamp")
                                              .add("meta_offer_bridge_updated_at", "timestamp")
                                              .add("transaction_data_created_at", "timestamp")
                                              .add("transaction_data_updated_at", "timestamp")
                                              .add("transaction_line_item_created_at", "timestamp")
                                              .add("transaction_line_item_updated_at", "timestamp")
                                              .add("conexxus_line_items",
                                                   ArrayType(TRANSACTION_LINE_ITEMS_SILVER_SCHEMA))
                                              .add("loyalty_line_items",
                                                   ArrayType(TRANSACTION_LINE_ITEMS_SILVER_SCHEMA))
                                              .add("transaction_discounts",
                                                   ArrayType(TRANSACTIONS_SILVER_DISCOUNT_SCHEMA))
                                              .add("meta_offer_bridge",
                                                   MapType(StringType(), ArrayType(StringType())))
                                              .add("timestamp", "timestamp"))
