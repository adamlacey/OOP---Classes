### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

    # Declare the class variable, with default value, for emails. 
 
    # Initialise the instance variables for emails.

    # Create the method to change 'has_been_read' emails from False to True.

# --- Lists --- #
# Initialise an empty list to store the email objects.

# --- Functions --- #
# Build out the required functions for your program.

# Define the Email class.
class Email:
    '''Represents an email object with attributes like email address, subject \
        line, content and read status.
    '''
    
    # This class variable keeps track of the total emails.
    total_emails = 0
    
    # Constructor used to initialise an email object.
    def __init__(self, email_address, subject_line, email_content):
        '''Initilises an Email object.
        
            Parameters:
            - email_address: The email address of the sender.
            - subject_line: The subject line of each email.
            - email_content: The content included in the email.
        '''
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False
        Email.total_emails += 1
    
    # This method is used to mark an email as read.    
    def mark_as_read(self):
        '''Marks the email as read.
        '''
        self.has_been_read = True

# Initialise an empty list to store emails.
inbox = []

# This function populates the inbox with 3 sample emails.
def populate_inbox():
    '''Populates the inbox with 3 seperate sample emails containing different \
        details.
    '''
    # Created 3 sample emails and add it to the Inbox list. 
    inbox.append(Email("adam@gmail.com", "Subject: Holiday", "Content of email: \
Travel"))
    inbox.append(Email("angela@gmail.com", "Subject: Weather", "Content of \
email: Forecast"))
    inbox.append(Email("alan@gmail.com", "Subject: House", "Content of email: \
Mortgage"))

# This function lists the emails in the inbox.
def list_emails():
    '''Lists all the emails in the inbox.
    '''
    # Created a function which prints the email’s subject_line, along with a corresponding number.
    for i, email in enumerate(inbox, start=1):
        print(f"{i}. {email.subject_line}")
       
# Displays the initial list of emails.
list_emails()

# Function to read an email.
def read_email(index):
    '''Reads an email at the specified index in the inbox.
    
        Parameters:
        - index: The index of the email which is to be read.
    '''
    # Created a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    if 0 <= index < len(inbox):
        email = inbox[index - 1] # Adjust index for list indexing.
        print("From:", email.email_address)
        print("Subject:", email.subject_line)
        print("Content:", email.email_content)
        email.mark_as_read() # Mark the email as read.
        print("Email marked as read.")
    else:
        print("Invalid email index.")
        
populate_inbox()

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.

# Fill in the logic for the various menu operations.
menu = True

while True:
    # Displays menu options.
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # Added logic here to read an email.
        list_emails()
        index = int(input("Please enter the number of the email you wish to \
read: "))
        read_email(index)
        
    elif user_choice == 2:
        # Added logic here to view unread emails.
        unread_emails = [email.subject_line for email in inbox if not email.has_been_read]
        print("Unread emails: ")
        for subject in unread_emails:
            print(subject)
            
    elif user_choice == 3:
        # Added logic here to quit appplication.
        print("Application will now terminate.")
        break

    else:
        print("Oops - incorrect input.")