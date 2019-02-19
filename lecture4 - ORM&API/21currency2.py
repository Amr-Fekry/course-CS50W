# making a request to fixer.io forex rates website
# using user input for api parameters

# NOT working anymore: base is always EURO for free accounts

import requests

def main():
    base = input("First Currency: ")
    other = input("Second Currency: ")
    # the takeaway is that url params can be passed as below 
    res = requests.get("https://api.fixer.io/latest",
                       params={"base": base, "symbols": other})
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    rate = data["rates"][other]
    print(f"1 {base} is equal to {rate} {other}")

if __name__ == "__main__":
    main()

