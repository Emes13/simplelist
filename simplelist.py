# Little coding practice
# Behavior: Simply appends any text entered to a list, split on single space
#           Upon entering '] ' as first term, three special commands are
#			available: list (list all items); search (match string to item); quit

# -removed need for global activesession
# -eliminated returns from each if statement - redundant

# To do:
# 1. make search not case sensitive
# 2. figure out how to avoid global by returning list from function instead

activesession = True
user_defined_data = []

'''
I want to wrap the user input in a function that will return a list of the terms, 
rather than splitting the string on the fly every time
'''
def get_text():
	return input("=> ").split(" ")

def is_command(user_input_list):
    if user_input_list[0] == "]": #use of \ was causing escape problems
        return True
    return False
    
def process_command(command, activesession):
    global user_defined_data
  
    if command[1] == "quit":
        activesession = False
         
    elif command[1] == "search":
        search_term = command[2]
        term_exists = False # Does not exist until proven otherwise.
        for i in user_defined_data:
            if search_term in i:
                term_exists = True
                print(i)
            
        if not term_exists: print("Your search term was not found.")
            
    elif command[1] == "list":
        for i in user_defined_data:
            print(i,)
		
    else:
	    print("Invalid command.")

    return activesession

def store_data(activesession):
    global user_defined_data
    user_input_list = get_text()
    
    if is_command(user_input_list):
        activesession = process_command(user_input_list, activesession)
    else:    
		#each separate word is listed separately
        user_defined_data.extend(user_input_list) 
        
    return activesession
    
while activesession:
    activesession = store_data(activesession)