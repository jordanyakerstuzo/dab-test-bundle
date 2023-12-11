from ctypes import ArgumentError
from typing import Dict, List, Union

from delta import DeltaTable
from pyspark.sql import Column, DataFrame, Window
from pyspark.sql.functions import coalesce, row_number, col
from sprak.data_mappers import MergeDataMapper


class BronzeStage1DataMapper(MergeDataMapper):
    __timestamp_cols: List[str] = None

    def __init__(self, delete_condition: str = None, existing_alias: str = None, id_col: str = None,
                 insert_condition: str = None, insert_map: Dict[str, Union[Column, str]] = None,
                 merge_condition: str = None, timestamp_col: str = None, timestamp_cols: List[str] = None,
                 update_condition: str = None, update_map: Dict[str, Union[Column, str]] = None,
                 updates_alias: str = None) -> None:
        (super()
         .__init__(delete_condition,
                   existing_alias,
                   id_col,
                   insert_condition,
                   insert_map,
                   merge_condition,
                   timestamp_col,
                   update_condition,
                   update_map,
                   updates_alias))

        if not timestamp_cols:
            raise ArgumentError("timestamp_cols is required")

        self.__timestamp_cols = timestamp_cols

    def save(self, table: DeltaTable):
        _inner_save = super().save(table)

        def _save(updates: DataFrame, batch: int):
            window = (Window
                      .partitionBy(self.id_col)
                      .orderBy(coalesce(*self.__timestamp_cols).desc(),
                               col("approx_arrival_timestamp").desc()))

            latest = (updates
                      .withColumn("row_number", row_number().over(window))
                      .where("row_number = 1")
                      .drop("row_number"))

            return _inner_save(latest, batch)

        return _save


class ActivateBronzeStage1DataMapper(BronzeStage1DataMapper):
    pass


class DayPartitionedActivateBronzeStage1DataMapper(ActivateBronzeStage1DataMapper):
    def __init__(self, delete_condition: str = None, existing_alias: str = None, id_col: str = None,
                 insert_condition: str = None, insert_map: Dict[str, Union[Column, str]] = None,
                 merge_condition: str = None, timestamp_col: str = None, timestamp_cols: List[str] = None,
                 update_condition: str = None, update_map: Dict[str, Union[Column, str]] = None,
                 updates_alias: str = None) -> None:
        id_col_modified = id_col if id_col else "id"
        existing_alias_modified = existing_alias if existing_alias else "existing"
        updates_alias_modified = updates_alias if updates_alias else "updates"

        merge_condition = (f"{existing_alias_modified}.day_id = {updates_alias_modified}.day_id AND "
                           f"{existing_alias_modified}.{id_col_modified} = {updates_alias_modified}.{id_col_modified}")

        super().__init__(delete_condition, existing_alias, id_col, insert_condition, insert_map, merge_condition,
                         timestamp_col, timestamp_cols, update_condition, update_map, updates_alias)


class OpenCommerceBronzeStage1DataMapper(BronzeStage1DataMapper):
    def __init__(self, delete_condition: str = None, existing_alias: str = None, id_col: str = None,
                 insert_condition: str = None, insert_map: Dict[str, Union[Column, str]] = None,
                 merge_condition: str = None, timestamp_col: str = None, timestamp_cols: List[str] = None,
                 update_condition: str = None, update_map: Dict[str, Union[Column, str]] = None,
                 updates_alias: str = None) -> None:
        timestamp_col = "updatedAt"

        (super()
         .__init__(delete_condition,
                   existing_alias,
                   id_col,
                   insert_condition,
                   insert_map,
                   merge_condition,
                   timestamp_col,
                   timestamp_cols,
                   update_condition,
                   update_map,
                   updates_alias))


class DayPartitionedOpenCommerceBronzeStage1DataMapper(OpenCommerceBronzeStage1DataMapper):
    def __init__(self, delete_condition: str = None, existing_alias: str = None, id_col: str = None,
                 insert_condition: str = None, insert_map: Dict[str, Union[Column, str]] = None,
                 merge_condition: str = None, timestamp_col: str = None, timestamp_cols: List[str] = None,
                 update_condition: str = None, update_map: Dict[str, Union[Column, str]] = None,
                 updates_alias: str = None) -> None:
        id_col_modified = id_col if id_col else "id"
        existing_alias_modified = existing_alias if existing_alias else "existing"
        updates_alias_modified = updates_alias if updates_alias else "updates"

        merge_condition = (f"{existing_alias_modified}.day_id = {updates_alias_modified}.day_id AND "
                           f"{existing_alias_modified}.{id_col_modified} = {updates_alias_modified}.{id_col_modified}")

        super().__init__(delete_condition, existing_alias, id_col, insert_condition, insert_map, merge_condition,
                         timestamp_col, timestamp_cols, update_condition, update_map, updates_alias)
