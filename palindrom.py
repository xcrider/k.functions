def is_palindrome (word):
    """Function is checking if the argument is a palindrome word.
    Function takes string (single word) as an argument.
    Function returns True statment if argument is a palindrome, and False for non palindrome.
    A palindrome is a word like - kajak, or Anna.
    Which can be read from left to right and right to left and have the same meaning."""

    text_input = word.lower()

    if(text_input==text_input[::-1]):  
        return True
    else:  
        return False

is_palindrome("kAjAk")
