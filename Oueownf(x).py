def dragon(heat, damage=10):
    """
    Creates a lovely dragon
    :param heat: potency of dragon fire (1-100)
    :param damage: How hard the dragon bites (1-50)
    :return: the sum of heat and damage
    """
    try:
        heat = int(heat)
        damage = int(damage)
    except ValueError:
        print("You must use numbers for dragon atributes")
        return

    #Here comes the body of the f(x)
    print(f"You are creating a dragon with a fire power of {heat} and bite power od {damage}")
    return heat+damage


dragon1 = dragon(77, 10)
dragon2 = dragon(damage=17, heat=45)
dragon3 = dragon(40)

if dragon1 > dragon2:
    print("dragon1 is stronger")
else:
    print("dragon 2 is stronger")