import numpy as np
import matplotlib.pyplot as plt


starter_grid=np.zeros(10*10).reshape(10,10)
plt.imshow(starter_grid)
    
    
def add_blok (i,j,grid = starter_grid):
    blok = np.array([[0,255,255],[0,255,255],[0,0,0]])
    
    x=blok.shape[0]
    y=blok.shape[1]
    
    grid[i:i+x, j:j+y] = blok
    
    plt.imshow(grid)
    return grid
   
def add_ul (i,j,grid = starter_grid):
    ul = np.array([[0,255,255,0],[255,0,0,255],[0,255,255,0]])
    
    x=ul.shape[0]
    y=ul.shape[1]
    
    grid[i:i+x, j:j+y] = ul
    
    plt.imshow(grid)
    return grid

def add_bochenek (i,j,grid = starter_grid):
    bochenek = np.array([[0,255,255,0],[255,0,0,255],[0,255,0,255], [0,0,255,0]])
    
    x=bochenek.shape[0]
    y=bochenek.shape[1]
    
    grid[i:i+x, j:j+y] = bochenek
    
    plt.imshow(grid)
    return grid
    
def add_lodka (i,j,grid = starter_grid):
    lodka= np.array([[255,255,0],[255,0,255],[0,255,0]])
    
    x=lodka.shape[0]
    y=lodka.shape[1]
    
    grid[i:i+x, j:j+y] = lodka
    
    plt.imshow(grid)
    return grid

def add_zaba (i,j,grid = starter_grid):
    zaba = np.array([[0,255,255,255],[255,255,255,0]])
    
    x=zaba.shape[0]
    y=zaba.shape[1]
    
    grid[i:i+x, j:j+y] = zaba
    
    plt.imshow(grid)
    return grid


def add_swiatla (i,j,grid = starter_grid):
    swiatla = np.array([[0,255,0],[0,255,0],[0,255,0]])
    
    x=swiatla.shape[0]
    y=swiatla.shape[1]
    
    grid[i:i+x, j:j+y] = swiatla
    
    plt.imshow(grid)
    return grid

def add_latarnia (i,j,grid = starter_grid):
    latarnia = np.array([[255,255,0,0],[255,0,0, 0],[0,0,0,255], [0,0,255,255]])
    
    x=latarnia.shape[0]
    y=latarnia.shape[1]
    
    grid[i:i+x, j:j+y] = latarnia
    
    plt.imshow(grid)
    return grid