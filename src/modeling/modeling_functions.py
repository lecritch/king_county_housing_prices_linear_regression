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