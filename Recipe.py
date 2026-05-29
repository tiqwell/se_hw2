from main import Ingredient
class Recipe:
    def __init__(self, title, ingredients=None):
        self.title = title
        if ingredients != None:
            self.ingredients = ingredients
        else:
            ingredients = []

    def add_ingredient(self, ingredient):
        for item in self.ingredients:
            if item == ingredient:
                item.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        return (type(ratio) == int or type(ratio) == float) and ratio > 0

    def scale(self, ratio : float):
        if not self.is_valid_ratio(ratio):
            raise ValueError("кэф отрицательный")
        ing = []
        for item in self.ingredients:
            ing.append(Ingredient(item.name, item.quantity * ratio, item.unit))

        return Recipe(self.title, ing)

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        a = [f"Recipe: {self.title}"]
        for ing in self.ingredients:
            a.append(f"- {ing}")
        return "\n".join(a)