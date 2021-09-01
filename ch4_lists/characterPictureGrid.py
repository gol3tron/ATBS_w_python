# import stuffs


def characterPictureGrid(grid):
# needed to transpose the output, so reverse i,j, indices
#    for i in range(len(grid)):
#        for j in range(len(grid[i])):
#            print(grid[i][j],end='')
#        print()

    for i in range(len(grid[0])):
        for j in range(len(grid)):
            print(grid[j][i],end='')
        print()



if __name__ == '__main__':

    grid = [['.','.','.','.','.','.'],
            ['.','0','0','.','.','.'],
            ['0','0','0','0','.','.'],
            ['0','0','0','0','0','.'],
            ['.','0','0','0','0','0'],
            ['0','0','0','0','0','.'],
            ['0','0','0','0','.','.'],
            ['.','0','0','.','.','.'],
            ['.','.','.','.','.','.']]

    characterPictureGrid(grid)
