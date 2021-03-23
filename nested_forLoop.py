websites = ['amazon','flipkart','google']

extensions = ("org","com","in")



for web in websites:
    for ext in extensions:
        print("www." + web + "." + ext)