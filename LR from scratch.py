#Goal:to create a linear regression model from scratch lets get started then
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import IPython as ip

def linear_regression():
    '''
    ill think about it
    1)y= mx + c is our golden equation where we will  try to predict y on
    the basis of the slope and constant we calculate on the basis of our
    training data with an error fuction and some wieghts and a  learning rate
    '''

    #importing dataset and plot it
    data_raw=pd.read_csv("weight-height.csv")
    data_main=np.array(data_raw)
    data_a=data_main[:8000,:]
    data_test=data_main[8000:,:]
    plt.scatter(data_a[:20,1],data_a[:20,2])
    #plt.show()

    '''
    The plot shows both values of x and y correlated to each other that means both are
    relted to each other linearly now we will try to fit a line to this data.
    '''
    #Now lets try and  plot out first line

    
    #plt.show()
    

    slope=(data_a[1,2]-data_a[0,2])/(data_a[1,1]-data_a[0,1])
    print("intial slope="+str(slope))
    constant=data_a[0,2]-(slope*data_a[0,1])
    print("intial constant="+str(constant))

    #now we start the mamoth task of updating slope and the constant

    learning_rate=.01

    for x,y in data_a[2:,1:]:
        #now updating slope
        t_slope=y/x
        if slope>t_slope:
            slope=slope-(t_slope*learning_rate)
        else:
            slope=slope+(t_slope*learning_rate)
        #now updating constant

        t_constant=y-(slope*x)

        if t_constant>constant:
            constant=constant-(t_constant*learning_rate)
        else:
            constant=constant+(t_constant*learning_rate)

    print("final slope="+str(slope))
    print("final constant="+str(constant))

    '''
    now that we ahve our slope and constant we have to import test
    data and get our predicitons
    '''
    
    for x,y in data_test[:,1:]:
        y_pred=x*slope+constant
        print(y_pred,y)

    return None    
    
    

linear_regression()
    
