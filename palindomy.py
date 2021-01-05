def is_palindrom(word):
    """Function is checking if the argument is a polidrome word. A polidrome is a word like - kajak, or Anna which can be read from left to right and right to left and have the same meaning."""
    text_input = word.lower()

    if(text_input==text_input[::-1]):  
        return True
    else:  
        return False

is_palindrom("kAjAk")
