import math
import random
import numpy

def getLowestEntropy():
    """
    Gets lowest entropy of all tiles on the board. Used to find the next piece to fill

    
    Returns:
        RETURNED_FLOWER_CHANCE : The chance a flower tile will be placed. Used in chooseTile()
        RETURNED_ROCK_CHANCE : The chance a rock tile will be placed. Used in chooseTile()
        RETURNED_WATER_CHANCE : The chance a water tile will be placed. Used in chooseTile()
        RETURNED_COAST_CHANCE : The chance a coast tile will be placed. Used in chooseTile()
        RETURNED_LAND_CHANCE : The chance a land tile will be placed. Used in chooseTile()
        lowestEntropyX : The X index with the lowest entropy on the map
        lowestEntropyY : The Y index with the lowest entropy on the map

    
    """
    import wavefunction
    lowestEntropy = 999
    lowestEntropyX = 999
    lowestEntropyY = 999
    currentEntropy = 999

   
    for i in range(24):
        for j in range(24):
            if wavefunction.map[i][j] == 0:
                FLOWER_CHANCE = 0
                ROCK_CHANCE = 0
                WATER_CHANCE = 0
                COAST_CHANCE = 0
                LAND_CHANCE = 0
    
                #List that contains neighbors of the current tile. Used to weight tiles of the same kind to be next to each other when applicable
                neighbors = []
                if i + 1 < 24:
                    if wavefunction.map[i + 1][j] > 0:
                        neighbors.append(wavefunction.map[i + 1][j])
                if j + 1 < 24:
                    if wavefunction.map[i][j + 1] > 0:
                        neighbors.append(wavefunction.map[i][j +1])
                if i - 1 >= 0:
                    if wavefunction.map[i - 1][j] > 0:
                        neighbors.append(wavefunction.map[i - 1][j])
                if j - 1 >= 0:
                    if wavefunction.map[i][j - 1] > 0:
                        neighbors.append(wavefunction.map[i][j - 1])
    
                possibleTiles = wavefunction.mapBool[i][j]
                if numpy.array_equiv(possibleTiles, [True, True, True, True, True]): #will only occur on first pick. Therefore all chances equal. Switch statement could also be used here
                    FLOWER_CHANCE = .20 
                    ROCK_CHANCE = .20 
                    WATER_CHANCE = .20
                    COAST_CHANCE = .20
                    LAND_CHANCE = .20 
                    currentEntropy = - ( math.log(FLOWER_CHANCE) * FLOWER_CHANCE + math.log(ROCK_CHANCE) * ROCK_CHANCE + math.log(WATER_CHANCE) * WATER_CHANCE + math.log(COAST_CHANCE) * COAST_CHANCE + math.log(LAND_CHANCE) * LAND_CHANCE) 
                
                #Entropy when flower is impossible 
                elif numpy.array_equiv(possibleTiles, [True, True, True, True, False]):
                    ROCK_CHANCE = .05 
                    WATER_CHANCE = .1
                    COAST_CHANCE = .1
                    LAND_CHANCE = .1
                    for tile in neighbors:
                        if tile == 3: #water
                            WATER_CHANCE += .1625
                        elif tile == 2: #coast
                            COAST_CHANCE += .1625
                        elif tile == 1:
                            LAND_CHANCE += .1625
                    
                    currentEntropy = - ( math.log(WATER_CHANCE) * WATER_CHANCE + math.log(COAST_CHANCE) * COAST_CHANCE + math.log(LAND_CHANCE) * LAND_CHANCE) 
                
                #Entropy when rock is impossible           
                elif numpy.array_equiv(possibleTiles, [True, True, True, False, True]):
                    FLOWER_CHANCE = .1
                    WATER_CHANCE = .1
                    COAST_CHANCE = .1
                    LAND_CHANCE = .1
                    for tile in neighbors:
                        if tile == 5:
                            FLOWER_CHANCE += .15
                        elif tile == 3:
                            WATER_CHANCE += .15
                        elif tile == 2:
                            COAST_CHANCE += .15
                        elif tile == 1:
                            LAND_CHANCE += .15

                    currentEntropy = - ( math.log(FLOWER_CHANCE) * FLOWER_CHANCE + math.log(WATER_CHANCE) * WATER_CHANCE + math.log(COAST_CHANCE) * COAST_CHANCE + math.log(LAND_CHANCE) * LAND_CHANCE) 
                
                #Entropy when flower and rock are impossible
                elif numpy.array_equiv(possibleTiles, [True, True, True, False, False]):
                    WATER_CHANCE = .1
                    COAST_CHANCE = .1
                    LAND_CHANCE = .1
                    for tile in neighbors:
                        if tile == 3:
                            WATER_CHANCE += .175
                        elif tile == 2:
                            COAST_CHANCE += .175
                        elif tile == 1:
                            LAND_CHANCE += .175
                    
                    currentEntropy = - (math.log(WATER_CHANCE) * WATER_CHANCE + math.log(COAST_CHANCE) * COAST_CHANCE + math.log(LAND_CHANCE) * LAND_CHANCE) 
                #Entropy when land and rock are impossible
                elif numpy.array_equiv(possibleTiles, [False, True, True, True, False, True]):
                    FLOWER_CHANCE = .1 
                    WATER_CHANCE = .1
                    COAST_CHANCE = .1
                    for tile in neighbors:
                        if tile == 5:
                            FLOWER_CHANCE += .175
                        elif tile == 3:
                            WATER_CHANCE += .175
                        elif tile == 2:
                            COAST_CHANCE += .175
                
                    currentEntropy = - ( math.log(FLOWER_CHANCE) * FLOWER_CHANCE + math.log(WATER_CHANCE) * WATER_CHANCE + math.log(COAST_CHANCE) * COAST_CHANCE) 
                
                #Entropy when rock, land, and flower are impossible
                elif numpy.array_equiv(possibleTiles, [False, True, True, False, False]):
                    WATER_CHANCE = .1
                    COAST_CHANCE = .1
                    for tile in neighbors:
                        if tile == 3:
                            WATER_CHANCE += .2
                        elif tile == 2:
                            COAST_CHANCE += .2
                
                    currentEntropy = - (math.log(WATER_CHANCE) * WATER_CHANCE + math.log(COAST_CHANCE) * COAST_CHANCE) 

                #Entropy when rock and water are impossible
                elif numpy.array_equiv(possibleTiles, [True, True, False, False, True]):
                    FLOWER_CHANCE = .1
                    COAST_CHANCE = .1
                    LAND_CHANCE = .1
                    for tile in neighbors:
                        if tile == 5:
                            FLOWER_CHANCE += .175
                        elif tile == 2:
                            COAST_CHANCE += .175
                        elif tile == 1:
                            LAND_CHANCE += .175
                    
                    currentEntropy = - ( math.log(FLOWER_CHANCE) * FLOWER_CHANCE + math.log(COAST_CHANCE) * COAST_CHANCE + math.log(LAND_CHANCE) * LAND_CHANCE) 
                
                #Entropy when rock, water, and flower are impossible
                elif numpy.array_equiv(possibleTiles, [True, True, False, False, False]):
                    COAST_CHANCE = .1
                    LAND_CHANCE = .1
                    for tile in neighbors:
                        if tile == 2:
                            COAST_CHANCE += .2
                        elif tile == 1:
                            LAND_CHANCE += .2
                    
                    currentEntropy = - (math.log(COAST_CHANCE) * COAST_CHANCE + math.log(LAND_CHANCE) * LAND_CHANCE) 
                
                #Entropy when flower and water are impossible
                elif numpy.array_equiv(possibleTiles, [True, True, False, True, False]):
                    ROCK_CHANCE = .05
                    COAST_CHANCE = .1
                    LAND_CHANCE = .1
                    for tile in neighbors:
                        if tile == 2:
                            COAST_CHANCE += .1875
                        elif tile == 1:
                            LAND_CHANCE += .1875

                    currentEntropy = - (math.log(ROCK_CHANCE) * ROCK_CHANCE + math.log(COAST_CHANCE) * COAST_CHANCE + math.log(LAND_CHANCE) * LAND_CHANCE) 
                
                #Entropy when water, rock, land, and flower are impossible
                elif numpy.array_equiv(possibleTiles, [False, True, False, False, False]):
                    COAST_CHANCE = 1
                    currentEntropy = 1
                
                #When land and rock are impossible
                elif numpy.array_equiv(possibleTiles, [False, True, True, False, True]):
                    FLOWER_CHANCE = .1
                    WATER_CHANCE = .1
                    COAST_CHANCE = .1
                    for tile in neighbors:
                        if tile == 5:
                            FLOWER_CHANCE += .175
                        elif tile == 3:
                            WATER_CHANCE += .175
                        elif tile == 2:
                            COAST_CHANCE += .175

                    currentEntropy = - ( math.log(FLOWER_CHANCE) * FLOWER_CHANCE + math.log(WATER_CHANCE) * WATER_CHANCE + math.log(COAST_CHANCE) * COAST_CHANCE) 
                            
                #When land and water are impossible
                elif numpy.array_equiv(possibleTiles, [False, True, False, True, True]):
                    FLOWER_CHANCE = .1
                    ROCK_CHANCE = .05
                    COAST_CHANCE = .1
                    for tile in neighbors:
                        if tile == 5:
                            FLOWER_CHANCE += .1875
                        elif tile == 2:
                            COAST_CHANCE += .1875
                            
                    currentEntropy = - ( math.log(FLOWER_CHANCE) * FLOWER_CHANCE + math.log(ROCK_CHANCE) * ROCK_CHANCE + math.log(COAST_CHANCE) * COAST_CHANCE) 

                #When land, water, and rock are impossible
                elif numpy.array_equiv(possibleTiles, [False, True, False, False, True]):
                    FLOWER_CHANCE = .1
                    COAST_CHANCE = .1
                    for tile in neighbors:
                        if tile == 5:
                            FLOWER_CHANCE += .2
                        elif tile == 2:
                            COAST_CHANCE += .2
                    
                    currentEntropy = - ( math.log(FLOWER_CHANCE) * FLOWER_CHANCE  + math.log(COAST_CHANCE) * COAST_CHANCE) 
                            
                #When land, water, and flower are impossible
                elif numpy.array_equiv(possibleTiles, [False, True, False, True, False]):
                    ROCK_CHANCE = .05
                    COAST_CHANCE = .1
                    for tile in neighbors:
                        if tile == 2:
                            COAST_CHANCE += .2125
                
                    currentEntropy = - ( math.log(ROCK_CHANCE) * ROCK_CHANCE  + math.log(COAST_CHANCE) * COAST_CHANCE) 
                
                #When water is impossible
                elif numpy.array_equiv(possibleTiles, [True, True, False, True, True]):
                    FLOWER_CHANCE = .1
                    ROCK_CHANCE = .05
                    COAST_CHANCE = .1
                    LAND_CHANCE = .1
                    for tile in neighbors:
                        if tile == 5:
                            FLOWER_CHANCE += .1625
                        elif tile == 2:
                            COAST_CHANCE += .1625
                        elif tile == 1:
                            LAND_CHANCE += .1625
                            
                    
                    currentEntropy = - ( math.log(FLOWER_CHANCE) * FLOWER_CHANCE + math.log(ROCK_CHANCE) * ROCK_CHANCE + math.log(COAST_CHANCE) * COAST_CHANCE + math.log(LAND_CHANCE) * LAND_CHANCE)            

                #Flower land impossible
                elif numpy.array_equiv(possibleTiles, [False, True, True, True, False]):
                    ROCK_CHANCE = .05
                    COAST_CHANCE = .1
                    WATER_CHANCE = .1
                    for tile in neighbors:
                        if tile == 3:
                            WATER_CHANCE += .1875
                        elif tile == 2:
                            COAST_CHANCE += .1875

                    currentEntropy = - ( math.log(ROCK_CHANCE) * ROCK_CHANCE  + math.log(COAST_CHANCE) * COAST_CHANCE + math.log(WATER_CHANCE) * WATER_CHANCE) 

                else: #Used to find missing scenarios during testing. Shouldn't occur 
                    print("Error: Scenario unaccounted for")
                    print(wavefunction.mapBool[i][j])            
                
                if currentEntropy < lowestEntropy:
                    lowestEntropyX = i
                    lowestEntropyY = j
                    lowestEntropy = currentEntropy
                    RETURNED_FLOWER_CHANCE = FLOWER_CHANCE
                    RETURNED_ROCK_CHANCE = ROCK_CHANCE
                    RETURNED_WATER_CHANCE = WATER_CHANCE
                    RETURNED_COAST_CHANCE = COAST_CHANCE
                    RETURNED_LAND_CHANCE = LAND_CHANCE

    if currentEntropy == 999:
        print("Map is complete!")
        quit()
        
    return RETURNED_FLOWER_CHANCE, RETURNED_ROCK_CHANCE, RETURNED_WATER_CHANCE, RETURNED_COAST_CHANCE, RETURNED_LAND_CHANCE, lowestEntropyX, lowestEntropyY 

