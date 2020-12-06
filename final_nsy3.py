# Reciepe Recommender
import webbrowser
lasagne_recipe = {'name':'lasagne_recipe','ingredients': ['bellpeper', 'zucchini', 'carrots','ricotta cheese', 'meat', 'lasagne sheet','Mozerella'],
                        'cooking_time': 30,
                        'allergies': '[cream]',
                        'rating': 4,
                        'type': ['vegetarian'],
                        'category': ['main_dish'] ,
                        'Calories': 306,
                        'link':'https://cookieandkate.com/best-vegetable-lasagna-recipe/'}

Green_bean_casrole = {'name':'Green_bean_casrole','ingredients': ['green beans', 'Butter', 'Flour','Onion powder', 'Garlic powder', 'Heavy cream', 'Nutmeg','Dijon','Veggie or chicken stock'],
                        'cooking_time': 20,
                        'allergies': ['nutmeg'],
                        'rating': 3,
                        'type': ["vegan","vegetarian"],
                        'category': ['salad'] ,
                        'Calories': 182,
                        'link':'https://cookieandkate.com/homemade-green-bean-casserole/'}
mushroom_soup = {'name':'mushroom_soup','ingredients':["mashrooms","garlic","onion","flour","milk","vegetable broth","olive oil","pepper","salt","light soyas auce"],
'cooking_time':25,
'rating':4,
'type': ["vegan","vegetarian"],
'category':["soup"],
'allergies':["milk"],
'link':'https://www.bbcgoodfood.com/recipes/mushroom-soup'}

lentil_soup={'name':'lentil_soup','ingredients':["lentil","carrots","onion","chicken broth","tomatoes",],
'cooking_time':20.0,
'type': ['vegan'],
'rating':3,
'category':["soup"],
'allergies':["lentil"],
'link':'https://cookieandkate.com/best-lentil-soup-recipe/'}

tomato_basil_soup = {'name':'tomato_basil_soup','ingredients': ['Canned tomatoes', 'Sweet potatoes', 'Onion','Fresh basil', 'olive oil', ' salt','pepper'],
                        'cooking_time': 28,
                        'allergies': [ ],
                        'type': ["vegan","vegetarian"],
                        'rating': 4,
                        'category': ['soup'] ,
                        'Calories': 244,
                        'link':'https://theclevermeal.com/tomato-soup/'}

chicken_recipe = {'name':'chicken_recipe','ingredients': ['chicken', 'yogurt',' butter', 'Onion','coriander','ginger', 'garlic','basil', 'oil', 'salt','pepper'],
                        'cooking_time': 28,
                        'allergies': [ ],
                        'type': ['non_vegetarian'],
                        'rating': 4,
                        'category': ['main_dish'] ,
                        'Calories': 244,
                        'link':'https://www.foodundco.de/indisches-butter-chicken-curry/'}
fajitas = {'name':'fajitas','ingredients':['black beans', 'avocado' ,'pepers'],
           'allergies':['black beans'],
        'cooking_time': 15.0,
        'rating':3,
        'type':['vegetarian'],
        'category':['main_dish'],
        'calories':100,
        'link':'www.bbcgoodfood.com'}
chinese_pancakes= {'name':'chinese_pancakes','ingredients':['mashrooms', 'soja sauce', 'sesame oil', 'sugar', 'chinese pancakes', 'cucumber' ,'hoisin sauce'],
    'allergies':['sugar'], 'cooking_time': 28,
    'rating':5,
    'type': ['vegetarian'],
    'category' :['snack'],
    'calories':150,
    'link':'www.bbcgoodfood.com'}
roast_pumpkin_salade = {'name':'roast_pumpkin_salade','ingredients':['roast pumpkin', 'chick pea', 'kale', 'corrinder'],
    'allergies':[ ],
    'cooking_time':7.0,
    'rating':3 ,
    'type':['vegeatrian'],
    'category':['salad'],
    'calories':110,
    'link':'www.olivemagasin.com'}
