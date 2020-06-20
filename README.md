# Analysis and Modelling of King County, WA Home Sale Prices

An analysis and model by Luluva Lakdawala, Amanda Potter and Leana Critchell

## Setting the Scene:

This project investigates the factors that determine housing prices in King County, Washington.  Our model and investigation is directed towards first time home buyers who are looking to live in a single family home.  Many factors contribute to real estate sales prices, and we aim to discover what some of these driving factors are. 

### Aims:

This project aims to:
- Investigate some of the features that appear to have a relationship with King County housing sale prices
- Develop a model that predicts housing prices in King County using the features that we identify
- Validate the following claims made by real estate professions:
    - Higher square footage increases home sale price
    - The presence of a nuisance (power lines, traffic noise, airport noise) decreases home sale price
    - Having a porch increases home sale price

### Definitions:

- Single family home:
    - A single family home is defined in this project as a single residence on one lot.  Condos are not included in our analysis/model but townhomes are.
- First-time home buyers:
    - Home buyers who are making their first ever home purchase.  We have made the assumption in our analysis that first-time home buyers will not typically buy homes greater than $2.5million 
- Model:
    - The term model referred to through this project is in reference to the linear regression model which we build to explain the variance in home sale prices
- Features:
    - Features refer to the independent variables we choose for our model to help predict sale prices
- Target:
    - Sale Price is our target variable which our model aims to predict

### Data:

The data used in this project is from the King County Department of Assessments website and can be found [here](https://info.kingcounty.gov/assessor/DataDownload/default.aspx).  From this link, you can find the files/tables that were used in this project:
- Real Property Sales
- Parcel
- Residential Building
- Lookup

Our analysis was only looking at the most recent data from 2019 so the data was filtered to this accordingly. 

Additional information about the table identifiers can be found [here](https://www5.kingcounty.gov/sdc/Metadata.aspx?Layer=parcel#AttributeInfo).

Note that this modelling analysis contains the 'stream lined' version iterations from getting from our first simple model to our final model.  To get a more in depth view of our exploration process, mistakes and tears - I mean - dead ends, please refer to [Leana's](exploratory/lmc_notebooks), [Luluva's](exploratory/ll_notebooks) and [Amanda's](exploratory/asp_notebooks) notebooks.

### Analysis Takeaways, Future Investigations and Recommendations:

- Our analysis finds square footage of total living area, porch and deck, bathroom count, building grade and township to be some of the more significant driving factors of home sale prices.
- We find that a higher square footage does increase home sale prices in King County
- We find that the presence of nuisances has little affect on home sale prices in King County
- We find that having a porch does increase the home sale price in King County
- Is there a large difference in pricing when looking at condominiums?
- What are the drivers of price in the upper bounds of the market?
- Think about buying smaller and adding extension later
- Consider homes without decks/porches and add later to increase value
- Bathrooms are expensive - look for homes that already have the number of baths you desire even at the expense of square footage

