def describe_city(city, country='dehli'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('islamabad')
describe_city('dehli', 'toronto')
describe_city('mumbai')