#dictionaries
#alien_1 = {"color":"green", 'points':20}
alien_1 = {'x_position':0, 'y_position':25, "speed":'low'}
if alien_1['speed'] == 'low':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
elif alien_1['speed'] == 'fast':
    x_increment = 3
alien_1['x_position'] = alien_1['x_position'] + x_increment  
print(f"The current x position of alien_1 is: {alien_1['x_position']} ")    
print(alien_1)
del alien_1['speed'], alien_1['x_position']
print(alien_1)
