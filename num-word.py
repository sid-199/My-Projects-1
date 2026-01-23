# Number-to-Words Converter (Up to 999)

# Dictionaries for mapping numbers to words
ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", 
         "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", 
        "sixty", "seventy", "eighty", "ninety"]

# Function to convert numbers to words
def number_to_words(num):
    if num == 0:
        return "zero"

    if num < 10:
        return ones[num]

    elif num < 20:
        return teens[num - 10]

    elif num < 100:
        return tens[num // 10] + (" " + ones[num % 10] if num % 10 != 0 else "")

    elif num < 1000:
        remainder = num % 100
        hundreds = ones[num // 100] + " hundred"
        if remainder != 0:
            return hundreds + " and " + number_to_words(remainder)
        else:
            return hundreds

    else:
        return "Number out of range (0–999)"

# Main program
while True:
    try:
        n = int(input("Enter a number (0–999): "))
        if 0 <= n <= 999:
            print("In words:", number_to_words(n))
        else:
            print("Please enter a number between 0 and 999.")
    except ValueError:
        print("Invalid input! Please enter a number.")
    
    choice = input("Do you want to continue? (y/n): ").lower()
    if choice != 'y':
        print("Goodbye!")
        break
