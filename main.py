from cnnClassifier import logging
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logging.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logging.info(f">>>>>> Stage {STAGE_NAME} completed successfully <<<<<<\n\nx==========================x")
except Exception as e:
    logging.error(e)
    logging.info(f">>>>>> Stage {STAGE_NAME} completed with errors <<<<<<")
    raise e