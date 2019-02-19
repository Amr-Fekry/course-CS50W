# making a request to fixer.io forex rates website
# and getting a json reponse

import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?access_key=9cf56a8a095b8a7263ecdfdf17d155ef&symbols=USD,AUD,CAD,PLN,MXN&format=1")
    
    # print status code
    print(f"Status code: {res.status_code}")
    print()
    
    # raise exception if status code != 200
    if res.status_code != 200:	
        raise Exception("ERROR: API request unsuccessful.")
    
    # print json if request was successful
    data = res.json()
    print(data)

if __name__ == "__main__":
    main()
