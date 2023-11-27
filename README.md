# IDA_2024_demo
## 1. Introduction
This repository allows to re-create series of experiments presented in the paper, as well as running custom experiments using attached libraries for generating federated data splits
and performing federated training. 
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
The Demo Library supports two types of operations to configure your simulation. Firstly, you can run the simulation using a pre-configured JSON format. Secondly, you can manually 
insert all the parameters.
Navigate inside the ida_2024_demo/ida_2024_demo folder and run:
~~~
python cli.py -c configuration.json
~~~
or
~~~
python cli.py -m
~~~
for manually inserting all the parameters.

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
