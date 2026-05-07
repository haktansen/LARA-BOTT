def test_filtering():
    cat_map = {
        "Aksiyon": ["action", "aksiyon", "adventure", "macera", "shooter", "nişancı"],
        "Strateji": ["strategy", "strateji", "puzzle", "bulmaca", "card game", "kart oyunu"],
        "RPG": ["rpg", "role-playing", "rol yapma", "simulation", "simülasyon"]
    }
    
    test_games = [
        {'title': 'Doom', 'category': 'Action', 'all_tags': ['action', 'shooter']},
        {'title': 'Return to Ash', 'category': 'Genel', 'all_tags': ['action', 'indie']},
        {'title': 'Civ VI', 'category': 'Strategy', 'all_tags': ['strategy', 'turn-based']},
        {'title': 'Stardew Valley', 'category': 'Simulation', 'all_tags': ['rpg', 'farming']},
    ]
    
    prefs = ["Aksiyon", "Strateji", "RPG", "Hepsi"]
    
    for pref in prefs:
        print(f"\n--- Testing preference: {pref} ---")
        required_tags = cat_map.get(pref, [])
        for game in test_games:
            match = False
            if pref == "Hepsi":
                match = True
            else:
                game_tags = game.get('all_tags', [])
                game_category = game.get('category', '').lower()
                if any(rt in game_category for rt in required_tags) or \
                   any(any(rt in tag for tag in game_tags) for rt in required_tags):
                    match = True
            print(f"Game: {game['title']}, Match: {match}")

if __name__ == "__main__":
    test_filtering()

