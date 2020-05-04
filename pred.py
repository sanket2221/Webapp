import pickle
import numpy as np

model = pickle.load(open('regressor.pkl','rb'))

g=model.predict(np.array([5]).reshape(1,-1))