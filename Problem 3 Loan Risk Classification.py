# A bank classifies loan applicants based on credit score and annual income
credit_score = int(input("What is your credit score? "))
annual_income = float(input("What is your annual income? "))

# conditional statements determine what category of risk you fall into
if credit_score >= 720 and annual_income >= 60000:
    category = "Low Risk"

elif credit_score >= 650 and annual_income >= 40000:
    category = "Medium Risk"
else:
    category = "High Risk"

# Use squiggly brackets to print value of category not just 'category'
print(f'Loan Risk Category: {category}')
