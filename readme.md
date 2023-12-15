Expense Tracker

input:

weekly?
fortnightly?
monthly?



Income:
if monthly
- monthly primary income
- monthly supplementary income

if fortnightly
- fortnightly primary income
- fortnightly supplementary income

if weekly
- weekly primary income 
- weekly supplementary income



rent/mortgage costs:
are these costs mandatory?
if monthly
- monthly rent cost

if fortnightly 
- fortnightly rent cost

if weekly
- weekly rent cost 



utility costs:
are these costs mandatory?
if monthly/fortnightly/weekly
- electricity
- gas/hot water
- internet
- mobile plan



transport costs:
are these costs mandatory?
if monthly/weekly/fortnightly
- fuel
- parking
- tolls
- PT 
- uber



subscription costs:
are these costs mandatory?
if monthly/fortnightly/weekly
- video streaming
- music streaming
- gym membership
- other



food/grocery costs:
are these costs mandatory?
if monthly/weekly/fortnightly
- supermarket
- eating out
- take away/delivery



do you have a saving goal?
- y/n
- how much would you like to save per month/fortnight/week?



Your total "mothly/fortnightly/weekly" expense is _______ 

if your_income > 0 after expense
    you have ________ from your income remaining 

if your_income < 0 after expense
    "your expenses are _______ higher than your current income 

if saving_goal = yes
    if remaining_income >= saving_goal
        "you are currently meeting your goals for saving"
    else
        "you are currently below your saving goal by _______"




if remaining_income < saving_goal
    from non_mandatory_costs_list
        print(non_mandatory_cost_list)
            input("where would you like to cut costs?
                    1.
                    2.
                    3.")

            if input
                if cost >= saving_margin * 3
                    cost_adjustment = cost - saving_margin
                    "you will need to spend {cost_adjustment} less per {month/fortnight/week} on {cost} to meet your savings goal."
                elif cost > saving_margin and cost < saving_margin * 3
                    cost_adjustment = cost / 3
                    "It is only feesable for you to spend {cost_adjustment} less per {month/fortnigh/week}, perhaps try cutting costs elsewhere as well."



