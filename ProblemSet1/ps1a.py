


current_savings = 0;
r = 0.04
# end of each month, savings += savings*r/12
# portion saved comes from annual salary (10%)
# end of each month savings += annual_salary*portion/12

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))



number_of_months = 0;
# minus down payment
down_payment = 0.25 * total_cost;

while current_savings < down_payment :
    current_savings += (current_savings*0.04 /12);
    current_savings += annual_salary*portion_saved/12;
    number_of_months +=1;

print("Number of Months for a down payment: " + str(number_of_months))
    
    


#do the work

