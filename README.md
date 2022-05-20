# pyGSM-Gaussian
pyGSM that can be cooperated with GSM  The original pyGSM repository is available in https://github.com/ZimmermanGroup/pyGSM. 
Also, our code follows the same licencse with the license entered in the original repository. Here, we modified the pyGSM that can run with Gaussian softwares.

# Install instructions
Assuming anaconda3 is installed on your linux server, (check whether `which conda` is found) .
You need to set your virtual environment with following instructions:
1. `conda create -n gsm` (assuming environment name is gsm)
2. `conda activate gsm`
Then, your virtual environment named "gsm" is activated. Then, you need to install following python packages on your environment:
numpy
six
matplotlib
networkx
scipy
To install those packages, run following commands
1. `conda install -c anaconda numpy` (normally this is well installed within anaconda3, if import numpy works, this is not required)
2. `conda install -c conda-forge six`
3. `conda install -c conda-forge matplotlib`
4. `conda install -c conda-forge networkx`
5. `conda install -c conda-forge scipy`

# Gaussian setup
First, you must identify whether gaussian can run well. In case of Gaussian09, check it by `which g09`. If you want to run `g16`, after checking `which g16`, you need to change the variable `command` in `pygsm/level_of_theories/gaussian.py` as 'g16' (`command=g16`)

Also, you need to specify working directory of Gaussian. For this, you need to change the variable `self.working_directory` in `pygsm/level_of_theories/base_lot.py` to desried directory.

# Running code with Gaussian
In this repository, we provide example input and running script within `diels` folder. In the folder, there is a `run.sh` script. Below is the example:

export PYTHONPATH=~/works/auto_ts/pyGSM/pygsm/ \
conda activate pygsm \
python -u ../pygsm/wrappers/main.py  -xyzfile R.xyz  \
    -isomers isomers.txt \
    -mode SE_GSM \
    -num_nodes 7 \
    -package Gaussian \
    -lot_inp_file gstart \
    -ID 1 \
    -coordinate_type DLC \
    -max_gsm_iters 30

Here, directory of PYTHONPATH should be the directory of `pygsm` folder. Also, you need to activate virtual environment that you have created previously, gsm if you followed the same instruction described above. 
Then, by running the script, it runs gsm with single-ended GSM with driving coordinates written in isomers.txt. Also, it reads the input of `gstart` which is written on the first part of the input.

For detail instruction of inputs, check the arguments written in `pygsm/wrappers/main.py`, and the original repository: https://github.com/ZimmermanGroup/pyGSM

# Interpretation of output result

# Tips on inputs
