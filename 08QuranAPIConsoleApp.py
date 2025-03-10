import requests
import json
import os
from playsound import playsound

# Base URL for the API
BASE_URL = "https://api.alquran.cloud/v1"

# Function to list all Surahs
def list_surahs():
    response = requests.get(f"{BASE_URL}/surah")
    if response.status_code == 200:
        surahs = response.json()['data']
        for surah in surahs:
            print(f"{surah['number']}. {surah['englishName']} ({surah['name']})")
    else:
        print("Error fetching Surahs.")

# Function to get Ayahs from a specific Surah
def get_surah(surah_number):
    response = requests.get(f"{BASE_URL}/surah/{surah_number}")
    if response.status_code == 200:
        ayahs = response.json()['data']['ayahs']
        for ayah in ayahs:
            print(f"{ayah['numberInSurah']}. {ayah['text']}")
    else:
        print("Invalid Surah number or API error.")

# Function to get translation of an Ayah
def get_translation(surah_number, ayah_number):
    response = requests.get(f"{BASE_URL}/ayah/{surah_number}:{ayah_number}/ur.maududi")
    if response.status_code == 200:
        translation = response.json()['data']['text']
        print(f"Translation: {translation}")
    else:
        print("Invalid Ayah or API error.")

# Function to play recitation of an Ayah
def play_recitation(surah_number, ayah_number):
    response = requests.get(f"{BASE_URL}/ayah/{surah_number}:{ayah_number}/ar.abdurrahmaansudais")
    if response.status_code == 200:
        audio_url = response.json()['data']['audio']
        print(f"Playing recitation: {audio_url}")
        playsound(audio_url)
    else:
        print("Error fetching recitation.")

# Main menu
def main():
    while True:
        print("\nQuran Console App")
        print("1. List Surahs")
        print("2. Get Surah Ayahs")
        print("3. Get Ayah Translation")
        print("4. Listen to Ayah Recitation")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_surahs()
        elif choice == "2":
            surah = input("Enter Surah number: ")
            get_surah(surah)
        elif choice == "3":
            surah = input("Enter Surah number: ")
            ayah = input("Enter Ayah number: ")
            get_translation(surah, ayah)
        elif choice == "4":
            surah = input("Enter Surah number: ")
            ayah = input("Enter Ayah number: ")
            play_recitation(surah, ayah)
        elif choice == "5":
            print("Exiting Quran Console App. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the app
if __name__ == "__main__":
    main()
