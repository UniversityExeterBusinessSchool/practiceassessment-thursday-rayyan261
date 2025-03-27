#######################################################################################################################################################
# 
# Name: Rayyan Ahmad 
# SID: 75001764
# Exam Date: 27- 03-2025
# Module:bemm458
# Github link for this assignment: https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-rayyan261 
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 

# Initialize an empty list to store (start, end) positions
my_list = []
##########################################ANSWERS############################################################################################################

# I am using my SID: 750001764
# The first digit is 7 and the last digit is 4.
# Therefore, I will only search for the words associated with keys 7 and 4 in the dictionary.

# The customer feedback text where we will look for the words
customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."""

# Provided dictionary of key comments
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',    # last digit of my SID
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',     # first digit of my SID
    8: 'overall',
    9: 'minor'
}

# Initialize an empty list to store (start, end) positions
my_list = []

# We only want the keys that match the first and last digit of my SID: 7 and 4
allocated_keys = [7, 4]

# Loop through the allocated keys
for key in allocated_keys:
    # Get the corresponding word from the dictionary
    word_to_find = key_comments[key]
    
    # Find the starting index of this word in the feedback
    start_index = customer_feedback.find(word_to_find)
    
    # If the word is found, find the ending index by adding the word length
    if start_index != -1:
        end_index = start_index + len(word_to_find)
        
        # Append the tuple of (start, end) to our my_list
        my_list.append((start_index, end_index))

# Print the final list of positions
print(my_list)
## OUTPUT (129, 136) & (142, 150)
## EXPLAINATION -  as per the SID the words "resolve" and "promptly," we choose the first and last digits of the SID each.

## The end index is determined by adding the length of each word, and the start index is determined using.find().
## If the words are present in the feedback, we save the (start, end) pairs in my_list.
## In order to verify the locations of each selected word, we lastly print my_list.


##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here:
# Insert last two digits of ID number here:

# Write your code for Operating Profit Margin

# Write your code for Revenue per Customer

# Write your code for Customer Churn Rate

# Write your code for Average Order Value

# Call your designed functions here
## my first two numbers of my SID -> 75
## my last two digits of my SID  -> 64
##########################################ANSWERS############################################################################################################

## This function is calculating the operating profit margin as % (perc)
def operating_profit_margin(operating_profit, revenue):
    return (operating_profit / revenue) * 100

## Function is calcuting the revenue per coutomers
def revenue_per_customer(total_revenue, total_customers):
    return total_revenue / total_customers

## the function calculates the customer churn rate as a % perc
def customer_churn_rate(lost_customers, total_customers):
    return (lost_customers / total_customers) * 100

## avg order  function calculating the avrg order value
def average_order_value(total_revenue, number_of_orders):
    return total_revenue / number_of_orders

## Assigning the SID digits to variables for more understanding
first_two_digits = 75
last_two_digits = 64

## Calling each function with the student ID digits
margin = operating_profit_margin(first_two_digits, last_two_digits)
rev_per_cust = revenue_per_customer(first_two_digits, last_two_digits)
churn = customer_churn_rate(first_two_digits, last_two_digits)
aov = average_order_value(first_two_digits, last_two_digits)

## Printing the results for these
print("Operating Profit Margin:", margin, "%")
print("Revenue per Customer:", rev_per_cust)
print("Customer Churn Rate:", churn, "%")
print("Average Order Value:", aov)
## OUTPUT - Operating Profit Margin: 117.1875 %
##Revenue per Customer: 1.171875
##Customer Churn Rate: 117.1875 %
##Average Order Value: 1.171875
### EXPlANATION of the code - Four basic functions are defined, each of which computes a crucial business metric (average order value, churn rate, revenue per customer, and profit margin).

## As example inputs, we use the SID's first two (75) and last two (64) digits.

##Each function that carries out common financial calculations (such as (profit / revenue) * 100) receives these values.

## To see how those metrics appear when applied to our SID-based sample data, we print each result.
##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here
## Creating a simple linear regression model to relate Price(X) to Demand(Y)
## Then, we'll figure out:
## 1) The price that maximizes revenue (price * demand),
## 2) The demand at a specific price (£52).

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Preparing the data
# ------------------------------------------------
# Prices and corresponding demands, aligned by index
prices = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]).reshape(-1, 1)
demands = np.array([300, 280, 260, 240, 210, 190, 160, 140, 120, 100,  85])

# Step 2: Creating and training the linear regression model
model = LinearRegression()
model.fit(prices, demands)

# Extract the slope (b) and intercept (a) from the trained model
a = model.intercept_
b = model.coef_[0]

## The linear model formula : Demand = a + b*Price

## Step 3: Find the price that maximizes revenue
# Revenue = Price * Demand = Price * (a + b*Price)
##           = a*Price + b*Price^2
##
# To find the maximum, we take derivative wrt Price and set it to 0:
# derivative(Revenue) = a + 2*b*Price = 0  =>  Price = -a / (2*b)
##We will calculate that and determine whether it falls within the practical range of 20 to 70.
optimal_price = -a / (2 * b)

# Step 4: Calculate the demand at Price = 52
# ------------------------------------------------
price_52 = 52
demand_at_52 = a + b * price_52

# Print the results
# ------------------------------------------------
print(f"Regression Model: Demand = {a:.2f} + ({b:.2f} * Price)")
print(f"1) Price that maximizes revenue: £{optimal_price:.2f}")

# If the optimal price is outside the data range, it's an estimate based on the linear model.
if optimal_price < 20 or optimal_price > 70:
    print("   (Note: This price is outside the collected price range of 20–70.)")

print(f"2) Demand at price £52: {demand_at_52:.2f} units")

OUTPUT - Regression Model: Demand = 391.23 + (-4.48 * Price)
1) Price that maximizes revenue: £43.65
2) Demand at price £52: 158.17 units
## explainationThe first thing we do is import matplotlib.pyplot as plt,
#  which is the main Python visualization tool. A simple line graph is produced by calling plt.plot(x_values, y_values) after defining our example data. 
# To maintain a clear and understandable visualization, we label each axis and give the graph a title. To ensure we can see the outcome of our plotting
#  instructions, we use plt.show() to display our chart in a separate window at the end.

##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# Generat 100 random numbers between 1 and student id number
# max-value = integer(input("Enter your Student ID: "))
# random_numbers = [random.randint(1, max_value) for i in range(0,100)]

# ## Plotting the numbers in a line chart
# plt.plot(random_numbers, marker='O', markercolor='green', markeredgcolor='red', linestyle='--', lable='Random Numbers', color='blue');
# plt.title(Line Chart of 100 Random Numbers)
# plt.xlabel="Index"
# plt.ylabel="Random Number"
# plt.legend('---')
# plt.grid(True)
# plt.show()
import random
import matplotlib.pyplot as plt

## Replace the input call with a direct assignment
max_value = 75001764  # Hardcode your Student ID

## Generating 100 random numbers
random_numbers = [random.randint(1, max_value) for _ in range(100)]

# Plot the random numbers as a line chart
plt.plot(
    random_numbers,
    marker='o',
    markerfacecolor='green',
    markeredgecolor='red',
    linestyle='--',
    label='Random Numbers',
    color='blue'
)

plt.title("Line Chart of 100 Random Numbers")
plt.xlabel("Index")
plt.ylabel("Random Number")
plt.legend()
plt.grid(True)
plt.show()

## not able to put the graph cause the vs code is not working properly and not even jupiter its taking time 
## showing the pending . ot will tske some time to show the output.



