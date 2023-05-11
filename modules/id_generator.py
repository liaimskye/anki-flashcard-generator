from random import randint

def id_create():

    with open("existing_ids.txt", 'r') as f:
        numbers = f.readlines()

    existing_id=[]
    for item in numbers:
        item = item.rstrip("\n")
        item = int(item)
        existing_id.append(item)

    while True:
        model_id = randint(1000000,9999999)
        if model_id not in existing_id:
            existing_id.append(model_id)
            break

    while True:
        deck_id = randint(100000,999999)
        if deck_id not in existing_id:
            existing_id.append(deck_id)
            break

    with open("existing_ids.txt", "w") as f:
        for id in existing_id:
            line = f"{str(id)}\n"
            f.write(line)

    return model_id,deck_id


    

    
    



