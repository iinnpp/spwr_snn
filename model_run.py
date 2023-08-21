import os
from pypet import Environment
from add_parameters import add_params
from model_network import run_net


def main(name, explore_dict, run_path):
    print('Preparing trajectory... '.format(name))
    output_folder = os.path.join(run_path, 'output')
    os.mkdir(output_folder)
    filename = os.path.join(run_path, 'data/', name + '.hdf5')
    log_folder = os.path.join(run_path, 'logs/')
    label = 'tr1'
    env = Environment(trajectory=label,
                      filename=filename,
                      log_folder=log_folder,
                      overwrite_file=False,
                      continuable=False)  # not clear what is that
    tr = env.trajectory
    add_params(tr)
    tr.f_explore(explore_dict)

    def run_sim(tr):
        print('Running simulation '.format(name))
        run_net(tr, output_folder)
        tr.f_add_result('z', 1.)

    env.run(run_sim)







