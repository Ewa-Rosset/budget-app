class Category:
    def __init__(self, name):
        self.name = name
        self.funds = 0
        self.ledger = []
        self.withdrawals = 0

    def check_funds(self, amount):
        if amount > self.funds:
            return False
        else:
            return True

    def deposit(self, amount, description=""):
        self.funds += amount
        return self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) is True:
            self.funds -= amount
            self.withdrawals += amount
            self.ledger.append({"amount": amount*(-1), "description": description})
            return True
        else:
            return False
            #print("not enough money to withdraw")
        
    def get_balance(self):
        #print(self.funds)
        return self.funds

    def transfer(self, amount, category_name):
            
            if self.withdraw(amount, "Transfer to " + category_name.name) is True:
                category_name.deposit(amount, "Transfer from " + self.name)
                return True
            else:
                return False

    def title_display(self):
        len_asterix_one_side = (30 - len(self.name))//2
        if (30 - len(self.name))%2 != 0:
            return "*"*(len_asterix_one_side + 1) + self.name + ("*"*len_asterix_one_side) 
        else:
           return "*"*len_asterix_one_side + self.name + "*"*len_asterix_one_side

    def ledger_items(self):

        ledger_list = []

        for addition in self.ledger:

            a_description = list(addition.values())[1]
            a_ammount = list(addition.values())[0]

            if len(a_description) >= 23:
                a_description = a_description[:23]
                amount_formatted = '{:.2f}'.format(float(a_ammount))
                right_aligned_amount = str(amount_formatted)[:8].rjust(30-(len(a_description[:25])))
    
                all_itmes = a_description + right_aligned_amount
                ledger_list.append(all_itmes)

                

            elif len(a_description) > 0:
                amount_formatted = '{:.2f}'.format(float(a_ammount))
                right_aligned_amount = str(amount_formatted)[:8].rjust(30-(len(a_description)))             
                all_itmes = a_description + right_aligned_amount
                ledger_list.append(all_itmes)
                

            else:
                amount_formatted = '{:.2f}'.format(float(a_ammount))
                right_aligned_amount = str(amount_formatted)[:8].rjust(30)
                all_itmes = a_description + right_aligned_amount
                ledger_list.append(all_itmes)

        return ledger_list

    def ledger_total(self):
        
        total_amount = self.get_balance()

        for addition in self.ledger:
            a_ammount = list(addition.values())[0]
            total_amount += int(a_ammount)
        
        return "Total: " + str('{:.2f}'.format(float(total_amount)))
        

    def ledger_display(self):
      
        title = self.title_display()    
        payments = self.ledger_items()  
        #totals = self.ledger_total()
        payments_str = '\n'.join(payments)

        

        return title + "\n" + payments_str + "\n" + "Total: " + str(self.funds)
        

    def __repr__(self):

        return self.ledger_display()



def vertical_names(categories):
    
    cat_names = []
    for category in categories:
        cat_names.append(category.name)

    maxs = 0
    for element in cat_names:
        if len(element) > maxs:
            maxs = len(element)

    index = 0
    numbered_strings_list = []
    while index < maxs:
        cat_line = "     "
        for element in cat_names:
            if len(element) <= index:
                cat_line += " " + "  "
            else:    
                cat_line += element[index] + "  "
        if index != maxs-1:
            cat_line += "\n"
        numbered_strings_list.append(cat_line)
        index += 1
        
    
    return numbered_strings_list
        
def category_spend_percent(categories):

    total = 0
    for category in categories:
        total += category.withdrawals
    total = round(total,2)
    
    perc_spend_list = []

    for category in categories:
        per_spend = round(category.withdrawals*100/total)
        perc_spend_list.append(per_spend)
        
    return perc_spend_list

def vertical_spend(perc_spend_list):

    percentage = 100
    numbered_spend_list = []

    while percentage >=0:

        if percentage == 100:
            line = str(percentage) + "|" + " "
        elif percentage < 100 and percentage > 0:
            line = " " + str(percentage) + "|" + " "
        else:
            line = "  " + str(percentage) + "|" + " "


        for element in perc_spend_list:
            if int(element) >= percentage:
                line += "o  "
            else:
                line += "   "

       
        line += "\n"
        numbered_spend_list.append(line)
        percentage -= 10

    return numbered_spend_list



def create_spend_chart(categories):
    first_line = "Percentage spent by category\n"
    numbers_lines = vertical_spend((category_spend_percent(categories)))
    straight_line = "    ----------\n"
    names_lines = vertical_names(categories)

    final_str = ""

    for element in first_line:
        final_str += element
    for element in numbers_lines:
        final_str += element
    final_str += straight_line


    for line in names_lines:
        final_str += line


    return final_str




food = Category("Food")
entertainment = Category("Entertainment")
general = Category("General")

food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
food.transfer(20, entertainment)

entertainment.deposit(50)
entertainment.withdraw(45.50)
general.deposit(130)
general.withdraw(80)

print(food)

names = [food, entertainment, general]

vertical_names(names)

category_spend_percent(names)



print(create_spend_chart(names))