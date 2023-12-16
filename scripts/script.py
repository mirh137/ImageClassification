# f = open("list.txt", "w")

# dirs = ['Rattata', 'Aerodactyl', 'Tentacool', 'Slowpoke', 'Magikarp', 'Bulbasaur', 'Horsea', 'Squirtle', 'Vulpix', 'Oddish', 'Venonat', 'Lickitung', 'Zubat', 'Seel', 'Dratini', 'Caterpie', 'Mr. Mime', 'Voltorb', 'Articuno', 'Farfetchd', 'Shellder', 'Cubone', 'Sandshrew', 'Drowzee', 'Omanyte', 'Porygon', 'Machop', 'Staryu', 'Koffing', 'Zapdos', 'Mew', 'Doduo', 'Scyther', 'Abra', 'Moltres', 'Weedle', 'Magnemite', 'Pinsir', 'Rhyhorn', 'Diglett', 'Kangaskhan', 'Charmander', 'Pidgey', 'Tauros', 'Ditto', 'Lapras', 'Pikachu', 'Meowth', 'Eevee', 'Geodude', 'Psyduck', 'Growlithe', 'Mankey', 'Grimer', 'Bellsprout', 'Ekans', 'Spearow', 'Goldeen', 'Gastly', 'Ponyta', 'Tangela', 'Poliwag', 'Exeggcute']
# dirs.sort()

# for dir in dirs:
#     f.write("def test_classify_" + dir + "():\n")
#     f.write("\tfor j in glob.glob('testingData/" + dir + "/*'):\n")
#     f.write("\t\tpytest.assume(classify(str(j)) == '" + dir + "')\n")


f = open("list.txt", "w")
dirs = ["Bug", "Dragon", "Electric", "Fighting", "Fire", "Flying", "Ghost", "Grass", "Ground", "Ice", "Normal", "Poison", "Psychic", "Rock", "Steel", "Water"]
dirs.sort()

for dir in dirs:
    f.write("def test_classify_" + dir + "():\n")
    f.write("\tfor j in glob.glob('typeTestingData/" + dir + "/*'):\n")
    f.write("\t\tpredictions = set(classify(str(j)))\n")
    f.write("\t\tactual = []\n")
    f.write("\t\tfname = j[21: j.index('.')]\n")
    f.write("\t\tif fname.index('_'):\n")
    f.write("\t\t\tactual.append(fname[:fname.index('_')])\n")
    f.write("\t\t\tactual.append(fname[fname.index('_')+1:])\n")
    f.write("\t\telse:\n")
    f.write("\t\t\tactual.append(fname[:fname.index('.')])\n")
    f.write("\t\tpytest.assume(len(predictions.intersection(set(actual))) != 0)\n")