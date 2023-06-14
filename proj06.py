  ###########################################################

    #  Computer Project #06

    #

    #  Algorithm
    #           This program imports the csv file to be used, it also calls the operator function to import itemgetter. 
    #           The program has 9 functions and 1 main function. 
    #           The docstrings for the various functions have been included in the functions. 
    #           The functions:
    #                          1. open_file()
    #                          2. read_file()
    #                          3. get_books_by_criterion()
    #                          4. get_books_by_criteria()
    #                          5. get_books_by_keyword()
    #                          6. sort_authors()
    #                          7. recommend_books()
    #                          8. display_books()
    #                          9. get_option()

    #           The main_function():
    #                  1. calls the open_file function to open the CSV file to get a file pointer for the input file. 
    #                  2. calls the read_file function to read the data and store it in a list of tuples.
    #                  3. call the get_option function to prompt the user for input. 
    #                  4. A while loop to keep taking the option from the user until the option is 4.
    #                       a. if option is 1:
    #                                         i. prompts the user for a title
    #                                         ii. call the get_books_by_criterion function and pass the title as a value and TITLE as a criterion
    #                                         iii. Display the book that has the title in it. 
    #                       b.if option is 2:
    #                                        filter books by a certain criterion. 
    #                                        i. prompt the user for criterion(3,5,6,7), and value inputs. float(value) if criterion is 6 or int(value) if criterion is 7
    #                                        ii. call get_books_by_criterion and pass on the arguments
    #                                        iii. call the sort_authors function to sort in place.
    #                                        iv. call the display_book function to output the first 30 books 
    #                       c. if option is 3:
    #                                          recommend a book based on certain criteria
    #                                       i. prompt the user for category, rating,and page number 
    #                                       ii. Ask for a_z boolean value, default to 1 if no input 
    #                                       iii. prompt for a list of keywords separated by spaces.
    #                                       iv. call the recommend books function and pass on the parameters to it. 
    #                                       v. call the display_books function to display the output
    #                       d. if option is 4:
    #                                         i. The program quits 
    #
    #
    ###########################################################

import csv
from operator import itemgetter

TITLE = 1
CATEGORY = 3
YEAR = 5
RATING = 6
PAGES = 7

MENU = "\nWelcome to the Book Recommendation Engine\n\
        Choose one of below options:\n\
        1. Find a book with a title\n\
        2. Filter books by a certain criteria\n\
        3. Recommend a book \n\
        4. Quit the program\n\
        Enter option: "

CRITERIA_INPUT = "\nChoose the following criteria\n\
                 (3) Category\n\
                 (5) Year Published\n\
                 (6) Average Rating (or higher) \n\
                 (7) Page Number (within 50 pages) \n\
                 Enter criteria number: "
TITLE_FORMAT = "{:15s} {:35s} {:35s} {:6s} {:8s} {:15s} {:15s}"
TABLE_FORMAT = "{:15s} {:35s} {:35s} {:6s} {:<8.2f} {:<15d} {:<15d}"

def open_file():
    """
    Prompts the user to input a file name, then opens it and keeps prompting until a valid name is entered.
    Returns the file pointer. Uses try-except to determine if the file can be opened. When opening the file,
    uses encoding="utf-8".

    param: None
    return: A file pointer to the opened file
    raises: FileNotFoundError: If the file specified by the user cannot be found
             IOError: If the file cannot be opened due to other errors
    display: Prompts the user to input a file name and displays error messages if the file cannot be found or opened.
    """
     
    while True:

        fname = input("Enter file name: ")           #ask the user for a file to open 
        try:
            fp = open(fname, "r",encoding="utf-8" )  #open the file
            return fp
            break
        except FileNotFoundError:                   #check for errors
            print("\nError opening file. Please try again.")
            continue 
            
