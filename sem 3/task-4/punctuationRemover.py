class Remover:
    def __init__(self):
        self.p = '!"£$%^&*()?:;@.,<>\''
        self.text = []

    def punctuationRemover( self, input_text):
        for i in range(len(input_text)):
            if input_text[i] not in self.p:
                self.text.append(input_text[i])

        text = ''.join(self.text)
        return text
    

a = Remover()
a.punctuationRemover('@Hamz@! h1')
