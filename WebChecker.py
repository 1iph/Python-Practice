print("WEB CHECKER")
text = input("Enter a URL: ")
if text.startswith("https://"):
    print("The URL is secure.")
elif text.startswith("http://"):
    print("The URL is not secure.")
elif text.startswith("www."):
    print("The URL is a website.")
elif text.endswith(".com"):
    print("The URL is a commercial website.")
elif text.endswith(".org"):
    print("The URL is an organization website.")
elif text.endswith(".net"):
    print("The URL is a network website.")
elif text.endswith(".edu"):
    print("The URL is an educational website.")
elif text.endswith(".gov"):
    print("The URL is a government website.")
elif text.endswith(".mil"):
    print("The URL is a military website.")
elif text.endswith(".int"):
    print("The URL is an international organization website.")
elif text.endswith(".info"):
    print("The URL is an informational website.")