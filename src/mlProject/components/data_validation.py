import os
from mlProject import logger
import pandas as pd
from mlProject.entity.config_entity import DataValidationConfig

class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            col_schema = self.config.all_schema.keys()         
            
            count = 0
            for col in all_cols:
                #validation check for column name and datatype present in schema.yaml against data file
                if (col not in col_schema) or (data.dtypes[col] != dict(self.config.all_schema)[col]):
                    count += 1
            
            if count > 0:
                validation_status = False
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f"Validation status: {validation_status}")
            else:
                validation_status = True
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e