planets=[['mercury','venus','earth'],['mars','jupiter','saturn'],['uranus','neptune']]
falt_planets=[planets for sublist in planets in planets for planet in sublist if len(planet)<6]
print(falt_planets)