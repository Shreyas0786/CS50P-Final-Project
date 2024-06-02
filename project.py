import json
from tabulate import tabulate
import random


def main():

    with open('data/characters.json') as f:
        characters = json.load(f)
    with open('data/villages.json') as f:
        villages = json.load(f)
    options = {
        1: display_village_info,
        2: random_character_info
    }
    while True:
        try:
            user_input = int(input("\n\n========================\n 1. Select Village and display characters\n 2. display random character info\n 3. End \n"))
            if user_input == 1:
                rows = options[user_input](villages)
                print(tabulate(rows, headers=["name", "uniqueTraits", "Nature Type"], tablefmt="rounded_grid") )
            elif user_input == 2:
                name,jutsus,nature_type, kekkei_genkai, titles = options[user_input](characters)
                print("=====================")
                print(f"Name: {name}")
                print(f"Kekkei Genkai: {kekkei_genkai}")
                print(f"Jutsu: {jutsus}")
                print(f"Nature Types: {nature_type}")
                print(f"Titles: {titles}")
                print("=====================")
            elif user_input == 3:
                break
            else:
                raise Exception()
        except:
            print("Invalid input")
    print("Finished...")

def formulate_village_ouput(village_characters):
    data = [(x['name'], x.get('uniqueTraits', None), x.get("natureType",None)) for x in village_characters]
    return data


def display_village_info(villages):
    prompt = "Chooase a village by number"
    count = 1
    village_names = sorted(list(villages.keys()))

    for village in village_names:
        prompt += f"\n {str(count)}. {village}: {villages[village]['title']}"
        count += 1

    choice = None

    try:
        idx = int(input(prompt+"\n"))

        if not 1 <= idx <= len(village_names):
            raise Exception
        choice = village_names[idx-1]
        rows = formulate_village_ouput(villages[choice]['characters'])

    except:
        print("invalid input")
        raise ValueError("Invalid input")
    return rows


def random_character_info(characters):
    id = random.randint(1, 1430)
    name = characters[id]['name']
    jutsus = characters[id].get("jutsu",None)
    nature_type = characters[id].get("natureType",None)
    kekkei_genkai =  characters[id]['personal'].get("kekkeiGenkai",None)
    titles = characters[id]['personal'].get("titles",None)
    return (name,jutsus,nature_type, kekkei_genkai, titles)


if __name__ == "__main__":
    main()

