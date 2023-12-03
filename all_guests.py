guests = {'alice':{'apples':5, 'pretzel':5},
          'bob':{'ham sandwiches':3, 'apple pies':2},
          'carol':{'cups':3, 'apple pies':1},
          'tom':{'bottle':2, 'cups':1},
          }

food_names = []
food_quantities = []
for person_name, food in guests.items():
    for food_name, food_quantity in food.items():
        #如果没有重复的food_name，那么增加链表
        if food_name not in food_names:
            food_names.append(food_name)
            food_quantities.append(food_quantity)
        else:
        #如果有重复的food_name，
        #首先确定重复food_name的位置,以得到当前的数量
        #然后将重复food_name的数量加到当前的数量上
            #print(f'重复的是：{food_name}')
            duplicate_food_name_pos = food_names.index(food_name)
            #print(f'位置为：{duplicate_food_name_pos}')
            food_quantities[duplicate_food_name_pos] += food_quantity

print(f'Number of things being bought:')
for i in range(len(food_names)):
    print(f'- {food_names[i]} {food_quantities[i]}')