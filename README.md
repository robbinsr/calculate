You are reading the README.md file in the calculating GitHub repository for Russ Robbins. This is a public service project that is a work in progress. Many non-interactive examples of confusion matrices exist on the internet. To my knowledge, no robust interactive confusion matrix is widely available. 

What is a confusion matrix? Why is it valuable?

Performance measures for tools that indicate whether something has occurred or has not occurred can be evaluated using a confusion matrix. 
For example, if a medical test is used to indicate whether I actually have cancer, how likely is it to be actually correct in its indication?

Similarly, performance measures for tools that predict whether something will occur or will not occur can be reported a confusion matrix.

For example, if I use a particular marketing campaign with a particular kind of customer, how likely is the campaign to be effective with this customer?

How will this interactive confusion matrix be valuable? What are its use cases?

The data product of this project seeks to:

1. Demystify the confusion matrix idea for non-scientist managers who may want to use its performance outputs (e.g., accuracy, precision).
2. Provide a "calculator" to help a researcher planning an experiment to easily see what needs to occur to acheive her goals.
3. Provide a "calculator" to help a data engineer perform sensitivity analysis, before spending effort to build a binary classifier.
4. Visually explain to data science customers or students the relationships of probabilities in the binary classification task.

How will a person actually use the interactive confusion matrix?

As currently designed, a user to enter three known or expected values. Based on these values the other values (up to 32) will be computed. Further, the computations used to generate the other values will be able to be seen. The user could then try other values, and in the process, think about all of the prospective tradeoffs for a particular planned prediction tool.

Ok, tell me more:

A confusion matrix is at its core a 2 by 2 table that presents the combinations of predictions about whether something will occur versus whether something actually did occur. The four "cells" in the 2 by 2 table are:

1. The number of times something was predicted and it occured (true positive). 
2. The number of times something was predicted and it did not occur (false positive). 
3. The number of times something was predicted to not occur, but it actually did occur (false negative). 
4. The number of times something was predicted to not occur, and it actuality, it did occur. (true negative).

The combinations of sums, differences, products, and quotients can be used to express various aspects of a predictive tool.

The twelve core probabilities that will be shown are:

1. True Positives
2. False Positives (a.k.a., Type I Errors, False Alarm)
3. True Negatives
4. False Negatives (a.k.a., Type II Errors)
5. Positive Predictive Value (a.k.a., Precision)
6. Negative Predictive Value
7. False Discovery Rate
8. False Omission Rate
9. True Positive Rate (a.k.a., Sensitivity, Recall)
10. False Positive Rate (a.k.a., Specificity)
11. False Positive Rate (a.k.a., Fallout)
12. False Negative Rate (a.k.a., Miss Rate)

Some of the derivative performance metrics planned to be shown include:

1. Accuracy Rate
2. Misclassification (a.k.a. Error) Rate
3. Prevalence Rate
4. Positive Likelihood Ratio
5. Negative Likelihood Ratio
6. Diagnostic Likelihood Ratio
7. Null Error RAte
8. Cohen's Kappa
9. F Score

Ok, what is the planned design of the product?

The current "back end" design includes:

1. an argument parser which parses and passes command line arguments.
2. a Python dictionary data structure that stores probabilities as provided or computed,
3. 56 probability equation-based lambda (anonymous) functions,  
4. another Python dictionary that contains and dispatches lambdas,
5. calls to the lambdas through the dictionary based on whether probabilities are known or not known. 

The front-end components include:

1. a grid framework just like a confusion matrix
2. that accepts any three input probabilities
3. calls calculate.py with the three inputs
4. presents the results in the grid framework

The code in this repository should provide a glimpse into my ability to design and develop robust, documented data oriented applications. 

