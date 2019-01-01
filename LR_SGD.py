import csv
def predict(row, coefficients):
	yhat = coefficients[0]
	for i in range(len(row)-1):
		yhat += coefficients[i + 1] * row[i]
	return yhat
 
# Estimate linear regression coefficients using stochastic gradient descent
def coefficients_sgd(train, l_rate, n_epoch):
	coef = [0.0 for i in range(len(train[0]))]
	for epoch in range(n_epoch):
		sum_error = 0
		for row in train:
			yhat = predict(row, coef)
			error = yhat - row[-1]
			sum_error += error**2
			coef[0] = coef[0] - l_rate * error
			for i in range(len(row)-1):
				coef[i + 1] = coef[i + 1] - l_rate * error * row[i]
	return coef
def main():
        x=[]
        y=[]
        # Importing training set
        csv_file_name=input('CSV File Name:')
        f=open(''+csv_file_name+'')
        csv_f = csv.reader(f)
        for row in csv_f:
                x.append(row[0])
                y.append(row[1])
        # Calculate coefficients
        for Z in range(len(x)):
                ds=ds(x[Z],y[Z])
        l_rate = 0.001
        n_epoch = 50
        coef=coefficients_sgd(dataset, l_rate, n_epoch)
        print(coef)
main()