def read_file(fp):
    """
    Reads the comma-separated value (csv) file using file pointer fp and returns a list of tuples.
    The file has one header line that is skipped. Each tuple represents a book and has the following format:
    (isbn13, title, authors, categories, description, year, rating, num_pages, rating_count).
    The type of each element in the tuple is (string, string, string, list(lowercase strings), string, string, float, int, int).
    If any conversion fails, that line of data is skipped.

    param fp: A file pointer to the csv file to be read.
    type fp: _io.TextIOWrapper
    return: A list of tuples representing the books in the csv file.
    rtype: list
    raises: csv.Error: If the csv file cannot be parsed.
    display: Nothing is displayed by this function.

    """
    books = csv.reader(fp)
    next(books, None)                    # skip header line
    tuple_list = []                      #initialize an empty list
    
    for row in books:
        #set up multiple assignment to take the values from the csv files  
        try:
            isbn13, title, authors, categories, description, year, rating, num_pages, rating_count = \
                row[0], row[2], row[4], [cat.lower() for cat in row[5].split(",")], row[7], \
                row[8], float(row[9]), int(row[10]), int(row[11])

            #append the list tuple generated into the list 
            tuple_list.append((isbn13, title, authors, categories, description, year, rating, num_pages, rating_count))
        except:
            continue

    return tuple_list 


def get_books_by_criterion(book_list, criterion, value):
    """
    Given a list of book tuples, retrieve the books that match a certain criterion based on the given value.
    If there is a problem with the value or criterion parameter, an empty list is returned. The criterion parameter
    is an int that represents the index of a criterion in a book tuple. For example, if filtering by TITLE, criterion
    should be 1; if filtering by YEAR, criterion should be 5, etc.
    No error checking

    Note:
    I. If searching by TITLE, only return the tuple of the book with that title. Do not put it in a list.
       Variations in case are accepted.
    II. For CATEGORY, value must be a string and variations in case are accepted, e.g. 'Fiction', 'FICTION', 'FiCTion'
        and similar will match. If not, do not add the book to the return list.
    III. For YEAR, value is a string. The returned books should be published during the given value.
    IV. For RATING, value is a float number. The returned books should have rating greater than or equal to the given value.
    V. For PAGES, value should be an integer. Books included should have a page number within 50 pages of this number
       inclusive. For example, if the value is 137, books included will have page numbers between 87 and 187, including
       those numbers.

    param book_list: A list of tuples representing the books to be filtered.
    type book_list: list
    param criterion: An int that represents the index of a criterion in a book tuple.
    type criterion: int
    param value: The value to filter by.
    type value: int/float/string
    return: A list of tuples representing the books that match the given criterion based on the given value.
    rtype: list
    display: Nothing is displayed by this function.
    """

    filtered_books = []
    try:
        if criterion == TITLE:
            # Retrieve the book tuple with matching title, case-insensitive
            for book in book_list:
                if book[TITLE].lower() == value.lower():
                    return book
                
        elif criterion == CATEGORY:
            # Retrieve books with matching category, case-insensitive
            for book in book_list:
                if value.lower() in [ch.lower() for ch in book[CATEGORY]]:
                        filtered_books.append(book)
            
        elif criterion == YEAR:
            # Retrieve books published during the given year
            for book in book_list:
                if value == book[YEAR]:
                    filtered_books.append(book)
        elif criterion == RATING:
            # Retrieve books with rating greater than or equal to the given value
            for book in book_list:
                if float(book[RATING]) >= float(value):
                    filtered_books.append(book)
        elif criterion == PAGES:
            # Retrieve books with page number within 50 pages of the given value
            target_pages = int(value)
            for book in book_list:
                num_pages = int(book[PAGES])
                if target_pages - 50 <= num_pages <= target_pages + 50:
                    filtered_books.append(book)
        else:
            # Invalid criterion
            return []
    except (ValueError, IndexError):
        # Invalid value or criterion index
        return []
    return filtered_books

    
def get_books_by_criteria(book_list, category, rating, page):
    """
    This function filters a list of book tuples based on three criteria: category, rating, and page number.
    It calls the get_books_by_criterion function three times, one for each criterion in the following order: 
    category, rating, then page number. The returned list of one function is passed as an argument to the next call.
    
    Parameters:
    book_list (list of tuples): A list of book tuples.
    category (str): The category to filter by (case-insensitive).
    rating (float): The minimum rating to filter by.
    page (int): The page number to filter by.
    
    Returns:
    list of tuples: A list of book tuples that match all three criteria.
    
    Display:
    nothing
    """

    # Filter by category
    filtered_books = get_books_by_criterion(book_list, CATEGORY, category)
    
    # Filter by rating
    filtered_books = get_books_by_criterion(filtered_books, RATING, rating)
    
    # Filter by page number
    filtered_books = get_books_by_criterion(filtered_books, PAGES, page)
    
    return filtered_books


