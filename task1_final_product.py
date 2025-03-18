#CODTECH IT SOLUTIONS. 
#Task-1 API integration and Data visualization using public API .
#PROGRAM TO DISPLAY THE DISTANCE FOR WALKING, BIKING, AND DRIVING FROM MADURAI TO COIMBATORE.

import googlemaps
import matplotlib.pyplot as plt
API=input("ENTER YOUR API KEY:  ")
API_KEY = API
try: 
    gmaps = googlemaps.Client(key=API)
    origin = 'Madurai'
    destination = 'Coimbatore'
    directions = gmaps.directions(origin, destination, mode='walking')
    walking= directions[0]['legs'][0]['distance']['value'] / 1000
    directions = gmaps.directions(origin, destination, mode='bicycling')
    biking= directions[0]['legs'][0]['distance']['value'] / 1000
    directions = gmaps.directions(origin, destination, mode='driving')
    driving= directions[0]['legs'][0]['distance']['value'] / 1000
    MODE = ['Walking', 'Biking', 'Driving']
    distances = [walking, biking, driving]
    plt.bar(MODE, distances,color='yellow')
    plt.xlabel('Mode of Transport')
    plt.ylabel('Distance (km)')
    plt.title('Distance from Madurai to Coimbatore')
    plt.show()
except:
    print("\n\n\nTHE API KEY YOU HAVE PROVIDED IS WRONG")
  
 
