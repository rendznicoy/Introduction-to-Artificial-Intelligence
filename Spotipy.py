import random #Random Library
import sys #System Library

emotions = ["happy", "sad", "relaxed", "energetic", "calm"] #Emotions List / Dictionary

music_database = {
    "happy": ["Blinding Lights by The Weeknd: This song is a synth-pop track with a catchy melody and upbeat tempo. It's perfect for dancing or just listening to when you want to feel happy and carefree.", 
              "Dance Monkey by Tones and I: This song is an electropop earworm with a sing-along chorus. It's sure to get you moving and grooving.", 
              "Levitating by Dua Lipa: This song is a disco-pop track with a funky beat. It's perfect for a night out dancing or just vibing at home.", 
              "Bad Habits by Ed Sheeran: This song is a catchy pop-rock track with a positive message. It's about letting go of the past and moving on to better things.", 
              "Heat Waves by Glass Animals: This song is a psychedelic pop track with a dreamy sound. It's perfect for a late-night drive or just relaxing and reflecting.", 
              "Montero (Call Me by Your Name) by Lil Nas X: This song is a hip-hop track with a catchy melody and upbeat tempo. It's about self-love and acceptance, and it's sure to make you feel good about yourself.", 
              "Good 4 U by Olivia Rodrigo: This song is a pop-punk track with a catchy chorus and relatable lyrics about heartbreak. It's sure to make you feel all the feels.", 
              "Peaches by Justin Bieber, Daniel Caesar & Giveon: This song is a smooth R&B track with a catchy melody and laid-back vibe. It's perfect for a chill night in or a romantic moment.", 
              "Leave the Door Open by Bruno Mars, Anderson .Paak & Silk Sonic: This song is a smooth soul track with a catchy melody and funky beat. It's perfect for a night out dancing or just relaxing and enjoying the good vibes.", 
              "Happier by Olivia Rodrigo: This song is a pop ballad with a catchy melody and sad lyrics about heartbreak. It's sure to make you feel all the feels, but in a good way."],
    "sad": ["Drivers License by Olivia Rodrigo: This song is another pop ballad by Olivia Rodrigo, and it's just as sad and relatable as 'Happier'.",
            "Easy on Me by Adele: This song is a piano ballad with a beautiful melody and heartbreaking lyrics about a breakup.",
            "Just Like That by Willow: This song is a pop ballad with a catchy melody and sad lyrics about the end of a relationship.",
            "Butterfly Effect by BTS: This song is a pop ballad with a catchy melody and emotional lyrics about the pain of heartbreak.",
            "My Tears Ricochet by Taylor Swift: This song is a country-pop ballad with a beautiful melody and heartbreaking lyrics about a breakup.",
            "Hold My Hand by Lady Gaga: This song is a pop ballad with a catchy melody and emotional lyrics about hope and resilience.",
            "The Breakup Song by FINNEAS: This song is a pop ballad with a catchy melody and funny lyrics about a breakup.",
            "30 by Adele: This album is full of sad songs about heartbreak and loss. It's a great album to listen to if you're feeling down.",
            "Traitor by Olivia Rodrigo: This song is a pop-punk ballad with a catchy chorus and relatable lyrics about heartbreak.",
            "Enough for You by Conan Gray: This song is a pop ballad with a beautiful melody and sad lyrics about feeling like you're not good enough."],
    "relaxed": ["Perfect by Ed Sheeran: This song is a slow, acoustic ballad about finding the perfect love. The gentle melody and Sheeran's soothing vocals make it a great choice for relaxation.", 
                "Happier by Marshmello and Bastille: This song is about letting go of a relationship that is no longer working. The mellow electronic soundscape and Bastille's airy vocals create a sense of calm and acceptance.",
                "Everything I Wanted by Billie Eilish: This song is about anxiety and fear, but it also has a hopeful message. The dreamy production and Eilish's haunting vocals make it a beautiful and moving song to relax to.",
                "Break My Heart by Dua Lipa: This song is about heartbreak, but it also has a catchy melody and upbeat tempo. It's a great choice if you're looking for a song that will help you to feel your emotions but also relax.",
                "Easy on Me by Adele: This song is about letting go of a relationship and moving on. The slow, piano-driven ballad is sure to touch your heart and help you to relax.",
                "In My Blood by Shawn Mendes: This song is about anxiety and self-doubt, but it also has a message of hope. The soft guitar and Mendes's vulnerable vocals make it a great song to relax to when you're feeling stressed or overwhelmed.",
                "Someone You Loved by Lewis Capaldi: This song is about heartbreak and loss, but it is also a beautiful and moving ballad. The gentle piano and Capaldi's soulful vocals will touch your heart and help you to relax.",
                "Say Something by A Great Big World and Christina Aguilera: This song is about communication and the importance of saying what you mean. The soft piano and Aguilera's soaring vocals make it a great song to relax to when you're feeling lost or alone.",
                "Sunflower by Post Malone and Swae Lee: This song is about finding happiness in the simple things. The laid-back vibe and catchy melody make it a great song to relax to when you're feeling stressed or overwhelmed.",
                "Levitating by Dua Lipa: This song is about feeling free and letting go. The upbeat tempo and funky beat make it a great song to relax to when you're feeling down.",
                "Bad Habits by Ed Sheeran: This song is about breaking bad habits and moving on. The catchy melody and upbeat tempo make it a great song to dance to, but the lyrics are also meaningful and thought-provoking."],
    "energetic": ["Blinding Lights by The Weeknd: This song is about a person who is obsessed with someone they can't have. The pulsing beat and Weeknd's soulful vocals will make you want to get up and dance.", 
                  "Levitating by Dua Lipa: This song is about feeling free and letting go. The upbeat tempo and funky beat will make you want to move your body.",
                  "Bad Guy by Billie Eilish: This song is about a girl who is not afraid to be herself. The dark and moody production will make you feel powerful and confident.",
                  "Montero (Call Me by Your Name) by Lil Nas X: This song is about embracing your sexuality and being true to yourself. The catchy melody and Lil Nas X's confident vocals will make you want to dance and celebrate yourself.",
                  "Industry Baby by Lil Nas X and Jack Harlow: This song is about overcoming adversity and achieving your goals. The upbeat tempo and catchy lyrics will make you feel unstoppable.",
                  "Good 4 U by Olivia Rodrigo: This song is about moving on from a toxic relationship. The catchy melody and Rodrigo's defiant vocals will make you feel empowered and ready to take on the world.",
                  "Positions by Ariana Grande: This song is about a woman who is in control of her relationships. The catchy melody and Grande's sultry vocals will make you want to dance and feel confident.",
                  "Say So by Doja Cat: This song is about a woman who is not afraid to take what she wants. The funky beat and Doja Cat's playful vocals will make you want to move your body and have fun.",
                  "Dance Monkey by Tones and I: This song is about a woman who is irresistible on the dance floor. The catchy melody and Tones and I's unique vocals will make you want to get up and dance.",
                  "Uptown Funk by Mark Ronson featuring Bruno Mars: This song is a classic dance track that will get you moving. The funky beat and Bruno Mars's energetic vocals will make you want to dance all night long."],
    "calm": [ "Perfect by Ed Sheeran: This song is a slow, acoustic ballad about finding the perfect love. The gentle melody and Sheeran's soothing vocals make it a great choice for relaxation.", 
             "Happier by Marshmello and Bastille: This song is about letting go of a relationship that is no longer working. The mellow electronic soundscape and Bastille's airy vocals create a sense of calm and acceptance.",
             "Everything I Wanted by Billie Eilish: This song is about anxiety and fear, but it also has a hopeful message. The dreamy production and Eilish's haunting vocals make it a beautiful and moving song to relax to.",
             "Break My Heart by Dua Lipa: This song is about heartbreak, but it also has a catchy melody and upbeat tempo. It's a great choice if you're looking for a song that will help you to feel your emotions but also relax.",
             "Easy on Me by Adele: This song is about letting go of a relationship and moving on. The slow, piano-driven ballad is sure to touch your heart and help you to relax.",
             "Bad Habits by Ed Sheeran: This song is about breaking bad habits and moving on. The catchy melody and upbeat tempo make it a great song to dance to, but the lyrics are also meaningful and thought-provoking.",
             "Heat Waves by Glass Animals: This song is about nostalgia and longing for the past. The dreamy production and Glass Animals' unique sound create a sense of calm and introspection.",
             "Montero (Call Me by Your Name) by Lil Nas X: This song is about embracing your sexuality and being true to yourself. The catchy melody and Lil Nas X's confident vocals make it a great song to dance to and feel good about yourself.",
             "drivers license by Olivia Rodrigo: This song is about heartbreak and the pain of losing a loved one. The raw emotion in Rodrigo's vocals and the simple piano melody make it a powerful and moving song to listen to.",
             "Holy by Justin Bieber and Chance the Rapper: This song is about finding peace and happiness in a relationship. The gentle melody and Bieber's soothing vocals make it a great choice for relaxation."]
} #Music List / Dictionary