def get_books_by_keyword(book_list, keywords):
    """
    Given a list of book tuples, retrieve all books whose description contains any of the keywords value.

    Parameters:
    book_list (list of tuples): List of book tuples to search through.
    keywords (list of strings): List of keywords to search for.

    Returns:
    list of tuples: List of book tuples that contain at least one keyword in their description.

    Display: nothing
    """
    matched_books = []                      #set up an empty list to store the books
    
    for book in book_list:
        description = book[4].lower()       #access the description of the book
        for word in keywords:
            if word.lower() in description:
                matched_books.append(book)  #append books that have at least one keyword in the description 
                break

    return matched_books


def sort_authors(list_of_tuples, a_z=True):
    """
    Sorts a list of book tuples by author name and returns the sorted list.

    Args:
    - list_of_tuples (list): a list of tuples representing books, with the following format:
        (isbn13, title, authors, categories, description, year, rating, num_pages, rating_count)
    - a_z (bool, optional): a boolean value that determines the sorting order. 
    If True (default), the list will be sorted in ascending order. 
    If False, the list will be sorted in descending order.
    
    Returns:
    - sorted_list (list): a sorted list of book tuples based on author name.
    """
    
    sorted_list = sorted(list_of_tuples, key=itemgetter(2), reverse=not a_z)

    return sorted_list

def recommend_books(books_list, keywords, category, rating, page_number, a_z=True) -> list:
    """
    Retrieves all books in a list of book tuples filtered by category, rating, page number criteria and
    whose description contains any of the keywords. Sort the returned list by author name. The a_z boolean
    value determines if you should return the books in descending or ascending order based on author name.

    Args:
        books_list (list of tuples): A list of book tuples.
        keywords (list of strings): A list of keywords to filter books by.
        category (str, optional): The category to filter books by. Defaults to None.
        rating (float, optional): The minimum rating a book must have to be included. Defaults to None.
        page_number (int, optional): The minimum number of pages a book must have to be included. Defaults to None.
        a_z (bool, optional): Determines whether to sort the books in ascending or descending order by author name.
            If True, sort the books in ascending order. If False, sort the books in descending order. Defaults to True.

    Returns:
        list of tuples: A list of book tuples that meet the filter criteria and are sorted by author name.

    Display:
        Nothing.
    """
    #call the get books by criteria function to filter the books on the parameters given
    filtered_books = get_books_by_criteria(books_list, category, rating, page_number)

    #call the get books by keyword function to check if the key word can be found in the filtered books
    filtered_books = get_books_by_keyword(filtered_books, keywords)

    #call the sort_authors function to sort the filtered books, already filtered by keywords. 
    sorted_books = sort_authors(filtered_books, a_z)
    
    return sorted_books

def display_books(list_of_tuples) -> None:
    """
    Given a list of book tuples, display the books along with their information.
    Ignore a book if its title or its authors are longer than 35 characters.
    If list_of_tuples is empty, print 'Nothing to print.'

    Args:
        list_of_tuples (list of tuples): A list of book tuples to display.

    Returns:
        None

    Display:
        Prints the formatted book information to the console.
    """

    #make a new variable to take on the list of tuples 
    new_list = list_of_tuples
    
    #check if the list of tuples is an empty list 
    #if it is display nothing to print 
    #if it is not empty, print a formatted table header 

    if len(new_list) == 0:
        print("\nBook Details:") 
        print("Nothing to print.")
    else:    
        print("\nBook Details:")
        print(TITLE_FORMAT.format("ISBN-13", "Title", "Authors", "Year", "Rating", "Number Pages", "Number Ratings"))
    
    for item in new_list:
        #create a new_list of tuple to store the items at specified indices 
        isbn13,title,authors,year,rating,num_pages,rating_count = \
                item[0], item[1], item[2], item[5], item[6], item[7], item[8]
    
        #condition 1: print out the desired values if both len(title) and len(author) are less than or equal to 35.
        if len(title) <= 35 and len(authors) <= 35: 
            print(TABLE_FORMAT.format(isbn13, title, authors, year, rating, num_pages, rating_count))

        #condition 2: if both lengths are greater 35, skip the book 
        elif len(title) > 35 and len(authors) > 35:  
            continue
        
        #condition 3: if len(title)>35 and len(authors) <= 35, skip book  
        elif len(title) > 35: 
            if len(authors) <= 35:
                continue
        
        #condition 4: if len(authors)>35 and len(title) <= 35, skip book
        elif len(authors) > 35: 
            if len(title) <= 35:
                continue
            
            
    
