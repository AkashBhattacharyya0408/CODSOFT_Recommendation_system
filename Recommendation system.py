import math

sample_data = {
    "movies": {
        "Action": {
            "User1": {"Mission Impossible": 5, "Avengers": 5, "Top gun:Maverick": 5, "Gladiator": 3, "John Wick": 5, "The working man": 4},
            "User2": {"Top gun:Maverick": 4, "Gladiator": 5,"The working man": 5, "John Wick": 3, "Mission Impossible": 4, "Avengers": 5},
            "User3": {"Gladiator": 3, "Top gun:Maverick": 4, "Mission Impossible": 5, "Avengers": 4, "The working man": 4, "John Wick": 4},
        },
        "Romance": {
            "User1": {"The Notebook": 4, "Titanic": 5, "The fault in our stars": 5, "My Fault": 4, "It ends with us": 4, "La La Land": 5},
            "User2": {"The fault in our stars": 5,"It ends with us": 4, "La La Land": 5, "My Fault": 4, "The Notebook": 4, "Titanic": 5 },
            "User3": {"It ends with us": 4, "La La Land": 5, "The Notebook": 4, "Titanic": 5, "The fault in our stars": 5, "My Fault": 4 },
        },
        "Horror": {
            "User1": {"The Conjuring": 4, "Anabelle": 5, "The Nun": 5, "Hereditary": 4, "The last exorcism": 4, "The grudge": 5},
            "User2": {"The Nun": 5, "Hereditary": 4,"The grudge": 5, "The last exorcism": 4, "The Conjuring": 4, "Anabelle": 5,},
            "User3": {"The last exorcism": 4, "The Conjuring": 4, "Anabelle": 5, "The grudge": 5, "The Nun": 5, "Hereditary": 4},
        },
    },
    "songs": {
        "Pop": {
            "User1": {"Blinding Lights": 5,"I want something like that": 5, "Hall of fame": 5, "Attention": 5, "Shape of You": 4, "See you Again": 4, "Levitating": 5, "Closer": 4, "Starboy": 5},
            "User2": {"See you Again": 4, "Levitating": 5,"I want something like that": 5, "Hall of fame": 5, "Attention": 5, "Starboy": 5, "Blinding Lights": 5, "Shape of You": 4, "Closer": 4},
            "User3": {"I want something like that": 5, "Hall of fame": 5, "Attention": 5, "Starboy": 5, "See you Again": 4, "Levitating": 5, "Closer": 4, "Blinding Lights": 5, "Shape of You": 4},
        },
        "Rock": {
            "User1": {"Numb": 5, "Dial tone": 5, "Obvious": 5, "Beggin": 4, "Like a rolling stone": 4, "Fight back": 5, "Believer": 5, "Thunder": 4, "Middle of the night": 4},
            "User2": {"Believer": 5, "Thunder": 4, "Middle of the night": 4, "Numb": 5, "Dial tone": 5, "Obvious": 5, "Beggin": 4, "Like a rolling stone": 4, "Fight back": 5},
            "User3": {"Beggin": 4, "Like a rolling stone": 4, "Fight back": 5, "Believer": 5, "Thunder": 4, "Middle of the night": 4, "Numb": 5, "Dial tone": 5, "Obvious": 5},
        },
    },
    "games": {
        "FPS": {
            "User1": {"Call of Duty": 5, "Overwatch": 4, "Counter Strike": 5, "Split Gate": 4, "Valorant": 5, "Far cry": 5, "Apex legends": 5, "Destiny": 4, "Metro Exodus": 4},
            "User2": {"Split Gate": 4, "Valorant": 5, "Far cry": 5, "Apex legends": 5, "Destiny": 4, "Metro Exodus": 4, "Call of Duty": 5, "Overwatch": 4, "Counter Strike": 5},
            "User3": {"Apex legends": 5, "Destiny": 4, "Metro Exodus": 4, "Call of Duty": 5, "Overwatch": 4, "Counter Strike": 5, "Split Gate": 4, "Valorant": 5, "Far cry": 5},
        },
        "Racing": {
            "User1": {"Need for speed": 5, "Forza Horizon": 5, "Asseto Corsa": 4, "Gran Turismo": 5, "Project cars": 4, "The crew": 4, "Le mans ultimate": 5, "MotoGP": 4, "Formula 1": 5},
            "User2": {"Gran Turismo": 5, "Project cars": 4, "Le mans ultimate": 5, "MotoGP": 4, "Formula 1": 5, "The crew": 4,"Need for speed": 5, "Forza Horizon": 5, "Asseto Corsa": 4},
            "User3": {"Le mans ultimate": 5, "MotoGP": 4, "Formula 1": 5, "Gran Turismo": 5, "Need for speed": 5, "Forza Horizon": 5, "Asseto Corsa": 4, "Project cars": 4, "The crew": 4},
        },
        "Story": {
            "User1": {"Black Myth:Wukong": 5, "GTA 5": 5, "Uncharted": 5, "God of War": 5, "Sekiro": 5, "Resident Evil": 5, "Assasin's Creed": 5, "The last of us": 5, "Red dead Redemption": 5},
            "User2": {"God of War": 5, "Sekiro": 5, "Resident Evil": 5, "Assasin's Creed": 5, "The last of us": 5, "Red dead Redemption": 5, "Black Myth:Wukong": 5, "GTA 5": 5, "Uncharted": 5},
            "User3": {"Assasin's Creed": 5, "The last of us": 5, "Black Myth:Wukong": 5, "GTA 5": 5, "Uncharted": 5, "Red dead Redemption": 5, "God of War": 5, "Sekiro": 5, "Resident Evil": 5},
        }
    }
}


