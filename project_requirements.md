# Module 2 Final Project

Another module down--you're almost halfway there!

This will be your first of several modeling projects.  

<ins>For this project, your goal is to build a model that provides inferential insights into real-world housing data.</ins>

## BACKGROUND

The factors that influence housing prices interest many people, from homeowners hoping to improve the market potential of their current homes, to policymakers making decisions about investment in public projects. Often we rely on the "expert judgement" of real estate professionals to determine which factors are the most important, but these recommendations may be out-of-date, irrelevant to our particular housing market, or otherwise inaccurate.

## PROJECT GOAL

Stakeholders in King County, WA have requested statistical analysis to validate several claims about housing prices in the most recent full calendar year, 2019.

Six of the claims can be addressed directly with the three datasets (from the King County Department of Assessments) described later in this document:

1. Higher square footage increases home sale price<sup>1, 2</sup>
2. Having a porch increases home sale price<sup>3, 4</sup>
3. Having a beachfront or lakefront increases home sale price<sup>5</sup>
4. The house filling a higher proportion of the overall lot decreases home sale price<sup>6</sup>
5. The cost per square foot is lower in duplexes than in single-family homes<sup>7</sup>
6. The presence of a nuisance (power lines, traffic noise, airport noise) decreases home sale price<sup>1, 5</sup>

Three of the claims would require you to seek out additional datasets:

7. Access to "frequent transit" increases home sale price<sup>6</sup>
8. Lower speed limits increase home sale price<sup>6</sup>
9. Having an accessory dwelling unit (ADU) increases home sale price<sup>6, 8</sup>

 <ins><b>Your task is to build a linear regression model to represent sales prices in King County, and use it to address some of these claims.</b></ins>

## THE DATASET

For this project, you'll be working with the King County House Sales dataset. As with most real world data sets, the column names are not perfectly described, so you'll have to do some research or use your best judgment if you have questions relating to what the data means.

