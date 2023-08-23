import os
import statistics
import argparse

def extract_plddt(pdb_file):
    plddt_values = []
    amino_acid_count = 0
    last_residue_number = None

    with open(pdb_file, 'r') as f:
        for line in f:
            if line.startswith("ATOM"):
                # B-factor column is columns 61-66 in PDB format.
                plddt = float(line[60:66].strip())
                plddt_values.append(plddt)
                
                # Residue number is columns 23-26 in PDB format.
                current_residue_number = int(line[22:26].strip())
                if current_residue_number != last_residue_number:
                    amino_acid_count += 1
                    last_residue_number = current_residue_number

    return plddt_values, amino_acid_count

def print_plddt(directory, threshold=90, min_amino_acids=250):

    # Print PDB files in a directory with a median pLDDT above a given threshold and a minimum amino acid count.

    for file in os.listdir(directory):
        if file.endswith(".pdb"):
            plddt_values, amino_acid_count = extract_plddt(os.path.join(directory, file))
            if statistics.mean(plddt_values) > threshold and amino_acid_count >= min_amino_acids:
                print(file)


def main():
    parser = argparse.ArgumentParser(description='Process a directory of AlphaFold2 model and output a list based on a mean confidence threshold.')
    parser.add_argument('-d', '--directory', help='Path to file directory', required=True)
    parser.add_argument('-t', '--threshold', help='Threshold for plddt confidence (default is 90)', type=int, default=90, required=True)
    parser.add_argument('-r', '--res_minim', help='Filter minimum number of residues in AlphaFold2 structure', type=int, default=90, required=True)


    args = parser.parse_args()

    print_plddt(args.directory, args.threshold, args.res_minim)

if __name__ == "__main__":
    main()
