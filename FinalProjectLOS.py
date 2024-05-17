# COP4710 Final Project - Great Home Loans LOS
# Authors - Vraj Patel, Daishak Patel, Harshit Suri
# Description - This application is the Great Home Loans
#               lender's loan origination software. The
#               application allows officers, processors,
#               underwriters, and closers to work on
#               borrowers's mortgages efficiently all united
#               by one database on which this app is built.
import os, time, shutil, copy, random, datetime, art, time
import psycopg2
from psycopg2 import Error
from MortgageCalculator import MortgageCalculator

# establish a postgres object connection
def connect():
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            user= 'vrajp1',         # replace with your username
            password= 'Vrajulal1@',   #replace with your password
            host="localhost",
            port="5432",
            database="los"
        )
        #print("Connection to database successful")
        return connection

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL Database", error)
        return None

# establish a connection object with limited priveleges for the home screen stats
def limited_connect():
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            user= 'los_home_screen',         # replace with your username
            password= 'homeScreen12#',   #replace with your password
            host="localhost",
            port="5432",
            database="los"
        )
        #print("Connection to database successful")
        return connection

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL Database", error)
        return None
    
def disconnect(db):
    db.close()

def waitForKeyPress(width,message=""):
    printCentered(message,width,fill="=")
    print("Press enter to continue ... ",end="")
    input()

# retrieves last month value
def get_last_month_and_year():
    # Get the current date
    current_date = datetime.datetime.now()

    # Calculate the last month and last year
    if current_date.month == 1:
        last_month = 12
        last_year = current_date.year - 1
    else:
        last_month = current_date.month - 1
        last_year = current_date.year

    return last_year, last_month

# given a width, prints a text centered within it
def printCentered(text, width=90,fill=" ",endChar='\n'):
    print(text.center(width,fill),end=endChar)
    
# clears the console 
def clearConsole():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
        
# returns the console's width
def getConsoleWidth():
    if os.name == 'posix':
        try:
            columns, _ = os.get_terminal_size(0)
            return columns - 1
        except OSError:
            return None
    else:
        try:
            columns, _ = shutil.get_terminal_size()
            return columns - 1
        except OSError:
            return None
        
# Helper function to print current date and time
def print_date_time():
    print("     DATE:-", datetime.date.today().strftime("%A, %d %B %Y"))
    print("     TIME:-", datetime.datetime.now().strftime("%H:%M:%S"))


def welcome_screen(width):
    d = datetime.date.today()
    t = datetime.datetime.now()
    print("\n\n     DATE:-", d.strftime("%A, %d %B %Y"))
    print("\n     TIME:-", t.strftime("%H:%M:%S"))
    art.tprint("  -Great Home Loans-")
    print("-"*width)
    print()
    printCentered("WELCOME TO THE GREAT HOME LOANS LOS",width)
    printCentered("Your Premier Mortgage Solution for Seamless Home Financing!",width)
    print()
    print("-"*width)
    
  


def user_profile_screen(los,user_id,width):
    print_date_time()
    printCentered(" USER PROFILE ",width,"=")
    print("\n")
    printCentered(f"Profile Details for User: {user_id}")
    # Fetch and display user profile details
    # Logic to retrieve and display the profile based on user_id

# print menues
def print_menu(menu_num,width):
    if menu_num == 1:
        printCentered("Choose what you wish to do:",width)
        print()
        print("1.) Search my loans by borrower's last name")
        print("2.) View all loans in my pipeline")
        print("3.) List all my loans (all time)")
        print("4.) Create a new loan")
        print("5.) Mortgage Calculator")
        print("6.) Logout")
    elif menu_num == 2:
        printCentered("Choose what you wish to do:",width)
        print()
        print("1.) Search my loans")
        print("2.) View all loans in my pipeline")
        print("3.) List all my loans (all time)")
        print("4.) Mortgage Calculator")
        print("5.) Logout")
    elif menu_num == 3:
        print("\nChoose which screen you wish to view for this file:")
        print("->1.) Loan Summary\n->2.) Qualification\n->3.) Conditions\n->4.) Exit Loan File\n")
    elif menu_num == 4:
        print("\nChoose which action you wish to take:")
        print("->1.) Update basic loan details\n->2.) Disclose Loan Estimate\n->3.) Submit file to processing\n->4.) Go back\n")
    elif menu_num == 5:
        print("\nChoose which action you wish to take:")
        print("->1.) Update basic loan details\n->2.) Go back\n")
    elif menu_num == 6:
        print("\nChoose which action you wish to take:")
        print("->1.) Go back\n")
    elif menu_num == 7:
        print("\nChoose which action you wish to take:")
        print("->1.) Upload an unsatisfied condition\n->2.) Go back\n")
    elif menu_num == 8:
        print("\nChoose which action you wish to take:")
        print("->1.) Clear an unsatisfied condition\n->2.) Add a condition\n->3.) Go back\n")
    elif menu_num == 9:
        print("\nChoose which action you wish to take:")
        print("->1.) Send out the Closing Disclosure\n->2.) Go back\n")
    elif menu_num == 10:
        print()
        printCentered("+ + + + + + + + + + + + + + + + + +",width)
        printCentered("+                                 +",width)
        printCentered("+        1-  LOAN SUMMARY         +",width)
        printCentered("+                                 +",width)
        printCentered("+ + + + + + + + + + + + + + + + + +",width)
        printCentered("+                                 +",width)
        printCentered("+        2- QUALIFICATION         +",width)
        printCentered("+                                 +",width)
        printCentered("+ + + + + + + + + + + + + + + + + +",width)
        printCentered("+                                 +",width)
        printCentered("+        3-  CONDITIONS           +",width)
        printCentered("+                                 +",width)
        printCentered("+ + + + + + + + + + + + + + + + + +",width)
        printCentered("+                                 +",width)
        printCentered("+             4- EXIT             +",width)
        printCentered("+                                 +",width)
        printCentered("+ + + + + + + + + + + + + + + + + +",width)
        
    return

def get_users(los, loan_id):
    cursor = los.cursor()
    query_24 = "SELECT U.fname, U.lname, U.nmls FROM Users U JOIN Loans L ON U.nmls = L.officer WHERE L.id = %s;"
    cursor.execute(query_24,(loan_id,))
    officer = cursor.fetchone()
    query_24 = "SELECT U.fname, U.lname, U.nmls FROM Users U JOIN Loans L ON U.nmls = L.processor WHERE L.id = %s;"
    cursor.execute(query_24,(loan_id,))
    processor = cursor.fetchone()
    query_24 = "SELECT U.fname, U.lname, U.nmls FROM Users U JOIN Loans L ON U.nmls = L.underwriter WHERE L.id = %s;"
    cursor.execute(query_24,(loan_id,))
    underwriter = cursor.fetchone()
    query_24 = "SELECT U.fname, U.lname, U.nmls FROM Users U JOIN Loans L ON U.nmls = L.closer WHERE L.id = %s;"
    cursor.execute(query_24,(loan_id,))
    closer = cursor.fetchone()
    return officer, processor, underwriter, closer

