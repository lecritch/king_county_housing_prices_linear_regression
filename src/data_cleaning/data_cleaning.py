def padded(row, pad_to):
    """
    This function takes an index item and pads it with 0's at the beginning
    to make it's total length equal to the pad_to value. 
    
    arguments:
    row (str):  item to add 0's infront of
    pad_to (int):  total length of padded item
    """
    num_zeros = pad_to - len(row)
    return num_zeros * '0' + row

def major_pad(row):
    """
    This function takes an index item and pads it with 0's at the beginning
    to make it's total length equal to the pad_to value. 
    
    arguments:
    row (str):  item to add 0's infront of
    pad_to (int):  total length of padded item
    """
    num_zeros = 6 - len(row)
    return num_zeros * '0' + row

def minor_pad(row):
    """
    This function takes an index item and pads it with 0's at the beginning
    to make it's total length equal to the pad_to value. 
    
    arguments:
    row (str):  item to add 0's infront of
    pad_to (int):  total length of padded item
    """
    num_zeros = 4 - len(row)
    return num_zeros * '0' + row


def maj_min_index(table):
    """
    Takes a table with a Minor and Major column, pads the Minor and Major columns with 0's at the beginning and then 
    concatenates Major and Minor together in a new column with the 10-digit number and sets it as the table index. 
    It also drops the old major/minor columns from the table
    """
    # change minor/minor to str
    table['Major'] = table['Major'].astype(str)
    table['Minor'] = table['Minor'].astype(str)
    
    # add padding to major/minor
    table['Major'] = table['Major'].apply(major_pad)
    table['Minor'] = table['Minor'].apply(minor_pad)
    
    # add maj_min column
    table['maj_min'] = table['Major'] + table['Minor']
    
    # drop old major/minor columns
    table.drop(labels = ['Major', 'Minor'], axis = 1, inplace = True)
    
    # set index
    table.set_index(keys = 'maj_min', inplace = True)
    
    return table

