def format_ingredients(items):    
    ingredients = ''

    if len(items) < 2:
        return items[0] if items else '' # *items -  так працювати не буде

    for item in items[:-1]:
        ingredients += item + ", "
    ingredients = ingredients[:-2] + ' and ' + items[-1]
      
    return ingredients

print(format_ingredients(["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]))    
print(format_ingredients(["2 eggs", "1 liter sugar"]))    
print(format_ingredients(["2 eggs", "1 liter sugar", "vinegar"]))    
print(format_ingredients(["2 eggs"]))