# Function to view and manage loans
def open_loan(los, width, user_id, user_type, loan_id, status, borrower_last_name, borrower_first_name):
    cursor = los.cursor()
    while True:
        query_get_status = "SELECT status FROM Loans WHERE id = %s";
        cursor.execute(query_get_status, (loan_id,))
        status = cursor.fetchone()[0]
        clearConsole()
        printCentered(" Great Home Loans ",width,"=")
        print()
        printCentered(f" Loan ID: {loan_id} | Primary Borrower {borrower_last_name}, {borrower_first_name} | Status: {status} ",width,"=")
        print("")
        officer, processor, underwriter, closer = get_users(los, loan_id)
        printCentered(" Loan File Users ",width,"=")
        print(f"{'Loan Officer:':<16} {officer[0]} {officer[1]}, NMLS# {officer[2]}")
        print(f"{'Processor:':<16} {processor[0]} {processor[1]}, NMLS# {processor[2]}")
        print(f"{'Underwriter:':<16} {underwriter[0]} {underwriter[1]}, NMLS# {underwriter[2]}")
        print(f"{'Closer:':<16} {closer[0]} {closer[1]}, NMLS# {closer[2]}")
        print("="*width)
        print_menu(10,width)
        print_menu(3,width)
        try:
            choice = int(input("Enter your choice: "))
            if choice < 1 or choice > 4:
                raise ValueError
        except:
            print("Invalid input. Enter a number between 1 and 4")

        if choice == 1:
            loan_summary(los, width, user_id, user_type, loan_id)
        elif choice == 2:
            qualification(los, width, user_id,user_type,loan_id)
        elif choice == 3:
            conditions(los, width, user_id, user_type, loan_id)
        elif choice == 4:
            display_user_profile(los, width, user_id)
            break

get_month = {1:'January',
             2:'February',
             3:'March',
             4:'April',
             5:'May',
             6:'June',
             7:'July',
             8:'August',
             9:'September',
             10:'October',
             11:'November',
             12:'December'}

def home_screen(width):
    limited = limited_connect()
    cursor = limited.cursor()
    printCentered(" GREAT HOME LOANS ",width,"=")
    print()
    year, month = get_last_month_and_year()
    query_22 = "SELECT SUM(volume) FROM Stats;"
    cursor.execute(query_22)
    total_funded = cursor.fetchone()[0]
    print()
    printCentered(f"Since 2021, Great Home Loans has funded ${total_funded:,.2f} in home loans!\n",width)
    query_23 = "SELECT * FROM Stats ORDER BY volume DESC LIMIT 1;"
    cursor.execute(query_23)
    lo_of_the_month = cursor.fetchone()
    printCentered(f"Congratulations to our Loan Officer of the Month for {get_month[lo_of_the_month[5]]}, {round(lo_of_the_month[4])}",width)
    print()
    printCentered(f"{lo_of_the_month[1]} {lo_of_the_month[2]}\n",width)
    printCentered(f"{lo_of_the_month[1]}'s volume was $ {lo_of_the_month[3]:,.2f}!",width)
    printCentered(f"Keep up the good work!",width)
    
    print("\n")
    printCentered("+ + + + + + + + + + + + + + + + + +",width)
    printCentered("+                                 +",width)
    printCentered("+        1-  USER LOGIN           +",width)
    printCentered("+                                 +",width)
    printCentered("+ + + + + + + + + + + + + + + + + +",width)
    printCentered("+                                 +",width)
    printCentered("+       2-  CREATE ACCOUNT        +",width)
    printCentered("+                                 +",width)
    printCentered("+ + + + + + + + + + + + + + + + + +",width)
    printCentered("+                                 +",width)
    printCentered("+             3- EXIT             +",width)
    printCentered("+                                 +",width)
    printCentered("+ + + + + + + + + + + + + + + + + +",width)
    
    cursor.close()
    limited.close()

def exit_now(width):
    print()
    printCentered("========================================================",width)
    print()
    printCentered("+ + + + + + + + + + + + + + + + + +",width)
    printCentered("+                                 +",width)
    printCentered("+           THANK YOU             +",width)
    printCentered("+                                 +",width)
    printCentered("+ + + + + + + + + + + + + + + + + +",width)
    print()
    printCentered("========================================================",width)
    print()
    printCentered("Thanks for using the Great Home Loans LOS",width)

def assign_processor(los):
    cursor = los.cursor()
    get_processors_query = "SELECT nmls FROM Users WHERE type = 'Processor';"
    cursor.execute(get_processors_query)
    processors = cursor.fetchall()
    cursor.close()
    return random.choice(processors)[0]

def assign_underwriter(los):
    cursor = los.cursor()
    get_underwriters_query = "SELECT nmls FROM Users WHERE type = 'Underwriter';"
    cursor.execute(get_underwriters_query)
    underwriters = cursor.fetchall()
    cursor.close()
    return random.choice(underwriters)[0]

def assign_closer(los):
    cursor = los.cursor()
    get_closers_query = "SELECT nmls FROM Users WHERE type = 'Closer';"
    cursor.execute(get_closers_query)
    closers = cursor.fetchall()
    cursor.close()
    return random.choice(closers)[0]


