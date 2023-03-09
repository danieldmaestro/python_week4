digit = int(input("Enter a number between 1 & 1000: "))

def num_to_word(number):
    if number < 1 or number > 1000:
        print("Number out of range")
        return
    
    digits = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    word = ""
    # check if number is equal to 100. append one thousand to word
    if number == 1000:
        word += "One Thousand"
    # check is number is greater than or equal to 100
    elif number >= 100:
        # expression evaluates to one - 9 and appends Hundred to the item of digits[index]
        word += digits[number//100] + " Hundred"
        # expression checks in number is not a whole hundredth. if nott, appends and
        if number % 100 != 0:
            word += " and "
    #expression checks if number is greater thanor equal to 20   
    if number % 100 >= 20:
        word += tens[number % 100 // 10]
        # expression checks if number is not a whole tens integer then appends unit integer
        if number % 10 != 0:
            word += " " + digits[number%10]
    # expression checks if number is greater than or equal to 10 so appends teens[index]
    elif number % 100 >= 10:
        word += teens[number % 10]
        # after all else fails, expression prints digits[index] unit integer
    else:
        word += digits[number % 100]

    print(word)

num_to_word(digit)


