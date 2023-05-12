
def get_units_and_links(dna_sequence):
    
    """
        Description:
            takes in a DNA sequence such as "-Gdo-Gdo-Ado-Ado-Tdo-Gro-Gro-Cro-Uro-Uro-Uro-Ur" and
            splits the different parts of the sequence into seperate counts. The seperation is
            from base sugar units and links within the chain

        Parametes:
            dna_sequence (str): a string representing a dna sequence
    
    """
    result_data = {"bs-units": {}, "links": {}}
    # Split sequence off of the "-" character 
    split_sequence = dna_sequence.split("-")[1:]

    # loop through each piece of the sequence and create counts 
    # for the base sugars and links
    for part in split_sequence:
        if not result_data["bs-units"].get(part[:2], False):
            result_data["bs-units"][part[:2]] = 1
        else:
            result_data["bs-units"][part[:2]] += 1

        
        # The end of the sequence will NOT have a link, so 
        # we need to make sure we check for the right sized
        # parts to see if there is a link to count
        if len(part) == 3:
            if not result_data["links"].get(part[-1], False):
                result_data["links"][part[-1]] = 1
            else:
                result_data["links"][part[-1]] += 1     

        
    return result_data


def get_molecular_masses(single_sequence):
    pass


def get_shipping_label(dna_sequence):
    """
    Description:
        takes in a DNA sequence such as "-Gdo-Gdo-Ado-Ado-Tdo-Gro-Gro-Cro-Uro-Uro-Uro-Ur" and
        determines the shipping label of just the base sugar units.

    Parametes:
        dna_sequence (str): a string representing a dna sequence

    returns:
        result_data (str): string representing DNA sequence in shipping format

    """
    result_data = ""
    split_sequence = dna_sequence.split("-")[1:]

    # create dna and rna seperated lists
    dna_only = []
    rna_only = []

    # loop through each piece of the sequence and check if the 
    # part is of DNA or RNA
    for part in split_sequence:
        if part[1] == "r" or part[1] == "m":
            rna_only.append(part[0])
        elif part[1] == "d":
            dna_only.append(part[0])
       
    

    # Format the lists properly for shipping label
    if dna_only:
        result_data =f"[{''.join(dna_only)}]{''.join(rna_only)}"
    elif dna_only and not rna_only:
        result_data =f"[{''.join(dna_only)}]"
    else:
        result_data =f"{''.join(rna_only)}"
    
    
    return result_data



