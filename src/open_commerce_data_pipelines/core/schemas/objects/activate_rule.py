from pyspark.sql.types import StructType

ACTIONS_SCHEMA = (StructType()
                  .add("id", "string")
                  .add("type", "string")
                  .add("rule_id", "string")
                  .add("configuration", "string")
                  .add("deleted_at", "timestamp")
                  .add("created_at", "timestamp")
                  .add("updated_at", "timestamp")
                  .add("offer_component_type", "string")
                  .add("offer_component_id", "string"))

LIMITERS_SCHEMA = (StructType()
                   .add("id", "string")
                   .add("type", "string")
                   .add("rule_id", "string")
                   .add("configuration", "string")
                   .add("deleted_at", "timestamp")
                   .add("created_at", "timestamp")
                   .add("updated_at", "timestamp")
                   .add("offer_component_type", "string")
                   .add("offer_component_id", "string"))

RULE_FULFILLMENTS_SCHEMA = (StructType()
                            .add("id", "string")
                            .add("rule_id", "string")
                            .add("membership_id", "string")
                            .add("count", "integer")
                            .add("created_at", "timestamp")
                            .add("updated_at", "timestamp")
                            .add("source_type", "string")
                            .add("source_id", "string")
                            .add("deleted_at", "timestamp"))

RULES_SCHEMA = (StructType()
                .add("id", "string")
                .add("name", "string")
                .add("chain_id", "string")
                .add("event_type", "string")
                .add("created_at", "timestamp")
                .add("updated_at", "timestamp")
                .add("publish_at", "timestamp")
                .add("expire_at", "timestamp")
                .add("offer_id", "string")
                .add("deleted_at", "timestamp"))

VOUCHER_SCHEMA = (StructType()
                  .add("id", "string")
                  .add("rule_id", "string")
                  .add("membership_id", "string")
                  .add("state", "string")
                  .add("deleted_at", "timestamp")
                  .add("created_at", "timestamp")
                  .add("updated_at", "timestamp")
                  .add("expire_at", "timestamp")
                  .add("source_rule_id", "string")
                  .add("source_id", "string")
                  .add("source_type", "string")
                  .add("reserved_until", "timestamp")
                  .add("reserved_key", "string")
                  .add("fulfilled_by_id", "string")
                  .add("fulfilled_by_type", "string"))