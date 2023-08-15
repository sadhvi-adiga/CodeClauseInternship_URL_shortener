import pyshorteners as pys

copied_url = input("Please paste your URL : ")
short_url = pys.Shortener().tinyurl.short(copied_url)
print("Shortened URL : ",short_url)