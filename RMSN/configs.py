
import os
import libs.net_helpers as helpers
import numpy as np

ROOT_FOLDER = os.path.dirname(os.path.realpath(__file__))
MODEL_ROOT = os.path.join(ROOT_FOLDER, "models")
RESULTS_FOLDER = os.path.join(ROOT_FOLDER, "results")


def get_parameters_from_string(serialisation_string):

    spec = serialisation_string.split("_")
    dropout_rate = float(spec[0])
    hidden_layer_size = int(spec[1])
    num_epochs = int(spec[2])
    minibatch_size = int(spec[3])
    learning_rate = float(spec[4])
    max_norm = float(spec[5])

    return (dropout_rate, hidden_layer_size, num_epochs, minibatch_size, learning_rate, max_norm)


def load_optimal_parameters(net_name, expt_name, select_max=False, add_net_name=False):

    model_folder = os.path.join(MODEL_ROOT, net_name)

    hyperparam_df = helpers.load_hyperparameter_results(model_folder, net_name)

    print(hyperparam_df.columns)
    col = hyperparam_df.columns[0]
    validation_scores = hyperparam_df[col]["validation_loss"]


    best_expt = col

    serialisation_string = best_expt.replace(expt_name+"_", "")
    params = get_parameters_from_string(serialisation_string)

    if add_net_name:
        params = [net_name] + list(params)

    return params


# In[*]: Test Stuff:
if __name__ == "__main__":
    expt_name = "treatment_effects"
    net_name = "treatment_rnn_action_inputs_only"


    test = load_optimal_parameters(net_name, expt_name, select_max=True)


