def is_palindrome(word):
    word = word.replace(" ", "").lower()
    if word == word[::-1]:
        print("palindrome.")
    else:
        print("not a palindrome.")



