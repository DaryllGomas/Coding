import re
import tkinter as tk
from bs4 import BeautifulSoup
import requests

# Create a window using the tkinter library
window = tk.Tk()

# Show the welcome message
welcome_message = "Welcome to Daryll's Amazon price checker"
tk.Label(window, text=welcome_message).grid(row=0, column=0, columnspan=2)

# Create a label and an entry field where the user can input the ASIN
tk.Label(window, text="Product ASIN:").grid(row=1, column=0)
product_asin = tk.Entry(window)
product_asin.grid(row=1, column=1)

# Create a label where the price will be displayed
price_label = tk.Label(window, text="")
price_label.grid(row=2, column=0, columnspan=2)

# Create a function that will be called when the user clicks the "Check Price" button
def check_price():
    # Get the ASIN from the entry field
    asin = product_asin.get()

    # Use the ASIN to construct the URL of the Amazon product page
    url = f"https://www.amazon.com/dp/{asin}"

    # Use the requests library to fetch the HTML of the page
    response = requests.get(url)

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all the elements that contain the price
    price_elements = soup.find_all("span", {"class": "a-price"})

    # If any price elements were found, find the specific element that contains the price
    if price_elements:
        price_element = price_elements[0]

        # Get the text inside the element
        price_text = price_element.text

        # Use a regular expression to find the numeric price in the text
        price_match = re.search(r"[\d\.]+", price_text)

        # If a match is found, set the price label text to the price
        if price_match:
            price = price_match.group(0)
            price_label.configure(text=price)
        else:
            price_label.configure(text="N/A")
    else:
        price_label.configure(text="N/A")

# Create a button that will call the check_price function when clicked
tk.Button(window, text="Check Price", command=check_price).grid(row=3, column=0, columnspan=2)

# Run the window loop
window.mainloop()
