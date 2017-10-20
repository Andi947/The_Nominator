def add_to_hero():
    hero_name = raw_input("Who is your hero this week? ")
    hero_reason = raw_input("Why are they your hero? ")
    heros = {}
    heros[str(hero_name)] = str(hero_reason)
    return heros


def add_to_zero():
    zero_name = raw_input("Who is your zero this week? ")
    zero_reason = raw_input("Why are they your zero? ")
    zeros = {}
    zeros[str(zero_name)] = str(zero_reason)
    return zeros

hero = add_to_hero()
hero.update(add_to_hero())
print
zero = add_to_zero()
zero.update(add_to_zero())

print hero
print
print zero
# for i in heros:
#     print "Your hero is " + i + " because " + hero[i]
