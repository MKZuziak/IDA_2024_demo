import json
from numpy.random import uniform
import os

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
    "save_path": os.getcwd()}


def fetch_simulation_configuration(parsed_file):
    return {
        "orchestrator": {
        "iterations": parsed_file['iterations'],
        "number_of_nodes": parsed_file['clients'],
        "sample_size": parsed_file['sample_size'],
        'enable_archiver': True,
        "archiver":{
            "root_path": os.getcwd(),
            "orchestrator": True,
            "clients_on_central": True,
            "central_on_local": True,
            "log_results": True,
            "save_results": True,
            "save_orchestrator_model": True,
            "save_nodes_model": True,
            "form_archive": True
            },
        "optimizer": {
            "name": "Simple",
            "learning_rate": parsed_file['global_learning_rate']},
        "evaluator" : {
        "LOO_OR": False,
        "Shapley_OR": False,
        "IN_SAMPLE_LOO": True,
        "IN_SAMPLE_SHAP": False,
        "LSAA": True,
        "EXTENDED_LSAA": False,
        "ADAPTIVE_LSAA": False,
        "line_search_length": parsed_file['alpha-amplification'],
        "preserve_evaluation": {
            "preserve_partial_results": True,
            "preserve_final_results": True},
        "full_debug": True,
        "number_of_workers": 50}},
    "nodes":{
    "local_epochs": parsed_file['local_epochs'],
    "model_settings": {
        "optimizer": "Adam",
        "betas": (0.9, 0.8),
        "weight_decay": 1e-4,
        "amsgrad": True,
        "batch_size": parsed_file['batch_size'],
        "learning_rate": parsed_file['learning_rate'],
        "gradient_clip": 2,
        "FORCE_CPU": False}}}


def main(path):
    json_config = fetch_json(path)
    data_config = fetch_data_configuration(json_config)
    simulation_config = fetch_simulation_configuration(json_config)
    print(data_config)
    print(simulation_config)