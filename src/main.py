def substructure_search(mols, mol):
    # Convertation of substructure SMILES to RDKit molecule object
    substructure = Chem.MolFromSmiles(substructure_smiles)
    
    # List to store matched molecules
    matched_molecules = []
    
    # Iterate through each SMILES string in smiles_list
    for smiles in smiles_list:
        molecule = Chem.MolFromSmiles(smiles)
        
        # Perform substructure search
        if molecule.HasSubstructMatch(substructure):
            matched_molecules.append(smiles)
    
    return matched_molecules