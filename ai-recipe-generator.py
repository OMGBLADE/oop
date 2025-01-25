import streamlit as st
from typing import List
import speech_recognition as sr

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
            "Haleem",
            [Ingredient("lentils"), Ingredient("wheat"), Ingredient("beef"), Ingredient("spices"), Ingredient("onion")],
            "1. Cook beef with lentils, wheat, and spices.\n2. Blend the mixture to a thick consistency.\n3. Fry onions and use as a garnish.\n4. Serve hot with naan and lemon."
        ),
        Recipe(
            "Pakoras",
            [Ingredient("chickpea flour"), Ingredient("potato"), Ingredient("onion"), Ingredient("spices"), Ingredient("green chili")],
            "1. Mix chickpea flour, spices, and water to form a batter.\n2. Dip potato and onion slices in the batter.\n3. Deep fry until golden brown.\n4. Serve with chutney."
        ),
        Recipe(
            "Chapli Kabab",
            [Ingredient("minced meat"), Ingredient("tomato"), Ingredient("onion"), Ingredient("spices"), Ingredient("egg")],
            "1. Mix minced meat with spices, onion, tomato, and egg.\n2. Shape into flat patties.\n3. Fry in oil until crispy.\n4. Serve hot with raita."
        ),
        Recipe(
            "Kheer",
            [Ingredient("milk"), Ingredient("rice"), Ingredient("sugar"), Ingredient("cardamom"), Ingredient("nuts")],
            "1. Boil milk and add rice.\n2. Cook until rice is soft and the mixture thickens.\n3. Add sugar and cardamom.\n4. Garnish with nuts and serve chilled."
        ),
        Recipe(
            "Samosa",
            [Ingredient("flour"), Ingredient("potato"), Ingredient("peas"), Ingredient("spices"), Ingredient("oil")],
            "1. Prepare dough with flour and water.\n2. Make a filling with boiled potatoes, peas, and spices.\n3. Shape dough into triangles, add filling, and seal.\n4. Deep fry until golden."
        ),
        Recipe(
            "Saag",
            [Ingredient("spinach"), Ingredient("mustard greens"), Ingredient("cornmeal"), Ingredient("spices"), Ingredient("butter")],
            "1. Cook spinach and mustard greens with spices.\n2. Blend to a smooth consistency.\n3. Add cornmeal to thicken.\n4. Serve with butter and makki ki roti."
        ),
        Recipe(
            "Aloo Paratha",
            [Ingredient("flour"), Ingredient("potato"), Ingredient("spices"), Ingredient("butter"), Ingredient("green chili")],
            "1. Prepare dough with flour and water.\n2. Make a spiced mashed potato filling.\n3. Roll dough, add filling, and seal.\n4. Cook on a griddle with butter."
        ),
        Recipe(
            "Gulab Jamun",
            [Ingredient("milk powder"), Ingredient("flour"), Ingredient("sugar"), Ingredient("cardamom"), Ingredient("oil")],
            "1. Make a dough with milk powder, flour, and water.\n2. Shape into small balls.\n3. Deep fry until golden brown.\n4. Soak in sugar syrup flavored with cardamom."
        ),
        Recipe(
            "Sheer Khurma",
            [Ingredient("milk"), Ingredient("vermicelli"), Ingredient("dates"), Ingredient("sugar"), Ingredient("nuts")],
            "1. Heat milk and add vermicelli.\n2. Cook until vermicelli softens.\n3. Add sugar, dates, and nuts.\n4. Serve warm."
        ),
        Recipe(
            "Payesh",
            [Ingredient("milk"), Ingredient("rice"), Ingredient("sugar"), Ingredient("cardamom"), Ingredient("nuts")],
            "1. Boil milk and add rice.\n2. Simmer until rice is cooked and the mixture thickens.\n3. Add sugar and cardamom.\n4. Garnish with nuts and serve chilled."
        ),
        Recipe(
            "Seekh Kabab",
            [Ingredient("minced meat"), Ingredient("spices"), Ingredient("onion"), Ingredient("ginger"), Ingredient("garlic")],
            "1. Mix minced meat with spices, onion, ginger, and garlic.\n2. Shape onto skewers.\n3. Grill or bake until cooked.\n4. Serve with chutney."
        ),
        Recipe(
            "Chicken Tikka",
            [Ingredient("chicken"), Ingredient("yogurt"), Ingredient("spices"), Ingredient("lemon"), Ingredient("oil")],
            "1. Marinate chicken pieces with yogurt, spices, and lemon.\n2. Grill or bake until cooked.\n3. Serve with naan and chutney."
        ),
        Recipe(
            "Chana Chaat",
            [Ingredient("chickpeas"), Ingredient("onion"), Ingredient("tomato"), Ingredient("spices"), Ingredient("lemon")],
            "1. Mix boiled chickpeas with chopped onion, tomato, and spices.\n2. Add lemon juice and mix well.\n3. Serve as a snack or side dish."
        ),
        Recipe(
            "Shami Kabab",
            [Ingredient("minced meat"), Ingredient("lentils"), Ingredient("onion"), Ingredient("spices"), Ingredient("egg")],
            "1. Cook minced meat with lentils and spices.\n2. Blend to a smooth mixture.\n3. Shape into patties and fry.\n4. Serve with chutney."
        ),
        Recipe(
            "Bhindi Masala",
            [Ingredient("okra"), Ingredient("onion"), Ingredient("tomato"), Ingredient("spices"), Ingredient("oil")],
            "1. Fry okra in oil and set aside.\n2. Cook onion and tomato with spices.\n3. Add fried okra and cook for a few minutes.\n4. Serve with roti."
        ),
        Recipe(
            "Keema Matar",
            [Ingredient("minced meat"), Ingredient("peas"), Ingredient("onion"), Ingredient("tomato"), Ingredient("spices")],
            "1. Cook minced meat with onion, tomato, and spices.\n2. Add peas and cook until tender.\n3. Serve with rice or roti."
        ),
        Recipe(
            "Halwa Puri",
            [Ingredient("semolina"), Ingredient("sugar"), Ingredient("flour"), Ingredient("oil"), Ingredient("spices")],
            "1. Make halwa by cooking semolina with sugar and water.\n2. Prepare dough for puris and roll into circles.\n3. Deep fry puris until golden.\n4. Serve hot with halwa."
        )
    ]

# Speech-to-Text Function
def recognize_speech() -> str:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Please speak now.")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            st.success(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            st.error("Sorry, could not understand the audio.")
        except sr.RequestError:
            st.error("Could not request results, please check your internet connection.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
        return ""

# Streamlit Frontend
def main():
    st.title("AI Recipe Maker")

    # Initialize recipes dataset
    recipes = initialize_recipes()
    engine = AIEngine(recipes)

    # User input for ingredients and recipe name
    st.header("Find Recipes by Ingredients or by There Names")
    user_input_ingredients = st.text_input("Enter ingredients (comma-separated):", "")
    user_input_recipe_name = st.text_input("Enter recipe name (optional):", "")

    # Speech recognition for ingredients
    if st.button("Use Microphone for Ingredients"):
        speech_input = recognize_speech()
        if speech_input:
            user_input_ingredients = speech_input

    # Speech recognition for recipe name
    if st.button("Use Microphone for Recipe Name"):
        speech_input = recognize_speech()
        if speech_input:
            user_input_recipe_name = speech_input

    if st.button("Get Recipes"):
        # Process user inputs
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

if __name__ == "__main__":
    main()
