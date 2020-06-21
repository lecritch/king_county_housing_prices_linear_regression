# Analysis and Modelling of King County, WA Home Sale Prices

An analysis and model by Luluva Lakdawala, Amanda Potter and Leana Critchell

## Setting the Scene:

The factors that influence housing prices interest many people, from homeowners hoping to improve the market potential of their current homes, to policymakers making decisions about investment in public projects. Often we rely on the "expert judgement" of real estate professionals to determine which factors are the most important, but these recommendations may be out-of-date, irrelevant to our particular housing market, or otherwise inaccurate.

### Aims:

This project aims to develop a model that predicts housing prices in King County using the features that we identify
For our purposes, we will be creating this analysis for a group of first-time homebuyers in the King County, WA area.  Our group is mostly younger couples who are interested in the long-term investment value in their first home purchase.  In order to get the most ‘bang for the buck’ our home buyers want to understand how features in homes will impact sales price, and especially how to use this information to find properties that are a good value.

In addition, our group of first-time homebuyers has come to us with a lot of questions about so-called ‘expert advice’ they have received since they started to look into purchasing a home.  These claims include:

Higher square footage increases the sale price
Having a porch increase sale price
Homes with a ‘nuisance’ such as power lines, traffic noise, airport noise, etc. will have a lower sales price

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
- Real property sales; contains data about the sale of homes in King County
- Residential building; contains details about the buildings in King County
- Parcel; contains details about parcels in King County
- Lookup; contains details about many of the features in the other tables (e.g., sale insturment)

### Methodology
Our analysis began with the full data tables.  We made an initial cut of the data to include the following:
- sales taking place between Jan 1, 2019 and December 31, 2019
- sales of only residential properties, all commercial properties were excluded for this analysis


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

