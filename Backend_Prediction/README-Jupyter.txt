README: SETTING UP AND CONFIGURING PYTHON ANACONDA MACHINE LEARNING ENVIRONMENT WITH JUPYTER

Install instructions for Mac OSX / Linux (also works for Windows)

Install Anaconda with Python 3.X
	https://www.anaconda.com/download/

Extra Windows Instructions
	For Windows, when you install Anaconda, choose to also install Anaconda Prompt.

Create Virtual Environment with Python 2.7
• Open Terminal
• Run the command:
	conda create -n py27 python=2.7 anaconda

Before installing packages or running a notebook Always Activate the Virtual Environment first!
Run:
      	source activate py27
	(on Windows: activate py27)

Download/Clone the Project content from:
	https://github.com/

Install The Following Conda/Pip Packages:
	conda install tensorflow keras html5lib py-xgboost
	pip install pydot pydotplus graphviz
	
Run the Spot Kernel Notebook:
In order to run the Jupyter notebook
	open the terminal
	source your Virtual Environment
	cd into the specific working directory
	run the command: jupyter notebook
A new browser window with your current directory will open and you can open the notebook spot_kernel.ipynb


