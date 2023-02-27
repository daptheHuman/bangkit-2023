##################### No 1 ######################
def format_address(address_string):

    house_number = ""
    street_name = ""

    # Separate the house number from the street name.
    address_parts = address_string.split()
    
    for address_part in address_parts:
       # Complete the if-statement with a string method.  
       if address_part.isnumeric():
         house_number = address_part
       else:
         street_name += address_part + " "
    # Remove the extra space at the end of the last "street_name".
    street_name = street_name.strip()
 
    # Use a string method to return the required formatted string.
    return "House number {} on a street named {}".format(house_number, street_name)

print(format_address("123 Main Street"))
# Should print: "House number 123 on a street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "House number 1001 on a street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "House number 55 on a street named North Center Drive"



##################### No 2 ######################
def alpha_length(string):
    character = ""
    count_alpha = 0
    # Complete the for loop sequence to iterate over "string".
    for char in string: 
        # Complete the if-statement using a string method. 
        if char.isalpha():
            count_alpha += 1  
    return count_alpha
 
print(alpha_length("This has 1 number in it")) # Should print 17
print(alpha_length("Thisisallletters")) # Should print 16
print(alpha_length("This one has punctuation!")) # Should print 21



##################### No 3 ######################
def combine_lists(list1, list2):

  combined_list = [] # Initialize an empty list variable
  list1.reverse()  # Reverse the order of "list1"
  list2.extend(list1) # Combine the two lists 
  combined_list = list2
  return combined_list  
  
Jaimes_list = ["Alma", "Chika", "Benjamin", "Jocelyn", "Oakley"]
Drews_list = ["Minna", "Carol", "Gunnar", "Malena"]

print(combine_lists(Jaimes_list, Drews_list))
# Should print ['Minna', 'Carol', 'Gunnar', 'Malena', 'Oakley', 'Jocelyn', 'Benjamin', 'Chika', 'Alma']



##################### No 4 ######################
def squares(start, end):
    return [x**2 for x in range(start, end+1) ] # Create the required list comprehension.

print(squares(2, 3)) # Should print [4, 9]
print(squares(1, 5)) # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



##################### No 5 ######################
def car_listing(car_prices):
  result = ""
  # Complete the for loop to iterate through the key and value items 
  # in the dictionary.
  for car, price in car_prices.items():
    result += "A {} costs {} dollars\n".format(car, price) # Use a string method to format the required string. 
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# Should print:
# A Kia Soul costs 19000 dollars
# A Lamborghini Diablo costs 55000 dollars
# A Ford Fiesta costs 13000 dollars
# A Toyota Prius costs 24000 dollars



##################### No 6 ######################
def check_guests(guest_list, guest):
  return guest_list[guest] # Return the value for the given key


guest_list = { "Adam":3, "Camila":3, "David":5, "Jamal":3, "Charley":2, "Titus":1, "Raj":6, "Noemi":1, "Sakira":3, "Chidi":5}


print(check_guests(guest_list, "Adam")) # Should print 3
print(check_guests(guest_list, "Sakira")) # Should print 3
print(check_guests(guest_list, "Charley")) # Should print 2



##################### No 7 ######################
def count_letters(text):
  # Initialize a new dictionary.
  dictionary = {} 
  # Complete the for loop to iterate through each "text" character and 
  # use a string method to ensure all letters are lowercase.
  for char in text.lower():   
    # Complete the if-statement using a string method to check if the
    # character is a letter.
    if char.isalpha():
      # Complete the if-statement using a logical operator to check if 
      # the letter is not already in the dictionary.
      if char not in dictionary:
           # Use a dictionary operation to add the letter as a key
           # and set the initial count value to zero.
           dictionary[char] = 0
      # Use a dictionary operation to increment the letter count value 
      # for the existing key.
      dictionary[char] += 1
      # ___ # Increment the letter counter. 
  return dictionary

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}



