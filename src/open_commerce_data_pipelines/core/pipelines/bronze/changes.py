from ctypes import ArgumentError
from typing import Any, Dict, Optional, cast

from pyspark.sql import DataFrame
from sprak.io import IoResourceFormats
from sprak.io.stream import StreamIoOutputModes
from sprak.pipelines import SingleSourceDataPipeline, SingleSourceDataPipelineConfig

from open_commerce_data_pipelines.core.mappers.kinesis import KinesisMapper
from open_commerce_data_pipelines.core.schemas.aws import KINESIS_MESSAGE_SCHEMA
from open_commerce_data_pipelines.core.schemas.models.bronze import CHANGES_BRONZE_STAGE_1_SCHEMA


class CdcChangesBronzeStage1PipelineConfig(SingleSourceDataPipelineConfig):
    """The configuration class for the CdcChangesBronzeStage1Pipeline."""

    __changes_raw_input_region: str = None
    __changes_raw_input_stream_opts: Dict[str, Any] = None

    def __init__(self, changes_raw_input_region: Optional[str] = None, input_database_location: Optional[str] = None,
                 input_location: Optional[str] = None, output_checkpoint_location: Optional[str] = None,
                 output_database_location: Optional[str] = None, output_hive_database_force_recreate=False,
                 output_location: Optional[str] = None, **changes_raw_input_stream_opts: Any) -> None:
        """Initialize a new instance of the CdcChangesBronzeStage1PipelineConfig class.

        Parameters
        ----------
        changes_raw_input_region : str
            The region of the input stream containing the raw CDC messages to be processed.

        changes_raw_input_stream_opts : dict[str, Any]
            A collection of parameters to be passed to the Kinesis stream reader as defined at
            https://docs.databricks.com/structured-streaming/kinesis.html.

        input_database_location: str
            Path for the database that the left input for the pipline is a part of.

        input_location: str
            Path for the left input of the pipeline.

        output_checkpoint_location: str
            Path for the output of the pipeline's streaming checkpoints.

        output_database_location: str
            Path for the database that this pipline is a part of.

        output_hive_database_force_recreate: bool
            A flag indicating that the output hive database needs to be dropped and recreated.

        output_location: str
            Path for the output of the pipeline.
        """
        super().__init__(input_database_location, input_location, output_checkpoint_location, output_database_location,
                         output_hive_database_force_recreate, output_location)

        if not changes_raw_input_region:
            raise ArgumentError("changes_raw_input_region is required")

        self.__changes_raw_input_region = changes_raw_input_region
        self.__changes_raw_input_stream_opts = changes_raw_input_stream_opts

    @property
    def changes_raw_input_region(self):
        """Get the region of the input stream containing the raw CDC messages to be processed."""

        return self.__changes_raw_input_region

    @property
    def changes_raw_input_stream_opts(self):
        """A collection of parameters to be passed to the Kinesis stream reader as defined at
        https://docs.databricks.com/structured-streaming/kinesis.html."""
        return self.__changes_raw_input_stream_opts


class CdcChangesBronzeStage1Pipeline(SingleSourceDataPipeline):
    """Handles the processing of the raw CDC data from the Kinesis stream."""

    _config: CdcChangesBronzeStage1PipelineConfig = None

    input_format = IoResourceFormats.KINESIS
    input_is_streaming = True
    input_schema = KINESIS_MESSAGE_SCHEMA
    output_is_streaming = True
    output_mode = StreamIoOutputModes.APPEND
    output_name = "changes-stage-1"
    output_schema = CHANGES_BRONZE_STAGE_1_SCHEMA
    partition_by = ["day_id"]

    def __init__(self, config: CdcChangesBronzeStage1PipelineConfig) -> None:
        """Initialize a new instance of the pipeline.

        Arguments:
        config (CdcChangesBronzeStage1PipelineConfig): the configuration for the pipeline."""

        super().__init__(config)

        self.input_io_opts = {
            **config.changes_raw_input_stream_opts,
            "region": self.config.changes_raw_input_region
        }

    @property
    def config(self) -> CdcChangesBronzeStage1PipelineConfig:
        """Gets the configuration for the pipeline."""

        return cast(CdcChangesBronzeStage1PipelineConfig, super().config)

    def mapper_function(self, src: DataFrame):
        return KinesisMapper.map_to_changes_bronze_stage_1(src)
