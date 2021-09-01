# code project "comma code" from ch4 of atbs w/ python


def commaCode(inputList):
    # convert all list values to strings
    output = ''
    delim = ', '

    for i in range(len(inputList)):
        if i == len(inputList)-1:
            output += 'and ' + str(inputList[i])
        else:
            output += str(inputList[i]) + delim

    #return
    return output


if __name__ == '__main__':

    spam0 = ['apples','bananas','tofu','cats']
    spam1 = [1,3.14,True,'hello']
    spam2 = []

    print(commaCode(spam0))
    print(commaCode(spam1))
    print(commaCode(spam2))
