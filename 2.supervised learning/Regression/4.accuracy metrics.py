'''
Accuracy Metrics
R-square is the most common metric to judge the performance of 
regression models
𝑹^2 lies between  0-100%
Example: Performing linear regression on sq. Area (x) and Price (y) returns R-square value as 16 
This means you have 16% information to make an accurate prediction about the price

The disadvantage with R-squared is that it assumes every independent variable in the model explains variations 
in the dependent variable.
Adjusted R square is used in multiple linear regression problem

Adjusted R^2=1-{(1-R^2)(N-1)/(N-p-1)}
where R2 is R-squared value
P is number of predictor variables
N is number data points

Cost Function
Mean-Squared Error (MSE) is also used to measure the performance of a model.
𝑀𝑆𝐸 =1/N Summation(y-y(bar))^2
Where N is the number of data points
𝑦 is the predicted value by the model
𝑦(bar) is the actual value for the data point 

RMSE=(MSE)^1/2

These functions are called the loss function or the cost function, and the value has to be minimized.


Gradient Descent
Gradient descent is another algorithm used to reduce the loss function
It is an optimization algorithm that tweaks it’s parameters (coefficients) 
iteratively to minimize a given cost function to its minimum.
Model stops learning when the gradient (slope) is zero
Algorithm : 
1) Initialize parameter by some value
2) For each iteration calculate the derivative of the cost function 
and simultaneously update the parameters until a global minimum
formula

where ἀ is the learning rate 


Evaluating Coefficients
In regression analysis, p-values and coefficients together indicate which relationships in the model are 
statistically significant and the nature of those relationships.
p < 0.05 REJECT the Null hypothesis, meaning variables have some effect and need to be retained
p > 0.05 ACCEPT the Null hypothesis, meaning variables have no effect and can be removed
'''