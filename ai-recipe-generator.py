import streamlit as st
from typing import List

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
        "Fried Chicken",
        [Ingredient("chicken pieces"), Ingredient("flour"), Ingredient("spices"), Ingredient("garlic powder"), Ingredient("oil")],
        "1. Marinate chicken with spices and garlic powder.\n2. Coat chicken pieces in flour.\n3. Fry in hot oil until crispy."
    ),
    Recipe(
        "Methi Thepla",
        [Ingredient("fenugreek leaves"), Ingredient("flour"), Ingredient("yogurt"), Ingredient("spices"), Ingredient("oil")],
        "1. Make dough with fenugreek leaves, flour, yogurt, and spices.\n2. Roll out into flatbreads and cook on a griddle with a little oil."
    ),
    Recipe(
        "Sajji",
        [Ingredient("whole chicken"), Ingredient("spices"), Ingredient("yogurt"), Ingredient("garlic"), Ingredient("lemon")],
        "1. Marinate chicken with yogurt, spices, garlic, and lemon juice.\n2. Roast the whole chicken until tender."
    ),
    Recipe(
        "Dahi Ke Kebab",
        [Ingredient("yogurt"), Ingredient("paneer"), Ingredient("spices"), Ingredient("ginger"), Ingredient("cilantro")],
        "1. Mix yogurt, paneer, and spices.\n2. Shape into kebabs and cook on a grill or fry in a pan."
    ),
    Recipe(
        "Korma",
        [Ingredient("chicken"), Ingredient("onion"), Ingredient("yogurt"), Ingredient("spices"), Ingredient("garlic")],
        "1. Brown onions and garlic.\n2. Add chicken and spices.\n3. Cook with yogurt until tender."
    ),
    Recipe(
        "Peshawari Chapli Kebab",
        [Ingredient("minced beef"), Ingredient("onion"), Ingredient("tomato"), Ingredient("spices"), Ingredient("green chilies")],
        "1. Mix minced beef with onions, tomatoes, chilies, and spices.\n2. Shape into patties and fry."
    ),
    Recipe(
        "Lassi",
        [Ingredient("yogurt"), Ingredient("water"), Ingredient("sugar"), Ingredient("mint")],
        "1. Blend yogurt, water, sugar, and mint.\n2. Serve chilled."
    ),
    Recipe(
        "Palak Gosht",
        [Ingredient("mutton"), Ingredient("spinach"), Ingredient("onion"), Ingredient("garlic"), Ingredient("spices")],
        "1. Fry onions and garlic.\n2. Add mutton and cook until browned.\n3. Add spinach and spices, cook until tender."
    ),
    Recipe(
        "Bhel Puri",
        [Ingredient("puffed rice"), Ingredient("onion"), Ingredient("tomato"), Ingredient("coriander"), Ingredient("tamarind chutney")],
        "1. Mix puffed rice with chopped vegetables and coriander.\n2. Add tamarind chutney and spices."
    ),
    Recipe(
        "Shami Kebab",
        [Ingredient("minced meat"), Ingredient("lentils"), Ingredient("onion"), Ingredient("spices"), Ingredient("egg")],
        "1. Cook minced meat with lentils and spices.\n2. Grind into a smooth mixture, shape into patties, and fry."
    ),
    Recipe(
        "Tandoori Roti",
        [Ingredient("flour"), Ingredient("yeast"), Ingredient("water"), Ingredient("salt"), Ingredient("ghee")],
        "1. Make dough with yeast and flour.\n2. Roll into rotis and bake in a tandoor.\n3. Brush with ghee."
    ),
    Recipe(
        "Chicken Jalfrezi",
        [Ingredient("chicken"), Ingredient("bell peppers"), Ingredient("onion"), Ingredient("tomato"), Ingredient("spices")],
        "1. Stir-fry chicken with onions, bell peppers, and tomatoes.\n2. Add spices and cook until tender."
    ),
    Recipe(
        "Mutton Seekh Kebab",
        [Ingredient("minced mutton"), Ingredient("onions"), Ingredient("green chilies"), Ingredient("spices"), Ingredient("coriander")],
        "1. Mix minced mutton with onions, chilies, and spices.\n2. Shape into skewers and grill or fry."
    ),
    Recipe(
        "Gajar Ka Halwa",
        [Ingredient("carrots"), Ingredient("milk"), Ingredient("sugar"), Ingredient("ghee"), Ingredient("cardamom")],
        "1. Grate carrots and cook them in milk.\n2. Add sugar, ghee, and cardamom, cook until thick."
    ),
    Recipe(
        "Lemon Rice",
        [Ingredient("rice"), Ingredient("lemon"), Ingredient("mustard seeds"), Ingredient("curry leaves"), Ingredient("green chilies")],
        "1. Cook rice.\n2. Heat mustard seeds, curry leaves, and chilies.\n3. Add lemon juice to rice and mix."
    ),
    Recipe(
        "Chana Chaat",
        [Ingredient("chickpeas"), Ingredient("onion"), Ingredient("tomato"), Ingredient("cucumber"), Ingredient("spices")],
        "1. Boil chickpeas and mix with diced veggies.\n2. Add spices and lemon juice."
    ),
    Recipe(
        "Dahi Puri",
        [Ingredient("pani puri shells"), Ingredient("yogurt"), Ingredient("potatoes"), Ingredient("tamarind chutney"), Ingredient("spices")],
        "1. Fill puris with boiled potatoes.\n2. Add yogurt, tamarind chutney, and sprinkle with spices."
    ),
    Recipe(
        "Pista Kulfi",
        [Ingredient("milk"), Ingredient("sugar"), Ingredient("pistachios"), Ingredient("cardamom")],
        "1. Boil milk with sugar and cardamom until thick.\n2. Add crushed pistachios and freeze in molds."
    ),
    Recipe(
        "Chicken Malai Tikka",
        [Ingredient("chicken"), Ingredient("yogurt"), Ingredient("cream"), Ingredient("spices"), Ingredient("lemon juice")],
        "1. Marinate chicken with yogurt, cream, spices, and lemon juice.\n2. Grill the chicken until cooked."
    ),
    Recipe(
        "Fish Karahi",
        [Ingredient("fish"), Ingredient("onion"), Ingredient("tomato"), Ingredient("garlic"), Ingredient("green chilies")],
        "1. Fry onions and garlic in oil.\n2. Add fish and cook with tomatoes and spices."
    ),
    Recipe(
        "Chana Daal",
        [Ingredient("chana daal"), Ingredient("onion"), Ingredient("tomato"), Ingredient("spices"), Ingredient("garlic")],
        "1. Boil chana daal until tender.\n2. Fry onions and tomatoes with spices.\n3. Add to daal and cook for a few minutes."
    ),
    Recipe(
        "Methi Aloo",
        [Ingredient("potatoes"), Ingredient("fenugreek leaves"), Ingredient("onions"), Ingredient("spices")],
        "1. Fry onions until golden.\n2. Add potatoes and spices, cook until tender.\n3. Add fenugreek leaves and cook for a few more minutes."
    ),
    Recipe(
        "Samosa",
        [Ingredient("flour"), Ingredient("potatoes"), Ingredient("peas"), Ingredient("spices"), Ingredient("oil")],
        "1. Boil and mash potatoes and peas.\n2. Add spices and fill the mixture into rolled dough triangles.\n3. Deep fry until golden."
    ),
    Recipe(
        "Vegetable Biryani",
        [Ingredient("rice"), Ingredient("vegetables"), Ingredient("yogurt"), Ingredient("spices"), Ingredient("onion")],
        "1. Marinate vegetables with yogurt and spices.\n2. Layer rice, vegetables, and fried onions.\n3. Cook until rice is done."
    ),
    Recipe(
        "Kebabs",
        [Ingredient("minced meat"), Ingredient("onion"), Ingredient("spices"), Ingredient("garlic")],
        "1. Mix minced meat with spices and onions.\n2. Shape into skewers and grill or fry."
    ),
    Recipe(
        "Masala Chai",
        [Ingredient("tea leaves"), Ingredient("milk"), Ingredient("cardamom"), Ingredient("ginger"), Ingredient("sugar")],
        "1. Boil tea leaves, ginger, and cardamom in water.\n2. Add milk and sugar, simmer until it boils."
    ),
    Recipe(
        "Mutton Pulao",
        [Ingredient("mutton"), Ingredient("rice"), Ingredient("onion"), Ingredient("garlic"), Ingredient("spices")],
        "1. Brown mutton with onions and garlic.\n2. Add rice and spices, cook until rice is tender."
    ),
    Recipe(
        "Haleem",
        [Ingredient("wheat"), Ingredient("lentils"), Ingredient("chicken"), Ingredient("spices"), Ingredient("ghee")],
        "1. Cook wheat and lentils until soft.\n2. Blend the mixture and add cooked chicken.\n3. Simmer with spices and ghee."
    ),
    Recipe(
        "Aloo Keema",
        [Ingredient("minced meat"), Ingredient("potatoes"), Ingredient("onion"), Ingredient("tomato"), Ingredient("spices")],
        "1. Cook minced meat with onions, tomatoes, and spices.\n2. Add diced potatoes and cook until tender."
    ),
    Recipe(
        "Zarda",
        [Ingredient("rice"), Ingredient("sugar"), Ingredient("milk"), Ingredient("cardamom"), Ingredient("saffron")],
        "1. Cook rice with sugar, milk, and cardamom.\n2. Add saffron and garnish with nuts."
    ),
    Recipe(
        "Dahi Bhalla",
        [Ingredient("dal"), Ingredient("yogurt"), Ingredient("tamarind chutney"), Ingredient("spices"), Ingredient("cilantro")],
        "1. Soak dal vadas in water and top with yogurt.\n2. Add tamarind chutney and sprinkle spices."
    ),
    Recipe(
        "Pani Puri",
        [Ingredient("puri shells"), Ingredient("potatoes"), Ingredient("chickpeas"), Ingredient("spices"), Ingredient("tamarind chutney")],
        "1. Fill puris with chickpeas and potatoes.\n2. Pour tamarind chutney and top with spices."
    ),
    Recipe(
        "Shahi Malai",
        [Ingredient("milk"), Ingredient("sugar"), Ingredient("cardamom"), Ingredient("saffron"), Ingredient("ghee")],
        "1. Boil milk with sugar and cardamom.\n2. Garnish with saffron and ghee."
    ),
    Recipe(
        "Vegetable Samosa",
        [Ingredient("flour"), Ingredient("potatoes"), Ingredient("peas"), Ingredient("spices"), Ingredient("oil")],
        "1. Prepare dough and roll it out.\n2. Fill with a mixture of vegetables and spices.\n3. Fry until golden."
    ),
    Recipe(
        "Methi Paratha",
        [Ingredient("flour"), Ingredient("fenugreek leaves"), Ingredient("spices"), Ingredient("ghee")],
        "1. Make dough with fenugreek leaves, flour, and spices.\n2. Roll out into parathas and cook on a griddle with ghee."
    ),
    Recipe(
        "Mutton Karahi",
        [Ingredient("mutton"), Ingredient("onion"), Ingredient("tomato"), Ingredient("garlic"), Ingredient("spices")],
        "1. Fry onions and garlic in oil.\n2. Add mutton and cook until browned.\n3. Add tomatoes and spices, cook until tender."
    ),
    Recipe(
        "Pasta",
        [Ingredient("pasta"), Ingredient("tomato sauce"), Ingredient("chicken"), Ingredient("garlic"), Ingredient("cheese")],
        "1. Cook pasta.\n2. Stir-fry chicken with garlic and tomato sauce.\n3. Mix pasta with chicken and top with cheese."
    ),
    Recipe(
        "Chana Daal Tikki",
        [Ingredient("chana daal"), Ingredient("spices"), Ingredient("green chilies"), Ingredient("onions")],
        "1. Boil chana daal and mash it.\n2. Shape into patties and fry until golden brown."
    ),
    Recipe(
        "Fried Fish",
        [Ingredient("fish"), Ingredient("spices"), Ingredient("flour"), Ingredient("oil")],
        "1. Marinate fish with spices.\n2. Coat in flour and deep fry until crispy."
    ),
    Recipe(
        "Pasta Karahi",
        [Ingredient("pasta"), Ingredient("chicken"), Ingredient("tomato"), Ingredient("green chilies"), Ingredient("spices")],
        "1. Cook pasta.\n2. Cook chicken with tomatoes and spices.\n3. Toss pasta in the chicken mixture."
    ),
    Recipe(
        "Chana Masala",
        [Ingredient("chickpeas"), Ingredient("onion"), Ingredient("tomato"), Ingredient("garlic"), Ingredient("spices")],
        "1. Boil chickpeas until tender.\n2. Fry onions and tomatoes, add spices.\n3. Add chickpeas and cook together."
    ),
    Recipe(
        "Bengan Bharta",
        [Ingredient("eggplant"), Ingredient("onion"), Ingredient("tomato"), Ingredient("garlic"), Ingredient("spices")],
        "1. Roast eggplant until soft.\n2. Mash and cook with onions, tomatoes, garlic, and spices."
    ),
    Recipe(
        "Aloo Paratha",
        [Ingredient("flour"), Ingredient("potatoes"), Ingredient("spices"), Ingredient("ghee")],
        "1. Make dough and stuff with spiced mashed potatoes.\n2. Roll out into parathas and cook with ghee."
    ),
    Recipe(
        "Seekh Kebab",
        [Ingredient("minced meat"), Ingredient("onion"), Ingredient("green chilies"), Ingredient("spices"), Ingredient("cilantro")],
        "1. Mix minced meat with onions, spices, and chilies.\n2. Shape into skewers and grill."
    ),
    Recipe(
        "Cucumber Raita",
        [Ingredient("yogurt"), Ingredient("cucumber"), Ingredient("spices"), Ingredient("cilantro")],
        "1. Grate cucumber and mix with yogurt.\n2. Add spices and cilantro."
    ),
    Recipe(
        "Prawn Masala",
        [Ingredient("prawns"), Ingredient("onion"), Ingredient("tomato"), Ingredient("spices"), Ingredient("garlic")],
        "1. Fry onions and garlic in oil.\n2. Add prawns and cook until pink.\n3. Add tomatoes and spices, cook until done."
    ),
    Recipe(
        "Gulab Jamun",
        [Ingredient("milk powder"), Ingredient("flour"), Ingredient("sugar"), Ingredient("ghee"), Ingredient("rose water")],
        "1. Make dough with milk powder and flour.\n2. Shape into balls and fry in ghee.\n3. Soak in sugar syrup with rose water."
    ),
    Recipe(
        "Kacha Gola",
        [Ingredient("crushed ice"), Ingredient("syrup"), Ingredient("lemon juice"), Ingredient("salt")],
        "1. Shave ice and pack it in a cup.\n2. Pour flavored syrup and sprinkle with salt."
    ),

    Recipe(
        "Chana Chaat",
        [Ingredient("chickpeas"), Ingredient("onion"), Ingredient("tomato"), Ingredient("cucumber"), Ingredient("spices")],
        "1. Boil chickpeas and chop vegetables.\n2. Add spices and lemon juice.\n3. Mix well and serve."
    ),
    Recipe(
        "Samosa Chaat",
        [Ingredient("samosa"), Ingredient("yogurt"), Ingredient("chili chutney"), Ingredient("spices"), Ingredient("coriander")],
        "1. Crush samosas.\n2. Pour yogurt and chili chutney over it.\n3. Garnish with spices and coriander."
    ),
    Recipe(
        "Chicken Shawarma",
        [Ingredient("chicken"), Ingredient("yogurt"), Ingredient("garlic"), Ingredient("spices"), Ingredient("flatbread")],
        "1. Marinate chicken with yogurt, garlic, and spices.\n2. Grill chicken and slice thin.\n3. Serve in flatbread."
    ),
    Recipe(
        "Kheer",
        [Ingredient("milk"), Ingredient("rice"), Ingredient("sugar"), Ingredient("cardamom"), Ingredient("almonds")],
        "1. Boil rice in milk.\n2. Add sugar, cardamom, and cook until thick.\n3. Garnish with almonds."
    ),
    Recipe(
        "Chicken Pulao",
        [Ingredient("chicken"), Ingredient("rice"), Ingredient("onion"), Ingredient("garlic"), Ingredient("spices")],
        "1. Brown chicken with onions and garlic.\n2. Add rice and spices, cook until rice is done."
    ),
    Recipe(
        "Kacha Gosht",
        [Ingredient("mutton"), Ingredient("onions"), Ingredient("ginger"), Ingredient("garlic"), Ingredient("spices")],
        "1. Marinate mutton with spices.\n2. Cook in a sealed pot with onions, ginger, and garlic."
    ),
    Recipe(
        "Chana Daal",
        [Ingredient("chana daal"), Ingredient("onion"), Ingredient("tomato"), Ingredient("garlic"), Ingredient("spices")],
        "1. Boil chana daal until tender.\n2. Fry onions and tomatoes with spices.\n3. Add to daal and cook."
    ),
    Recipe(
        "Shahi Korma",
        [Ingredient("chicken"), Ingredient("yogurt"), Ingredient("cream"), Ingredient("spices"), Ingredient("onion")],
        "1. Brown onions and cook chicken.\n2. Add yogurt, cream, and spices, cook until thick."
    ),
    Recipe(
        "Egg Bhurji",
        [Ingredient("eggs"), Ingredient("onion"), Ingredient("green chilies"), Ingredient("tomato"), Ingredient("spices")],
        "1. Scramble eggs with onions, tomatoes, and chilies.\n2. Add spices and cook until done."
    ),
    Recipe(
        "Aloo Tikki",
        [Ingredient("potatoes"), Ingredient("onion"), Ingredient("spices"), Ingredient("green chilies"), Ingredient("oil")],
        "1. Boil and mash potatoes.\n2. Shape into patties with onions, chilies, and spices.\n3. Fry until golden."
    ),
    Recipe(
        "Mango Lassi",
        [Ingredient("mango"), Ingredient("yogurt"), Ingredient("milk"), Ingredient("sugar")],
        "1. Blend mango, yogurt, milk, and sugar.\n2. Serve chilled."
    ),
    Recipe(
        "Chicken Korma",
        [Ingredient("chicken"), Ingredient("yogurt"), Ingredient("spices"), Ingredient("onion"), Ingredient("garlic")],
        "1. Fry onions and garlic.\n2. Add chicken and spices, cook until browned.\n3. Add yogurt and simmer."
    ),
    Recipe(
        "Nihari",
        [Ingredient("mutton"), Ingredient("onion"), Ingredient("spices"), Ingredient("flour"), Ingredient("garlic")],
        "1. Cook mutton with onions, garlic, and spices.\n2. Thicken with flour and cook until tender."
    ),
    Recipe(
        "Masala Dosa",
        [Ingredient("rice flour"), Ingredient("potatoes"), Ingredient("onion"), Ingredient("spices"), Ingredient("oil")],
        "1. Make a dosa batter from rice flour.\n2. Cook a spiced potato filling.\n3. Serve dosa with filling."
    ),
    Recipe(
        "Gulab Jamun",
        [Ingredient("milk powder"), Ingredient("flour"), Ingredient("sugar"), Ingredient("ghee"), Ingredient("rose water")],
        "1. Make dough with milk powder and flour.\n2. Shape into balls and fry in ghee.\n3. Soak in sugar syrup with rose water."
    ),
    Recipe(
        "Haleem",
        [Ingredient("wheat"), Ingredient("lentils"), Ingredient("chicken"), Ingredient("spices"), Ingredient("ghee")],
        "1. Cook wheat and lentils until soft.\n2. Blend the mixture and add cooked chicken.\n3. Simmer with spices and ghee."
    ),
    Recipe(
        "Baked Chicken Wings",
        [Ingredient("chicken wings"), Ingredient("garlic powder"), Ingredient("paprika"), Ingredient("spices"), Ingredient("oil")],
        "1. Season chicken wings with garlic, paprika, and spices.\n2. Bake in the oven until crispy."
    ),
    Recipe(
        "Gajar Halwa",
        [Ingredient("carrots"), Ingredient("milk"), Ingredient("sugar"), Ingredient("ghee"), Ingredient("cardamom")],
        "1. Grate carrots and cook them in milk.\n2. Add sugar, ghee, and cardamom, cook until thick."
    ),
    Recipe(
        "Chana Masala",
        [Ingredient("chickpeas"), Ingredient("onion"), Ingredient("tomato"), Ingredient("garlic"), Ingredient("spices")],
        "1. Boil chickpeas until tender.\n2. Fry onions and tomatoes, add spices.\n3. Add chickpeas and cook together."
    ),
    Recipe(
        "Keema Paratha",
        [Ingredient("flour"), Ingredient("minced meat"), Ingredient("onion"), Ingredient("spices"), Ingredient("ghee")],
        "1. Cook minced meat with spices and onions.\n2. Stuff the mixture in paratha dough and cook with ghee."
    ),
    Recipe(
        "Biryani",
        [Ingredient("rice"), Ingredient("chicken"), Ingredient("yogurt"), Ingredient("spices"), Ingredient("onion")],
        "1. Marinate chicken with yogurt and spices.\n2. Fry onions until golden brown.\n3. Layer rice, chicken, and fried onions in a pot.\n4. Cook on low heat until rice is fully cooked."
    ),
    Recipe(
        "Kofta Curry",
        [Ingredient("minced meat"), Ingredient("onion"), Ingredient("spices"), Ingredient("garlic"), Ingredient("yogurt")],
        "1. Make meatballs with minced meat, onions, and spices.\n2. Fry meatballs and add to curry made from garlic, onions, and yogurt."
    ),
    Recipe(
        "Gosht Karahi",
        [Ingredient("mutton"), Ingredient("onion"), Ingredient("tomato"), Ingredient("green chilies"), Ingredient("spices")],
        "1. Fry onions and tomatoes.\n2. Add mutton and cook with spices.\n3. Simmer until tender."
    ),
    Recipe(
        "Aloo Keema",
        [Ingredient("minced meat"), Ingredient("potatoes"), Ingredient("onion"), Ingredient("tomato"), Ingredient("spices")],
        "1. Cook minced meat with onions, tomatoes, and spices.\n2. Add diced potatoes and cook until tender."
    ),
    Recipe(
        "Mutton Seekh Kebab",
        [Ingredient("minced mutton"), Ingredient("onions"), Ingredient("green chilies"), Ingredient("spices"), Ingredient("cilantro")],
        "1. Mix minced mutton with onions, chilies, and spices.\n2. Shape into skewers and grill or fry."
    ),
    Recipe(
        "Methi Paratha",
        [Ingredient("flour"), Ingredient("fenugreek leaves"), Ingredient("spices"), Ingredient("ghee")],
        "1. Make dough with fenugreek leaves and spices.\n2. Roll into parathas and cook on a griddle with ghee."
    ),
    Recipe(
        "Pista Kulfi",
        [Ingredient("milk"), Ingredient("sugar"), Ingredient("pistachios"), Ingredient("cardamom")],
        "1. Boil milk with sugar and cardamom until thick.\n2. Add crushed pistachios and freeze in molds."
    ),
    Recipe(
        "Chana Daal Tikki",
        [Ingredient("chana daal"), Ingredient("spices"), Ingredient("green chilies"), Ingredient("onions")],
        "1. Boil chana daal and mash it.\n2. Shape into patties and fry until golden brown."
    ),
    Recipe(
        "Pasta Karahi",
        [Ingredient("pasta"), Ingredient("chicken"), Ingredient("tomato"), Ingredient("green chilies"), Ingredient("spices")],
        "1. Cook pasta.\n2. Cook chicken with tomatoes and spices.\n3. Toss pasta in the chicken mixture."
    ),
    Recipe(
        "Dahi Bhalla",
        [Ingredient("dal"), Ingredient("yogurt"), Ingredient("tamarind chutney"), Ingredient("spices"), Ingredient("cilantro")],
        "1. Soak dal vadas in water and top with yogurt.\n2. Add tamarind chutney and sprinkle spices."
    ),
    Recipe(
        "Fried Fish",
        [Ingredient("fish"), Ingredient("spices"), Ingredient("flour"), Ingredient("oil")],
        "1. Marinate fish with spices.\n2. Coat in flour and deep fry until crispy."
    ),
    Recipe(
        "Tandoori Roti",
        [Ingredient("flour"), Ingredient("yeast"), Ingredient("water"), Ingredient("salt"), Ingredient("ghee")],
        "1. Make dough with yeast and flour.\n2. Roll into rotis and bake in a tandoor.\n3. Brush with ghee."
    ),
    Recipe(
        "Bhel Puri",
        [Ingredient("puffed rice"), Ingredient("onion"), Ingredient("tomato"), Ingredient("coriander"), Ingredient("tamarind chutney")],
        "1. Mix puffed rice with chopped vegetables and coriander.\n2. Add tamarind chutney and spices."
    ),
    Recipe(
        "Pulao",
        [Ingredient("rice"), Ingredient("meat"), Ingredient("onion"), Ingredient("spices")],
        "1. Brown meat and onion.\n2. Add rice and spices, cook until rice is tender."
    ),
    Recipe(
        "Chana Pulao",
        [Ingredient("rice"), Ingredient("chickpeas"), Ingredient("onion"), Ingredient("spices")],
        "1. Cook chickpeas with onions and spices.\n2. Add rice and cook until tender."
    ),
    Recipe(
        "Sajji",
        [Ingredient("whole chicken"), Ingredient("spices"), Ingredient("yogurt"), Ingredient("garlic"), Ingredient("lemon")],
        "1. Marinate chicken with yogurt, spices, garlic, and lemon juice.\n2. Roast the whole chicken until tender."
    ),
    Recipe(
        "Dahi Ke Kebab",
        [Ingredient("yogurt"), Ingredient("paneer"), Ingredient("spices"), Ingredient("ginger"), Ingredient("cilantro")],
        "1. Mix yogurt, paneer, and spices.\n2. Shape into kebabs and cook on a grill or fry in a pan."
    ),
    Recipe(
        "Lassi",
        [Ingredient("yogurt"), Ingredient("water"), Ingredient("sugar"), Ingredient("mint")],
        "1. Blend yogurt, water, sugar, and mint.\n2. Serve chilled."
    ),
]


