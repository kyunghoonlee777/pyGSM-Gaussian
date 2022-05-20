export PYTHONPATH=~/works/auto_ts/pyGSM/pygsm/

conda activate pygsm

python -u ../pygsm/wrappers/main.py  -xyzfile R.xyz  \
    -isomers isomers.txt \
    -mode SE_GSM \
    -num_nodes 7 \
    -package Gaussian \
    -lot_inp_file gstart \
    -ID 1 \
    -coordinate_type DLC \
    -max_gsm_iters 30
