def get_market_cap(coin):
    coin = str(coin) 
    import requests
    # URL for Coingecko
    url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"

    # Defining parameters
    parameters = {
        "vs_currency":"usd",
        "days":"5",
        "interval":"daily",
        "accept": "application/json"
    }

    # sending request to url with parameters
    response = requests.get(url, params=parameters)

    print("Market Cap")

    # converting response to json and getting the market_cap

    market_cap = response.json()
    return market_cap

print(get_market_cap("bitcoin"))



    # parsing the market_cap and appending it to a list & dict for using in fb_prophet
#     cap_list = []
#     cap_dict = {
#         "Market_caps":[]
#     }
#     for i in cap:
#         i = int(i[1])
#         cap_list.append(i)
#         cap_dict['Market_caps'].append(i)
#         return cap_list
#         return cap_dict
#         print("Got the values inside list and dict!!")
# get_market_cap(bitcoin)
# print(cap_list)
# print(cap_dict)