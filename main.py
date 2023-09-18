# Imports
from argparse import ArgumentParser, Namespace
from rich import print
from datetime import *
from functions import *


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.

parser = ArgumentParser()
subparser = parser.add_subparsers(dest="command")
parser.usage = "Welcome to SuperPy! Choose your command to use this program."

# Change the date of today.
product_parser = subparser.add_parser("date_today", help="Use to change the date of today.")
product_parser.add_argument("new_date", type=str, help="Type here the date that you want the system believe its today. (format : yyyy-mm-dd).")

# Advance date.
product_parser = subparser.add_parser("advance_date", help="Use to advance the date of today.")
product_parser.add_argument("add_days", type=int, help="Type here the amount of days to forward or backward the date of today. (format : int).")

# Create and add new product to bought.csv
product_parser = subparser.add_parser("add_product", help="Use to add a product to bought.")
product_parser.add_argument("product_name", type=str, help="Type here the name of the product (format : string).")
product_parser.add_argument("product_amount", type=int, help="Type here the total amount of product in this purchase")
product_parser.add_argument("purchase_price", type=float, help="Type here the purchase price of the product (format : float).")
product_parser.add_argument("expiration_date", type=str, help="Type here the experiation date of the product (format : yyyy-mm-dd).")
product_parser.add_argument("-purchase_date", "-p", type=lambda d: datetime.strptime(d, '%Y-%m-%d').date(), help="Use -p and type here the purchase date of the product (format : yyyy-mm-dd).")

# Create and add new product to sell en remove from bought.csv
product_parser = subparser.add_parser("sell_product", help="Use to add a product to sell and remove from bought.")
product_parser.add_argument("product_name", type=str, help="Type here the name of the product (format : string).")
product_parser.add_argument("product_amount", type=int, help="Type here the total amount of product in this purchase")
product_parser.add_argument("selling_price", type=float, help="Type here the purchase price of the product (format : float).")
product_parser.add_argument("-selling_date", "-s", type=lambda d: datetime.strptime(d, '%Y-%m-%d').date(), help=" Use -s and type the purchase date of the product (format : yyyy-mm-dd).")

# Remove product from file based on product_id
product_parser = subparser.add_parser("remove_product", help="Use to remove a product from bought.csv or sold.csv.")
product_parser.add_argument("csv_file", type=str, help="Please select file where you want to delete from. Choose between bought and sold")
product_parser.add_argument("product_number", type=int, help="Type here the productnumber of the product (format : int).")

# Create report
report_parser = subparser.add_parser("report", help="Use to show a report from bought, sold, expired, current_stock or revenue.")
report_parser.add_argument("report_type", type=str, help="Use bought, sold, expired, current_stock to select the right report." )
report_parser.add_argument("--total", help="Choose --total to get the total product revenue list.", action="store_true" )
report_parser.add_argument("--yesterday", help="Select yesterday to see the revenue of yesterday.", action="store_true")
report_parser.add_argument("--today", help="Select today to see the revenue of today.", action="store_true")
report_parser.add_argument("--period", help="Select to see the revenue of that period.", action="store_true")



# Shorting name to args
args : Namespace = parser.parse_args()

def Superpy():

    # CHANGE DATE OF TODAY:
    if args.command == "date_today":
        outcome = dateToday(
                        new_date=args.new_date
                        )

    # ADVANCE DAY WITH AMOUNT OF DAYS:
    if args.command == "advance_date":
        outcome = advanceDate(
                add_days=args.add_days
                )

    # BUYING A PRODUCT:
    if args.command == "add_product":
        outcome = addNewProduct(
                        product_name=args.product_name, 
                        product_amount=args.product_amount, 
                        purchase_price=args.purchase_price, 
                        expiration_date=args.expiration_date,
                        purchase_date=args.purchase_date, 
                        )

    # SELLING A PRODUCT:
    if args.command == "sell_product":
        outcome = sellProduct(
                        product_name=args.product_name,  
                        product_amount=args.product_amount, 
                        selling_price=args.selling_price, 
                        selling_date=args.selling_date, 
                        )           

    # REMOVING A PRODUCT:        
    if args.command == "remove_product":
        outcome = removeProduct( 
                        csv_file=args.csv_file, 
                        product_number=args.product_number
                        )    

    # CREATING REPORTS:
    if args.command == "report":
        outcome = get_report( 
                        report_type=args.report_type,  
                        rev_total=args.total, 
                        rev_today=args.today, 
                        rev_yesterday=args.yesterday, 
                        rev_period=args.period
                        )
    print(f"{outcome}")
                    
    
def main():
    Superpy()       

if __name__ == "__main__":
    
    main()