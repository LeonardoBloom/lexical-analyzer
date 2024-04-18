
from enum import Enum # imported Enum for use of Enumerations

# TOKENS defined for enumeration of types
class TOKENS(Enum):
    INTEGER = 1
    FLOAT = 2
    ID = 3
    BITWISE_OR = 4
    LOGICAL_OR = 5
    BITWISE_AND = 6
    LOGICAL_AND = 7
    FOR = 8
    WHILE = 9
    IF = 10
    ELSE = 11
    ERROR = 12

class LEX_RESULT:
    # constructor for LEX_RESULT, showing all the properties of the desired return object
    def __init__(self, token, symbol_index=None, integer_value=None, float_value=None, string_char=None):
        self.token = token
        self.symbol_index = symbol_index
        self.integer_value = integer_value
        self.float_value = float_value
        self.string_char = string_char # the unrecognized string


# lex is the method that identifies each token and lexeme and then
# adds the information about them in the LEX_RESULT object
def lex(file_content, symbol_table):
    # dictionary created assigning the tokens to the token types
    tokens = {
        '|': TOKENS.BITWISE_OR,
        '||': TOKENS.LOGICAL_OR,
        '&': TOKENS.BITWISE_AND,
        '&&': TOKENS.LOGICAL_AND,
        'for': TOKENS.FOR,
        'while': TOKENS.WHILE,
        'if': TOKENS.IF,
        'else': TOKENS.ELSE
    }

    # go through each lexeme in the file
    for lexeme in file_content.split():
        
        # check if lexeme is integer
        if lexeme.isdigit() or (lexeme[0] == '-' and lexeme[1:].isdigit()):
            yield LEX_RESULT(TOKENS.INTEGER, integer_value=int(lexeme))

        # check for float
        elif lexeme.replace('.', '', 1).isdigit():
            yield LEX_RESULT(TOKENS.FLOAT, float_value=float(lexeme))

        # check if lexeme is a token
        elif lexeme in tokens:
            yield LEX_RESULT(tokens[lexeme])

        
        elif lexeme.isidentifier():  # Check if lexeme is a valid identifier
            if lexeme not in symbol_table:
                symbol_table.append(lexeme)  # Add identifier to symbol table
            yield LEX_RESULT(TOKENS.ID, symbol_index=symbol_table.index(lexeme))
        else:
            # if lexeme is not an expected token or identifier
            yield LEX_RESULT(TOKENS.ERROR, string_char=lexeme)

# initialize symbol table with these reserved words
symbol_table = ["for", "while", "if", "else"]

# read the contents of our input text file
with open("assignment2.txt", "r") as file:
    file_content = file.read()

# program loop starts here
while True:

    # interface for the menu
    print("1. Call lex()")
    print("2. Show Symbol Table")
    print("3. Exit")

    choice = input("Enter your choice (1-3)")


    match choice:
        case '1':

            # if choice is 1, Call the lex() function, taking the input file content 
            # and the symbol table as parameters

            for result in lex(file_content, symbol_table):
                
                # print the object properties for the lexeme every time lex() is called
                print(f"<token={result.token.name}, index={result.symbol_index}, "
                    f"integer_value={result.integer_value}, float_value={result.float_value}, "
                    f"unrecognized_string='{result.string_char}'>")
        case '2':
            # show our symbol table. It will be updated if lex() is called
            print("Symbol Table:")
            print(symbol_table)
            
        case '3':
            # Exit the program
            print("Exiting Program...")
            break