def create_loan(los, width, user_id):
    printCentered(" Great Home Loans ",width,"=")
    print()
    printCentered("Creating New Loan",width)
    print()
    
    # Create a cursor object
    cursor = los.cursor()
    
    # Get the Loan Officer's details
    query_get_officer = "SELECT fname, lname, email, phone FROM Users WHERE nmls = %s"
    cursor.execute(query_get_officer, (user_id,))
    officer_details = cursor.fetchone()

    # Get the borrower's details
    borrower_fname = input("Enter the borrower's first name: ").capitalize()
    borrower_lname = input("Enter the borrower's last name: ").capitalize()
    borrower_email = input("Enter the borrower's email: ").lower()
    if '@' not in borrower_email:
        print("Must be a valid email. Left blank for now.")
        borrower_email = None
    borrower_phone = input("Enter the borrower's phone number: ")
    if not borrower_phone.isdigit() or len(borrower_phone) != 10:
        borrower_phone = print("Invalid. Must be exactly 10 digits. Left blank for now.")
        borrower_phone = '8888888888'
    try:
        borrower_credit_score = int(input("Enter the borrower's credit score: "))
        if borrower_credit_score < 500 or borrower_credit_score > 850:
            raise ValueError
    except:
        borrower_credit_score = None
        print("Must enter an integer between 500 and 850. Left blank for now.")
    try:
        borrower_income = int(input("Enter the borrower's monthly income: "))
        if borrower_income < 0:
            raise ValueError
    except:
        borrower_income = None
        print("Must enter a value greater than zero. Left blank for now.")
    
    # Insert the borrower into the Borrowers table
    query_max_Id = "SELECT MAX(id) FROM Borrowers;"
    cursor.execute(query_max_Id)
    borrower_id = cursor.fetchone()[0]+1
    query_insert_borrower = "INSERT INTO Borrowers (id, fname, lname, email, credit, phone, income) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(query_insert_borrower, (borrower_id, borrower_fname, borrower_lname, borrower_email, borrower_credit_score, borrower_phone, borrower_income))


    # Get the co-borrower's details (if applicable)
    coborrower_exists = input("\nIs there a co-borrower? (y/n): ").lower()
    while coborrower_exists not in ['y','n']:
        coborrower_exists = input("Enter 'y' or 'n': ").lower()
    coborrower_id = None
    if coborrower_exists == 'y':
        coborrower_fname = input("\nEnter the co-borrower's first name: ").capitalize()
        coborrower_lname = input("Enter the co-borrower's last name: ").capitalize()
        coborrower_email = input("Enter the co-borrower's email: ").lower()
        if '@' not in coborrower_email:
            print("Must be a valid email. Left blank for now.")
            coborrower_email = None
        coborrower_phone = input("Enter the co-borrower's phone number: ")
        if not coborrower_phone.isdigit() or len(phone) != 10:
            coborrower_phone = print("Must be exactly 10 digits. Left blank for now.")
            coborrower_phone = '8888888888'
        try:
            coborrower_credit_score = int(input("Enter the co-borrower's credit score: "))
            if coborrower_credit_score < 500 or coborrower_credit_score > 850:
                raise ValueError
        except:
            print("Must enter an integer between 500 and 850. Left blank for now.")
            coborrower_credit_score = None
        try:
            coborrower_income = int(input("Enter the co-borrower's monthly income: "))
            if coborrower_income < 0:
                raise ValueError
        except:
            print("Must enter a value greater than zero. Left blank for now.")
            coborrower_income = None
        
        
        # Insert the co-borrower into the Borrowers table
        query_max_Id = "SELECT MAX(id) FROM Borrowers;"
        cursor.execute(query_max_Id)
        coborrower_id = cursor.fetchone()[0]+1
        query_insert_coborrower = "INSERT INTO Borrowers (id, fname, lname, email, credit, phone, income) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(query_insert_coborrower, (coborrower_id, coborrower_fname, coborrower_lname, coborrower_email, coborrower_credit_score, coborrower_phone, coborrower_income))


    # Get the property details
    property_address = input("\nEnter the property address: ")
    property_city = input("Enter the property city: ")
    property_state = input("Enter the property state: ")
    property_zip = input("Enter the property zip code: ")
    try:
        property_value = int(input("Enter the property's value: "))
        if property_value <= 0:
            raise ValueError
    except:
        print("Must be a number greater than 0. Left blank for now.")
        property_value = 0
    try:
        property_taxes = int(input("Enter the property taxes (annual): "))
        if property_taxes <= 0:
            raise ValueError
    except:
        print("Must be a number greater than 0. Left blank for now.")
        property_taxes = 0
    try:
        property_insurance = int(input("Enter the property insurance (annual): "))
        if property_insurance <= 0:
            raise ValueError
    except:
        print("Must be a number greater than 0. Left blank for now.")
        property_insurance = 0
    try:
        property_hoa = int(input("Enter the monthly Homeowner Association HOA fees (0 if none): "))
        if property_hoa <= 0:
            raise ValueError
    except:
        print("Must be a number greater than or equal to 0. Left blank for now.")
        property_hoa = 0
        
    # Insert the property into the Properties table
    query_max_Id = "SELECT MAX(id) FROM Properties;"
    cursor.execute(query_max_Id)
    property_id = cursor.fetchone()[0]+1
    query_insert_property = "INSERT INTO Properties (id, value, street, state, city, zip, taxes, hoi, hoa) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(query_insert_property, (property_id, property_value, property_address, property_state, property_city, property_zip, property_taxes, property_insurance, property_hoa))
    #property_id = cursor.fetchone()[0]

    # Get the loan details
    loan_type = input("Enter the loan type (Purchase or Refinance) Enter 'P' or 'R': ").capitalize()
    while loan_type not in ['P','R']:
        loan_type = input("Invalid. Enter 'P' or 'R': ").capitalize()
    loan_type = 'Purchase' if loan_type == 'P' else 'Refinance'
    while True:
        try:
            loan_amount = int(input("Enter the loan amount: "))
            if loan_amount < 0:
                raise ValueError
            break
        except:
            print('Enter a valid loan amount: ')
            continue
    while True:
        try:
            loan_rate = float(input("Enter the rate: "))
            if loan_rate < 0:
                raise ValueError
            break
        except:
            print('Enter a valid rate: ')
            continue
    while True:
        try:
            loan_term = int(input("Enter the loan term in number of years: "))*12
            if loan_term < 0:
                raise ValueError
            break
        except:
            print('Enter a valid loan term: ')
            continue
    
    # assign processor, underwriter, and closer for the loan
    processor = assign_processor(los)
    underwriter = assign_underwriter(los)
    closer = assign_closer(los)

    # Insert the loan into the Loans table
    query_max_Id = "SELECT MAX(id) FROM Loans;"
    cursor.execute(query_max_Id)
    loan_id = cursor.fetchone()[0]+1
    query_insert_loan = "INSERT INTO Loans (id, borrower, coborrower, officer, processor, underwriter, closer, status, type, loanEstimateSent, closingDisclosureSent, property, loanAmount, rate, term) VALUES (%s, %s, %s, %s, %s, %s, %s, 'Application', %s, FALSE, FALSE, %s, %s, %s, %s);"
    cursor.execute(query_insert_loan, (loan_id, borrower_id, coborrower_id, user_id, processor, underwriter, closer, loan_type, property_id, loan_amount, loan_rate, loan_term))

    # enter the basic conditions always needed
    # find the max condition ID
    query_max_ID = "SELECT MAX(id) FROM Conditions;"
    cursor.execute(query_max_ID)
    condition_id = cursor.fetchone()[0] + 1
    query_23 = "INSERT INTO Conditions VALUES (%s, %s, 'Tax Returns Form 1040', %s);"
    cursor.execute(query_23,(condition_id,loan_id,False))
    condition_id += 1
    query_23 = "INSERT INTO Conditions VALUES (%s, %s, 'Prior Year W2', %s);"
    cursor.execute(query_23,(condition_id,loan_id,False))
    condition_id += 1
    query_23 = "INSERT INTO Conditions VALUES (%s, %s, 'Photo ID', %s);"
    cursor.execute(query_23,(condition_id,loan_id,False))
    condition_id += 1
    query_23 = "INSERT INTO Conditions VALUES (%s, %s, 'Paystubs', %s);"
    cursor.execute(query_23,(condition_id,loan_id,False))

    # Commit the changes and close the cursor
    los.commit()
    cursor.close()

    print(f"\nNew loan with ID {loan_id} has been created successfully for borrower {borrower_fname}, {borrower_lname}!")
    waitForKeyPress(width)

