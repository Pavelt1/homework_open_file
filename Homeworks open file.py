from pprint import pprint
# Задание 1

def cook_book(link):
    cook_book = {}
    ingredients = []
    count_ingredient = 0
    name = ""
    helper = []
    with open (link, "r", encoding="utf-8") as file:
        for i in file:
            if "|" in i:
                ingredients.append((i[:-1]).split(" | "))
                if len(ingredients) == count_ingredient:
                    for g,e,r in ingredients:
                        helper.append({'ingredient_name': g, 'quantity': int(e), 'measure': (r+" ")})
                        cook_book[name] = helper
                    helper = []
                    ingredients = []
                    name = ""
                    count_ingredient = 0
            elif 2 == len(i) or 3 == len(i):# 3 на случай если часло ингредиентов будет двухзначное 
                count_ingredient = int(i)
            elif 4 <= len(i) :
                name = i[:-1]
        return cook_book

# pprint(cook_book("recipes.txt"))
# Задача 2
def get_shop_list_by_dishes(dishes, person_count:int):
    answer1:dict = {}
    helper = 0
    for dish in dishes:
        for i in cook_book("recipes.txt")[dish]:
            if i['ingredient_name'] in answer1: # Если ингредиент повторяется несколько раз складывае количиство "quantity"
                helper = answer1[i['ingredient_name']]["quantity"]
                q,w,e = i['ingredient_name'], i['measure'], i['quantity']
                answer1[q] = {"measure": w,"quantity": ((e*person_count)+helper)}
                
            else:
                q,w,e = i['ingredient_name'], i['measure'], i['quantity']
                answer1[q] = {"measure": w,"quantity": (e*person_count)}
    return(answer1)

# pprint(get_shop_list_by_dishes(['Омлет','Запеченный картофель',], 2))
# pprint(get_shop_list_by_dishes(['Омлет','Фахитос','Омлет'], 2))

# Задание 3

textholder1:dict = {}
textholder2:dict = {}
textholder3:dict = {}
with open ("text1.txt", "r", encoding="utf-8") as file:
    for num,i in enumerate(file):
        textholder1[num] = i[:-1]
        # print(textholder1)
with open ("text2.txt", "r", encoding="utf-8") as file:
    for num,i in enumerate(file):
        textholder2[num] = i[:-1]
        # print(textholder2)
with open ("text3.txt", "r", encoding="utf-8") as file:
    for num,i in enumerate(file):
        textholder3[num] = i[:-1]
        # print(textholder3)


# Вариант решение 1
with open ("resultfile v1.txt", "a", encoding="utf-8") as file:
    file.write(f"text2.txt\n")
    file.write(f"В этом файле {len(textholder2)} строк\n")  
    file.write(f'{textholder2[0]}\n') 
    file.write(f"text1.txt\n")
    file.write(f"В этом файле {len(textholder1)} строк\n")  
    file.write(f'{textholder1[0]}\n')
    file.write(f'{textholder1[1]}')
    # Напишит в файл "resultfile v1.txt" то что показано в примере задания

# Вариант решение 2
len_files:list = []
len_files += textholder1,textholder2,textholder3
sorted_list = sorted(len_files, key=lambda x:len(x))

with open ("resultfile v2.txt", "a", encoding="utf-8") as file:
    for num,i in enumerate(sorted_list):
        file.write(f"text{num+1}.txt\n")
        file.write(f"В этом файле {len(i)} строк\n")
        for o in i:
            file.write(f'{(i[o])}\n')
 # Напишит в файл "resultfile v2.txt" то что написано Задание 3.1( первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)


