# If a customer buys more than 5 books of any genre (fiction or non-fiction), they get a 10% discount on the total purchase.
# If the customer buys 3 or more fiction books, they get an additional 5% discount on the fiction books' total cost.
# For non-fiction books, buying 4 or more books gives an extra 7% discount on the total cost of non-fiction books.

fiction=int(input("Enter The Number OF Fiction BOOk You Requiered"))
nonfiction=int(input("Enter The Number OF NON Fiction BOOk You Requiered"))

if(fiction+nonfiction>=5):
    print("You Got 10% Discount")
if(fiction>=3):
    print("You Got 5% Discount")
if(fiction>=4):
    print("You Got 5% Discount")