def update_details(los, width, user_id, user_type, loan_id):
    printCentered(" Great Home Loans ",width,"=")
    print()
    printCentered(f"Updating Loan Details for Loan {loan_id}",width)
    print()
    
    cursor = los.cursor()

    # Fetch the loan details from the database
    query_6 = "SELECT * FROM Loans WHERE id = %s;"
    cursor.execute(query_6, (loan_id,))
    loan_info = cursor.fetchone()

    # Fetch the borrower details from the database
    query_7 = "SELECT * FROM Borrowers WHERE id = %s;"
    cursor.execute(query_7, (loan_info[1],))
    borrower_info = cursor.fetchone()

    # Fetch the coborrower details from the database (if applicable)
    coborrower_info = None
    if loan_info[2]:
        cursor.execute(query_7, (loan_info[2],))
        coborrower_info = cursor.fetchone()

    # Fetch the property details from the database
    query_8 = "SELECT * FROM Properties WHERE id = %s;"
    cursor.execute(query_8, (loan_info[11],))
    property_info = cursor.fetchone()

    print("Update Loan Details")
    print("===================")

    print("\nLoan Details:")
    print("-------------")
    print(f"Loan Status: {loan_info[7]}")
    print(f"Officer: {loan_info[3]}")
    print(f"Processor: {loan_info[4]}")
    print(f"Underwriter: {loan_info[5]}")
    print(f"Closer: {loan_info[6]}")
    print(f"Loan Estimate Sent: {loan_info[15]}")
    print(f"Closing Disclosure Sent: {loan_info[16]}")
    print(f"Loan Amount: {loan_info[12]}")
    print(f"Rate: {loan_info[13]} %")
    print(f"Term: {loan_info[14]//12} years")

    print("\nBorrower Details:")
    print("-----------------")
    print(f"First Name: {borrower_info[1]}")
    print(f"Last Name: {borrower_info[2]}")
    print(f"Email: {borrower_info[3]}")
    print(f"Credit Score: {borrower_info[4]}")
    print(f"Phone: {borrower_info[5]}")
    print(f"Income: ${borrower_info[5]}")

    if coborrower_info:
        print("\nCoborrower Details:")
        print("-------------------")
        print(f"First Name: {coborrower_info[1]}")
        print(f"Last Name: {coborrower_info[2]}")
        print(f"Email: {coborrower_info[3]}")
        print(f"Credit Score: {coborrower_info[4]}")
        print(f"Phone: {coborrower_info[5]}")
        print(f"Income: ${coborrower_info[5]}")

    print("\nProperty Details:")
    print("-----------------")
    print(f"Property Value: ${property_info[1]}")
    print(f"Address: {property_info[2]}")
    print(f"City: {property_info[4]}")
    print(f"State: {property_info[3]}")
    print(f"Zip Code: {property_info[5]}")
    print(f"Taxes: ${property_info[6]} per year")
    print(f"Insurance: ${property_info[7]} per year")
    print(f"HOA: ${property_info[8]} per month")

    # Ask user for updated information
    confirmation = input("\nDo you want to update any details? (y/n): ").lower()
    print("\nPress enter for any input to keep that detail unchanged.")
    if confirmation.lower() == "y":
        print("\nUpdate Loan Details:")
        try:
            loan_amount = float(input(f"Loan Amount (${loan_info[12]}): "))
        except:
            loan_amount = ""
        if loan_amount == "":
            loan_amount = loan_info[12]

        try:    
            rate = float(input(f"Rate ({loan_info[13]}%): "))
        except:
            rate = ""
        if rate == "":
            rate = loan_info[13]

        try:   
            term = int(input(f"Term in years ({loan_info[14]//12}): "))*12
        except:
            term = ""
        if term == "":
            term = loan_info[14]

        try: 
            credit = int(input(f"Borrower Credit Score ({borrower_info[4]}): ")) 
        except:
            credit = "" 
        if credit == "": 
            credit = borrower_info[4]
         
        try: 
            income = int(input(f"Borrower Monthly Income (${borrower_info[6]}): "))
        except:
            income = ""
        if income == "": 
            income = borrower_info[6] 
        
        # Update the database here
        query_26 = """
            UPDATE Loans 
            SET loanAmount = %s, rate = %s, term = %s 
            WHERE id = %s;
        """
        cursor.execute(query_26, (loan_amount, rate, term, loan_id))

        query_26 = "UPDATE Borrowers SET credit = %s, income = %s WHERE id = %s;"
        cursor.execute(query_26, (credit, income, borrower_info[0]))

        query_26 = "UPDATE LE_Info SET credit = %s, income = %s WHERE id = %s;"
        cursor.execute(query_26, (credit, income, loan_id))
        
        los.commit()
        print("\nLoan details updated successfully!")
    else:
        print("\nNo updates were made.")
    

    cursor.close()
    
# the three main menues
def loan_summary(los, width, user_id, user_type, loan_id):
    clearConsole()
    printCentered(" Great Home Loans ",width,"=")
    print()
    cursor = los.cursor()
    query_6 = "SELECT * FROM Loans WHERE id = %s;"
    cursor.execute(query_6,(loan_id,))
    loan_info = cursor.fetchone()
    query_7 = "SELECT * FROM Borrowers WHERE id = %s;"
    cursor.execute(query_7,(loan_info[1],))
    borrower_info = cursor.fetchone()
    coborrower_info = None
    if loan_info[2]:
        cursor.execute(query_7,(loan_info[2],))
        coborrower_info = cursor.fetchone()
    query_8 = "SELECT * FROM Properties WHERE id = %s;"
    cursor.execute(query_8,(loan_info[11],))
    property_info = cursor.fetchone()

    # Display Loan Summary Data Neatly
    loan_status = loan_info[7]
    printCentered(f"{loan_info[8]} (Status: {loan_status})",width)
    print()
    if not loan_info[15]:
        printCentered("Inital LE has not been disclosed yet.",width)
        printCentered("TRID Compliance Laws require LE disclosure within 3 business days of the application!",width)
    print()
    print(f"{'Primary Borrower:':<24} {borrower_info[1]} {borrower_info[2]}")
    print(f"--> {'Email:':<20} {borrower_info[3]}")
    print(f"--> {'Phone:':<20} {print_phone(borrower_info[5])}")
    print(f"--> {'Credit Score:':<20} {borrower_info[4]}")
    print()
    if loan_info[2]:
        print(f"{'Coborrower:':<24} {coborrower_info[1]} {coborrower_info[2]}")
        print(f"--> {'Email:':<20} {coborrower_info[3]}")
        print(f"--> {'Phone:':<20} {print_phone(coborrower_info[5])}")
        print(f"--> {'Credit Score:':<20} {coborrower_info[4]}")
    print()
    print("Subject Property:")
    print(f"--> {'Address:':<20} {property_info[2]}, {property_info[4]}, {property_info[3]} {property_info[5]}")
    if loan_info[8] == 'Purchase:':
        print(f"--> {'Purchase Price:':<20} $ {property_info[1]}")
    else:
        print(f"--> {'Property Value:':<20} $ {property_info[1]}")
    print()
    print("Loan Terms:")
    print(f"--> {'Loan Amount:':<20} $ {loan_info[12]}")
    print(f"--> {'Loan to Value:':<20} {round(loan_info[12]*100/property_info[1],2)} %")
    print(f"--> {'Note Rate:':<20} {loan_info[13]} %")
    print(f"--> {'Term:':<20} {loan_info[14]//12} years")
    monthly_payment = round((loan_info[12])*(((loan_info[13]/1200)*(1+(loan_info[13]/1200))**loan_info[14])/(((1+(loan_info[13]/1200))**loan_info[14])-1)),2)
    print(f"--> {'Monthly PI Payment:':<20} $ {monthly_payment}")
    print('\n'+"="*width)
    print()
    

    # Allow operations on this screen depending on user type and loan details
    if user_type == 'Loan Officer' and loan_status == 'Application':
        while True:
            print_menu(4,width)
            try:
                choice = int(input("Enter your choice: "))
                if choice < 1 or choice > 4:
                    raise ValueError
            except:
                print("Invalid input. Enter a number between 1 and 4")
                continue

            if choice == 1:
                #tkinter module
                clearConsole()
                update_details(los, width, user_id, user_type, loan_id)
            elif choice == 2:
                LESent = loan_info[15]
                if LESent:
                    print("You have already sent a Loan Estimate to this borrower.")
                    sendLE = input("Do you wish to send a revised Loan Estimate to the Borrower at this time? ").lower()
                    while sendLE not in ['yes','no']:
                        sendLE = input("Invalid input. Enter 'yes' or 'no': ").lower()
                else:
                    sendLE = input("Do you wish to send the initial Loan Estimate to the Borrower at this time? ").lower()
                    while sendLE not in ['yes','no']:
                        sendLE = input("Invalid input. Enter 'yes' or 'no': ").lower()
                if sendLE == 'yes':
                    # clear the Loan Officer's alert box
                    query_21 = "UPDATE Users SET alerts = '' WHERE nmls = %s;"
                    cursor.execute(query_21,(user_id,))
                    query_13 = "UPDATE Loans SET loanestimatesent = true WHERE id = %s;"
                    cursor.execute(query_13,(loan_id,))
                    los.commit()
                    print(f"\nLoan Estimate Successfully Sent to Borrowers on {datetime.date.today().strftime('%A, %d %B %Y')} at {datetime.datetime.now().strftime('%H:%M:%S')}\n")
                    waitForKeyPress(width)
                    break
            elif choice == 3:
                LESent = loan_info[15]
                if not LESent:
                    print("You must first send the LE before submitting to processing!")
                    continue
                print("\nWARNING: This loan will become read only for you once it is moved to processing.")
                submit = input("Do you wish to submit the file to processing at this time? ").lower()
                while submit not in ['yes','no']:
                    submit = input("Invalid input. Enter 'yes' or 'no': ").lower()
                if submit == 'yes':
                    query_14 = "UPDATE Loans SET status = 'Processing' WHERE id = %s;"
                    cursor.execute(query_14,(loan_id,))
                    los.commit()
                    print(f"\nLoan File Successfully Moved to Processing on {datetime.date.today().strftime('%A, %d %B %Y')} at {datetime.datetime.now().strftime('%H:%M:%S')}\n")
                    waitForKeyPress(width)
                    break
            elif choice == 4:
                break
    elif user_type == 'Processor' and loan_status == 'Processing':
        while True:
            print_menu(5,width)
            try:
                choice = int(input("Enter your choice: "))
                if choice < 1 or choice > 2:
                    raise ValueError
            except:
                print("Invalid input. Enter a number between 1 and 2")
                continue

            if choice == 1:
                pass
                #tkinter module
                update_details(los, width, user_id, user_type, loan_id)
            elif choice == 2:
                break
    else:
        while True:
            print_menu(6,width)
            try:
                choice = int(input("Enter your choice: "))
                if choice < 1 or choice > 1:
                    raise ValueError
            except:
                print("Invalid input. You have only view permissions for this screen. Enter 1 to go back.")
                continue
            if choice == 1:
                break
            
    cursor.close()
    

