import argparse
import datetime
from pathlib import Path
import model

def handle_results(path):
    print(f"---Loading configuration: {path}---")
    model.main(path)

parser = argparse.ArgumentParser(prog='cli',
                                description="Command Line Interface for Contribution Measure Simulation",
                                epilog="Thanks you for using our tool ;)!")
general = parser.add_argument_group("general output")
general.add_argument("path") 

args = parser.parse_args()
target_dir = Path(args.path)

if not target_dir.exists():
    print("The target directory doesn't exist.")
    raise SystemExit(1)

if not str(target_dir).endswith('.json'):
    print("The configuration file must be in json format!")
    raise SystemExit()

handle_results(path=target_dir)