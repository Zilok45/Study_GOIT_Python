# def format_ingredients(items):
    
#     ingredients = ''
    
#     for item in items:
        
#         if len(items) == 1:
#             return item
        
#         lastElement = items[-1]
#         previesElement = items[-2]
        
#         if item == lastElement:
#             ingredients = ingredients + 'and' + ' ' + item
#         elif item == previesElement:
#             ingredients = ingredients + item + " "
#         else:
#             ingredients = ingredients + item + ", "  
        
    
#     return ingredients

# print(format_ingredients(["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]))    
# print(format_ingredients(["2 eggs", "1 liter sugar"]))    
# print(format_ingredients(["2 eggs", "1 liter sugar", "vinegar"]))    
# print(format_ingredients(["2 eggs"]))

def get_grade(key):
    
    grade = {"F": 1, "FX": 2, "E": 3, "D": 3, "C": 4, "B": 5, "A": 5}
    print(grade)
    return grade.get(key)

print(get_grade("F"))

def get_description(key):
    
    description = {"F": "Unsatisfactorily", "FX": "Unsatisfactorily", "E": "Enough", "D": "Satisfactorily", "C": "Good", "B": "Very good", "A": "Perfectly"}
       
    return description.get(key)
    
        
        
        
        
        
        
        
    
    