The data itself (CSV files) and descriptions of the data (DOC files) can be downloaded [here](https://info.kingcounty.gov/assessor/DataDownload/default.aspx). Additional information about the `MAJOR` and `MINOR` attributes can be found [here](https://www5.kingcounty.gov/sdc/Metadata.aspx?Layer=parcel#AttributeInfo).

<u>The particular tables required for this analysis are:</u>

 - Real Property Sales
 - Residential Building
 - Parcel

There is also a table called "Lookup" that explains the meaning of many of the attributes in the above tables (e.g. the `Street Surface` attribute of a parcel is a number with lookup code 60, which indicates that `1` means `PAVED`, `2` means `GRAVEL`, `3` means `DIRT`, and `4` means `UNDEVELOPED`).

## PROJECT REQUIREMENTS

**At minimum, your team of data scientists should:**

 - Build a linear regression model with a target variable of home sale price, which is statistically valid such that any interpretation of coefficients are valid
    - Do your best to have features meet the assumptions of a linear regression (no multicollinearity, linear with respect to the outcome variable, errors are normally distributed, etc.). 
      - Note: This is difficult! We will be looking most of all for _improvement_ on this score. In order to demonstrate improvement, you should create a (not very good) model that will serve as a kind of _baseline_. Then you can compare future regression models that you build with that baseline.
    - Try to maximize R<sup>2</sup> _without breaking any assumptions_
 - Address at least 3 of the 9 claims about housing prices made by subject-matter experts
    - Report the effect size as well as the statistical significance
    - It is perfectly acceptable to report a non-finding here
 - Communicate your findings

In any extra time:

 - Engineer additional features to improve R<sup>2</sup> (without violating assumptions), either with the existing datasets or by acquiring additional datasets.
 - Address additional claims from the subject-matter experts (without violating assumptions).
 - Utilize additional statistical techniques other than linear regression to address research questions related to the claims investigated.
 - Make use of bootstrapping to generate confidence intervals for your regression parameters and then compare them with the intervals that statsmodels generates.

## DELIVERABLES

1. A public GitHub repository.
2. An `environment.yml` file that contains all the necessary packages needed to recreate your `linreg-env` conda environment.
    - Unlike Mod 1, we haven't not given you an `environment.yml` file. Be sure to refer [to the documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) to learn how to create and export the `linreg-env` conda environment.
3. A standalone `src/` directory that stores all relevant source code.
    - All functions have docstrings that act as [professional-quality documentation](http://google.github.io/styleguide/pyguide.html#381-docstrings). 
    - If applicable, [well documented](https://www.sqlstyle.guide/) SQL queries with appropriate single-line or multiline comments.
    - Quality linear regression model
       - Your model should avoid violating any of the assumptions of a linear regression
       - Whenever necessary, briefly explain in comments the changes made from one iteration to the next, and why you made these choices
4. A standalone `data/` directory that stores all relevant raw and processed data files
    - **Be sure to include how the data was obtained!**
    - All large files are labeled in the `.gitignore` file to avoid having them accidentally live in your commit history.
5. A standalone `references/` directory that stores all relevant literature, data dictionaries, or useful references that were used to help you during the project.
    - Use this directory to store physical copies of the `.pdf` files; or
    - Create a `README.md` file that cites external resources that were used.
6. A standalone `reports/` directory that stores your `presentation.pdf` file
7. A standalone `notebooks/` directory that stores both your exploratory and report notebooks
    - A record of your workflow should be stored in `notebooks/exploratory`. Don't be afraid to leave in error messages, so you know what didn't work!
8. A user-focused `README.md` file that briefly covers your process, methodology and findings.
    - Someone with no context on your project should be able to use this document to understand the structure of your project, and adapt your code for their needs.
9. One final Jupyter Notebook file stored in `notebooks/report` that focuses on visualization and presentation
    - The very beginning of the notebook contains a description of the purpose of the notebook.
       - This is helpful for your future self and anyone of your colleagues that needs to view your notebook. Without this context, you’re implicitly asking your peers to invest a lot of energy to help solve your problem. Help them to jump into your project by providing them the purpose of this Jupyter Notebook.
    - Explanation of the data sources and where one can retrieve them
       - Whenever possible, link to the corresponding data dictionary
    - Custom functions and classes are imported from Python modules and are not created directly in the notebook. As soon as you have a working function in one of your exploratory notebooks, copy it over to `src` so it is reusable.
    - At least 4 meaningful data visualizations, with corresponding interpretations. All visualizations are well labeled with axes labels, a title, and a legend (when appropriate)
    - Take the time to make sure that you craft your story well, and clearly explain your process and findings in a way that clearly shows both your technical expertise and your ability to communicate your results!
10. An "Executive Summary" Keynote/PowerPoint/Google Slide presentation (delivered as a PDF export) that explains what you have found.
    - Make sure to also add and commit this file as presentation.pdf of your non-technical presentation to your repository with a file name of `reports/presentation.pdf`.
    - Contain between 5-10 professional quality slides detailing:
       - A high-level overview of your methodology
       - The results you’ve uncovered
       - Any real-world recommendations you would like to make based on your findings (ask yourself--why should the executive team care about what you found? How can your findings help the company/stakeholder?)
       - Avoid technical jargon and explain results in a clear, actionable way for non-technical audiences.
    - The slides should use visualizations whenever possible, and avoid walls of text
    - All visualizations included in this presentation should also be exported as image files (e.g. with `plt.savefig`, not by taking a screenshot) and saved under `reports/figures/`


## THE PROCESS

These steps are informed by Smart Vision's<sup>9</sup> description of the CRISP-DM process.

### 1. Business Understanding

Start by reading this document, and making sure that you understand the kinds of questions being asked. In order to narrow your focus, you will likely want to make some design choices about your specific audience, rather than addressing all of the "many people" mentioned in the background section. Do you want to emphasize affordability, investment, or something else? This framing will help you choose which stakeholder claims to address.

Some potential audiences are:

1. Homeowners who want to increase the sale price of their homes through home improvement projects
2. Advocacy groups who want to promote affordable housing
3. Local elected officials who want to understand how their policy ideas (e.g. zoning changes, permitting) might impact home prices
4. Real estate investors looking for potential "fixer-uppers" or "tear-downs"

Three things to be sure you establish during this phase are:

1. **Objectives:** what questions are you trying to answer, and for whom?
2. **Project plan:** you may want to establish more formal project management practices, such as daily stand-ups or using a Trello board, to plan the time you have remaining. Regardless, you should determine the division of labor, communication expectations, and timeline.
3. **Success criteria:** what does a successful project look like? How will you know when you have achieved it?

### 2. Data Understanding

Write a script to download the data (or instructions for future users on how to manually download it), and explore it. Do you understand what the columns mean? How do the three data tables relate to each other? How will you select the subset of relevant data? What kind of data cleaning is required?

Make sure that you document the process for retrieving this data so it can be reproduced by a future user.

It may be useful to generate visualizations of the data during this phase.

### 3. Data Preparation

Through SQL and/or Pandas, perform any necessary data cleaning and develop a query that pulls in all relevant data for analysis in a linear regression model, including any merging of tables. Be sure to document any data that you choose to drop or otherwise exclude. This is also the phase to consider any feature scaling or one-hot encoding required to feed the data into a linear regression model.

### 4. Modeling

The modeling phase in this project should be a brief stop-over as you are jumping back and forth between the data preparation and the evaluation phases.  If the data preparation was done correctly, it only takes a few lines of code to build a linear regression model.  Then you should be able to print out your model's metrics and quickly move to the evaluation phase.

(In future modules, there will be more complex steps involved with tuning the model itself.)

### 5. Evaluation

**Your goal here is not to build just one model; it is to build many models and then choose the best one.** In this case (which is different from future machine learning models), your goal is to gain additional insight into the housing sales data from 2019 in King County, as opposed to building a generalizable model that can make predictions about unseen data.

**In other words, you are not trying to build a tool to compete with the Zillow Zestimate to predict home values.**

Because of this framing, a higher R<sup>2</sup> is ideal, but you should not focus on attaining a higher R<sup>2</sup> so long as you have gross violations of the assumptions of a linear regression. These assumptions should be your focus both when selecting features and when assessing the quality of your model. Even with a relatively low R<sup>2</sup>, coefficients and p-values will be valid and meaningful if there are no violations of the assumptions.

This framing has some implications for your process. For example, you do not want to perform a train-test split or have some other form of hold-out data; you want all of your data to go into getting the best possible coefficients. There is also no single number you can reference to demonstrate that you have the best possible model; in this way causal inference is more of an art, whereas machine learning is more of a science. You can use as many features as you want, but every step of the way you need to check the assumptions, not just check whether R<sup>2</sup> has improved. Because R<sup>2</sup> can only go up when you add more features, you may want to consult the adjusted R<sup>2</sup> metric as well.

Your first cycle through these steps should result in some kind of "baseline" model.  Once you have that model, create a mini "report" that describes the model performance (in terms of R<sup>2</sup> or adjusted R<sup>2</sup>) as well as checks for the assumptions of linear regression.  The Learn labs [Assumptions for Linear Regression](https://learn.co/tracks/module-2-data-science-career-2-1/statistics-ab-testing-and-linear-regression/section-18-introduction-to-linear-regression/assumptions-for-linear-regression), [Ordinary Least Squares in Statsmodels (OLS)](https://learn.co/tracks/module-2-data-science-career-2-1/statistics-ab-testing-and-linear-regression/section-18-introduction-to-linear-regression/ordinary-least-squares-in-statsmodels-ols), and [Regression Diagnostics in Statsmodels](https://learn.co/tracks/module-2-data-science-career-2-1/statistics-ab-testing-and-linear-regression/section-18-introduction-to-linear-regression/regression-diagnostics-in-statsmodels) are a good starting point for this, but you are also free to use external resources, e.g. looking through the statistics available in the [Statsmodels `stats` submodule](https://www.statsmodels.org/stable/stats.html).

As you build each new model, perform these checks repeatedly to see whether the new models are better than the baseline.  You will almost certainly want to build functions to perform these checks once you get into a rhythm of tweaking the model slightly, evaluating the result, rinse, repeat.

### 6. Deployment

When you are approaching the end of the available time, choose your best model and report what it says about your research questions. An example finding you might report is: "There is a statistically significant relationship between `<x variable>` and housing price. For every increase of 1 `<x variable>`, the housing price increases by `<amount>`, all else being equal". Consider what types of visualizations would help to communicate the scale and direction of these findings.

Beyond just the numbers, tie these findings into a broader narrative that incorporates your business understanding.  Complete the deliverables listed above, and make sure you can answer the following questions about your process:

 - "How did you pick the question(s) that you did?"
 - "Why are these questions important from a business perspective?"
 - "How did you decide on the data cleaning options you performed?"
 - "Why did you choose a given method or library?"
 - "Why did you select those visualizations and what did you learn from each of them?"
 - "Why did you pick those features as predictors?"
 - "How would you interpret the results?"
 - "How confident are you in the predictive quality of the results?"
 - "What are some of the things that could cause the results to be wrong?"

## Citations

1. Gomez, J. 2019. "8 critical factors that influence a home’s value". OpenDoor. Available at: https://www.opendoor.com/w/blog/factors-that-influence-home-value
2. Buczynski, B. 2019. "5 Proven Ways to Increase Home Value". NerdWallet. Available at: https://www.nerdwallet.com/blog/mortgages/how-to-increase-home-value/
3. Taylor, A.B. 2019. "11 Features That Will Sell Your Home Faster". Kiplinger. Available at: https://www.kiplinger.com/slideshow/real-estate/T010-S001-home-features-today-s-buyers-want-most/index.html
4. Crow, S. 2019. "50 Clever Ways to Instantly Add Value to Your Home". BestLife. Available at: https://bestlifeonline.com/home-value-upgrades/
5. Unknown author. 2018. "5 Features That Make A Property Valuable". House Flipping School. Available at: https://houseflippingschool.com/5-features-valuable/
6. Ludwick, R. 2019. Personal correspondence.
7. Yeh, K. "Duplex vs. Single-Family Home: What's the difference and which one should I invest in?". Homebuyer's School by Brookfield Residential. Available at: https://stories.brookfieldresidential.com/homebuyersschool/duplex-vs.-single-family-home-whats-the-difference-and-which-one-should-i-invest-in
8. "This is What Could Happen to Your Resale Value if You Add an Accessory Dwelling Unit (ADU) to Your Silicon Valley Property". Acton ADU. Available at: https://actonadu.com/blog/this-is-what-could-happen-to-your-resale-value-if-you-add-an-accessory-dwelling-unit-adu-to-your-silicon-valley-property
9. "What is the CRISP-DM Methodology?" Smart Vision Europe. Available at: https://www.sv-europe.com/crisp-dm-methodology/
