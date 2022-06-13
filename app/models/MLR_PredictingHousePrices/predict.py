from sklearn import linear_model
import pickle


class PredictHousePrice():

    def __init__(self):
        self.loaded_model = pickle.load(open('app/models/MLR_PredictingHousePrices/model.pickle.sav', 'rb'))

    def getPrice(self,features):

        predictions = self.loaded_model.predict(features)
        results = []
        for y in predictions:
            results.append(round(y, 2))

        return results