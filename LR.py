import numpy as np 
import matplotlib.pyplot as plt 

def estimate_coef(x, y):  
        n = np.size(x)  
        m_x, m_y = np.mean(x), np.mean(y) 
        # calculating cross-deviation and deviation about x 
        SS_xy = np.sum(y*x - n*m_y*m_x) 
        SS_xx = np.sum(x*x - n*m_x*m_x)  
        b_1 = SS_xy / SS_xx 
        b_0 = m_y - b_1*m_x 

        return(b_0, b_1) 

def plot_regression_line(x, y, b): 
        # plotting the actual points as scatter plot 
        plt.scatter(x, y, color = "m", marker = "o", s = 30) 
        # predicted response vector 
        y_pred = b[0] + b[1]*x 
        plt.plot(x, y_pred, color = "g") 
        plt.xlabel('x') 
        plt.ylabel('y') 

        # function to show plot 
        plt.show() 

def main():
        x=[]
        y=[]
        print("Enter the quantity of data u want to feed:")
        n=int(input())
        print("Enter the values of investment:")
        for i in range(0,n):
                c=int(input())
                x.append(c)
        print("Enter the values of areas(in sqrt feet):")
        for j in range(0,n):
                d=int(input())
                y.append(d)
        x=np.array(x)
        y=np.array(y)
        # estimating coefficients 
        b = estimate_coef(x,y)
        print("Estimated coefficients:\nb_0 = {} \nb_1 = {}".format(b[0], b[1]))
        plot_regression_line(x, y, b)
        print("Do u want to estimate future value(yes=1,no=0):")
        ans=int(input())
        if(ans==1):
                print("Enter year for which you want to find the sales:")
                t=int(input())
                h=b[0]+b[1]*t
                print(h)
        else:
                exit()

main() 
 
