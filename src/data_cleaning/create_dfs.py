import data_cleaning as dc


# Create dataframes:

def rps_2019_df():
    """Use this if you want lean df without AF features"""
    # load data
    rps = pd.read_csv("../data/EXTR_RPSale.csv")
    
    # change date to datetime object
    rps['DocumentDate'] = pd.to_datetime(rps['DocumentDate'])
    
    # create year column
    rps['year'] = rps['DocumentDate'].dt.year
    
    # create df of just 2019 entries    
    rps_2019 = rps[rps['year'] == 2019]
    
    # drop useless columns
    cols_to_drop = ['Volume', 'Page', 'PlatNbr', 'PlatType', 
                'PlatLot', 'PlatBlock', 'SellerName', 'BuyerName', 'year', 
                    'DocumentDate', 'RecordingNbr', 'AFForestLand', 'AFCurrentUseLand', 
                    'AFNonProfitUse', 'AFHistoricProperty', 'SaleReason', 'PropertyClass', 'SaleWarning']
    
    rps_2019.drop(columns = cols_to_drop, inplace = True)
    
        
    return rps_2019


def rps_2019_AF_df():
    """ Use this if you want the AFForestLand etc features"""
    # load data
    rps = pd.read_csv("../data/EXTR_RPSale.csv")
    
    # change date to datetime object
    rps['DocumentDate'] = pd.to_datetime(rps['DocumentDate'])
    
    # create year column
    rps['year'] = rps['DocumentDate'].dt.year
    
    # create df of just 2019 entries    
    rps_2019 = rps[rps['year'] == 2019]
    
    # drop useless columns
    cols_to_drop = ['Volume', 'Page', 'PlatNbr', 'PlatType', 
                'PlatLot', 'PlatBlock', 'SellerName', 'BuyerName', 'year', 
                    'DocumentDate', 'RecordingNbr', 'AFForestLand', 'AFCurrentUseLand', 
                    'AFNonProfitUse', 'AFHistoricProperty', 'SaleReason', 'PropertyClass', 'SaleWarning']
    
    rps_2019.drop(columns = cols_to_drop, inplace = True)
    
    # create a list of columns that I want to be bools:
    cols_to_bool = ['AFForestLand', 'AFCurrentUseLand', 'AFNonProfitUse', 'AFHistoricProperty']

    # create for loop that changes values in cols above to category and then codes them to 0's and 1's:
    for col in cols_to_bool:
        rps_2019[col] = rps_2019[col].astype('category').cat.codes
        
    return rps_2019