def qualification(los, width, user_id, user_type, loan_id):
    cursor = los.cursor()
    query_6 = "SELECT * FROM Loans WHERE id = %s;"
    cursor.execute(query_6,(loan_id,))
    loan_info = cursor.fetchone()
    loan_status = loan_info[7]
    query_7 = "SELECT * FROM Borrowers WHERE id = %s;"
    cursor.execute(query_7,(loan_info[1],))
    borrower_info = cursor.fetchone()
    coborrower_info = None
    if loan_info[2]:
        cursor.execute(query_7,(loan_info[2],))
        coborrower_info = cursor.fetchone()
    query_8 = "SELECT * FROM Properties WHERE id = %s;"
    cursor.execute(query_8,(loan_info[11],))
    property_info = cursor.fetchone()
    query_11 = "SELECT * FROM Liabilities WHERE loan = %s;"
    cursor.execute(query_11,(loan_id,))
    liabilities_info = cursor.fetchall()

    
    # Display Qualification Data Neatly
    loan_status = loan_info[7]
    clearConsole()
    printCentered(" Great Home Loans ",width,"=")
    printCentered(f"{loan_info[8]} (Status: {loan_status})",width)
    print()
    print(f"{'Primary Borrower:':<25} {borrower_info[1]} {borrower_info[2]}")
    print(f"--> {'Monthly Income:':<21} $  {borrower_info[6]}")
    print()
    if loan_info[2]:
        print(f"{'Coborrower:':<25} {coborrower_info[1]} {coborrower_info[2]}")
        print(f"--> {'Monthly Income:':<21} $  {coborrower_info[6]}")
    print()
    if coborrower_info:
        total_income = borrower_info[6] + coborrower_info[6]
    else:
        total_income = borrower_info[6]
    print(f"{'Total Monthly Income:':>24}  $ {total_income}")
    print()
    print("Subject Property Monthly Liabilities:")
    print(f"--> {'Address:':<20} {property_info[2]}, {property_info[4]}, {property_info[3]} {property_info[5]}")
    monthly_payment = round((loan_info[12])*(((loan_info[13]/1200)*(1+(loan_info[13]/1200))**loan_info[14])/(((1+(loan_info[13]/1200))**loan_info[14])-1)),2)
    print(f"--> {'Monthly PI Payment:':<20} $ {monthly_payment}")
    print(f"--> {'Property Taxes:':<20} $ {round(property_info[6]/12,2)}")
    print(f"--> {'Homeowner Insurance:':<20} $ {round(property_info[7]/12,2)}")
    print(f"--> {'HOA:':<20} $ {property_info[8]}")
    total_liabilities = round(float(monthly_payment) + (property_info[6]/12) + (property_info[7]/12) + property_info[8],2)
    front_end_liabilities = total_liabilities
    print()
    print(f"{'Total PITIA:':>24} $ {total_liabilities}")
    print()
    print("Other monthly liabilities")
    for count, liability in enumerate(liabilities_info,1):
        omitted = 'Yes' if liability[6] else 'No'
        print(f"-->{str(count)+'.)':<4} Creditor: {liability[2]:<27}")
        print(f"          Type: {liability[3]:<25} Bal: ${liability[4]:>6} Amount: ${liability[5]:>5} Omitted: {omitted:>3}")
        
        if omitted == 'Yes':
            total_liabilities += round(liability[5],2)
    print()
    print(f"{'Total Liabilities:':>25} $ {round(total_liabilities,2)}")
    print()
    print(f"{'Front End Debt to Income (DTI) Ratio:':<40} {round(front_end_liabilities*100/total_income,2)} %")
    print(f"{'Back  End Debt to Income (DTI) Ratio:':<40} {round(total_liabilities*100/total_income,2)} %")

    if round(total_liabilities*100/total_income,2) > 45:
        print("\nWARNING: DTI Ratio is above 45 % which is likely to lead to a loan denial from AUS.")
    print('\n'+"="*width)
    print()

    # Allow operations on this screen depending on user type and loan details
    if user_type == 'Loan Officer' and loan_status == 'Application':
        while True:
            print_menu(5,width)
            try:
                choice = int(input("Enter your choice: "))
                if choice < 1 or choice > 2:
                    raise ValueError
            except:
                print("Invalid input. Enter a number between 1 and 2")
                continue

            if choice == 1:
                clearConsole()
                #tkinter module
                update_details(los, width, user_id, user_type, loan_id)
            elif choice == 2:
                break
    elif user_type == 'Processor' and loan_status == 'Processing':
        while True:
            print_menu(5,width)
            try:
                choice = int(input("Enter your choice: "))
                if choice < 1 or choice > 2:
                    raise ValueError
            except:
                print("Invalid input. Enter a number between 1 and 2")
                continue

            if choice == 1:
                clearConsole()
                #tkinter module
                update_details(los, width, user_id, user_type, loan_id)
            elif choice == 2:
                break
    else:
        while True:
            print_menu(6,width)
            try:
                choice = int(input("Enter your choice: "))
                if choice < 1 or choice > 1:
                    raise ValueError
            except:
                print("Invalid input. You have only view permissions for this screen. Enter 1 to go back.")
                continue
            if choice == 1:
                break

    cursor.close()

