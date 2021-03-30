websites = ['Amazon', 'flipkart', 'paytm']
extensions = ['.com', '.org', '.in']

result = ['www.' + item + x for item in websites for x in extensions]
print(result)