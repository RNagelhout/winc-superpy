from datetime import datetime, timedelta
import csv
from datetime import *
from tabulate import tabulate
import pandas as pd
import numpy as np

# Import of the csv files with date columns and date format
df_bought = pd.read_csv ('./data/bought.csv', parse_dates=["purchase_date", "expiration_date"], date_format="%Y%m%d")
df_sold = pd.read_csv ('./data/sold.csv', parse_dates=["selling_date"], date_format="%Y%m%d")

# Different fieldnames for the overview
fieldnames = ["product_id","product_number","product_name","product_amount","purchase_date","purchase_price","expiration_date"]
fieldnames_sold = ["product_id","product_number","product_name","product_amount","purchase_price","selling_date", "selling_price"]
fieldnames_revenue = ["product_id","product_number","product_name","product_amount","purchase_price","selling_date", "selling_price", "Total_product_revenue"]

# CHANGING DATE TODAY
def dateToday(new_date):
    try:
        datetime.strptime(new_date, "%Y-%m-%d")
        with open("./data/date.txt", "w") as today:
            today.write(new_date)
            today.close()
        return (f"Changed the date of today to {new_date}.")
    except ValueError:
        return "Incorrect data format, should be YYYY-MM-DD."

# BUYING A PRODUCT:
# Function for adding a product to bought.csv. It will increase the amount when the product exist or 
# if the product does not exist, it will create a new row.
def addNewProduct(product_number, product_name,  product_amount, purchase_date, purchase_price, expiration_date):
    max_id = df_bought['product_id'].max()
    try:
        datetime.strptime(purchase_date, "%Y-%m-%d")
        datetime.strptime(expiration_date, "%Y-%m-%d")
        with open('./data/bought.csv', 'a', newline='') as bought_file:
            if product_number in df_bought.values:
                csv_reader = pd.read_csv ('./data/bought.csv')
                get_amount = csv_reader[csv_reader["product_number"] == product_number].product_amount
                new_amount = get_amount + product_amount
                get_index = csv_reader[csv_reader["product_number"] == product_number].index.values
                csv_reader.loc[get_index, 'product_amount'] = new_amount
                csv_reader.to_csv("./data/bought.csv", index=False)
                outcome = (f"You've added {product_amount} {product_name} to bought.csv.")
            else:
                csv_writer = csv.DictWriter(bought_file, fieldnames=fieldnames)
                new_transaction = {'product_number': product_number}
                new_transaction['product_id'] = max_id+1
                new_transaction['product_name'] = product_name
                new_transaction['product_amount'] = product_amount
                new_transaction['purchase_date'] = purchase_date
                new_transaction['purchase_price'] = purchase_price
                new_transaction['expiration_date'] = expiration_date
                csv_writer.writerow(new_transaction)
                bought_file.close  
                outcome = (f"You've added {product_amount} {product_name} to bought.csv.")
            return outcome
    except ValueError:
        return "Incorrect data format for purchase_date or expiration_date, should be YYYY-MM-DD."   
    
