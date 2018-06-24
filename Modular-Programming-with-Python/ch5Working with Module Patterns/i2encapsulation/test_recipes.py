import recipes
recipe = recipes.new("Pizza Dough", num_servings=1)
recipes.add_ingredient(recipe, "Greek Yogurt", 1, "cup")
recipes.add_ingredient(recipe, "Self-Raising Flour", 1.5, "cups")
recipes.add_instruction(recipe, "Combine yogurt and 2/3 of the flour in a bowl \
    and mix with a beater until combined")
recipes.add_instruction(recipe, "Slowly add additional flour until it forms a stiff dough")
recipes.add_instruction(recipe, "Turn out onto a floured surface and knead until dough is tacky")
recipes.add_instruction(recipe, "Roll out into a circle of the desired thickness \
    and place on a greased and lined baking tray")

for s in recipes.to_string(recipe, num_servings=2):
    print(s)