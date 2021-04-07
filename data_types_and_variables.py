#What data type would best represent:

#A term or phrase typed into a search box? String
#If a user is logged in? Boolean  
#A discount amount to apply to a user's shopping cart? Float
#Whether or not a coupon code is valid? Boolean
#An email address typed into a registration form? String
#The price of a product? Float
#A Matrix? List of a list
#The email addresses collected from a registration form? List of strings
#Information about applicants to Codeup's data science program? Dictionary

#You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear 
#(for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). 
#If price for a movie per day is 3 dollars, how much will you have to pay?

days_of_movies = [3, 5, 1]  #Make a list of the number of days each movie was rented
cost = sum([num * 3 for num in days_of_movies]) #Perform a list comprehension to multiply each number of 
                                                #days by the cost, 3 dollars.
                                                #then add all everything together to find the total cost
cost

# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a 
# different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will 
# you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 
# hours for Amazon.
rate_of_pay = [400, 380, 350]
hours_worked = [6, 4, 10]
payment = sum([rate_of_pay[i] * hours_worked[i] for i in range(len(rate_of_pay))])
payment

#A student can be enrolled to a class only if the class is not full and the class schedule does 
# not conflict with her current schedule.
class_full = False
no_conflict = True
can_enroll = not class_full and no_conflict
print(can_enroll)

#A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.

items = 3
offer_not_expired = True
premium = False
offer = offer_not_expired and (items > 2 or premium)
offer

#Create a variable that holds a boolean value for each of the following conditions:

#the password must be at least 5 characters
#the username must be no more than 20 characters
#the password must not be the same as the username
#bonus neither the username or password can start or end with whitespace

username = 'codeup'
password = 'notastrongpassword'

good_login = len(password) >= 5 and len(username) <= 20 and password != username
good_login