# Streamlit Frontend
def main():
    # Apply custom styles for a refined UI
    st.markdown(
        """
        <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #007acc;
            color: white;
            border: none;
            border-radius: 20px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #005fa3;
        }
        .stTextInput>div>div>input {
            padding: 10px;
            border: 2px solid #007acc;
            border-radius: 15px;
            font-size: 14px;
        }
        .stHeader, .stSubheader {
            text-align: center;
        }
        .steps-title {
            color: red;
            font-size: 18px;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("🍽️ AI Recipe Maker | A Project by MindFlow Solutions 🌟")

    # Initialize recipes dataset
    recipes = initialize_recipes()
    engine = AIEngine(recipes)

    # User input for ingredients and recipe name
    st.header("Find Recipes by Ingredients or by Name")

    # Wrapping the inputs in a form
    with st.form(key="recipe_form"):
        st.markdown("#### Enter Ingredients")
        user_input_ingredients = st.text_input(
            "Ingredients (comma-separated):", placeholder="e.g., tomato, chicken, onion"
        )

        st.markdown("#### Enter Recipe Name (Optional)")
        user_input_recipe_name = st.text_input("Recipe Name:", placeholder="e.g., Biryani")

        # Add a submit button to trigger the form submission
        submit_button = st.form_submit_button(label="🔍 Get Recipe")

    # Handle form submission logic
    if submit_button:
        # Process the search logic
        ingredients = [Ingredient(ing.strip()) for ing in user_input_ingredients.split(",") if ing.strip()]
        recipe_name = user_input_recipe_name.strip()

        if recipe_name:  # Search by recipe name
            recipe = engine.get_recipe_by_name(recipe_name)
            if recipe:
                st.subheader(f"🍴 {recipe.name.title()} 🍴")
                st.markdown(f"**Ingredients:** {', '.join([ing.name for ing in recipe.ingredients])}")
                st.markdown('<div class="steps-title">Steps:</div>', unsafe_allow_html=True)
                for step in recipe.steps.split("\n"):
                    st.markdown(f"- {step}")
            else:
                st.error("❌ No recipe found with the given name.")
        elif ingredients:  # Search by ingredients
            suggested_recipes = engine.suggest_recipes(ingredients)
            if suggested_recipes:
                st.subheader("🍽️ Suggested Recipes:")
                for recipe in suggested_recipes:
                    st.markdown(f"### 🍲 {recipe.name.title()}")
                    st.markdown(f"**Ingredients:** {', '.join([ing.name for ing in recipe.ingredients])}")
                    st.markdown('<div class="steps-title">Steps:</div>', unsafe_allow_html=True)
                    for step in recipe.steps.split("\n"):
                        st.markdown(f"- {step}")
                    st.divider()
            else:
                st.error("❌ No recipes found for the given ingredients.")
        else:
            st.error("⚠️ Please enter at least one ingredient or a recipe name.")


if __name__ == "__main__":
    main()
