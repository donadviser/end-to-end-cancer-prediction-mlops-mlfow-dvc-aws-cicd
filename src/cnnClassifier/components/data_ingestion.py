import os
import zipfile
import gdown
from cnnClassifier import logging
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def download_data(self):
        """
        Downloads data from source_url to local_data_file
        """
        try:
            dataset_url = self.config.source_url
            zip_download_dir = self.config.local_data_file
            os.makedirs("artefacts/data_ingestion", exist_ok=True)
            logging.info(f"Downloading data from {dataset_url} to {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]
            file_prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(file_prefix+file_id, zip_download_dir)
            logging.info(f"Downloaded data from {dataset_url} to {zip_download_dir}")

        except Exception as e:
            logging.error(e)
            raise e
        
    def extract_zip_file(self):
        """
        Extracts zip file to unzip_dir

        Return:
            None
        """
        try:
            zip_download_dir = self.config.local_data_file
            unzip_dir = self.config.unzip_dir
            os.makedirs(unzip_dir, exist_ok=True)
            logging.info(f"Extracting data from {zip_download_dir} to {unzip_dir}")

            with zipfile.ZipFile(zip_download_dir, 'r') as zip_ref:
                zip_ref.extractall(unzip_dir)
            logging.info(f"Extracted data from {zip_download_dir} to {unzip_dir}")

        except Exception as e:
            logging.error(e)
            raise e

