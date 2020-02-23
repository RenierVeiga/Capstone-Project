# Capstone-Project
Machine learning project for stock market analysis.

# Missing Data and Generalization
  
  I found it very difficult to find stock market data on a small enough timeframe. For this reason I decided to work with data on a daily timeframe. Generalization can be an issue because of the limited amount of samples. In order to ensure this isn't and issue, noise will be added to the data so this can be fed to the model multiple times to ensure generalization and conversion. 

# Features and Dimensionality

  In order to have a higher success rate and minimize prediction error, relevant features(predictors) may be added to our samples. One feature to be consired in particular is the day of week. It is believed by many traders that the day of week has some impact on the market behaviour. Another feature to be considered is days to earnings release. The price of a stock tends to increase in volatility as the date approaches the earnings release date. Although I don't believe I can acquire this information at this time.
  
  One issue with increasing the number of features is the increase in dimentionalty. The higher the dimensionality of your model the more difficult it is to train it and less reliable it becomes. To account for this only the most relevant features are used to train the model. This problem can also be addressed by feeding the model the same original data with added random noise multiple times.
  
  # Data Smothing / Low Pass Filter
  
  In order to reduce the influence of noise on the model a the data will be smothed by log function before training the model, and converted back to the original scale when evaluating the prediction. 
    
  # Decomposition
  
  In order to reduce the model's complexity and predict more accurate results, the data will be decomposed in the form of f(x) = T(x) + T(x) + T(x), where f(x) is the original data decomposed into T(x) = Trend, S(x) = Seasonality and R(x) = Residual. Each decomposed function derived from a certain model and trained separately. The final prediction will be the sum of the evaluations of each decomposed function on the form of &Ycirc; = &Tcirc; + &Scirc; + &Rcirc; 
