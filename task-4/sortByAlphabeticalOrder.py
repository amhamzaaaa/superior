class Sorting:
    def __init__( self ):
        self.sorted = None

    def sortByAlphabeticalOrder( self, text ):
        list1 = text.split()
        for x in range(len(list1)):
            for i in range( len(list1)-1-x):
                if list1[i] > list1[i+1]:
                    list1[i],list1[i+1] = list1[i+1],list1[i]

        self.sorted = list1
        print(self.sorted)


a = Sorting()
a.sortByAlphabeticalOrder('I am a boy')
