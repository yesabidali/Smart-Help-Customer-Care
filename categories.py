# Using functions so I can reuse my code
def catagory_name():
    categories = ["Banking", "University", "Telecom", "E-commerce","Car_Service"] # List to store data
    for i, category in enumerate(categories,1): # using for loop to avoide hard-coding and using enumerate for printing values with range
        print(i, category)
    print("6 Exit") 