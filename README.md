# QSAR


### QSAR1 
Fetches all the data and files from chEMBL for the drug interactions performed on HIV. Converts it into a data frame containing chEMBL ID, canonical smiles, IC50 and bioactivity class. The bioactivity class groups the drugs with IC50 values. Anything above 10000 is active, between 1000 and 10000 is intermediate and anything less than 10000 is inactive.

### QSAR2

Calculates the lipinski descriptors for the molecule of interest and converts the IC50 values to the pIC50 value. Filters the sample between active compounds and inactive compounds. These features are further subjected to statistical analyses (Mann-Whitney tests) to assess the significance of each column. These are plotted and the final data frame of the significant columns are used for the further analyses.

### QSAR3
Reads the output of QSAR2 and makes a dataframe consisting chembl ID and the structure. Using these, two columns creates a .smi file on which padel is downloaded and run to obtain the molecule's finger printsfrom pubchem. The pIC50 is tagged with the fingerprints and then stored as the final output of this file.

### QSAR4
Takes the input of QSAR3 and divides the dataset into train and test sets. Then runs the machine learning algorithms to predict the pIC50 values. This also helps to understand how the predictions are made compared to the data through visualization.
