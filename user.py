#!/usr/bin/env python
# coding: utf-8

# In[3]:


import admin as ad

class User:
    login_info = {}

    def __init__(self, name, phoneno, email, address, password):
        self.name = name
        self.number = phoneno
        self.email = email
        self.address = address
        self.password = password
        User.login_info[self.name] = self.password
        self.profile = {}
        self.order_history = {}

    
    def login(cls, username, password):
        if cls.login_info.get(username) == password:
            print("successfully logged in.....")
            return True
        else:
            print("SORRY!Wrong Credentials")
            return False

    def see_profile(self):
        self.profile[self.name] = {
            "Full Name": self.name,
            "Phone Number": self.number,
            "E-Mail": self.email,
            "Address": self.address,
            "Password": self.password
        }
        return self.profile

    def update_profile(self):
        x = input("What you want to update in your profile..")
        y = input("And changes to the new one: ")
        self.profile[x] = y
        print("Your Profile is Successfully Updated")
        return self.profile

    def place_order(self):
        print("What you want to order here is the menu")
        print(ad.show_menu())
        print("Enter the food ID to order to order the food")
        user_choice = int(input("If you want to order then select 1.YES 2.NO"))
        if user_choice == 1:
            foodid = int(input("Enter the food id here: "))
            quan = int(input("Enter the quantity of the food: "))
            x = ad.menu[foodid]["Price"] * quan
            again_ask = input("Are you still want to order this Enter YES or NO")
            if again_ask == "YES":
                print(f'''Your food name is {ad.menu[foodid]["Food Name"]}''')
                print(f'''Price of your food is {ad.menu[foodid]["Price"]}''')
                print(f"This is your quantity {quan}")
                print(f"It costs you {x}INR in total")
                print("You're all set for this order")
                self.order_history[foodid] = {
                    "Food Name": ad.menu[foodid]["Food Name"],
                    "Price": ad.menu[foodid]["Price"],
                    "Quantity": quan
                }
                final_stock = ad.menu[foodid]["Stock"] - quan
                ad.menu[foodid]["Stock"] = final_stock
                print("You're order is successfully placed")

            elif again_ask == "NO":
                print(" Order is cancelled!! You can look once more")
            else:
                print("Invalid choice")
        elif user_choice == 2:
            print("select 2 option so we cancelled this")
        else:
            print("Enter the invalid choice")

    def watch_profile(self):
        print(self.profile)

prajwal = User("prajwal J", "7406436618", "prajprajwal17@gmail.com", "mysore", "praj@1234")
ABC     = User("ABCD", "1234567891", "Abcd@gmail.com", "vijayanagar mysore", "abc12@14")
prajwal.see_profile()
ABC.see_profile()


# In[ ]:




