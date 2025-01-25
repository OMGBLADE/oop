import streamlit as st
from typing import List
import sounddevice as sd
import vosk
import numpy as np
import json

# Define OOP Classes
class Ingredient:
    def __init__(self, name: str):
        self.name = name.strip().lower()  # Normalize ingredient name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Ingredient):
            return self.name == other.name
        return False

class Recipe:
    def __init__(self, name: str, ingredients: List[Ingredient], steps: str):
        self.name = name.strip().lower()
        self.ingredients = ingredients
        self.steps = steps

    def matches_ingredients(self, available_ingredients: List[Ingredient]) -> bool:
        return any(ingredient in available_ingredients for ingredient in self.ingredients)

    def __repr__(self):
        return f"{self.name}: Ingredients: {[ing.name for ing in self.ingredients]}, Steps: {self.steps}"

class AIEngine:
    def __init__(self, recipes: List[Recipe]):
        self.recipes = recipes

    def suggest_recipes(self, available_ingredients: List[Ingredient]) -> List[Recipe]:
        return [recipe for recipe in self.recipes if recipe.matches_ingredients(available_ingredients)]

    def get_recipe_by_name(self, recipe_name: str) -> Recipe:
        recipe_name = recipe_name.strip().lower()
        for recipe in self.recipes:
            if recipe.name == recipe_name:
                return recipe
        return None

# Initialize Recipes Dataset
def initialize_recipes() -> List[Recipe]:
    return [
        Recipe(
            "Biryani",
            [Ingredient("rice"), Ingredient("chicken"), Ingredient("yogurt"), Ingredient("spices"), Ingredient("onion")],
            "1. Marinate chicken with yogurt and spices.\n2. Fry onions until golden brown.\n3. Layer rice, chicken, and fried onions in a pot.\n4. Cook on low heat until rice is fully cooked."
        ),
        Recipe(
            "Chicken Karahi",
            [Ingredient("chicken"), Ingredient("tomato"), Ingredient("ginger"), Ingredient("garlic"), Ingredient("spices")],
            "1. Heat oil in a wok and add garlic and ginger paste.\n2. Add chicken and cook until golden.\n3. Add chopped tomatoes and spices, and cook until oil separates.\n4. Garnish with fresh coriander and serve hot."
        ),
        Recipe(
            "Nihari",
            [Ingredient("beef"), Ingredient("wheat flour"), Ingredient("spices"), Ingredient("ginger"), Ingredient("onion")],
            "1. Cook beef with ginger, garlic, and spices.\n2. Prepare a flour-based gravy and add it to the meat.\n3. Simmer for several hours.\n4. Garnish with ginger slices and serve with naan."
        ),
        Recipe(
            "Pasta Carbonara",
            [Ingredient("pasta"), Ingredient("egg"), Ingredient("cheese"), Ingredient("bacon"), Ingredient("garlic")],
            "1. Boil pasta in salted water.\n2. Fry bacon and garlic in a pan until crispy.\n3. In a bowl, whisk eggs and cheese together.\n4. Combine pasta with bacon, then mix in egg mixture to create a creamy sauce."
        ),
        Recipe(
            "Caesar Salad",
            [Ingredient("romaine lettuce"), Ingredient("croutons"), Ingredient("parmesan cheese"), Ingredient("caesar dressing")],
            "1. Tear romaine lettuce into pieces.\n2. Add croutons, parmesan cheese, and Caesar dressing.\n3. Toss well and serve chilled."
        ),
        Recipe(
            "Mashed Potatoes",
            [Ingredient("potatoes"), Ingredient("butter"), Ingredient("milk"), Ingredient("salt"), Ingredient("pepper")],
            "1. Boil potatoes until tender.\n2. Mash them with butter and milk until smooth.\n3. Season with salt and pepper, and serve hot."
        ),
        Recipe(
            "Veggie Stir Fry",
            [Ingredient("bell pepper"), Ingredient("broccoli"), Ingredient("carrot"), Ingredient("soy sauce"), Ingredient("garlic")],
            "1. Stir fry vegetables in a hot pan with garlic.\n2. Add soy sauce and cook for a few more minutes.\n3. Serve with rice."
        ),
        Recipe(
            "Pancakes",
            [Ingredient("flour"), Ingredient("egg"), Ingredient("milk"), Ingredient("butter"), Ingredient("maple syrup")],
            "1. Mix flour, egg, milk, and butter to make the batter.\n2. Cook pancakes on a hot griddle.\n3. Serve with maple syrup."
        ),
        Recipe(
            "Fried Rice",
            [Ingredient("rice"), Ingredient("egg"), Ingredient("peas"), Ingredient("soy sauce"), Ingredient("carrot")],
            "1. Stir fry rice with peas, carrots, and soy sauce.\n2. Scramble eggs in a separate pan and add to the rice.\n3. Serve hot."
        ),
        Recipe(
            "Chicken Tikka Masala",
            [Ingredient("chicken"), Ingredient("yogurt"), Ingredient("tomato"), Ingredient("cream"), Ingredient("spices")],
            "1. Marinate chicken with yogurt and spices.\n2. Grill or cook the chicken.\n3. Prepare a creamy tomato sauce and add the chicken.\n4. Serve with naan or rice."
        ),
        # Add more recipes as needed
    ]

# Recognize speech using Vosk
def recognize_speech_vosk() -> str:
    model = vosk.Model(".\vosk-model-small-en-us-0.15")  # Path to the Vosk model
    samplerate = 16000
    rec = vosk.KaldiRecognizer(model, samplerate)

    # Record audio for 5 seconds
    with sd.InputStream(channels=1, dtype='int16', samplerate=samplerate) as stream:
        st.info("Listening... Please speak now.")
        audio_data = []
        
        for _ in range(0, int(samplerate / 1024 * 5)):  # Record for 5 seconds
            audio_chunk, overflowed = stream.read(1024)  # Read audio in chunks
            audio_data.append(audio_chunk)
            if rec.AcceptWaveform(audio_chunk):  # Check if speech is recognized
                break

        # Combine audio chunks into one array
        audio_array = np.concatenate(audio_data, axis=0)

        # Recognize speech using Vosk model
        if rec.AcceptWaveform(audio_array):
            result = rec.Result()
            result_json = json.loads(result)
            return result_json.get('text', '')
        else:
            st.error("Could not recognize the speech.")
            return ""

# Streamlit Frontend
def main():
    st.title("AI Recipe Maker | A Project by MindFlow Solution")

    # Initialize recipes dataset
    recipes = initialize_recipes()
    engine = AIEngine(recipes)

    # User input for ingredients and recipe name
    st.header("Find Recipes by Ingredients or by Name")
    
    # Wrapping the inputs in a form
    with st.form(key='recipe_form'):
        user_input_ingredients = st.text_input("Enter ingredients (comma-separated):", "")
        user_input_recipe_name = st.text_input("Enter recipe name (optional):", "")
        
        # Add a submit button to trigger the form submission
        submit_button = st.form_submit_button(label='Get Recipe')

    # Check if the form was submitted
    if submit_button:
        # Function to process the search logic when text input is entered
        ingredients = [Ingredient(ing) for ing in user_input_ingredients.split(",") if ing.strip()]
        recipe_name = user_input_recipe_name.strip()

        if recipe_name:  # Search by recipe name
            recipe = engine.get_recipe_by_name(recipe_name)
            if recipe:
                st.subheader(f"Recipe Found: {recipe.name.title()}")
                st.text(f"Ingredients: {[ing.name for ing in recipe.ingredients]}")
                st.text(f"Steps: {recipe.steps}")
            else:
                st.error("No recipe found with the given name.")
        elif ingredients:  # Search by ingredients
            suggested_recipes = engine.suggest_recipes(ingredients)
            if suggested_recipes:
                st.subheader("Suggested Recipes:")
                for recipe in suggested_recipes:
                    st.text(f"- {recipe.name.title()}\n  Ingredients: {[ing.name for ing in recipe.ingredients]}\n  Steps: {recipe.steps}\n")
            else:
                st.error("No recipes found for the given ingredients.")
        else:
            st.error("Please enter at least one ingredient or a recipe name.")

    # Speech recognition buttons
    if st.button("Use Microphone for Ingredients"):
        speech_input = recognize_speech_vosk()
        if speech_input:
            user_input_ingredients = speech_input
            st.success(f"Recognized Ingredients: {user_input_ingredients}")

    if st.button("Use Microphone for Recipe Name"):
        speech_input = recognize_speech_vosk()
        if speech_input:
            user_input_recipe_name = speech_input
            st.success(f"Recognized Recipe Name: {user_input_recipe_name}")

if __name__ == "__main__":
    main()
