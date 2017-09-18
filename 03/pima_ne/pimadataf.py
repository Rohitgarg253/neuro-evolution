

import numpy as np
import pylab as pl
def myrange(start,end,step):
    i=start
    while i+step < end:
        i+=step
        yield i
def standardize_dataset(traindata, means, stdevs):
    for row in traindata:
        for i in range(len(row)):

            row[i] = (row[i] - means[i])
            if stdevs[i]:
                row[i]/=stdevs[i]
def give_data():
    #1. make iris.data in usable form
    #2. make input set and output set out of it
    #3. make setpool out of the dataset
    #4. make pcn and train it
    #5. test on validation and testing set



    
    pimadata=np.loadtxt("pima_dataset.csv", delimiter=',')
    print("Hello")
    np.random.shuffle(pimadata)
    
    nin =8;
    nout=2;
    pimadata=pimadata.astype(float)
    traindata=pimadata
    means= traindata.mean(axis=0)

    stdevs=np.std(traindata,axis=0)
    # standardize dataset
    standardize_dataset(traindata[:,:8],means,stdevs)
    rest_setx=pimadata[:538,:8]#tuple of two shared variable of array
    rest_sety=pimadata[:538,8:]
    test_setx=pimadata[538:,:8]
    test_sety=pimadata[538:,8:]
  
    return ((rest_setx,rest_sety),(test_setx,test_sety))

def main():
    print(give_data()[1])
if __name__=="__main__":
    main()