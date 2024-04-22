import json
import time
import pickle
import os
from numpy.random import uniform
from fedata.hub.generate_dataset import generate_dataset
import datasets
from forcha.components.orchestrator.evaluator_orchestrator import Evaluator_Orchestrator
from forcha.components.settings.evaluator_settings import EvaluatorSettings
from models.mnist_fmnist import MNIST_CNN
from models.cifar_resnet import ResNet18


def fetch_json(path):
    with open(path) as j_file:
        json_config = j_file.read()
    parsed_file = json.loads(json_config)
    return parsed_file


def fetch_data_configuration(parsed_file):
    return {
    "dataset_name" : parsed_file['dataset'],
    "split_type" : parsed_file['split'],
    "shards": parsed_file['clients'],
    "local_test_size": 0.3,
    "transformations": {client: {"transformation_type": "noise", "noise_multiplyer": uniform(0, 0.5)} for client in parsed_file['transformations']},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": parsed_file['clients'],
    "shuffle": True,
    "save_path": os.getcwd(),
    "alpha": 0.5}


def main(path = None,
         from_json: bool = True,
         config: dict = None,
         savepath = None):
    
    if from_json:
        config = fetch_json(path)
    data_config = fetch_data_configuration(config)
    
    os.chdir(savepath)
    # generating datset
    loaded_dataset = generate_dataset(config=data_config)
    orchestrator_data = loaded_dataset[0]
    nodes_data = loaded_dataset[1]
    
    settings = EvaluatorSettings(
        simulation_seed=42,
        global_epochs=config['iterations'],
        local_epochs=config['local_epochs'],
        number_of_nodes=config['clients'],
        sample_size=config['sample_size'],
        optimizer='SGD',
        batch_size=config['batch_size'],
        learning_rate=config['learning_rate'],
        in_sample_loo=True,
        in_sample_shap=False,
        in_sample_alpha=True,
        line_search_length=config['alpha-amplification'])

    if config['dataset'] == 'mnist' or config['dataset'] == 'fmnist':
        model = MNIST_CNN()
    else:
        model = ResNet18()
    
    orchestrator = Evaluator_Orchestrator(
        settings=settings, 
        full_debug=True,
        parallelization=False,
        number_of_workers=2
        )
    orchestrator.prepare_orchestrator(
        model=model, 
        validation_data=orchestrator_data)
    orchestrator.prepare_training(nodes_data=nodes_data)
    
    signal = orchestrator.train_protocol()

if __name__ == '__main__':
    main()