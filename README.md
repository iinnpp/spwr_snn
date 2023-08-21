## Code for spiking neural network model from "A developmental increase of inhibition promotes the emergence of hippocampal ripples"

Preprint on biorxiv ([here][spwr_biorxiv]).

[spwr_biorxiv]:https://www.biorxiv.org/content/10.1101/2023.08.11.552951v1

#### Requirements

brian2 v.2.4.2
pypet v.0.6.0

#### How-to run

1. Specify the parameters to test in explored_params.py. 

The provided example is a run with external input and membrane noise at one level of EI and II inhibition.

2. Run model_main.py script. 

The result are saved in current_dir/'runs'/%Y%m%d_%H%M%S subfolder. This subfolder includes 3 folders:
* data (parameters used in the run in hdf5 format)
* logs (logs of the model run in .txt files, errors are written in separate ERROR.txt file)
* output (the results of the model simulation in .npy format, subfolder for every run)

Results include: LFP and spiking data plus overview figure with LFP, population rates, spiking raster plots and fractions of active neurons(.png).



