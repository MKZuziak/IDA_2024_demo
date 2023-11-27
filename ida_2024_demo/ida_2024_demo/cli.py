import argparse
import datetime
from pathlib import Path
import model

def handle_results(path):
    print(f"---Loading configuration: {path}---")
    model.main(path)


def handle_from_json(path):
    if not path.exists():
        print("The target directory doesn't exist.")
        raise SystemExit(1)

    if not str(path).endswith('.json'):
        print("The configuration file must be in json format!")
        raise SystemExit(1)

    print(f"---Loading configuration: {path}---")
    model.main(path)


def parse_input_str(choice: str,
                        choices: list):
    while True:
        input_1 = input(f"Please select {choice}. Available choices: {*choices,}: ").lower()
        if input_1 in choices:
            return input_1
        else:
            print(f"Invalid input. Valid inputs: {*choices,}")


def parse_input_int(choice: str,
                    limited_by: str = None,
                    limit: int = None):
    while True:
        input_2 = input(f"Please select {choice} (must be an int): ")
        try:
            input_2 = int(input_2)
            if limited_by and limit:
                if input_2 <= limit and input_2 > 0:
                    return input_2
                else:
                    print(f"Invalid input. Input must be smaller or equal to {limited_by} and larger than 0.")
            else:
                if input_2 > 0:
                    return input_2
                else:
                    print("Invalid input. Input > 0.")
        except ValueError:
            print(f"Invalid input. Input must be a positive integer.")


def parse_input_float(choice: str):
    while True:
        input_3 = input(f"Please select {choice} (must be an int): ")
        try:
            input_3 = float(input_3)
            if input_3 > 0:
                return input_3
            else:
                print("Invalid input. Input > 0.")
        except ValueError:
            print(f"Invalid input. Input must be a positive real number.")


def parse_input_list(limit: int):
    clients_transform = []
    while True:
        input_4 = input(f"Please select which client you would like to transform (by client ID, type b to skip): ")
        if input_4 == 'b':
            return clients_transform
        else:
            try:
                input_4 = int(input_4)
                if input_4 > 0 and input_4 < limit:
                    clients_transform.append(input_4)
                    input_5 = input("Would you like to continue inserting the clients? Type c if yes: ")
                    if input_5 == 'c':
                        continue
                    else:
                        return clients_transform 
            except ValueError:
                print(f"Invalid input. Input must be a positive integer.")
        

def handle_manual():
    configuration = {}
    configuration['dataset'] = parse_input_str(choice='dataset',
                                                   choices=['mnist', 'fmnist', 'cifar10'])
    configuration['split'] = parse_input_str(choice='splt_type',
                                                   choices=['homogeneous', 'heterogeneous_size', 'dirchlet'])
    configuration['clients'] = parse_input_int(choice='number of clients')
    configuration['iterations'] = parse_input_int(choice='number of iterations')
    configuration['sample_size'] = parse_input_int(choice='sample size',
                                                   limited_by="global number of clients",
                                                   limit=configuration['clients'])
    configuration['local_epochs'] = parse_input_int(choice='number of local epochs')
    configuration['batch_size'] = parse_input_int(choice='batch size')
    configuration['alpha-amplification'] = parse_input_int(choice='alpha amplification')
    configuration['global_learning_rate'] = parse_input_float(choice='global learning rate')
    configuration['learning_rate'] = parse_input_float(choice='local learning rate')
    configuration['transformations'] = parse_input_list(limit=configuration['clients'])
    model.main(from_json=False, config=configuration)

        
def main():
        parser = argparse.ArgumentParser(prog='cli',
                                    description="Command Line Interface for Contribution Measure Simulation",
                                    epilog="Thanks you for using our tool ;)!")
        general = parser.add_mutually_exclusive_group(required=True)
        
        general.add_argument("-m", "--manual", action="store_true")
        general.add_argument("-c", "--json", action="store_true")
        
        # For json mode
        parser.add_argument('-p', '--path', action='store', const=None, required=False)
        args = parser.parse_args()
        if args.json == True:
            if args.path == None:
                print("Enabling configuration mode requires setting up the path. Usage: 'python cli.py -c path/to/configuration.json' ")
                raise SystemExit(1)
            else:
                handle_results(path=args.path)
        # For manual mode
        else:
            handle_manual()
            
            
                
if __name__=='__main__':
    main()