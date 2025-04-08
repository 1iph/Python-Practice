import random

print("Music Recommender")
def recommend_music(genre):
    music_recommendations = {
        "pop": ["Sabrina Carpenter", "Harry Styles", "Ariana Grande"],
        "hip-hop": ["Drake", "Kendrick Lamar", "Eminem"],
        "rock": ["Queen", "Led Zepplin", "The Beatles"],
        "jazz": ["Moondance", "Carol King", "Billie Joel"],
        "classical": ["Bach", "Vivaldi", "Beethoven"]
    }
    
    return random.choice(music_recommendations.get(genre.lower(), []))
def main():
    genre = input("Enter your favorite music genre (pop, rock, jazz, classical): ")
    recommendation = recommend_music(genre)
    
    if recommendation:
        print(f"Recommended Sing/Band for you: {recommendation}")
    else:
        print("Sorry, we don't have recommendations for that genre.")
if __name__ == "__main__":
    main()