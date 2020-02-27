def saveData(arq):
    with open(arq+'.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        return reader
