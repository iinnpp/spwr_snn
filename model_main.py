# add sys.path.append(os.path.join(os.getcwd(), 'brian_models/ripples_2populations_v2')) for imports to work
import os
import datetime
from explored_params import explore_dict, name
from model_run import main

# make a new subfolder inside /runs folder
current_dir = os.getcwd()
parent_dir = os.path.join(current_dir, 'runs')
# print(parent_dir)
run_dir = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
run_path = os.path.join(parent_dir, run_dir)
os.mkdir(run_path)

main(
    name=name,
    explore_dict=explore_dict,
    run_path=run_path
)
