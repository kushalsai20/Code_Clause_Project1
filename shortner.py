import pyshorteners
print("Enter the link:")
link=input()
shortener=pyshorteners.Shortener()
shorted_link=shortener.tinyurl.short(link)
print(shorted_link)
