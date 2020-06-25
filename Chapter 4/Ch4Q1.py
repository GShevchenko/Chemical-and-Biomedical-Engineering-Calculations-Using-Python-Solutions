# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:27:01 2020

@author: JackM
"""

def find_weight_on_planet():
    while True:
        try:
            mass = float(input("Input your mass in kg: "))
                
            planets_and_gravities = {
                "Mercury": 0.38,
                "Venus": 0.91,
                "Earth": 1.0,
                "Mars": 0.38,
                "Jupiter": 2.34,
                "Saturn": 1.06,
                "Uranus": 0.92,
                "Neptune": 1.19,
                }
            
            joined_planets = (", ".join(planets_and_gravities))
            while True:
                    planet = str(input((f"Choose a planet from: {joined_planets} - ")))
                    if planet in planets_and_gravities.keys():
                        gravity = planets_and_gravities.get(planet)
                        break
                    else:
                       print("Please choose a planet from the list!")
        
            weight = mass * gravity
            
            print(f"Your weight on {planet} is {weight} kg")    
            break
        except ValueError:
                print('Please input a number!')
                
find_weight_on_planet()