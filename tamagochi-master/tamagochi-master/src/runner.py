from src.tamagotchi import Tamagotchi

if __name__ == '__main__':
    tamagotchi = Tamagotchi(20, 10, 15, 30)
    print(tamagotchi)

    tamagotchi.brincar()
    print(tamagotchi)

    tamagotchi.comer()
    print(tamagotchi)

    tamagotchi.brincar()
    tamagotchi.brincar()

    tamagotchi.dormir()
    print(tamagotchi)

    tamagotchi.banhar()
    print(tamagotchi)

    if not tamagotchi.dormir():
        print("fail: o tamagotchi não está com sono")

    tamagotchi.brincar()
    tamagotchi.brincar()
    tamagotchi.brincar()
    tamagotchi.brincar()
    tamagotchi.brincar()
    print(tamagotchi)

    if not tamagotchi.comer():
        print("fail: o seu tamagotchi morreu.")

    if not tamagotchi.dormir():
        print("fail: o seu tamagotchi morreu.")

    if not tamagotchi.brincar():
        print("fail: o seu tamagotchi morreu.")

    if not tamagotchi.banhar():
        print("fail: o seu tamagotchi morreu.")