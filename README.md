# Machine-Learning-Project_with_MLFlow


## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py


# How to run?
### STEPS 01 - Clone the repository:

```bash
https://github.com/AbhilashAnand06/Machine-Learning-Project_with_MLFlow
```
### STEP 02- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.11 -y
```

```bash
conda activate mlproj
```


### STEP 03- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 04- Run
```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## For MLflow, refer to the following link for the documentation

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui


### dagshub
[dagshub](https://dagshub.com/)

Run this to export as env variables:

```bash

import dagshub
dagshub.init(repo_owner='AbhilashAnand06', repo_name='Machine-Learning-Project_with_MLFlow', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)

```