import requests

url = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=tr&country=TR&allowCountries=TR"
try:
    response = requests.get(url, timeout=10)
    data = response.json()
    elements = data['data']['Catalog']['searchStore']['elements']
    for game in elements:
        promotions = game.get('promotions')
        if not promotions or not (promotions.get('promotionalOffers')):
            continue
        
        offers = promotions.get('promotionalOffers', [{}])[0].get('promotionalOffers', [])
        for offer in offers:
            if offer.get('discountSetting', {}).get('discountPercentage') == 0:
                print(f"Title: {game['title']}")
                tags = [tag['name'] for tag in game.get('tags', [])]
                print(f"Tags: {tags}")
                print(f"End Date: {offer['endDate']}")
                print("-" * 20)
except Exception as e:
    print(f"Error: {e}")
