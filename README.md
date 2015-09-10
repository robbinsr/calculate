You are reading the README.md file in the calculating GitHub repository for Russ Robbins. This is a project that is a work in progress. 

The purpose of the code in this repository is to provide some insight into how I am using or can use Python. The package is far from complete. When/if completed this will be the processor for an interactive binary classification confusion matrix that will allow you to enter three of any of the individual, joint, or conditional probabilities and in return receive the other thirteen probability values back. In addition, ratios and derivative ratios such as positive likelihood and diagnostic odds will be provided. The current design relies on

1. an argument parser which parses and passes command line arguments.
1. a dictionary that stores probabilities as provided or computed,
1. 56 probability equation-based lambda functions,  
1. a dictionary that contains and dispatches lambdas,
1. calls to the lambdas through the dictionary based on whether probabilities are known or not known. 

Concurrently, I am building an Angular-based front end. Its components are:

1. a grid framework just like a confusion matrix
1. that accepts any three input probabilities
1. calls calculate.py with the three inputs
1. presents the results in the grid framework

In a more advanced form, it could show the user the path from the three inputs to the probabilities and their ratios.

The code in this repository should provide a glimpse into my ability to design and develop robust, documented applications. 

Further, the result will provide individuals that are learning probability a method to see the relationships of probabilities, their complements, their intersections, their conditional values, as well as how all of these relate to Bayes' Rule. Currently individuals learning probability theory are given pieces of the pie, but never really see all the pieces in the pie and how they are all interdependent, in a concrete as well as abstract form.

Instead, usually it appears that students are provided the abstraction, but not concrete example, in its fullest, most meaningful form.
