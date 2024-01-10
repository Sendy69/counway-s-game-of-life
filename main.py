import numpy as np
import os
import time

frame = np.array([[0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 1, 1, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]])


#définition de la fonction qui calcule le nombre de voisins

def compute_number_neighbours(paded_frame , index_line , index_column):
    index_row = index_line 
    index_col = index_column
    number_neighbours = np.sum(paded_frame[index_row-1:index_row+2, index_col-1:index_col+2]) - paded_frame[index_row, index_col]

    return number_neighbours

print(compute_number_neighbours(frame, 3, 3))

def compute_next_frame(frame):
    paded_frame = np.pad(frame, 1 , mode='constant')

# récupération du nombres de lignes et de colonnes de la nouvelle matrice
    line_number_paded_frame = paded_frame.shape[0] 
    col_number_paded_frame = paded_frame.shape[1] 

    for index_line in range(1,line_number_paded_frame-1):
        for index_column in range(1,col_number_paded_frame-1):
            number_neighbours = compute_number_neighbours(paded_frame, index_line, index_column)
            if paded_frame[index_line, index_column] == 0 and number_neighbours == 3:
                frame[index_line-1, index_column-1] = 1
            elif paded_frame[index_line, index_column] == 1 and 2<= number_neighbours <=3:
                frame[index_line-1, index_column-1] = 1
            else:
                frame[index_line-1, index_column-1] = 0

    return frame

while True: 
    print(frame)
    os.system("cls")
    frame = compute_next_frame(frame)
        
        
    
