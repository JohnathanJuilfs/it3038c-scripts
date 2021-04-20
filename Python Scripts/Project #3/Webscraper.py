# This program uses beautiful soup to generate a random wikipedia article.
# The program will prompt the user with an article and ask if they want to view it or not.
# If the user selects yes, it will open the browser and go to the selected wikipedia link
# If the user selects no it will generate a new article until the user says yes to one.
import requests
from bs4 import BeautifulSoup
import webbrowser

while True:
    w = "https://en.wikipedia.org/wiki/Special:Random"
    # Makes the variable w correspond to the link that sends you to a random article.
    g = requests.get(w)
    BS = BeautifulSoup(g.content, 'html.parser')
    # Parsing the link, after it is parsed the same link cannot be used twice after getting users choice.
    title = BS.find(class_="firstHeading").text
    # Telling BS to find the first heading of the article.
    print(title + "\nDo You want to view this article? (Y/N)")
    #  Printing title of article and prompt to ask user if they want this link or not.
    userchoice = str(input(""))
    # Creating a variable for the users input.
    if userchoice.lower() == "y":
        url = 'https://en.wikipedia.org/wiki/%s' % title
        webbrowser.open(url)
        # If users choice is "y", open wikipedia article int he browser.
        break
    elif userchoice.lower() == "n":
        print("Okay\nFinding a new link!")
        # If users choice is "N", find a new link.
        continue
    else:
        print("Invalid selection, please choose Y or N")
        # Extra option for if someone doesn't type "Y" or "N".
        break
