#import stuffs

#define functions
def printTable(inputList):
    """this function takes a list of lists of strings and pdisplays in a
    well-organized table with each column right-justified. Assume all inner
    lists contain the same number of strings"""

    #first find longest string in each inner list of inputList
    colWidths = [0] * len(inputList)

    for i in range(len(colWidths)):
        biggest = 0

        #iterate over all words in each column, look for longest word
        for word in tableData[i]:
            newWordSize = len(word)
            if newWordSize > biggest:
                biggest = newWordSize

        #store the longest word in each column
        colWidths[i] = biggest

    #now print the table
    for col in range(len(inputList)):
        for word in inputList[col]:
            print(word.rjust(colWidths[col]))


#main
if __name__ == '__main__':

    tableData = [['apples','oranges','cherries','banana'],['Alice','Bob','Carol','David'],['dogs','cats','moose','goose']]

    printTable(tableData)