choco_banane_ice_cream = {'name':'choco_banane_ice_cream','ingredients':['cocoa powder', 'banane'],
    'allergies':['banane'],
    'cooking_time' :6.0,
    'rating':4,
    'type':['vegetarian'],
    'category':['dessert'],
    'calories':70,
    'link':'www.olivemagasin.com'}
pesto_pizza = {'name':'pesto_pizza', 'ingredients':['pesto', 'wheat pizza crust', 'spinach', 'tomato' , 'mozzrella' ,'feta cheese'],
    'allergies':['banane'],
    'cooking_time' :6.0,
    'rating':4,
    'type':['vegetarian'],
    'category':['dessert'],
    'calories':70,
    'link':'www.olivemagasin.com'}
Grilled_Lemon_Chicken = {'name':'Grilled_Lemon_Chicken','ingredients': ['chicken', 'parsley', ' lemon juice','oregano', 'olive oil', ' salt','pepper'],
                        'cooking_time': 30,
                        'allergies': [ ],
                        'type': ['non_vegetarian'],
                        'rating': 5,
                        'category': ['main_dish'] ,
                        'Calories': 216,
                        'link':'https://feelgoodfoodie.net/recipe/grilled-lemon-chicken/'}
tandoori_Fish = {'name':'tandoori_Fish','ingredients':['salmon fish', 'yogurt' ,'oil','gram flour'],
                 'cooking_time' :30,
                 'allergies':['ginger'],
                 'type':['non_vegetarian'],
                 'rating': 4,
                 'category': ['main_dish'] ,
                 'Calories': 200,
                 'link':'https://recipes.timesofindia.com/recipes/tandoori-fish/rs54669275.cms'}
mutton_recipe = {'name':'mutton_recipe','ingredients':['mutton',' Onion', 'yogurt' ,'garlic','ginger','fenugreek_seed '],
                         'cooking_time':75,
                        'allergies': ['fenugreek_seed'],
                        'type': ['non_vegetarian'],
                        'rating': 4,
                        'category': ['main_dish'] ,
                        'Calories': 433,
                        'link':'https://recipes.timesofindia.com/recipes//mutton-do-pyaza/rs75550345.cms'}
Lahmacun = {'name':'Lahmacun','ingredients': ['lamb', 'pepper', 'shallot','tomato paste', 'olive oil', ' paprika','pepper'],
                        'cooking_time': 25,
                        'allergies': [ ],
                        'type': ['non_vegetarian'],
                        'rating': 5,
                        'category': ['main_dish'] ,
                        'Calories': 244,
                        'link':'https://www.themediterraneandish.com/easy-turkish-lahmacun-recipe/'}
Honey_Garlic_Chicken = {'name':'Honey_Garlic_Chicken','ingredients': ['chicken', 'honey’, ‘soy sauce', 'rice wine vinegar','garlic', 'olive oil', ' salt','pepper'],
                        'cooking_time': 30,
                        'allergies':['honey'],
                        'type': ['non_vegetarian'],
                        'rating': 5,
                        'category': ['main_dish'] ,
                        'Calories': 384,
                        'link':'https://cafedelites.com/easy-honey-garlic-chicken/'}
hummus_recipe= {'name':'hummus_recipe','ingredients': ['chickpeas', 'tahini’, ‘baking soda', 'lemon juice’,’garlic', 'paprika', 'olive oil', ' salt','pepper'],
                        'cooking_time': 30,
                        'allergies': [ ],
                        'type': ['vegetarian'],
                        'rating': 4,
                        'category': ['snack'] ,
                        'Calories': 254,
                        'link':'https://cafedelites.com/best-hummus-recipe/'}
falafel_recipe = {'name':'falafel_recipe','ingredients': ['chickpeas', 'parsley', 'onion','flour, ''olive oil', ' Sesame seeds'],
                        'cooking_time': 4,
                        'allergies':['chickpeas’'],
                        'type': ['vegetarian'],
                        'rating': 5,
                        'category': ['main_dish'],
                        'Calories': 149,
                        'link':'https://feelgoodfoodie.net/ecipe/falafel/'}
