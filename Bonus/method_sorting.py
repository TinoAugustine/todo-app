waiting_list=["Tino","Evin","Tinnu","Eyan"]
waiting_list.sort()

for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)
