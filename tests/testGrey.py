import tensorflow as tf
import cv2
import numpy as np

def classify(path, pokemonName):
    model = tf.keras.models.load_model("../models/nameModel")
    pokemonNames = ['Abra', 'Aerodactyl', 'Articuno', 'Bellsprout', 'Bulbasaur', 'Caterpie', 'Charmander', 'Cubone', 'Diglett', 'Ditto', 'Doduo', 'Dratini', 'Drowzee', 'Eevee', 'Ekans', 'Exeggcute', 'Farfetchd', 'Gastly', 'Geodude', 'Goldeen', 'Grimer', 'Growlithe', 'Horsea', 'Kangaskhan', 'Koffing', 'Lapras', 'Lickitung', 'Machop', 'Magikarp', 'Magnemite', 'Mankey', 'Meowth', 'Mew', 'Moltres', 'Mr. Mime', 'Oddish', 'Omanyte', 'Pidgey', 'Pikachu', 'Pinsir', 'Poliwag', 'Ponyta', 'Porygon', 'Psyduck', 'Rattata', 'Rhyhorn', 'Sandshrew', 'Scyther', 'Seel', 'Shellder', 'Slowpoke', 'Spearow', 'Squirtle', 'Staryu', 'Tangela', 'Tauros', 'Tentacool', 'Venonat', 'Voltorb', 'Vulpix', 'Weedle', 'Zapdos', 'Zubat']                                                                                                                  
    image = tf.keras.utils.load_img(                                                                                                                                                   
        path, target_size=(60,60)                                                                                                                                          
    )                                  
    im = cv2.imread(path)     
    cv2.imshow(pokemonName, im)   
    cv2.waitKey(0)                                                                                                                             
    arr = tf.keras.utils.img_to_array(image)                                                                                                                                             
    arr = tf.expand_dims(arr,0)                                                                                                                                                  
    res = model.predict(arr)                                                                                                                                                   
    probabilities = tf.nn.softmax(res[0])    
    print(pokemonNames[np.argmax(probabilities)])

classify("/home/mir/Desktop/PokemonProject/tests/TestImages/greyPokemons/zapdos.jpg", "Zapdos")
classify("/home/mir/Desktop/PokemonProject/tests/TestImages/greyPokemons/aerodactyl.jpg", "Aerodactyl")
classify("/home/mir/Desktop/PokemonProject/tests/TestImages/greyPokemons/pikachu.jpg", "Pikachu")

cv2.waitKey(0)