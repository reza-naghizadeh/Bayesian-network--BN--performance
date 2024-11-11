import numpy as np

# Just to sho full row and column of numpy array
np.set_printoptions(threshold=np.inf)


# Function for reading the data
def readData():
    # first file as df1 (the dataset file)
    df1 = np.loadtxt('insilico_size10_1_timeseries.txt', dtype='str')
    # Second file as df2 (the BN file)
    df2 = np.loadtxt('net1.txt', dtype='str')
    # Second file as df3 (the BN file)
    df3 = np.loadtxt('net2.txt', dtype='str')
    # Some eliminations which are necessary like deleting time column and the genes name row
    df1 = np.delete(df1, 0, 1)
    df1 = np.delete(df1, 0, 0)
    # changing the dataframes' type so we can calculate them
    df1 = df1.astype(float)
    df2 = df2.astype(float)
    df3 = df3.astype(float)
    # Return dataset and BNs
    return df1, df2, df3


# Preprocess function
def preProcess(df1):
    # Find the average
    df1Average = np.average(df1)

    # Loop over the dataset rows and columns and change the variables to 0 and 1 //// bigger than mean will be 1
    # smaller than mean will be 0
    for i in range(0, df1[:, 0].shape[0]):
        for z in range(0, df1[0, :].shape[0]):
            if df1[i, z] >= df1Average:
                df1[i, z] = 1
            else:
                df1[i, z] = 0
    # Return dataset in 0 and 1
    return df1



def configurations(df1, df):
    a = []
    s = 0
    # Finding the ones
    for i in range(0, 10):
        a.insert(i, list(np.argwhere(df[i] == 1)))
    # Changing the ones(a) to list form
    for j in range(0, 10):
        for z in range(0, len(a[j])):
            a[j][z] = int(a[j][z])
    # Finding the configurations
    for k in range(0, len(a)):
        d = np.empty([105, len(a[k])])
        for u in range(0, 105):
            for y in range(0, len(a[k])):
                d[u][y] = df1[u][y]
        # Just keeping the unique configurations
        dd = np.unique(d, axis=0)
        scorePi = score(df1, dd, d, k)
        s = s + scorePi
    return s



def score(df1, dd, d, k):
    zero = 0
    one = 0
    pi = 0
    for i in range(0, len(dd)):
        for j in range(0, 105):
            if (dd[i] == d[j]).all():
                if df1[j, k] == 0:
                    zero += 1
                else:
                    one += 1
        allCount = zero + one
        if one != 0:
            oneC = (one / allCount) * np.log10((one / allCount))
        else:
            oneC = 0
        if zero != 0:
            zeroC = (zero / allCount) * np.log10((zero / allCount))
        else:
            zeroC = 0
        pi = pi + (oneC + zeroC)
        zero = 0
        one = 0
    return pi


def betterOne(finalScoreForDf2, finalScoreForDf3):
    # Changing the results to positive form
    firstBNScore = np.abs(finalScoreForDf2)
    SecondBNScore = np.abs(finalScoreForDf3)
    # Check which one is closer smaller
    if firstBNScore < SecondBNScore:
        return 'First BN'
    else:
        return 'Second BN'


# Simple function to print out the data frames and final score
def printOut(df1, df2, df3, finalScoreForDf2, finalScoreForDf3, finalResult):
    print('*' * 120)
    print('DataSet that we have:')
    print(df1)
    print('*' * 120)
    print('First BN')
    print(df2)
    print('*' * 120)
    print('Second BN')
    print(df3)
    print('*' * 65)
    print('Final score for first BN ', end='    *   ')
    print('Final score for second BN')
    print(finalScoreForDf2, end='          *       ')
    print(finalScoreForDf3)
    print('*' * 65)
    if finalResult == 'First BN':
        print(f'According to the results,  {finalResult} is better with {finalScoreForDf2} score')
    else:
        print(f'According to the results,  {finalResult} is better with {finalScoreForDf3} score')

    print('*' * 65)


def main():
    # Read the files from finder
    df1, df2, df3 = readData()

    # Give the dataset to the preProcess function
    df1 = preProcess(df1)

    # Find the final score for each BN separately
    finalScoreForDf2 = configurations(df1, df2)
    finalScoreForDf3 = configurations(df1, df3)

    # Check witch BN is better
    finalResult = betterOne(finalScoreForDf2, finalScoreForDf3)

    # Print out everything
    printOut(df1, df2, df3, finalScoreForDf2, finalScoreForDf3, finalResult)


main()