potato_cutlet_recipe = {'name':'potato_cutlet_recipe','ingredients':['potato', 'green chillie', 'onion','bread', ' oil'],
                        'cooking_time': 19,
                        'allergies': [''],
                        'type': ['vegetarian'],
                        'rating': 5,
                        'category': ['snack'] ,
                        'Calories': 160,
                        'link':'https://feelgoodfoodie.net/ecipe/potatocutlet/'}
egg_roll_recipe = {'name':'egg_roll_recipe','ingredients': ['egg', 'flour', 'onion’,green chillie',' oil','paprika'],
                        'cooking_time': 35,
                        'allergies':[''],
                        'type': ['vegetarian'],
                        'rating': 4,
                        'category': ['snack','main_dish'],
                        'Calories': 160,
                        'link':'https://www.playfulcooking.com/snack-and-fingerfood/kolkata-egg-roll/'}
burrito = {'name':'burrito','ingredients': ['cooked rice ', 'black bean','onion’,’garlic’,‘hot sauce','oil’,’tortilla'],
                        'cooking_time': 15,
                        'allergies': ['beans'],
                        'type': ['vegetarian'],
                        'rating': 5,
                        'category': ['main_dish'],
                        'Calories': 287,
                        'link':'https://www.thespruceeats.com/vegetarian-bean-and-rice-burrito-recipe-3378550'}
our_recipes=[lasagne_recipe,mushroom_soup,lentil_soup, tomato_basil_soup,Green_bean_casrole ,
              chicken_recipe, chinese_pancakes, roast_pumpkin_salade, choco_banane_ice_cream,
              pesto_pizza,Grilled_Lemon_Chicken,tandoori_Fish, mutton_recipe, Lahmacun,
              Honey_Garlic_Chicken, hummus_recipe, falafel_recipe, potato_cutlet_recipe, egg_roll_recipe, burrito   ]
user_type= input("please enter your type of recipe: vegetarian, vegan or non_vegetarian")
user_rating=input("please enter your preferred rating ")
user_cooking_time=input("cooking time wanted ")
#user_category=input("category:snack,soup,dessert, salad or main_dish ")
user_allergies=input("please enter allergy if any ")

for x in our_recipes:
    if user_type in x['type'] and int(user_rating) <= x['rating'] and user_allergies not in x['allergies']:
       
            print("recipe 4 u ", x)
weblink= input("would you like to go to webpage?")

###########
#to open link of entered recipe
###########

if weblink == "yes":
    choosen_recipe = input ("enter the name of recipe")
    for x in our_recipes:
        
        if choosen_recipe in str(x) :
            
            print(x['link'])
            #print(x.get('link'))
            webbrowser.open(x['link'])
            break
###############
# to enter the new recipe
###############
answer = input("do u want to add recipes? ")
if answer == "yes" :
    name = input("enter the name of recipe ")
    type = str(input(" please add the type of recipe:vegan, vegitarian or non vegitarian: "))
    ingredients = input(" Enter the list of ingriedients seperated by comma ")
    ingredients = ingredients.split(',')
    cooking_time = int(input("add cooking time in minutes "))
    allergies = str(input("please enter the allergies if any "))
    rating = int(input("rating if_any "))
    Calories = int(input("kcal "))
    link = str(input("add link to your recipe "))
    recipe_added = {'name' : name, 
     'ingredients': ingredients,
     'type' : type,
     'cooking_time' : cooking_time,
     'allergies' : allergies,
     'rating' : rating,
     'link' : link}
    #print(recipe_added)
    print("thanks for adding your recipe : ", name)
    our_recipes.append(recipe_added)
    print("total number of recipes ", len(our_recipes))
else :
    print("thanks for using my app")



