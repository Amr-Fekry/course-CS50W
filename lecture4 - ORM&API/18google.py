# making HTTP requests in Python

import requests

def main():
	# response = requests.method(url) 
	# method: get/post/put/patch/delete
    res = requests.get("https://www.google.com/")
    print(res.text)

if __name__ == "__main__":
    main()

# res.text returns the html of the page requested
# res.json() returns the json of the page requested

# for html, xml we use res.text and then parse it to get specific content from a webpage
