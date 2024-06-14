from cnnClassifier import logging
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingesion = DataIngestion(config=data_ingestion_config)
        data_ingesion.download_data()
        data_ingesion.extract_zip_file()


if __name__ == "__main__":
    try:
        logging.info(f">>>>>> Sage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f">>>>>> Sage {STAGE_NAME} completed successfully <<<<<<")
    except Exception as e:
        logging.error(e)
        logging.info(f">>>>>> Sage {STAGE_NAME} completed with errors <<<<<<")
        raise e