# making a request to fixer.io forex rates website
# and getting a json reponse
# and extracting info from json

import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?access_key=9cf56a8a095b8a7263ecdfdf17d155ef&symbols=USD,AUD,CAD,PLN,MXN&format=1")
    
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    
    # extracting info from json
    rate = data["rates"]["USD"]
    print(f"1 EUR is equal to {rate} USD") # base is EUR for free accounts

if __name__ == "__main__":
    main()