def recommend_music(user_emotion, music_database): #Define recommended music
    recommend_music = music_database.get(user_emotion, []) #Gets user emotion

    if recommend_music:
        if all(music.startswith("recommended:") for music in recommend_music): #Checks if the music is already recommended
            print("No more songs to recommend. Thank you for using Spotipy!")
            sys.exit()
        random.shuffle(recommend_music) #Randomly picks an item from the list of music
        selected_music = next(music for music in recommend_music if not music.startswith("recommended:")) #Finds the item without a mark
        recommend_music.remove(selected_music) #Marks item from the list as recommended
        recommend_music.append("recommended: " + selected_music) 

        print(f"Since you're {user_emotion} today, I recommend listining to:\n {selected_music} \n")
    else:
        print(f"No songs found for {user_emotion} emotion.")

print("Good Day Hooman! I'm Spotipy, your AI Music Recommendation Assistant :>\n I'm here to help you find your music based on the emotions that you feel right now.\n You can choose from the list of available emotions below.")

user_emotion = input("So, how are you feeling today? (happy, sad, relaxed, energetic, calm): ").lower()
print("\n")

while True:
    if user_emotion in emotions:
        recommend_music(user_emotion, music_database)
    else:
        print("Sorry, I don't have recommendations for that emotion as of now. Please choose any available emotions on the list.")

    user_decision = input("Would like another music suggestion? (Y, N): ").upper()
    if user_decision == "Y":
        continue
    elif user_decision == "N":
        print("Thank you for using Spotipy! Have a great day!")
        break
    else:
        print("Invalid Input. Please select 'Y' or 'N' to continue or exit the program")