def chooseTile(xIndex, yIndex, RETURNED_FLOWER_CHANCE, RETURNED_ROCK_CHANCE, RETURNED_WATER_CHANCE, RETURNED_COAST_CHANCE, RETURNED_LAND_CHANCE):
    """
    Method to choose and fill a weighted random tile on the map. Uses chances from getLowestEntropy() to make a weighted choice

    Parameters:
        xIndex : The X index with the lowest entropy on the map
        yIndex : The Y index with the lowest entropy on the map
        RETURNED_FLOWER_CHANCE : The chance a flower tile will be placed. 
        RETURNED_ROCK_CHANCE : The chance a rock tile will be placed. 
        RETURNED_WATER_CHANCE : The chance a water tile will be placed. 
        RETURNED_COAST_CHANCE : The chance a coast tile will be placed. 
        RETURNED_LAND_CHANCE : The chance a land tile will be placed. 
    
    
    """
    tileList = [1, 2, 3, 4, 5]
    
    choice = random.choices(tileList, weights = (RETURNED_LAND_CHANCE, RETURNED_COAST_CHANCE, RETURNED_WATER_CHANCE, RETURNED_ROCK_CHANCE, RETURNED_FLOWER_CHANCE))
    choice = choice[0]

    if choice == 1:
        land(xIndex, yIndex)
    elif choice == 2:
        coast(xIndex, yIndex)
    elif choice == 3:
        water(xIndex, yIndex)
    elif choice == 4:
        rock(xIndex, yIndex)
    elif choice == 5:
        flower(xIndex, yIndex)
        




