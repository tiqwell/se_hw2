from Recipe import Recipe


class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients=None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio):
        scaled = super().scale(ratio)
        return DietaryRecipe(scaled.title, self.diet_type, scaled.ingredients)

    def __str__(self):
        return f"[{self.diet_type}] {super().__str__()}"