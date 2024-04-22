# IDA_2024_demo
## 1. Introduction
This repository allows to re-create series of experiments presented in the paper 'Amplified Contribution Analysis for Federated Learning', as well as run custom experiments using attached libraries for generating federated data splits and performing federated training. 
## 2. How to Install
a) Clone the repo using:
~~~
git clone https://github.com/MKZuziak/IDA_2024_demo.git
~~~
b) Navigate to the clone folder and install the virtual environment with all the dependencies
~~~
poetry install
~~~
c) Enter the shell inside the poetry virtual environment
~~~
poetry shell
~~~
or
~~~
poetry [cmd]
~~~
## 2. How to Use
The Demo Library supports two types of operations to configure your simulation. Firstly, you can run the simulation using a pre-configured JSON format. Secondly, you can manually insert all the parameters.
Navigate inside the ida_2024_demo/ida_2024_demo folder and run:
~~~
python cli.py -c -p configuration.json
~~~
or
~~~
python cli.py -m
~~~
for manually inserting all the parameters.
To change the directory in which the results of the simulation will be stored, you can use '-s' option with desired global path.
~~~
python cli.py -c configuration.json -s global/path/to/desired/directory || python cli.py -m -s global/path/to/desired/directory
~~~
## 3. Using JSON format
All the required parameters are placed inside the configuration.json file. The template is as follows:
~~~
{
    "dataset": "mnist",      ### You can select: mnist, fmnist and cifar10 [str]
    "split": "homogeneous",      ### homogeneous, heterogeneous_size or dirchlet [str]
    "clients": 15,      ### Number of clients [int]
    "transformations": [0, 1, 2, 3, 4, 5],      ### Select clients (by ID) which will be noised out [list[int]]
    "iterations": 40,      ### Number of iterations [int]
    "sample_size": 3,      ### Size of the sample  [int]
    "global_learning_rate": 1.0,      ### Global Learning Rate [float]
    "local_epochs": 3,      ### Number of local epochs [int]
    "optimizer": "Adam",    ### Optimizer to choose from [str]
    "batch_size": 32,      ### Batch size [int]
    "learning_rate": 0.001,      ### Local learning rate [float]
    "alpha-amplification": 2      ### Alpha amplification [int]
}
~~~
Please note that in this case, alpha-amplification must be an int, as this is interpreted as the number of copies that will be added to the set (Remark no. 1 in the original paper).
## 4. Output format
The script will produce two different results: dataset generation output and simulation output. Dataset generation output will be saved in the current working directory at the time of invoking the python cli.py script. This category contains the dataset in a universal HuggingFace format, HuggingFace arrows that allow quick load of the cached dataset, distribution blueprint and transformations visualizations. This can be discarded or preserved, depending on the preferences. Simulation output will be saved in a 'demo_results' folder, and it will contain an 'archiver' subfolder with all the results. This category contains metrics from all training rounds, contribution evaluation metrics, preserved global and local models and more.

