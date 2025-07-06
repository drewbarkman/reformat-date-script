import os

folder_list = os.listdir()

for folder in folder_list:
    try:
        int(folder[0])
    except:
        continue

    month = folder[:2]
    day = folder[3:5]
    year = folder[6:10]
    rest = folder[13:]

    print(folder[:10])
    
    new_name = f"{year}.{month}.{day} | {rest}"
    print(f'New name: {new_name}')

    os.rename(folder, new_name)