def flower(xIndex, yIndex):
    """
    Method used to place pixels corresponding to a flower tile

    Parameters:
        xIndex: the xIndex of map to place the tile
        yIndex: the yIndex of map to place the tile

    """
    import wavefunction
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6), (255,255,255))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6), (0,154,23)) 
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6), (0,154,23)) 
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6), (0,154,23)) 
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 1), (255,255,255))
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 2), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 3), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 4), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 5), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 1), (255, 216, 0))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 2), (255,255,255))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 3), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 4), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 5), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 1), (255,255,255))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 2), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 3), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 4), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 5), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 1), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 2), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 3), (255,255,255))
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 4), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 5), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 1), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 2), (255,255,255))
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 3), (255, 216, 0))
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 4), (255,255,255))
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 5), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 1), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 2), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 3), (255,255,255))
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 4), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 5), (0,154,23))

    wavefunction.map[xIndex][yIndex] = 5

    wavefunction.img.save("output.png")

    
    if xIndex + 1 < 24:
        wavefunction.mapBool[xIndex + 1][yIndex][2] = False
    if xIndex - 1 >= 0: 
        wavefunction.mapBool[xIndex - 1][yIndex][2] = False
    if yIndex + 1 < 24:
        wavefunction.mapBool[xIndex][yIndex + 1][2] = False
    if yIndex - 1 >= 0:
        wavefunction.mapBool[xIndex][yIndex - 1][2] = False

    
