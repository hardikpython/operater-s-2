# Function to convert decimal to binary
def decimal_to_binary(decimal_num):
    # Check if the decimal number is zero
    if decimal_num == 0:
        return "0"
    
    binary_num = ""
    
    # Loop to divide the decimal number by 2 and collect remainders
    while decimal_num > 0:
        remainder = decimal_num % 2  # Get remainder (either 0 or 1)
        binary_num = str(remainder) + binary_num  # Prepend remainder to the binary number
        decimal_num = decimal_num // 2  # Integer division by 2
    
    return binary_num


# Input: Decimal number from the user
decimal_number = int(input("Enter a decimal number: "))

# Call the function to convert decimal to
