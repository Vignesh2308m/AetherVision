from transformers import AutoModel, AutoTokenizer

class Load_AI():
    def __init__(self):

        model = AutoModel.from_pretrained("distilbert-base-uncased")
        tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
        
        self.layers = []
        for name, param in model.named_parameters():
            self.layers.append({name:param.shape})
         
        self.layers_type = []
        for name, module in model.named_modules():
            self.layers_type.append({name:module}) 
        
        print(self.layers)