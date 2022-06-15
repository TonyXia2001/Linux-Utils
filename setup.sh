#!/bin/bash

# back up bashrc
cp ~/.bashrc ./.bashrc_cp

# change command prompt style
echo '' >> ~/.bashrc
echo '' >> ~/.bashrc
echo '#prompt setting' >> ~/.bashrc
echo 'PROMPT_DIRTRIM=1' >> ~/.bashrc
echo 'PS1="\[\e[0;36m\]TonyX\[\e[m\] \[\e[0;32m\]\A\[\e[m\] \[\e[0;36m\]\w\[\e[m\] > "' >> ~/.bashrc

# Create an alias for UCLA linux server
echo '' >> ~/.bashrc
echo '# aliases' >> ~/.bashrc
echo 'alias lnxsrv="ssh -Y tanglin@lnxsrv09.seas.ucla.edu"' >> ~/.bashrc
echo 'alias chrome="google-chrome &"' >> ~/.bashrc

# update current terminal
source ~/.bashrc
