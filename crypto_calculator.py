import requests

def get_crypto_price(crypto: str, currency: str = 'USD'):
    """Fetch the current price of a cryptocurrency in a given currency."""
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={currency}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data.get(crypto, {}).get(currency, None)
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

def main():
    print("Crypto Price Calculator")
    crypto = input("Enter the cryptocurrency (e.g., bitcoin, ethereum): ").lower()
    currency = input("Enter the fiat currency (default is USD): ").upper() or 'USD'

    price = get_crypto_price(crypto, currency)
    
    if price:
        print(f"The current price of {crypto.capitalize()} in {currency} is {price}.")
    else:
        print(f"Could not fetch the price for {crypto} in {currency}.")

if __name__ == "__main__":
    main()
