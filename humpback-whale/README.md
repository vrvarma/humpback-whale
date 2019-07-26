# humpback-whale
Udacity MLND capstone project

# Setup instructions
  Install conda from [anaconda](https://www.anaconda.com/distribution/)
## Extract the code
  * In the zip file extract the code into a folder (for example humpback-whale)

## Software requirements
  * Install conda and follow the steps
  * Open a command prompt
  * conda create --name ml-project python=3.6.4
  * conda activate ml-project
  * cd humpback-whale
  * pip install -r requirements.txt

## Download the Kaggle data set
Download the dataset from Kaggle, by following these steps
* Install [Kaggle API](https://github.com/Kaggle/kaggle-api) from this link.

## Once the kaggle api is installed, do the following.
* Generate/Build  kaggle.json file from your Kaggle account
* mkdir -p ~/.kaggle
* cp kaggle.json ~/.kaggle/kaggle.json
* chmod 600 ~/.kaggle/kaggle.json
* cd humpback-whale
* kaggle competitions download -c humpback-whale-identification 
* rm -rf input
* mkdir -p input 
* unzip -q -d input/train train.zip
* unzip -q -d images test_images.zip
## Running the software
  * jupyter notebook
  * Select udacity-capstone.ipynb