# imports:
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('darkgrid')

from statsmodels.formula.api import ols
import statsmodels.api as sm
import scipy.stats as stats


def check_for_assumptions(modelname):
#     rsquared = modelname.rsquared
#     params = modelname.params
#     print(f'Rsquared of Model: {rsquared}')
#     print('----------')
#     print('Beta values of Model:')
#     print(params)
#     rainbow_statistic, rainbow_p_value = linear_rainbow(model1)
#     print("Rainbow statistic:", rainbow_statistic)
#     print("Rainbow p-value:", rainbow_p_value)
    fig, ax = plt.subplots(1,2, figsize=(12,6))
    residuals = modelname.resid
    fig = sm.graphics.qqplot(residuals, dist=stats.norm, line='45', fit=True, ax=ax[0])
    ax[0].set_title('QQ-Plot of Residuals')
    ax[1].scatter(modelname.predict(), modelname.resid)
    sns.set(font_scale = 1)
    ax[1].set_title('Homoscadasicity Assumption')
    plt.xlabel('Model Predictions')
    plt.ylabel('Model Residuals')
    ax[1].plot(modelname.predict(), [0 for i in range(len(df))], color = 'red')
    fig.tight_layout()
    return plt.show()


def z_score(feature, df):
    """
    feaure is a string of the feature you want the z-score of
    df is the dataframe where the feature can be found
    """
    z_name = 'z_' + feature
    df[z_name] = (df[feature] - df[feature].mean()) / df[feature].std()
    
    return df


def model(lst_of_features, df, target_var):
    """
    lst_of_features is a list of strings of the features to use from the df
    df is the data frame to subset the features from 
    target_var is a string of the target variable
    """

    # Create a dataframe with only the target and the chosen corellation feature
    df_model = df[lst_of_features]

    # build the R-style formula.
    target = target_var
    copy_lst_features = lst_of_features.copy()
    copy_lst_features.remove(target)
    x_vals = copy_lst_features
    x_formula = '+'.join(x_vals)
    formula = target + '~' + x_formula

    # Fit the model on the dataframe composed of the two features
    model = ols(formula=formula, data=df_model).fit()
    
    print(model.summary())
    # view r^2 and model summary:
    
    # check assumptions
#     normality_assumption(model)
#     homo_assumption(model, df)
    
    return model


def normality_assumption(model):
    # plot normality assumption
    fig, ax = plt.subplots(figsize = (15, 10))
    figure = sm.graphics.qqplot(model.resid, dist=stats.norm, line='45', fit=True, ax = ax);
    ax.set_title('QQ-Plot of Residuals', fontsize = 25)
    return plt.show()


def homo_assumption(model, df):
    # plot homoscadasicity assumption
    fig, ax = plt.subplots(figsize = (15, 10))
    plt.scatter(model.predict(), model.resid)
    sns.set(font_scale = 1)
    fig.suptitle('Scatter Plot of Model Predictions vs. Residuals', fontsize = 25)
    # ax.set_title('Homoscadasicity Assumption Not Met', fontsize = 20) - change this to an iff statement maybe...
    plt.xlabel('Model Predictions', fontsize = 18)
    plt.ylabel('Model Residuals', fontsize = 18)
    ax.tick_params(labelsize=10)
    plt.plot(model.predict(), [0 for i in range(len(df))], color = 'red')
    return plt.show()

def heatmap_multi(x_features, df):
    """
    Creates a heatmap of all the x feautres in a model to show multicollinearity.
    x_features (lst):  A list of strings of the column header names of the x features in the model
    df:  the dataframe where the features belong
    returns the plotted heatmap
    """
    df_x_feats = df.loc[:, x_features]

    x_corrs = df_x_feats.corr()

    mask = np.triu(np.ones_like(x_corrs, dtype=np.bool))
    f, ax = plt.subplots(figsize = (18, 16))
    sns.heatmap(x_corrs, mask = mask, cmap="YlGnBu", vmax = 0.3, 
            center = 0, square = True, linewidths = 0.5, 
            cbar_kws = {'shrink': 0.5})
    ax.tick_params(axis='both', which='major', labelsize=20, labelrotation = 45)
    ax.set_title('Heat Map of Feature Multicollinearity', fontsize = 30)
    
    return plt.show()


def Cohen_d(group1, group2):
    """
    Takes two groups and returns the cohen d effect size
    """
    diff = group1.mean() - group2.mean()

    n1, n2 = len(group1), len(group2)
    var1 = group1.var()
    var2 = group2.var()
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    
    d = diff / np.sqrt(pooled_var)
    print(f"Effect Size for difference in Home Prices for the two groups (Cohen's d): {d}")
    
    return d


def ttest_vis(group1, group2, test_result):
    """
    takes 2 samples and a t-test result and returns a visualisation of the critical value and t statistic.
    """
    xs = np.linspace(-4, 4, 200)
    # use stats.t.pdf to get values on the probability density function for the t-distribution
    # the second argument is the degrees of freedom
    ys = stats.t.pdf(xs, len(group1)+len(group2)-2, 0, 1)
    t_crit = np.round(stats.t.ppf(1 - 0.05, df=len(group1)+len(group2)-2),3)

    fig = plt.figure(figsize=(15,8))
    ax = fig.gca()

    # plot the lines using matplotlib's plot function:
    ax.plot(xs, ys, linewidth=3, color='darkblue', alpha=.75)

    ax.axvline(t_crit,color='green',linestyle='--',lw=4,label='critical t-value', alpha=.75)
    ax.axvline(test_result[0],color='red',linestyle='--',lw=4,label='test t-stat', alpha=.75)
    ax.legend()
    ax.fill_betweenx(ys,xs,t_crit,where= xs > t_crit)
    return plt.show()