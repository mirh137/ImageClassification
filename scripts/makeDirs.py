import os
pokemon_list = [
    'Abra', 'Bellsprout', 'Charmander', 'Ditto', 'Drowzee', 'Exeggcute', 'Geodude', 'Growlithe', 'Koffing', 'Machop',
    'Mankey', 'Moltres', 'Omanyte', 'Pinsir', 'Porygon', 'Rhyhorn', 'Seel', 'Spearow', 'Tangela', 'Venonat', 'Weedle',
    'Aerodactyl', 'Bulbasaur', 'Cubone', 'Doduo', 'Eevee', 'Farfetchd', 'Goldeen', 'Horsea', 'Lapras', 'Magikarp',
    'Meowth', 'Mr. Mime', 'Pidgey', 'Poliwag', 'Psyduck', 'Sandshrew', 'Shellder', 'Squirtle', 'Tauros', 'Voltorb',
    'Zapdos', 'Articuno', 'Caterpie', 'Diglett', 'Dratini', 'Ekans', 'Gastly', 'Grimer', 'Kangaskhan', 'Lickitung',
    'Magnemite', 'Mew', 'Oddish', 'Pikachu', 'Ponyta', 'Rattata', 'Scyther', 'Slowpoke', 'Staryu', 'Tentacool',
    'Vulpix', 'Zubat'
]
os.chdir("/home/mir/Desktop/PokemonProject/greyscaleSet/archive/pokemon")
for dir in pokemon_list:
    os.mkdir(dir)