# SELLING A PRODUCT:
# Function for selling a product. It will add the product and amount to sold.csv. 
# It will increase the amount when the product exist or if the product does not exist, it will create a new row. and reduce the amount in bought.csv.
def sellProduct(product_number, product_amount, selling_date, selling_price):
    try:
        datetime.strptime(selling_date, "%Y-%m-%d")
        max_id = df_sold['product_id'].max()
        if product_number in df_bought.values:
            csv_reader = pd.read_csv ('./data/bought.csv')
            get_index = csv_reader[csv_reader["product_number"] == product_number].index.values
            get_product_name = csv_reader[csv_reader["product_number"] == product_number].product_name
            get_amount = csv_reader.loc[csv_reader["product_number"] == product_number].product_amount.values
            if get_amount < product_amount:
                print("The amount is higher then the current stock, please check your input.")
            elif get_amount == product_amount:
                get_index = csv_reader[csv_reader["product_number"] == product_number].index.values
                new_amount = get_amount - product_amount     
                csv_reader.loc[get_index, 'product_amount'] = new_amount
                csv_reader.to_csv("./data/bought.csv", index=False)
                with open('./data/sold.csv', 'a', newline='') as sold_file:
                    if product_number in df_sold.values:
                        csv_reader = pd.read_csv ('./data/sold.csv')
                        get_amount = csv_reader[csv_reader["product_number"] == product_number].product_amount
                        new_amount = get_amount + product_amount
                        get_index = csv_reader[csv_reader["product_number"] == product_number].index.values
                        csv_reader.loc[get_index, 'product_amount'] = new_amount
                        csv_reader.to_csv("./data/sold.csv", index=False)
                    else:    
                        csv_writer = csv.DictWriter(sold_file, fieldnames=fieldnames_sold)
                        new_transaction = {'product_number': product_number}
                        new_transaction['product_id'] = max_id+1
                        new_transaction['product_name'] = get_product_name.values[0]
                        new_transaction['product_amount'] = product_amount
                        new_transaction['selling_date'] = selling_date
                        new_transaction['selling_price'] = selling_price
                        csv_writer.writerow(new_transaction)
                        sold_file.close  
                outcome = (f"You've added {product_amount} {get_product_name.values[0]} to sold.csv")
            else:
                csv_reader = pd.read_csv ('./data/bought.csv')
                get_amount = csv_reader[csv_reader["product_number"] == product_number].product_amount
                new_amount = get_amount - product_amount
                get_index = csv_reader[csv_reader["product_number"] == product_number].index.values
                csv_reader.loc[get_index, 'product_amount'] = new_amount
                csv_reader.to_csv("./data/bought.csv", index=False)
                with open('./data/sold.csv', 'a', newline='') as sold_file:
                    if product_number in df_sold.values:
                        csv_reader = pd.read_csv ('./data/sold.csv')
                        get_amount = csv_reader[csv_reader["product_number"] == product_number].product_amount
                        new_amount = get_amount + product_amount
                        get_index = csv_reader[csv_reader["product_number"] == product_number].index.values
                        csv_reader.loc[get_index, 'product_amount'] = new_amount
                        csv_reader.to_csv("./data/sold.csv", index=False)
                        outcome = (f"You've added {get_amount} {get_product_name.values[0]} to sold.csv.")
                    else:    
                        csv_writer = csv.DictWriter(sold_file, fieldnames=fieldnames_sold)
                        new_transaction = {'product_number': product_number}
                        new_transaction['product_id'] = max_id+1
                        new_transaction['product_name'] = get_product_name.values[0]
                        new_transaction['product_amount'] = product_amount
                        new_transaction['selling_date'] = selling_date
                        new_transaction['selling_price'] = selling_price
                        csv_writer.writerow(new_transaction)
                        sold_file.close  
                outcome = (f"You've added {product_amount} {get_product_name.values[0]} to sold.csv")  
            return outcome
    except ValueError:
        return "Incorrect data format for selling_date, should be YYYY-MM-DD."

# REMOVING A PRODUCT:
# Function for removing an product from a selected csv.file 
def removeProduct(csv_file, product_number):
    df_sold = pd.read_csv ('./data/sold.csv', parse_dates=["selling_date"], date_format="%Y%m%d")
    df_bought = pd.read_csv ('./data/bought.csv', parse_dates=["purchase_date", "expiration_date"], date_format="%Y%m%d")
    if csv_file == "bought":
        if product_number in df_bought.values:
            get_index = df_bought[df_bought['product_number'] == product_number].index.values[0]
            df_bought.drop(get_index, inplace=True)
            df_bought.to_csv('./data/bought.csv', index=False)
            outcome = (f"Product deleted {product_number} from bought.csv!")
        else:
            outcome = print("The productnumber does not exist in bought.csv, please check your input!")    
    elif csv_file == "sold":
        if product_number in df_sold.values:
            get_index = df_sold[df_sold['product_number'] == product_number].index.values[0]
            df_sold.drop(get_index, inplace=True)
            df_sold.to_csv('./data/sold.csv', index=False)
            outcome =  (f"Product deleted {product_number} from sold.csv!")
        else:
            outcome = "The productnumber does not exist in sold.csv, please check your input!"
    else: 
        outcome = "The selected file does not exist. Please choose between bought en sold."
    return outcome
 

