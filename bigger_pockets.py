# Foursquare method:

def acceptInt(text):
    x = 0
    while True:
        try:
            x = int(input(text))
            break
        except ValueError:
            print('Invalid input, please enter a whole number value with no dollar sign...')
    return x

# income
# -rental income
# -laundry income
# -storage income
# -misc
# -total monthly income

def calcIncome():
    prop_type = input('What type of rental property is this? ')
    rental_income = acceptInt('How much income will you receive monthly by tenants paying rent for all units? ')
    laundry_income = acceptInt('Will there be any income from on-site laundry units? If no, please enter 0. ')
    storage_income = acceptInt('Will there be any income from on-site storage? If no, please enter 0. ')
    misc_income = acceptInt('Will there be any additional income from miscellanious sources? Please add up all other sources of income and input as a whole dollar amount. If no, please enter 0. ')
    total_income = rental_income + laundry_income + storage_income + misc_income
    print('Rental property type: ' + prop_type + '\n Total monthly income: $' + str(total_income))
    return total_income
    
# expenses
# -taxes
# -insurance
# -utilities
# --electric
# --water
# --sewer
# --garbage
# --gas
# -HOA fees
# -lawn/snow
# -vacancy
# -repairs
# -Capital Expenditures
# -Property Management
# -Mortgage

def calcExpenses():
    rental_taxes = acceptInt('How much will you pay monthly in taxes on the property? ')
    rental_insurance = acceptInt('How much will you pay monthly in insurance on the property? ')
    rental_utilities = acceptInt('Will there be any utilities to pay monthly? If no, please enter 0. ')
    rental_HOA = acceptInt('Will there be any HOA fees to pay monthly? If no, please enter 0. ')
    rental_landscaping = acceptInt('Will there be any landscaping, gardening or snow clearing fees to pay monthly? If no, please enter 0. ')
    rental_vacancy = acceptInt('How much will you set aside monthly for vacancy allowance? ')
    rental_repairs = acceptInt('How much will you set aside monthly for repairs? ')
    rental_CapEx = acceptInt('How much will you set aside monthly for Capital Expenditures? ')
    rental_mgmt = acceptInt('Will there be any Property Management fees to pay monthly? If no, please enter 0. ')
    rental_mortgage = acceptInt('How much will you pay monthly in mortgage on the property? ')
    rental_misc = acceptInt('Will there be any additional expenses from miscellanious sources? Please add up all other expenses and input as a whole dollar amount. If no, please enter 0. ')
    rental_total = rental_taxes + rental_insurance + rental_utilities + rental_HOA + rental_landscaping + rental_vacancy + rental_repairs + rental_CapEx + rental_mgmt + rental_mortgage + rental_misc
    print('Total expenses per month: $' + str(rental_total))
    return rental_total

# cash flow
# -income minus expenses

def calcCashFlow():
    cash_flow = calcIncome() - calcExpenses()
    print('Monthly cash flow: $' + str(cash_flow))
    return cash_flow

# cash on cash ROI (return on investment)
# -down payment
# -closing costs
# -rehab budget
# -misc other
# total investment:
# ------
# annual cash flow: monthly cash flow x 12
# annual cash flow / total investment (percentage)

def calcInvestment():
    down_payment = acceptInt('How much will you pay as a down payment? ')
    closing_costs = acceptInt('How much will you pay in closing costs? ')
    rehab_budget = acceptInt('How much is your rehab budget? ')
    misc_investment = acceptInt('Will there be any additional investment amounts from miscellanious sources? Please add up all other investment amounts and input as a whole dollar amount. If no, please enter 0. ')
    total_investment = down_payment + closing_costs + rehab_budget + misc_investment
    print('Total Investment: $' + str(total_investment))
    return total_investment

def calcAnnualCashFlow():
    monthly_cash_flow = calcCashFlow()
    annual_cash_flow = monthly_cash_flow * 12
    print('Annual cash flow: $' + str(monthly_cash_flow) + ' monthly * 12 = $' + str(annual_cash_flow))
    return annual_cash_flow

def calcROI():
    print('Welcome to your personal Cash on Cash ROI Calculator! \n Please enter each point of data for the following questions to receive your final ROI analysis. \n Please enter whole dollar amounts without any dollar symbol, digits only. ')
    annual_cash_flow = calcAnnualCashFlow()
    total_investment = calcInvestment()
    cash_on_cash_ROI = str(annual_cash_flow / total_investment) + '%'
    ROI_message = 'Your Cash on Cash ROI for this property:\nAnnual cash flow: $' + str(annual_cash_flow) + '\nTotal investment: $' + str(total_investment) + '\nAnnual cash flow divided by total investment: ' + cash_on_cash_ROI
    print('Calculating your ROI...')
    return ROI_message

print(calcROI())