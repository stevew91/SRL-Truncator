# This tool uses a reference list of protein accessions to truncate a given SRL into a specific SRL containing only proteins from the supplied list.

import pandas as pd
import sys

#set the working directory
cd "C:\Data\"

#set the inputs and output
full_srl = 'full_ion_library.txt'
protein_list = 'Proteins_Of_Intrest.txt'
output_SRL = 'Truncated_SRL.txt'

#run each line
srl = pd.read_csv(full_srl, sep="\t")
prt_list = pd.read_csv(protein_list, header=None)
outsrl = output_SRL
prt = prt_list[0].tolist()
nsrl = srl[srl["uniprot_id"].isin(prt)]
nsrl.to_csv(outsrl, sep="\t", index=False)
