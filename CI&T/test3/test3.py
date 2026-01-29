from typing import List

def find_snake_on_grid(grid: List[str]) -> List[List[int]]:
    # map symbols to their pointing direction 
    directions = {
        '>': (1, 0),
        '<': (-1, 0),
        '^': (0, -1),
        'v': (0, 1),
    }

    cobra_coords = []
    cor_x, cor_y = -1, -1
    
    # locate the head to start the search
    for y, row in enumerate(grid):
        if 'h' in row:
            cor_x, cor_y = row.index('h'), y
            break
            
    cobra_coords.append([cor_x, cor_y])
    cabeca_x, cabeca_y = cor_x, cor_y
    
    # identify the first body segment that points to the head
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = cabeca_x + dx, cabeca_y + dy
        
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]):
            char_vizinho = grid[ny][nx]
            if char_vizinho in directions:
                mov_x, mov_y = directions[char_vizinho]
                #check if this segments direction leads back to the head
                if nx + mov_x == cabeca_x and ny + mov_y == cabeca_y:
                    cor_x, cor_y = nx, ny
                    cobra_coords.append([cor_x, cor_y])
                    break
    
    # find the next segment pointing to the current one
    while True:
        encontrou_proximo = False
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = cor_x + dx, cor_y + dy
            
            if [nx, ny] in cobra_coords:
                continue
                
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]):
                char_vizinho = grid[ny][nx]
                if char_vizinho in directions:
                    mov_x, mov_y = directions[char_vizinho]
                    # verify if the neighbor points to the current segment
                    if nx + mov_x == cor_x and ny + mov_y == cor_y:
                        cor_x, cor_y = nx, ny
                        cobra_coords.append([cor_x, cor_y])
                        encontrou_proximo = True
                        break
        
        if not encontrou_proximo:
            break
                  
    return cobra_coords