# CREATING REPORTS:
# Function for creating different reports:
#  bought, sold, current_stock, expired, revenue( --total, --today, --yesterday, --month )
def get_report(report_type, rev_total, rev_today, rev_yesterday, rev_period ):
    open_date= open("./data/date.txt", "r")
    today = open_date.read()
    print("")
    print(f"Date of today: {today}")
    today_object = datetime.strptime(today,"%Y-%m-%d")
    df_sold = pd.read_csv ('./data/sold.csv', parse_dates=["selling_date"], date_format="%Y%m%d")
    outcome = "No report type is selected or report_type does not exist, please select type bought, sold, expired"
    if report_type == "bought":
        print("Description: Overview of all the products we bought:")
        print("")
        get_all = df_bought[df_bought["purchase_date"] <= today]
        outcome = (tabulate(get_all, headers = fieldnames, showindex=False, tablefmt = "fancy_grid")) 
    if report_type == "sold":
        print("Description: Overview of all the products we sold:")
        print("")
        df_sold = df_sold[df_sold["selling_date"] <= today]
        outcome = (tabulate(df_sold, headers = fieldnames_sold, showindex=False, tablefmt = "fancy_grid")) 
    if report_type == "current_stock":
        print("Description: Overview of all the products in our stock. Exclusive expired products:")
        print("")
        get_stock = df_bought[df_bought["expiration_date"] <= today]
        outcome = (tabulate(get_stock, headers = fieldnames, showindex=False, tablefmt = "fancy_grid"))
    if report_type == "expired":
        print("Description: Overview of all the expired products:")
        print("")
        get_all = df_bought[df_bought["expiration_date"] < today]
        outcome = (tabulate(get_all, headers = fieldnames, showindex=False, tablefmt = "fancy_grid")) 
    if report_type == "revenue":
        if rev_total:
            print("Description: Overview of the total revenue:")
            print("")
            df_sold = df_sold[df_sold["selling_date"] <= today]
            df_sold["Total_product_revenue"] = df_sold["product_amount"] * (df_sold["selling_price"] - df_sold["purchase_price"])
            df_sold.loc["Total_revenue"] = pd.Series(df_sold["Total_product_revenue"].sum(axis=0), index=["Total_product_revenue"])
            outcome = (tabulate(df_sold.replace(np.nan, None), headers = fieldnames_revenue, showindex=False, tablefmt = "fancy_grid"))
        if rev_today:
            print("Description: Overview of the todays revenue:")
            print("")
            df_sold = df_sold[df_sold["selling_date"] == today]
            df_sold["Total_product_revenue"] = df_sold["product_amount"] * (df_sold["selling_price"] - df_sold["purchase_price"])
            df_sold.loc["Total_revenue"] = pd.Series(df_sold["Total_product_revenue"].sum(axis=0), index=["Total_product_revenue"])
            outcome = (tabulate(df_sold.replace(np.nan, None), headers = fieldnames_revenue, showindex=False, tablefmt = "fancy_grid"))
        if rev_yesterday:  
            yesterday = (today_object - timedelta(days = 1)).strftime("%Y-%m-%d")
            print(f"Description: Overview of the revenue from yesterday {yesterday}:")
            print("")
            df_sold = df_sold[df_sold["selling_date"] == yesterday]
            df_sold["Total_product_revenue"] = df_sold["product_amount"] * (df_sold["selling_price"] - df_sold["purchase_price"])
            df_sold.loc["Total_revenue"] = pd.Series(df_sold["Total_product_revenue"].sum(axis=0), index=["Total_product_revenue"])
            outcome = (tabulate(df_sold.replace(np.nan, None), headers = fieldnames_revenue, showindex=False, tablefmt = "fancy_grid"))
        if rev_period:
            start_date = input("Type here the start date of the period.(format : yyyy-mm-dd) : ")
            end_date = input("Type here the end date of the period.(format : yyyy-mm-dd) : ")
            try:
                datetime.strptime(start_date, "%Y-%m-%d")
                datetime.strptime(end_date, "%Y-%m-%d")  
                print(f"Description: Overview of the revenue from {start_date} till {end_date} :")
                print("")
                df_sold = df_sold[(df_sold["selling_date"] > start_date) & (df_sold["selling_date"] < end_date) == True]
                df_sold["Total_product_revenue"] = df_sold["product_amount"] * (df_sold["selling_price"] - df_sold["purchase_price"])
                df_sold.loc["Total_revenue"] = pd.Series(df_sold["Total_product_revenue"].sum(axis=0), index=["Total_product_revenue"])
                outcome = (tabulate(df_sold.replace(np.nan, None), headers = fieldnames_revenue, showindex=False, tablefmt = "fancy_grid"))
            except ValueError:
                return "Incorrect data format for start date or end date, should be YYYY-MM-DD."    
    return outcome