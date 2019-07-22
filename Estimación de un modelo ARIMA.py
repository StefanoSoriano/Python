
import pandas as pd ### 
import numpy as np  ######  Paquetes de computación científica
import scipy as sp  ###
                   
# Cargando dataset desde la web
var = "\car.csv"
path = "F:\OneDrive\Documentos\Computer Science\Python\datasets" + var
car = pd.read_csv(path, header = None)
headers = ["Weigth_1","Weigth_2","Number_1","Number_2","Heigth", "Weidth","Brand"]
car.columns = headers

car.describe(include="all")
car.info()

#  Accediendo a las columnas del DataFrame

car["Weigth_1"]
car["Heigth"]
car["Brand"]

# Tratando valores perdidos

#car.dropna(subset=["Brand"],axis=0, inplace = True)
Number = car["Number_1"].replace("5more", 5)
Number = Number.astype("int")
mean = Number.mean()
mean

#  Variable dummie 

Weidth_y_n = pd.get_dummies(car["Weidth"])


car["Number_1"] = car["Number_1"].replace("5more", 5)
car["Number_1"] = car["Number_1"].astype(int)
bins = np.linspace(min(car["Number_1"]),max(car["Number_1"]),4)
labels = ["Low","Medium","High"]
car["Number_1_Category"] = pd.cut(car["Number_1"], bins, labels= labels, include_lowest= True)


