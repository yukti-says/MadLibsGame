# string concatenation(mean how to put string together)
# suppose we want to want to create a string that says "do your  _______" (task can be->homework,project completion,eating food etc)
# lets say 
# work="homework" #some string variable
# #few ways to do so(concatenate)
# print("do your " + work)
# print("do your {}".format(work))
# print(f"do your {work}")


# short cut for comment ctrl+/
# adj=input("Adjevtive: ")
# verb1=input("Verb: ")
# verb2=input("Verb: ")
# famous_person=input("Famous person: ")
# madlib=f"Computer programming is so {adj}! It makes me so excited all the time because  I love to {verb1}.Stay hydrated and {verb2} like you are {famous_person}!"

# print(madlib)

# import random

# story_templates = [
#     "Once upon a time in a {place}, there lived a {adjective} {animal} who loved to {verb}.",
#     "In a {adjective} world, a {noun} decided to {verb} every day.",
#     "The {noun} was so {adjective} that it could {verb} like no other.",
#     "Every {time_of_day}, the {animal} would {verb} in the {place}.",
#     "A {adjective} {noun} went on an adventure to {verb} in the {place}."
# ]

# def get_user_inputs():
#     inputs = {}
#     inputs['place'] = input("Enter a place: ")
#     inputs['adjective'] = input("Enter an adjective: ")
#     inputs['animal'] = input("Enter an animal: ")
#     inputs['verb'] = input("Enter a verb: ")
#     inputs['noun'] = input("Enter a noun: ")
#     inputs['time_of_day'] = input("Enter a time of day: ")
#     return inputs

# def create_mad_lib(inputs):
#     template = random.choice(story_templates)
#     mad_lib = template.format(**inputs)
#     return mad_lib

# def main():
#     print("Welcome to the Advanced Mad Libs Game!")
#     user_inputs = get_user_inputs()
#     mad_lib_story = create_mad_lib(user_inputs)
#     print("\nHere is your Mad Libs story:\n")
#     print(mad_lib_story)

# if __name__ == "__main__":
#     main()


#more advanced game
import random
import json
import os

# Predefined lists of words
nouns = ["dog", "car", "house", "cat", "computer"]
verbs = ["run", "jump", "swim", "dance", "sing"]
adjectives = ["happy", "sad", "angry", "excited", "bored"]
places = ["park", "beach", "city", "mountain", "forest"]
times_of_day = ["morning", "afternoon", "evening", "night"]

# Default story templates
default_templates = [
    "Once upon a time in a {place}, there lived a {adjective} {noun} who loved to {verb}.",
    "In a {adjective} world, a {noun} decided to {verb} every day.",
    "The {noun} was so {adjective} that it could {verb} like no other.",
    "Every {time_of_day}, the {noun} would {verb} in the {place}.",
    "A {adjective} {noun} went on an adventure to {verb} in the {place}."
]

TEMPLATES_FILE = "story_templates.json"
STORIES_FILE = "mad_libs_stories.txt"

def load_templates(filename):
    """Load story templates from a JSON file or return default templates."""
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return default_templates

def save_templates(filename, templates):
    """Save story templates to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(templates, file, indent=4)

def get_user_inputs():
    """Get user inputs for the story."""
    return {
        'place': input("Enter a place: "),
        'adjective': input("Enter an adjective: "),
        'noun': input("Enter a noun: "),
        'verb': input("Enter a verb: "),
        'time_of_day': input("Enter a time of day: ")
    }

def get_random_word(word_type):
    """Get a random word from predefined lists."""
    word_lists = {
        'noun': nouns,
        'verb': verbs,
        'adjective': adjectives,
        'place': places,
        'time_of_day': times_of_day
    }
    return random.choice(word_lists.get(word_type, [""]))

def create_mad_lib(template, inputs):
    """Create a Mad Libs story from user inputs and a template."""
    return template.format(**inputs)

def save_story(story):
    """Save the generated story to a file."""
    with open(STORIES_FILE, "a") as file:
        file.write(story + "\n\n")

def view_saved_stories():
    """View previously saved stories."""
    if os.path.exists(STORIES_FILE):
        with open(STORIES_FILE, "r") as file:
            stories = file.read()
            print("\nSaved Stories:\n")
            print(stories if stories else "No stories saved yet.")
    else:
        print("\nNo stories saved yet.")

def main():
    print("Welcome to the Enhanced Mad Libs Game!")
    
    # Load templates from file
    story_templates = load_templates(TEMPLATES_FILE)

    while True:
        print("\nMenu:")
        print("1. Create a new story")
        print("2. Add a new story template")
        print("3. View saved stories")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            print("You can either input your own words or use random words.")
            use_random = input("Use random words? (y/n): ").strip().lower() == 'y'
            
            if use_random:
                inputs = {key: get_random_word(key) for key in ['place', 'adjective', 'noun', 'verb', 'time_of_day']}
            else:
                inputs = get_user_inputs()

            template = random.choice(story_templates)
            mad_lib_story = create_mad_lib(template, inputs)

            print("\nHere is your Mad Libs story:\n")
            print(mad_lib_story)
            save_story(mad_lib_story)

        elif choice == '2':
            new_template = input("Enter a new story template (use placeholders like {noun}, {verb}, etc.): ")
            if new_template:
                story_templates.append(new_template)
                save_templates(TEMPLATES_FILE, story_templates)
                print("New template added successfully!")

        elif choice == '3':
            view_saved_stories()

        elif choice == '4':
            print("Thanks for playing! Goodbye.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
