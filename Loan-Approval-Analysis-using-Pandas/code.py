# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
# code starts here

bank =pd.read_csv(path)

categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)




# code ends here


# --------------
# code starts here

banks = bank.drop(columns='Loan_ID')

bank_mode = banks 



bank_mode =banks.mode().iloc[0]

banks.fillna(bank_mode, inplace=True)
print(banks.isnull().sum())

#code ends here


# --------------
# Code starts here




avg_loan_amount = pd.pivot_table(banks, index=['Gender','Married','Self_Employed'], values = 'LoanAmount',
aggfunc ='mean')

print(avg_loan_amount)




# code ends here



# --------------
# code starts here

# code for loan aprroved for self employed
loan_approved_se = banks.loc[(banks["Self_Employed"]=="Yes")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_se)

# code for loan approved for non self employed
loan_approved_nse = banks.loc[(banks["Self_Employed"]=="No")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_nse)

# percentage of loan approved for self employed
percentage_se = (loan_approved_se * 100 / 614)
percentage_se=percentage_se[0]
# print percentage of loan approved for self employed
print(percentage_se)

#percentage of loan for non self employed
percentage_nse = (loan_approved_nse * 100 / 614)
percentage_nse=percentage_nse[0]
#print percentage of loan for non self employed
print (percentage_nse)

# code ends here


# --------------
# code starts here
#Convert months to years

loan_term = banks["Loan_Amount_Term"].apply(lambda x : int(x) / 12)

#the number of applicants having loan amount term greater than or equal to 25 years

big_loan_term=len(loan_term[loan_term>=25])

print(big_loan_term)



# code ends here


# --------------
# code starts here

# Income/ Credit History vs Loan Amount

#Checking average income of an applicant and the average loan given to a person based on their income.

loan_groupby = banks.groupby('Loan_Status')

loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]

mean_values = loan_groupby.agg([np.mean])


# code ends here


