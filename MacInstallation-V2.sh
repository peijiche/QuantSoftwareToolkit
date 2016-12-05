
# Created on Sept 3, 2016

# @author: Peiji Chen
# @contact: m
# @summary: My Updated Mac Installation script of QSTK 
#

# The updated doc is at https://docs.google.com/document/d/1qOzB-aUtCLcPPLfwEkwaCIoCsVe5MV2AkDnhZwESrSU/edit#



# Homebrew has already been installed.
echo "Installing python"
brew install python
echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.bash_profile
source ~/.bash_profile

#brew tap samueljohn/python
#brew tap homebrew/science

#echo "virtualenv"
pip install virtualenv
pip install nose
pip install pyparsing
pip install python-dateutil

echo "Installing gcc which includes gfortran"
brew install gcc

echo "Installing numpy, scipy, matplotlib"
pip install numpy
pip install scipy
pip install matplotlib

# virtualenv env --distribute --system-site-packages
# source ~/QSTK/env/bin/activate

echo "Install pandas, scikits"
pip install pandas
pip install scikits.statsmodels
pip install scikit-learn


# echo "Create QSTK directory"
#git clone https://github.com/QuantSoftware/QuantSoftwareToolkit.git	# original
#git clone https://peijicheyahoo@bitbucket.org/peijicheyahoo/quantsoftwaretoolkit.git  # forked and cleaned up

cd quantsoftwareToolkit
pip install QSTK


echo "validating the installations"
echo "you should see the following last line"
echo " Everything works fine: You're all set." 
cd Examples
python Validation.py







