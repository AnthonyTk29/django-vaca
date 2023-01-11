from tkinter import N
import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO

import numpy as np 

def get_graph():
    buffer= BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png= buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(a,b):
    #array.reshape(-1, 1)
    #array.reshape(1, -1) 
    n=len(a)
    x=np.array(a)
    y=np.array(b)
    #crear el modelo
    sumx=sum(x)
    sumy=sum(y)
    sumx2=sum(x*x)
    sumy2=sum(y*y)
    sumxy=sum(x*y)
    promx=sumx/n
    promy=sumy/n
    m=(sumx*sumy - n*sumxy)/(sumx**2 - n*sumx2)
    b=promy - m*promx
    
    viz_train = plt
    viz_train.switch_backend('AGG')
    viz_train.figure(figsize=(7,5))
    viz_train.plot(x, y,'o',label='Datos')
    viz_train.plot(x, m*x + b,label='Ajuste')
    viz_train.grid()
    viz_train.legend(loc=4)
    viz_train.title('Predicción de producción')
    viz_train.xlabel('Kilos de comida')
    viz_train.ylabel('Litros de leche')
    viz_train.tight_layout()
    graph=get_graph()
    return graph