def rock(xIndex, yIndex):
    """
    Method used to place pixels corresponding to a rock tile

    Parameters:
        xIndex: the xIndex of map to place the tile
        yIndex: the yIndex of map to place the tile

    """

    import wavefunction
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6), (128, 132, 135)) 
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6), (128, 132, 135)) 
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6), (128, 132, 135)) 
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 1), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 2), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 3), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 4), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 5), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 1), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 2), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 3), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 4), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 5), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 1), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 2), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 3), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 4), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 5), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 1), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 2), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 3), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 4), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 5), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 1), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 2), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 3), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 4), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 5), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 1), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 2), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 3), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 4), (128, 132, 135))
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 5), (128, 132, 135))

    wavefunction.img.save("output.png")

    wavefunction.map[xIndex][yIndex] = 4

    if xIndex + 1 < 24:
        wavefunction.mapBool[xIndex + 1][yIndex][3] = False
    if xIndex - 1 >= 0: 
        wavefunction.mapBool[xIndex - 1][yIndex][3] = False
    if yIndex + 1 < 24:
        wavefunction.mapBool[xIndex][yIndex + 1][3] = False
    if yIndex - 1 >= 0:
        wavefunction.mapBool[xIndex][yIndex - 1][3] = False

def water(xIndex, yIndex):
    """
    Method used to place pixels corresponding to a water tile

    Parameters:
        xIndex: the xIndex of map to place the tile
        yIndex: the yIndex of map to place the tile

    """

    import wavefunction
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6), (56,132,207)) 
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6), (56,132,207)) 
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6), (56,132,207)) 
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 1), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 2), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 3), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 4), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 5), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 1), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 2), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 3), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 4), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 5), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 1), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 2), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 3), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 4), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 5), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 1), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 2), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 3), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 4), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 5), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 1), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 2), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 3), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 4), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 5), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 1), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 2), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 3), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 4), (56,132,207))
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 5), (56,132,207))

    wavefunction.img.save("output.png")

    wavefunction.map[xIndex][yIndex] = 3
    
    if xIndex + 1 < 24:
        wavefunction.mapBool[xIndex + 1][yIndex][0] = False
        wavefunction.mapBool[xIndex + 1][yIndex][4] = False
    if xIndex - 1 >= 0: 
        wavefunction.mapBool[xIndex - 1][yIndex][0] = False
        wavefunction.mapBool[xIndex - 1][yIndex][4] = False
    if yIndex + 1 < 24:
        wavefunction.mapBool[xIndex][yIndex + 1][0] = False
        wavefunction.mapBool[xIndex][yIndex + 1][4] = False
    if yIndex - 1 >= 0:
        wavefunction.mapBool[xIndex][yIndex - 1][0] = False
        wavefunction.mapBool[xIndex][yIndex - 1][4] = False


