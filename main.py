"""
A virtual cookie shop.
Do not modify this file.
"""

import cookie_shop

# get data from the CSV file into a list
list_of_cookies = cookie_shop.bake_cookies('data/cookies.csv')

# open the cookie shop with the cookies read from the file
# this must run the rest of the program as documented
cookie_shop.run_shop(list_of_cookies)
