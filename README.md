# CS50P-Final-Project

# Naruto Character and Villages Viewer
### Description 
The Naruto Character and Village Viewer is a Python-based interactive application that allows users to explore detailed information about characters and villages from a fictional dataset. Users can choose a village to display a list of its characters along with their unique traits and nature types, or get detailed information about a randomly selected character.


### Features
1. Display Village Characters: Select a village to see a list of its characters with their unique traits and nature types.
2. Random Character Info: Display detailed information about a randomly selected character.

### How to Run
1. Clone the repository or download the source code.
2. Ensure you have Python installed (preferably Python 3.6 or higher).
3. pip install tabulate (Installing the dependencies)
4. Prepare the data files:
    - characters.json: Contains character data.
    - villages.json: Contains village data.

### Pre-requisite
#### Data Preparation

The project relies on two JSON files:

- characters.json: Contains detailed information about various characters.
- villages.json: Contains information about different villages and their associated characters.

These JSON files were created to store structured data, making it easy to load and manipulate within the Python program. I generated these files using the API's and data found from [Naruto Database](https://narutodb.xyz/)

### Program Details

#### Main Script
The main script (main.py) is designed to load the data from the JSON files and provide an interactive command-line interface for the user. The key components of the script are:

1. Data Loading: The script begins by loading the JSON data into Python dictionaries using the json module.
2. User Interaction Loop: The script then enters a loop where it presents the user with options to either display characters from a selected village or get information about a random character.
3. Display Village Characters: If the user chooses to display characters from a selected village, the display_village_info function is called. This function prompts the user to select a village and then formats the village characters' data for display using the tabulate library.
4. Random Character Information: If the user opts for random character info, the random_character_info function selects a random character and displays their details.

#### Libraries Used
- json: For loading and parsing JSON data.
- tabulate: For displaying tabular data in a formatted manner.
- random: For selecting a random character from the dataset.

### References

- [PyPi](https://pypi.org/)
- [Naruto Database](https://narutodb.xyz/)