def conditions(los, width, user_id, user_type, loan_id):
    cursor = los.cursor()
    query_15 = "SELECT EXISTS(SELECT * FROM Conditions WHERE loan = %s AND satisfied = FALSE);"
    cursor.execute(query_15,(loan_id,))
    unsatisfied = cursor.fetchall()[0]
    query_6 = "SELECT * FROM Loans WHERE id = %s;"
    cursor.execute(query_6,(loan_id,))
    loan_info = cursor.fetchone()
    query_10 = "SELECT * FROM Conditions WHERE loan = %s AND satisfied = TRUE;"
    cursor.execute(query_10,(loan_id,))
    conditions_info_satisfied = cursor.fetchall()
    query_10 = "SELECT * FROM Conditions WHERE loan = %s AND satisfied = FALSE;"
    cursor.execute(query_10,(loan_id,))
    conditions_info_unsatisfied = cursor.fetchall()
    print()
    
    loan_status = loan_info[7]
    clearConsole()
    printCentered(" Great Home Loans ",width,"=")
    printCentered(f"{loan_info[8]} (Status: {loan_status})",width)
    print()
    print("Satisfied Conditions:")
    for count, condition in enumerate(conditions_info_satisfied,1):
        print(f"-->{str(count)+'.)':<4} Description: {condition[2]}")
    print()
    print("Unsatisfied Conditions:")
    for count, condition in enumerate(conditions_info_unsatisfied,1):
        print(f"-->{str(count)+'.)':<4} Description: {condition[2]}")
    print('\n'+"="*width)
    print()

    

    # Allow operations on this screen depending on user type and loan details
    if user_type == 'Processor' and loan_status == 'Processing':
        while True:
            print_menu(7,width)
            try:
                choice = int(input("Enter your choice: "))
                if choice < 1 or choice > 2:
                    raise ValueError
            except:
                print("Invalid input. Enter a number between 1 and 2")
                continue
            
            if choice == 1:
                if not unsatisfied:
                    print("All conditions have been satisfied. This loan is now in the Clear to Close Status.")
                    query_16 = "UPDATE Loans SET status = 'Clear to Close' WHERE id = %s;"
                    cursor.execute(query_16,(loan_id,))
                    los.commit()
                else:
                    while True:
                        try:
                            condition_choice = int(input("Select the number of the unsatisfied condition you wish to upload: "))
                            if condition_choice < 0 or condition_choice > len(conditions_info_unsatisfied):
                                raise ValueError
                        except:
                            print(f"Invalid input. Enter number between 1 and {len(conditions_info_unsatisfied)}. Enter 0 to go back.")
                            continue
                        if condition_choice == 0:
                            break
                        alert = conditions_info_unsatisfied[condition_choice-1][2] + ' submitted for loan id ' + str(loan_id)
                        query_17 = "UPDATE Users SET alerts = %s WHERE nmls = %s"
                        cursor.execute(query_17,(alert,loan_info[5]))
                        los.commit()
                        print(f"Condition {conditions_info_unsatisfied[condition_choice-1][2]} was successfully uploaded on")
                        print(f"{datetime.date.today().strftime('%A, %d %B %Y')} at {datetime.datetime.now().strftime('%H:%M:%S')}")
                        waitForKeyPress(width)
                        exit_flag = True
                        break
                if exit_flag == True:
                    break
            elif choice == 2:
                break
    elif user_type == 'Underwriter' and loan_status == 'Processing':
        while True:
            print_menu(8,width)
            try:
                choice = int(input("Enter your choice: "))
                if choice < 1 or choice > 3:
                    raise ValueError
            except:
                print("Invalid input. Enter a number between 1 and 3")
                continue
            if choice == 1:
                if not unsatisfied:
                    print("All conditions have been satisfied. This loan is now in the Clear to Close Status")
                    query_16 = "UPDATE Loans SET status = 'Clear to Close' WHERE id = %s;"
                    cursor.execute(query_16,(loan_id,))
                    los.commit()
                else:
                    exit_flag = False
                    while True:
                        try:
                            condition_choice = int(input("Select the number of the unsatisfied condition you wish to clear: "))
                            if condition_choice < 0 or condition_choice > len(conditions_info_unsatisfied):
                                raise ValueError
                        except:
                            print(f"Invalid input. Enter number between 1 and {len(conditions_info_unsatisfied)}. Enter 0 to go back.")
                            continue
                        if condition_choice == 0:
                            break
                        if len(conditions_info_unsatisfied) == 1:
                            print("\nWARNING: This is the last unsatisfied condition. Proceeding will move the file into CTC status.")
                            confirm = input("Do you wish to continue? ").lower()
                            while confirm not in ['yes','no']:
                                confirm = input("Invalid input. Enter 'yes' or 'no': ")
                            if confirm == 'no':
                                break
                            else:
                                query_18 = "UPDATE Loans SET status = 'Clear to Close' WHERE id = %s"
                                cursor.execute(query_18,(loan_id,))
                                los.commit()
                        query_17 = "UPDATE Conditions SET satisfied = TRUE WHERE id = %s"
                        cursor.execute(query_17,(conditions_info_unsatisfied[condition_choice-1][0],))
                        los.commit()
                        print(f"\nCondition {conditions_info_unsatisfied[condition_choice-1][2]} was successfully cleared on")
                        print(f"{datetime.date.today().strftime('%A, %d %B %Y')} at {datetime.datetime.now().strftime('%H:%M:%S')}")
                        waitForKeyPress(width)
                        exit_flag = True
                        break
                if exit_flag:
                    break
            elif choice == 2:
                descr = input("Enter description of the condition: ")
                # find the max condition ID
                query_22 = "SELECT MAX(id) FROM Conditions;"
                cursor.execute(query_22)
                condition_id = cursor.fetchone()[0] + 1
                query_23 = "INSERT INTO Conditions VALUES (%s, %s, %s, %s);"
                cursor.execute(query_23,(condition_id,loan_id,descr,False))
                los.commit()
            elif choice == 3:
                break
    elif user_type == 'Closer' and loan_status == 'Clear to Close':
        while True:
            print_menu(9,width)
            try:
                choice = int(input("Enter your choice: "))
                if choice < 1 or choice > 2:
                    raise ValueError
            except:
                print("Invalid input. Enter a number between 1 and 2")
                continue

            if choice == 1:
                CDSent = loan_info[16]
                if CDSent:
                    print("You have already sent a Closing Disclosure to this borrower.")
                    sendCD = input("Do you wish to send a revised CD to the Borrower at this time? ").lower()
                    while sendCD not in ['yes','no']:
                        sendCD = input("Invalid input. Enter 'yes' or 'no': ").lower()
                else:
                    sendCD = input("Do you wish to send the Initial Closing Disclosure to the Borrower at this time? ").lower()
                    while sendCD not in ['yes','no']:
                        sendCD = input("Invalid input. Enter 'yes' or 'no': ").lower()
                if sendCD == 'yes':   
                    query_19 = "UPDATE Loans SET closingdisclosuresent = true WHERE id = %s;"
                    cursor.execute(query_19,(loan_id,))
                    los.commit()
                    print(f"\nClosing Disclosure Successfully Sent to Borrowers on {datetime.date.today().strftime('%A, %d %B %Y')} at {datetime.datetime.now().strftime('%H:%M:%S')}\n")
                    waitForKeyPress(width)
                    break
            elif choice == 2:
                break
    else:
        while True:
            print_menu(6,width)
            try:
                choice = int(input("Enter your choice: "))
                if choice < 1 or choice > 1:
                    raise ValueError
            except:
                print("Invalid input. You have only view permissions for this screen. Enter 1 to go back.")
                continue
            if choice == 1:
                break

    cursor.close()