def coast(xIndex, yIndex):
    """
    Method used to place pixels corresponding to a coast tile

    Parameters:
        xIndex: the xIndex of map to place the tile
        yIndex: the yIndex of map to place the tile

    """
    import wavefunction
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6), (242,209, 107)) 
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6), (242,209, 107)) 
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6), (242,209, 107)) 
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 1), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 2), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 3), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 4), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 5), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 1), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 2), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 3), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 4), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 5), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 1), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 2), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 3), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 4), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 5), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 1), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 2), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 3), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 4), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 5), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 1), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 2), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 3), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 4), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 5), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 1), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 2), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 3), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 4), (242,209, 107))
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 5), (242,209, 107))

    wavefunction.img.save("output.png")

    wavefunction.map[xIndex][yIndex] = 2


    
def land(xIndex, yIndex):
    """
    Method used to place pixels corresponding to a land tile

    Parameters:
        xIndex: the xIndex of map to place the tile
        yIndex: the yIndex of map to place the tile

    """
    import wavefunction
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6), (0,154,23)) 
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6), (0,154,23)) 
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6), (0,154,23)) 
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 1), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 2), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 3), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 4), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 5), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 1), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 2), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 3), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 4), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 5), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 1), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 2), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 3), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 4), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 5), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 1), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 2), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 3), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 4), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 5), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 1), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 2), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 3), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 4), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 5), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 1), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 2), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 3), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 4), (0,154,23))
    wavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 5), (0,154,23))

    wavefunction.img.save("output.png")
    
    if xIndex + 1 < 24:
        wavefunction.mapBool[xIndex + 1][yIndex][2] = False
    if xIndex - 1 >= 0: 
        wavefunction.mapBool[xIndex - 1][yIndex][2] = False
    if yIndex + 1 < 24:
        wavefunction.mapBool[xIndex][yIndex + 1][2] = False
    if yIndex - 1 >= 0:
        wavefunction.mapBool[xIndex][yIndex - 1][2] = False

    wavefunction.map[xIndex][yIndex] = 1