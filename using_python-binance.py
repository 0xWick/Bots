from binance.client import Client


API_KEY = "iq7rxbTcwRp2bQfPLSN7dkIupwT7Z7767gqAOR6kv6Gl8eM2r8ZNAl3jn1zNNpFC"
API_SECRET = "idzEA8ymid452YkRjxSY2HIlntcs5HJ094vQ4KqcxSTknHe4q6WSlmgbeg3Sae9i"

def main():
	client = Client(API_KEY, API_SECRET, testnet=True)

	response = client.get_exchange_info()
	print(client.response.headers)

if __name__ == "__main__":
	main()
