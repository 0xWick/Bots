from binance.client import Client


API_KEY = YOUR_API_KEY
API_SECRET = API_SECRET

def main():
	client = Client(API_KEY, API_SECRET, testnet=True)

	response = client.get_exchange_info()
	print(client.response.headers)

if __name__ == "__main__":
	main()
