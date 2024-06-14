from cnnClassifier import logging
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_trainer import Training

STAGE_NAME = "Training Stage"


class ModelTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()


if __name__ == "__main__":
    try:
        logging.info(f"********************************")
        logging.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logging.info(f">>>>>> Stage {STAGE_NAME} completed successfully <<<<<<\n\nx================================x")
    except Exception as e:
        logging.error(e)
        logging.info(f">>>>>> Stage {STAGE_NAME} completed with errors <<<<<<")
        raise e