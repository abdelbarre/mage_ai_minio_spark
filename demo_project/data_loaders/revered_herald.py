from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.druid import Druid
from os import path
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


import os
from pyspark.sql import SparkSession
spark = SparkSession.builder.master(os.getenv('SPARK_MASTER_HOST', 'local')).getOrCreate()

@data_loader
def load_data_from_druid(*args, **kwargs):
    """
    Template for loading data from a Druid warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#druid
    """
    print(spark)


