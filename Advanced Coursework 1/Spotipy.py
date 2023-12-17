import random #Random Library
import sys #System Library
import json #To access the json file
from difflib import get_close_matches
import os

recommended_songs = []

def loadEmotions(filePath: str) -> list:
    try:
        with open(filePath, 'r') as file:
            data: dict = json.load(file)
            return data.get("emotions", [])
    except (FileNotFoundError, json.JSONDecodeError):
        # If file does not exist, return empty
        return []

def loadMusic(filePath: str) -> dict:
    try:
        with open(filePath, 'r') as file:
            data: dict = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    
def saveEmotion(filePath: str, emotions: list):
    with open(filePath, 'w') as file:
        json.dump({"emotions": emotions}, file, indent=2)
    
def saveMusic(filePath:str, data: dict):
    with open(filePath, 'w') as file:
        json.dump(data, file, indent=2)

def recommend_music(user_emotion: str, emotions: list) -> str|None:
    matches: list = get_close_matches(user_emotion, emotions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def discover(user_emotion: str, emotions_file_path: str, music_database_file_path: str):
    emotion_list = loadEmotions(emotions_file_path)

    if user_emotion not in emotion_list:
        emotion_list.append(user_emotion)
        saveEmotion(emotions_file_path, emotion_list)

        fresh_discovery: str = input(f'Enter new music that fits with your emotion right now or type "pass" if nothing comes to mind\n{user_emotion}: ')

        if fresh_discovery.upper() != 'PASS':
            # Load existing music database
            music_database = loadMusic(music_database_file_path)
            # Update the music database with the new discovery
            if user_emotion in music_database:
                music_database[user_emotion].append(fresh_discovery)
            else:
                music_database[user_emotion] = [fresh_discovery]
            saveMusic(music_database_file_path, music_database)
            print("Thank you for your recommendation!")
    # Load the music database after potential updates
    music_database = loadMusic(music_database_file_path)

    # Randomizer
    songs_for_emotion = music_database.get(user_emotion, [])

    if songs_for_emotion:
        # Filter out songs that have already been recommended
        unrecommended_songs = [song for song in songs_for_emotion if song not in recommended_songs]
        
        if unrecommended_songs:
            recommend_song = random.choice(unrecommended_songs)
            recommended_songs.append(recommend_song)
            return [recommend_song]
    
    # If no unrecommended songs are left, ask the user for recommendations
    print(f'Sorry, ran out of music recommendation for {user_emotion}.')
    more_suggestions = input(f'Please recommend a music for {user_emotion} (Type "pass" if nothing comes to mind): ')
    if more_suggestions.upper() != 'PASS':
        music_database.setdefault(user_emotion, []).append(more_suggestions)
        saveMusic(music_database_file_path, music_database)
        print("Thank you for your recommendation!")

    return []


def runProgram():
    current_directory = os.path.dirname(os.path.abspath(__file__))

    emotions_file_path = os.path.join(current_directory, 'emotionList.json')
    emotion_list = loadEmotions(emotions_file_path)

    music_database_file_path = os.path.join(current_directory, 'musicList.json')
    music_database = loadMusic(music_database_file_path)

    while True:
        user_emotion: str = input("How are you feeling today? (happy, sad, relaxed, energetic, calm, angry, etc.): ").lower()

        while True:
            response: list = discover(user_emotion, emotions_file_path, music_database_file_path)

            if response:
                print(f'Recommended songs for {user_emotion}: ')
                for song in response:
                    print(song)

            # Check if there are more songs to recommend or if the user recommended a song
            if not response or input("Would you like another music suggestion? (Y, N): ").upper() != 'Y':
                break

        run_again = input("Would you like to run the program again? (Y, N): ")
        if run_again.upper() != 'Y':
            print('Thank you for using Spotipy! Have a great day!')
            break

if __name__ == '__main__':
    runProgram()