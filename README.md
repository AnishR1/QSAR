# QSAR


### QSAR1 
Fetches all the data and files from chEMBL for the drug interactions performed on HIV. Converts it into a data frame containing chEMBL ID, canonical smiles, IC50 and bioactivity class. The bioactivity class is grouping the drugs with IC50 values. Anything above 10000 is active, between 1000 and 10000 is intermediate and anything less than 1000 is inactive.