def search_loans(los, width, user_id, user_type, borrower_name="%", current = True):
    cursor = los.cursor()
    
    # Construct the SQL query based on the user type and preference for all time or just current loans
    if user_type.lower() == "loan officer" and current:
        query_9 = "SELECT L.id, B.lname, B.fname, L.status FROM Loans L JOIN Borrowers B ON L.borrower = B.id WHERE L.officer = %s AND B.lname LIKE %s AND L.status = 'Application';"
    elif user_type.lower() == "loan officer":
        query_9 = "SELECT L.id, B.lname, B.fname, L.status FROM Loans L JOIN Borrowers B ON L.borrower = B.id WHERE L.officer = %s AND B.lname LIKE %s;"
    elif user_type.lower() == "processor" and current:
        query_9 = "SELECT L.id, B.lname, B.fname, L.status FROM Loans L JOIN Borrowers B ON L.borrower = B.id WHERE L.processor = %s AND B.lname LIKE %s AND L.status = 'Processing';"
    elif user_type.lower() == "processor":
        query_9 = "SELECT L.id, B.lname, B.fname, L.status FROM Loans L JOIN Borrowers B ON L.borrower = B.id WHERE L.processor = %s AND B.lname LIKE %s;"
    elif user_type.lower() == "underwriter" and current:
        query_9 = "SELECT L.id, B.lname, B.fname, L.status FROM Loans L JOIN Borrowers B ON L.borrower = B.id WHERE L.underwriter = %s AND B.lname LIKE %s AND L.status = 'Processing';"
    elif user_type.lower() == "underwriter":
        query_9 = "SELECT L.id, B.lname, B.fname, L.status FROM Loans L JOIN Borrowers B ON L.borrower = B.id WHERE L.underwriter = %s AND B.lname LIKE %s;"
    elif user_type.lower() == "closer" and current:
        query_9 = "SELECT L.id, B.lname, B.fname, L.status FROM Loans L JOIN Borrowers B ON L.borrower = B.id WHERE L.closer = %s AND B.lname LIKE %s AND L.status = 'Clear to Close';"
    else:
        query_9 = "SELECT L.id, B.lname, B.fname, L.status FROM Loans L JOIN Borrowers B ON L.borrower = B.id WHERE L.closer = %s AND B.lname LIKE %s;"

    cursor.execute(query_9, (user_id,borrower_name))
    loans = cursor.fetchall()
    
    if len(loans) == 0 and current:
        print("No loans found for the current user in the pipeline.")
        cursor.close()
        return
    elif len(loans) == 0:
        print("You have no history of originating loans with Great Home Loans.")
        cursor.close()
        return
    
    # Display the loans
    num_loans = len(loans)
    print("\nLoans:")
    count = 1
    for loan in loans:
        loan_id, last_name, first_name, status = loan
        print(f"{count}.) Loan ID: {loan_id} ({status}): {last_name}, {first_name}")
        count += 1
    print()
    
    # Prompt the user to select a loan
    exit_flag = False
    while True:
        try:
            loan_choice = int(input("Enter the loan # to open loan file or '0' to quit: "))
            if loan_choice < 0 or loan_choice > num_loans:
                raise ValueError
            if loan_choice == 0:
                exit_flag = True
            break
        except:
            print(f"Invalid input. Enter a number between 0 and {num_loans}")
            continue

    if not exit_flag:
        clearConsole()
        printCentered(" Great Home Loans ",width,"=")
        print()
        loan_id = loans[loan_choice-1][0]
        status = loans[loan_choice-1][3]
        borrower_last_name = loans[loan_choice-1][1]
        borrower_first_name = loans[loan_choice-1][2]
        cursor.close()
        open_loan(los, width, user_id, user_type, loan_id, status, borrower_last_name, borrower_first_name)

def display_user_profile(los, width, user_id):
    # logic to verify the username and password
    # Execute a SQL query to check the credentials
    cursor = los.cursor()
    query_1 = "SELECT * FROM users WHERE nmls = %s"
    cursor.execute(query_1, (user_id,))
    
    # Fetch the user's information
    user_info = cursor.fetchone()
    clearConsole()
    user_id, first_name, last_name, email, phone, alerts, user_type  = user_info[0:7]
    user_type = user_type.strip()
    printCentered(f" Welcome {first_name} {last_name}! ",width,"=")
    print()
    if user_type.lower() == 'underwriter':
        printCentered(f"You are logged on as an {user_type}",width)
    else:
        printCentered(f"You are logged on as a {user_type}",width)
        
    if alerts:
        print()
        print("You have the following alerts:")
        print(f"{alerts}")

    print()
    printCentered(" Account Info ",width,"=")
    print()
    print(f"{'NmlsID#':<35}", user_id)
    print(f"{'First Name:':<35}", first_name)
    print(f"{'Last Name:':<35}", last_name)
    print(f"{'Email:':<35}", email)
    print(f"{'Phone Number:':<35}",print_phone(phone))
    if user_type == "Loan Officer":    
        query_2 = "SELECT COUNT(*) FROM Users U JOIN Loans L ON U.NMLS = L.officer WHERE U.NMLS = %s AND L.status = 'Application'"
    elif user_type == "Processor":
        query_2 = "SELECT COUNT(*) FROM Users U JOIN Loans L ON U.NMLS = L.processor WHERE U.NMLS = %s AND L.status = 'Processing'"
    elif user_type == "Underwriter":
        query_2 = "SELECT COUNT(*) FROM Users U JOIN Loans L ON U.NMLS = L.underwriter WHERE U.NMLS = %s AND L.status = 'Processing'"
    else:
        query_2 = "SELECT COUNT(*) FROM Users U JOIN Loans L ON U.NMLS = L.closer WHERE U.NMLS = %s AND L.status = 'Clear to Close'"
    cursor.execute(query_2, (user_id,))
    num_loans = cursor.fetchone()[0]
    print(f"{'Number of Loans Requiring Work:':<35}",num_loans)
    print()
    print("="*width)
    print("")
    
    
