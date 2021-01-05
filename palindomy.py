def is_palindrom(word):

    text_input = word.lower()

    if(text_input==text_input[::-1]):  
        return True
    else:  
        return False

is_palindrom("kAjAk")
