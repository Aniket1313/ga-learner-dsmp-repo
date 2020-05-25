# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data =pd.read_csv(path)
loan_status=data['Loan_Status'].value_counts()

loan_status.plot(kind='bar',stacked=True,figsize=(10,5))
#Code starts here


# --------------
#Code starts here

property_and_loan = data.groupby(['Property_Area', 'Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar',stacked=False,figsize=(10,5))
plt.xlabel('Property Area',)
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()





# --------------
education_and_loan = data.groupby(['Education', 'Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked=True,figsize=(10,5))
plt.xlabel('Education Status',)
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()

#Code starts here


# --------------
#Let's check whether being graduate or not also leads to different loan amount distribution by plotting an overlapping density plot of two values

graduate= data[data['Education'] == 'Graduate']
not_graduate=data[data['Education'] == 'Not Graduate']


#data.groupby(['LoanAmount','graduate']).size().plot(kind='density',label='Graduate')

#plot.show()

#data.groupby(['LoanAmount','not_graduate']).size().plot(kind='density',label='Not Graduate')

#plt.show()

graduate['LoanAmount'].plot(kind='density', label='Graduate')
not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate')

plt.show()
plt.show()








#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig ,(ax_1,ax_2,ax_3)=plt.subplots(nrows = 3 , ncols = 1)


ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])

ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])

data['TotalIncome']=data['ApplicantIncome'] + data['CoapplicantIncome']

ax_3.scatter(data['TotalIncome'],data["LoanAmount"])


ax_1.set(title='Applicant Income')
ax_2.set(title='Coapplicant Income')
ax_3.set(title='Total Income')