def login(los,width):
    clearConsole()
    printCentered("Great Home Loans LOS",width,"=")
    printCentered("Introducing Great Home Loans LOS!",width)
    printCentered("Your Premier Mortgage Solution for Seamless Home Financing!",width)

    cursor = los.cursor()

    attempts = 0
    exit_flag = False
    while attempts < 3:
        
        if exit_flag == True:
            break
        
        username = input("\nEnter your username: ").lower()
        if username == 'q':
            break
        password = input("Enter your password: ")
        

        
        # logic to verify the username and password
        # Execute a SQL query to check the credentials
        query_1 = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query_1, (username, password))
        
        # Fetch the user's information
        user_info = cursor.fetchone()
        
        if user_info:
            clearConsole()
            print("Login Successful!")  # Message indicates a successful login
            user_id, first_name, last_name, email, phone, alerts, user_type  = user_info[0:7]
            user_type = user_type.strip()
            printCentered(f" Welcome {first_name} {last_name}! ",width,"=")
            print()
            if user_type.lower() == 'underwriter':
                printCentered(f"You are logged on as an {user_type}",width)
            else:
                printCentered(f"You are logged on as a {user_type}",width)
                
            if alerts:
                print()
                print("You have the following alerts:")
                print(f"{alerts}")

            print()
            printCentered(" Account Info ",width,"=")
            print()
            print(f"{'NmlsID#':<35}", user_id)
            print(f"{'First Name:':<35}", first_name)
            print(f"{'Last Name:':<35}", last_name)
            print(f"{'Email:':<35}", email)
            print(f"{'Phone Number:':<35}",print_phone(phone))
            if user_type == "Loan Officer":    
                query_2 = "SELECT COUNT(*) FROM Users U JOIN Loans L ON U.NMLS = L.officer WHERE U.NMLS = %s AND L.status = 'Application'"
            elif user_type == "Processor":
                query_2 = "SELECT COUNT(*) FROM Users U JOIN Loans L ON U.NMLS = L.processor WHERE U.NMLS = %s AND L.status = 'Processing'"
            elif user_type == "Underwriter":
                query_2 = "SELECT COUNT(*) FROM Users U JOIN Loans L ON U.NMLS = L.underwriter WHERE U.NMLS = %s AND L.status = 'Processing'"
            else:
                query_2 = "SELECT COUNT(*) FROM Users U JOIN Loans L ON U.NMLS = L.closer WHERE U.NMLS = %s AND L.status = 'Clear to Close'"
            cursor.execute(query_2, (user_id,))
            num_loans = cursor.fetchone()[0]
            print(f"{'Number of Loans Requiring Work:':<35}",num_loans)
            print()
            print("="*width)
            print("")

            if user_type == "Loan Officer":
                ################## THIS IS THE BASIC INPUT VALIDATION METHOD WE USE WHEN ASKING FOR USER INPUT ##########
                
                while True:
                    print_menu(1,width)
                    try:
                        choice = int(input("\nEnter your choice: "))
                        if choice < 1 or choice > 6:
                            raise ValueError
                    except:
                        print("Invalid choice! Enter a number between 1 and 6")
                        continue
                    if choice == 1:
                        borrower_last_name = input("Enter the borrower's last name: ").capitalize()
                        search_loans(los, width, user_id, user_type, borrower_last_name)
                        waitForKeyPress(width)
                    elif choice == 2:
                        search_loans(los, width, user_id, user_type)
                        waitForKeyPress(width)
                    elif choice == 3:
                        search_loans(los, width, user_id, user_type, current = False)
                        waitForKeyPress(width)
                    elif choice == 4:
                        clearConsole()
                        create_loan(los, width, user_id)
                    elif choice == 5:
                        MC = MortgageCalculator()
                        MC.mainloop()
                    else:
                        exit_flag = True
                        clearConsole()
                        break
                ################################################################################################################
            else:
                ################## THIS IS THE BASIC INPUT VALIDATION METHOD WE USE WHEN ASKING FOR USER INPUT ##########
                while True:
                    print_menu(2,width)
                    try:
                        choice = int(input("\nEnter your choice: "))
                        if choice < 1 or choice > 5:
                            raise ValueError
                    except:
                        print("Invalid choice! Enter a number between 1 and 5")
                        continue
                    if choice == 1:
                        borrower_last_name = input("Enter the borrower's last name: ").capitalize()
                        search_loans(los, width, user_id, user_type, borrower_last_name)
                        waitForKeyPress(width)
                    elif choice == 2:
                        search_loans(los, width, user_id, user_type)
                        waitForKeyPress(width)
                    elif choice == 3:
                        search_loans(los, width, user_id, user_type, current = False)
                        waitForKeyPress(width)
                    elif choice == 4:
                        MC = MortgageCalculator()
                        MC.mainloop()
                    else:
                        exit_flag = True
                        clearConsole()
                        break
                ################################################################################################################
                
        else:
            attempts += 1
            print(f"Invalid username or password. {3-attempts} attempts remaining. Enter 'q' in username to exit.")   
    cursor.close()
    if attempts == 3:
        print("Too many incorrect attempts ...")
        time.sleep(5)

#Function to check minimum password requirements
def check_password(password):
    #print requirements:
    special_char = "!@#$%^&*()-_+=<>,.?/:;{}[]|~"
    #requirements
    if len(password) < 8:
        print('Invalid password! Minimum length of 8.')
        return False
    elif len(password) > 12:
        print('Invalid password! Maximum length of 12.')
        return False
    elif not any(char.isupper() for char in password):
        print('Invalid password! Must contain a capital letter.')
        return False
    elif not any(char.isdigit() for char in password):
        print('Invalid password! Must contain a digit.')
        return False
    elif not any((char in special_char) for char in password):
        print('Invalid password! Must contain a special character.')
        return False
    else:
        return True

#guides user to register a new InCollege account
def create_account(los, width):
    printCentered(" Creating a new user account ",width,"=")
    print()
    account_types = {'l':'Loan Officer',
                     'p':'Processor',
                     'u':'Underwriter',
                     'c':'Closer'}
    cursor = los.cursor()
    
    while (True):
        successful = False
        exit_flag = False

        first_name = input("Enter your first name: ").capitalize()
        while len(first_name) == 0:
            first_name = input("Enter your first name or q to quit: ").capitalize()
        if first_name == 'q':
            break
        last_name = input("Enter your last name: ").capitalize()
        while len(last_name) == 0:
            last_name = input("Enter your last name or q to quit: ").capitalize()
        if last_name == 'q':
            break
        nmls = input("Enter your NMLS #: ")
        while len(nmls) != 7 or not nmls.isdigit():
            nmls = input("Invalid. NMLS # must be exacly 7 digits. Your NMLS #:  ")
        
        #check if the nmls already exists
        query_3 = "SELECT EXISTS(SELECT * FROM USERS WHERE nmls = %s);"
        cursor.execute(query_3,(nmls,))
        nmls_exists = True if cursor.fetchone()[0] == 1 else False
        
        if nmls_exists:
            print(f"There is already an account with NMLS# {nmls}")
            break

        new_username = input("Enter username: ").lower()
        while len(new_username) == 0:
            new_username = input("Enter your user name: ").lower()
        if new_username == 'q':
            break

        
        while (True):
            new_password = input("Enter new password: ")
            if check_password(new_password):
                while True:
                    email = input("Enter your company email: ").lower()
                    while '@' not in email:
                        email = input("Invalid email input. Enter a valid email: ").lower()
                    domain = '@' + email.split('@')[1]
                    while domain != '@greathomeloans.com':
                        email = input("Email must end with @greathomeloans.com\nContact your admin if you do not have a company email. Your email: ").lower()
                        domain = '@' + email.split('@')[1]
                    #check if the email already exists
                    query_4 = "SELECT EXISTS(SELECT * FROM USERS WHERE email = %s);"
                    cursor.execute(query_4,(email,))
                    email_exists = True if cursor.fetchone()[0] == 1 else False
                    if email_exists:
                        print(f"This email {email} is already taken. Enter a unique email address.")
                    else:
                        break
                phone = input("Enter your work phone: ")
                while (False if phone.isdigit() and len(phone)==10 else True):
                    phone = input("Invalid. Must be exactly 10 digits. Enter your work phone: ")
                new_account_type = input("Are you a loan officer, processor, underwriter, or closer? Enter 'l','p','u', or 'c': ")
                while new_account_type not in ['l','p','u','c']:
                    new_account_type = input("Invalid input. Select one of 'l','p','u', or 'c'. ")
                account_type = account_types[new_account_type]
                query_5 = "INSERT INTO Users VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                cursor.execute(query_5,(nmls,first_name,last_name,email,phone,"",account_type, new_username, new_password))
                successful = True
                break
            elif new_password == 'q':
                break
            else:
                exit_flag = True
                continue
            
        if (successful):
            los.commit()
            cursor.close()
            print("\nAccount successfully created.\n")
            break
        elif (exit):
            break
        else:
            continue
    waitForKeyPress(width)
    clearConsole()
   
def main():
    los = connect()
    if not los:
        return 
    console_width = getConsoleWidth()
    welcome_screen(console_width)
################## THIS IS THE BASIC INPUT VALIDATION METHOD WE USE WHEN ASKING FOR USER INPUT ##########
    print()
    while True:
        home_screen(console_width)
        try:
            choice = int(input("\nSelect your choice:\n1.) Log in\n2.) Create a new user account\n3.) Exit the system\nYour choice: "))
            if choice < 1 or choice > 3:
                raise ValueError
        except:
            print("Invalid choice! Enter a number between 1 and 2!")
            waitForKeyPress(console_width)
            clearConsole()
            continue
        if choice == 1:
            login(los,console_width)
            pass
        elif choice == 2:
            clearConsole()
            create_account(los,console_width)
        else:
            exit_now(console_width)
            try:
                los.close()
            except:
                pass
            break
################################################################################################################

def print_phone(phone):
    return '(' + phone[0:3] + ') ' + phone[3:6] + '-' + phone[6:]

if __name__ == "__main__":
  main()
