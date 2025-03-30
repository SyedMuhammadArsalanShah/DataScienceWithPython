import requests
import json
import os
# from playsound import playsound

# Base URL for the API
BASE_URL ="https://hadithapi.com/api"
API_KEY = "$2y$10$BylaBcXs5Lw7ZOtYmQ3PXO1x15zpp26oc1FeGktdmF6YeYoRd88e"

# Function to list all Surahs
def list_hadiths_books():

    response = requests.get(f"{BASE_URL}/books?apiKey={API_KEY}")
    if response.status_code == 200:
        books = response.json()['books']
        for book in books:
            print(f"{book['bookName']}. {book['chapters_count']} ({book['hadiths_count']})")
    else:
        print("Error fetching Books")

# Function to get Ayahs from a specific Surah
def get_chapters(bookslug):
    response = requests.get(f"{BASE_URL}/{bookslug}/chapters?apiKey={API_KEY}")
    if response.status_code == 200:
        chapters = response.json()['chapters']
        for chapter in chapters:
            print(f"{chapter['chapterNumber']}. {chapter['chapterArabic']}. {chapter['chapterUrdu']}")
    else:
        print("Invalid Surah number or API error.")


# Function to get Ayahs from a specific Surah
def get_hadiths(bookslug, chapter):
    response = requests.get(f"{BASE_URL}/hadiths?apiKey={API_KEY}&book={bookslug}&chapter={chapter}&paginate=100000")
    if response.status_code == 200:
        hadiths = response.json()["hadiths"]['data']
        for hadith in hadiths:
            print(f"{hadith['hadithNumber']}. {hadith['hadithUrdu']}. {hadith['hadithEnglish']}")
    else:
        print("Invalid Surah number or API error.")




# Main menu
def main():
    while True:
        print("\nQuran Console App")
        print("1. List Books")
        print("2. Get  Chapters Of Hadith")
        print("3. Get  Hadith")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_hadiths_books()
        elif choice == "2":
            chapter = input("Enter Chapter number: ")
            get_chapters(chapter)
        elif choice == "3":
            book = input("Enter BookSlug: ")
            chapter = input("Enter Chapter number: ")
            get_hadiths(bookslug=book,chapter=chapter)
        elif choice == "4":
            print("Exiting Hadith Console App. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the app
if __name__ == "__main__":
    main()
