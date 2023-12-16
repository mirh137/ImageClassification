import tensorflow as tf
import cv2
import numpy as np

def classify(path, type1, type2):
    model = tf.keras.models.load_model("../models/typeModel")
    pokemon_types = [
    'Bug', 'Dragon', 'Electric', 'Fighting', 'Fire', 'Flying', 'Ghost', 
    'Grass', 'Ground', 'Ice', 'Normal', 'Poison', 'Psychic', 'Rock', 
    'Steel', 'Water'
]
    image = tf.keras.utils.load_img(                                                                                                                                                   
        path, target_size=(60,60)                                                                                                                                          
    )                                  
    im = cv2.imread(path)     
    if type2 == "None":
        cv2.imshow(type1, im)
        cv2.waitKey(0)  
    else:
        cv2.imshow(type1 + "_" + type2, im)   
        cv2.waitKey(0)  
    arr = tf.keras.utils.img_to_array(image)                                                                                                                                             
    arr = tf.expand_dims(arr,0)                                                                                                                                                  
    res = model.predict(arr)                                                                                                                                                   
    probabilities = tf.nn.softmax(res[0])  
    topTwo = np.argsort(probabilities)[::-1][:2]
    print(pokemon_types[topTwo[0]], pokemon_types[topTwo[1]])

classify("/home/mir/Desktop/PokemonProject/tests/TestImages/TypePokemon/gyrados.jpg", "Flying", "Water")
classify("/home/mir/Desktop/PokemonProject/tests/TestImages/TypePokemon/magmortar.jpeg", "Fire", "None")
classify("/home/mir/Desktop/PokemonProject/tests/TestImages/TypePokemon/lucario.jpeg", "Steel", "Fighting")
classify("/home/mir/Desktop/PokemonProject/tests/TestImages/TypePokemon/skarmory.jpeg", "Flying", "Steel")
classify("/home/mir/Desktop/PokemonProject/tests/TestImages/TypePokemon/Ampharos.jpeg", "Electric", "None")
classify("/home/mir/Desktop/PokemonProject/tests/TestImages/TypePokemon/leavany.jpeg", "Bug", "Grass")
classify("/home/mir/Desktop/PokemonProject/tests/TestImages/TypePokemon/rhyhorn.jpeg", "Rock", "Ground")

cv2.waitKey(0)