def cosine_similarity(user1, user2):
    common_items = set(user1) & set(user2)
    if not common_items:
        return 0
    sum1 = sum(user1[item] ** 2 for item in common_items)
    sum2 = sum(user2[item] ** 2 for item in common_items)
    dot_product = sum(user1[item] * user2[item] for item in common_items)
    return dot_product / (math.sqrt(sum1) * math.sqrt(sum2))


def get_recommendations(user_input, category_data, top_n=3):
    scores = {}
    for other_user, ratings in category_data.items():
        sim = cosine_similarity(user_input, ratings)
        if sim <= 0:
            continue
        for item in ratings:
            if item not in user_input:
                scores.setdefault(item, 0)
                scores[item] += ratings[item] * sim
    sorted_recommendations = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [item for item, _ in sorted_recommendations[:top_n]]


def run_recommender():
    print("🎯 Welcome to the Multi-Category Recommendation System!")

    user_name = input("May I know your name please? ").strip().title()
    print(f"Nice to meet you, {user_name}!\n")

    while True:
        category = input("What would you like recommendations for (movies/songs/games)? ").strip().lower()
        if category not in sample_data:
            print("❌ Invalid category. Try again.")
            continue

        genres = list(sample_data[category].keys())
        print(f"\nAvailable genres in {category.capitalize()}: {', '.join(genres)}")

        genre_input = input("Enter your preferred genre: ").strip().lower()
        genre = next((g for g in genres if g.lower() == genre_input), None)

        if not genre:
            print("❌ Genre not available. Try again.")
            continue

        print(f"\nPlease rate the following {category[:-1]}s from 1 to 5 (or press Enter to skip):")
        sample_items = set()
        for ratings in sample_data[category][genre].values():
            sample_items.update(ratings.keys())

        user_ratings = {}
        for item in sorted(sample_items):
            rating = input(f"Your rating for '{item}': ")
            if rating.isdigit() and 1 <= int(rating) <= 5:
                user_ratings[item] = int(rating)

        if not user_ratings:
            print("⚠️ No ratings provided. Cannot generate recommendations.")
            return

        top_n = input("How many recommendations would you like to see? (default 3): ")
        try:
            top_n = int(top_n)
        except:
            top_n = 3

        recommendations = get_recommendations(user_ratings, sample_data[category][genre], top_n)

        print(f"\n✅ Top {category[:-1].capitalize()} Recommendations for {user_name}:")
        if recommendations:
            for rec in recommendations:
                print(f"- {rec}")
        else:
            print("No suitable recommendations found.")

        again = input("\nWould you like to try another category? (yes/no): ").strip().lower()
        if again != 'yes':
            print(f"👋 Thanks for using the recommender, {user_name}! Goodbye!")
            break


if __name__ == "__main__":
    run_recommender()
