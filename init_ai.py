from sklearn import linear_model as lm 


class AI_Interface():
    def __init__(self):

        self.model = lm.LinearRegression() 
        
        self.model.fit(
            [[0],[1],[2]],[0,6,12]
        )

        self.data = self.model.coef_

        pass