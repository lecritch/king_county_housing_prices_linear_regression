from . import cleaning_functions as cfs
import pandas as pd
import datetime as dt


# Create dataframes:

def merge_tables():
    """
    This function loads all three tables from csv's and performs some basic data cleaning.
    It returns a dataframe with the three tables merged and cleaned down to the relevant features.
    """
    # load tables
    rps = pd.read_csv("../data/EXTR_RPSale.csv")
    res_build = pd.read_csv("../data/EXTR_ResBldg.csv")
    parcel = pd.read_csv("../data/EXTR_Parcel.csv", encoding='latin-1')
    
    # create list of tables to be able to perform similar tasks on all tables
    tables = [rps, res_build, parcel]
    
    for table in tables:
        # make all column names for all tables lower case:
        cfs.lower_cols(table)
        
        # pad major/minor columns and create major_minor column:
        cfs.maj_min_index(table)
        
        
    
    
    ## rps specific modifications: ##
    
    # change document date to datetime object and isolate 2019 data
    rps['documentdate'] = pd.to_datetime(rps['documentdate'])
    rps2019 = rps[rps['documentdate'].dt.year == 2019]
    
    # choose relevant property type items
    prop_types = [11, 12, 14, 18]
    rps2019 = rps2019[rps2019['propertytype'].isin(prop_types)]
    
    # ignore all sales prices $0 or below:
    rps2019 = rps2019[rps2019['saleprice'] > 0]
    
    # choose relevant principal use items
    princ_use = [6,2]
    rps2019 = rps2019[rps2019['principaluse'].isin(princ_use)]
    
    # choose relevant property class items
    prop_class = [8,3,9]
    rps2019 = rps2019[rps2019['propertyclass'].isin(prop_class)]

    # drop irrelevant columns
    cols_to_drop = ['volume', 'page', 'platnbr', 'plattype', 'platlot', 'platblock', 'sellername', 'buyername']
    rps2019.drop(columns = cols_to_drop, inplace = True)
    
    ## merge rps with res_build:
    rps_res_build = rps.merge(res_build, on='major_minor', suffixes=("", "_resbldg"))
    
    ## merge rps_res_build with parcel
    df = rps_res_build.merge(parcel, on='major_minor', suffixes=("", "_parcel"))
    
    # isolate down to relevant features
#     df = df.loc[:, ['saleprice', 'sqfttotliving', 'yrbuilt', 'yrrenovated', 'bedrooms',
#                  'zipcode', 'sqftopenporch', 'sqftenclosedporch', 'sqftdeck', 'heatsystem',
#                  'heatsource','bathhalfcount', 'bath3qtrcount', 'bathfullcount', 'condition',
#                  'hbuasifvacant', 'inadequateparking', 'mtrainier', 'olympics', 'cascades', 
#                  'territorial', 'seattleskyline', 'pugetsound', 'lakewashington', 'lakesammamish',
#                  'smalllakerivercreek', 'otherview', 'wfntlocation', 'trafficnoise', 'airportnoise',
#                  'powerlines', 'othernuisances', 'adjacentgreenbelt']]
    
    return df









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