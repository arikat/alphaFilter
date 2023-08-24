# alphaFilter
###### written by Aarya Venkat


alphaFilter is a Python script that processes a directory of AlphaFold2 models and outputs a list of models based on a mean confidence threshold. This is especially useful for filtering out AlphaFold2 models below a certain confidence level and ensuring that the models have a minimum number of desired residues. The goal of the script is for the user to quickly find high-confidence alphafold models without pulling models created from fragmentary sequences.

## Features

- Filter AlphaFold2 models by their plddt confidence scores.
- Ensure models have a minimum number of residues.
- Simple and easy-to-use command-line interface.

## Requirements

- Python 3.6 or later
- AlphaFold2 models in a directory

## Usage

To use alphaFilter, simply provide the path to the directory containing the AlphaFold2 models, the desired plddt confidence threshold, and the minimum number of residues a model should have.

```bash
python3 alphafilter.py -d DIRECTORY -t THRESHOLD -r RES_MINIM
```

### Arguments

- `-d DIRECTORY, --directory DIRECTORY`: Path to the directory containing the AlphaFold2 models.
- `-t THRESHOLD, --threshold THRESHOLD`: Threshold for plddt confidence. The default value is 90.
- `-r RES_MINIM, --res_minim RES_MINIM`: Filter minimum number of residues in AlphaFold2 structure.

### Optional Arguments

- `-h, --help`: Shows the help message and exits.

## Example

For a directory of AlphaFold2 models located at `./models`, to filter out models with a plddt confidence score below 92 and with less than 100 residues:

```bash
python3 alphafilter.py -d ./models -t 92 -r 100
```

## Contributing

Feel free to open issues or submit pull requests if you find any bugs or have suggestions for improvements.