def get_option() -> int:
    """
    Display a menu of options and prompt for input. Return the input if it is between 1-4 inclusive. Otherwise, it
    prints an error message and returns None. Ask for the input in the function, this function does not take parameters.

    Args:
        None

    Returns:
        int: The selected menu option.

    Display:
        Prints the menu and error message to the console.
    """

    while True:
        try:
            #asks the user to make a choice from a list of menu options
            #if the option is not in the menu of options, reprompt the user 
            #if the option is not a number, reprompt the user.

            option = int(input(MENU))
            if (1 <= option <= 4) is False:
                print("\nInvalid option")
            else:
                return option
            
        except ValueError:
            print("\nInvalid input")     

def main():
    fp = open_file()                 #open the file
    books = read_file(fp)            #read the file
    fp.close()                       #close the file 
    
    while True:
        option = get_option()       #call the get_option function 
        
        if option == 1:
            title = input("\nInput a book title: ")

            #call the get_books_by_criterion function to get all the books with the title
            book = get_books_by_criterion(books, TITLE, title )

            #call the display_books function to print out the output 
            display_books([book]) 
               
        elif option == 2:
            #set up a loop to keep asking the user for the right criterion input 
            #if the input is in the desired quantity we break out of the loop

            while True:
                criterion = input(CRITERIA_INPUT)
                if criterion.isdigit() and int(criterion) in [3, 5, 6, 7]:
                    criterion = int(criterion)
                    break
                else:
                    print("\nInvalid input")
            value = input("\nEnter value: ")

            #convert value into a float if criterion input is 6
            #convert value into an integer if criterion input is 7 
            if criterion in [6, 7]:
                try:
                    value = float(value) if criterion == 6 else int(value)
                except ValueError:
                    print("\nInvalid input")
                    value = input("\nEnter value: ")

            #Call the get_books_by_criterion function to filter the books based on criterion       
            filtered_books = get_books_by_criterion(books, criterion, value)
            
            #call the sorted_books function to sort the filtered books in place
            sorted_books = sort_authors(filtered_books, itemgetter(2))
            
            #Call the display_books function to display the first 30 books. ([:30] list slicing)
            display_books(sorted_books[:30])
            
        elif option == 3:
            #Ask the user for category
            #Ask the user for rating
            #Ask the user for number of pages

            category = input("\nEnter the desired category: ")
            rating = input("\nEnter the desired rating: ")
            pages = input("\nEnter the desired page number: ")

            #check if the rating is a float or pages is an integer, if not re-prompt the user
            try:
                rating = float(rating)
                pages = int(pages)
            except ValueError:
                print("\nInvalid input")
                continue

            #ask for the a_z input from the user (1 or 2) 
            # if no input, set it to 1 
            a_z = input("\nEnter 1 for A-Z sorting, and 2 for Z-A sorting: ") == "1"

            #prompt for a list of keywords that are space separated 
            keywords = input("\nEnter keywords (space separated): ").split()

            #call the recommend_books function and pass on the parameters above into it. 
            recommended_books = recommend_books(books, keywords, category, rating, pages, a_z)
          
            #call the display_books function to display the output 
            display_books(recommended_books)
             
        elif option == 4:
            break
             

# DO NOT CHANGE THESE TWO LINES
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
if __name__ == "__main__":
    main()
    
    
    
"Enter file name: "
"\nError opening file. Please try again."
"\nInput a book title: "
"\nInvalid input"
"\nInvalid option"
"\nEnter value: "
"\nBook Details:"
"\nEnter the desired category: "
"\nEnter the desired rating: "
"\nEnter the desired page number: "
"\nEnter 1 for A-Z sorting, and 2 for Z-A sorting: "
"\nEnter keywords (space separated): "
"Nothing to print."
"{:15s} {:35s} {:35s} {:6s} {:8s} {:15s} {:15s}"
"{:15s} {:35s} {:35s} {:6s} {:<8.2f} {:<15d} {:<15d}"

