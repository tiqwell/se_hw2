from Recipe import Recipe
from main import Ingredient


class ShoppingList:
    def __init__(self):
        self._items = []
    def add_recipe(self, recipe : Recipe, portions : float):
        if portions <= 0:
            raise ValueError("Количество порций отрицательно")
        recipe_scale = recipe.scale(portions)
        for ingredient in recipe_scale.ingredients:
            self._items.append((ingredient, recipe.title))

    def remove_recipe(self, title : str):
        self._items = [item for item in self._items if item[1] != title]

    def get_list(self):
        a = {}
        for ingredient, title in self._items:
            key = (ingredient.name, ingredient.unit)
            if key in a:
                a[key] += ingredient.quantity
            else:
                a[key] = ingredient.quantity
        result = [Ingredient(name, quantity, unit) for (name, unit), quantity in a.items()]
        res_sort = sorted(result, key=lambda x: x.name)
        return res_sort

    def __add__(self, other):
        listN = ShoppingList()
        listN._items = self._items + other._items
        return listN