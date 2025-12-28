class Univariate():
    def QuanQual(dataset):
        qual=[]
        quan=[]
        for columnName in dataset.columns:
            #print(columnName)
            if (dataset[columnName].dtypes=='O'):
                #print("qual")
                qual.append(columnName)
            else:
                #print("quan")
                quan.append(columnName)
        return quan,qual
class central_tendency_percentile():
    def MMM_per_IQR(dataset,quan):
         import numpy as np
         import pandas as pd
         descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%",                                                                        "Q4:100%","IQR","1.5rule","Lesser","Greater","Min","Max","kurtosis","skew","Variance","Standdev"],columns=quan)                                  
         for ColumnName in quan:
              # descriptive[ColumnName]["Mean"]=dataset[ColumnName].mean()
              # descriptive[ColumnName]["Median"]=dataset[ColumnName].median()
              # descriptive[ColumnName]["Mode"]=dataset[ColumnName].mode()[0]
                descriptive.loc ["Mean",ColumnName]=dataset[ColumnName].mean()
                descriptive.loc ["Median",ColumnName]=dataset[ColumnName].median()
                descriptive.loc ["Mode",ColumnName]=dataset[ColumnName].mode()[0]
                descriptive.loc ["Q1:25%",ColumnName]=dataset.describe()[ColumnName]["25%"]
                descriptive.loc ["Q2:50%",ColumnName]=dataset.describe()[ColumnName]["50%"]
                descriptive.loc ["Q3:75%",ColumnName]=dataset.describe()[ColumnName]["75%"]
                descriptive.loc ["99%",ColumnName]=np.percentile(dataset[ColumnName],99)
                descriptive.loc ["Q4:100%",ColumnName]=dataset.describe()[ColumnName]["max"]
                descriptive.loc ["IQR",ColumnName]=descriptive.loc ["Q3:75%",ColumnName]-descriptive.loc ["Q1:25%",ColumnName]
                descriptive.loc ["1.5rule",ColumnName]=1.5* descriptive.loc ["IQR",ColumnName]
                descriptive.loc ["Lesser",ColumnName]=descriptive.loc ["Q1:25%",ColumnName]-descriptive.loc ["1.5rule",ColumnName]
                descriptive.loc ["Greater",ColumnName]=descriptive.loc ["Q3:75%",ColumnName]+descriptive.loc ["1.5rule",ColumnName]
                descriptive.loc ["Min",ColumnName]=dataset[ColumnName].min()
                descriptive.loc ["Max",ColumnName]=dataset[ColumnName].max()
                descriptive.loc ["kurtosis",ColumnName]=dataset[ColumnName].kurtosis()
                descriptive.loc ["skew",ColumnName]=dataset[ColumnName].skew()
                descriptive.loc ["Variance",ColumnName]=dataset[ColumnName].var()
                descriptive.loc ["Standdev",ColumnName]=dataset[ColumnName].std()
         return descriptive
    def outlayer_column_names(dataset,quan):
        central_tendency_per_IQR=central_tendency_percentile.MMM_per_IQR(dataset,quan)
        descriptive=central_tendency_per_IQR # Automation after checking replaceing the value Lesser should not greater min
        lesser=[]
        greater=[]
        for ColumnName in quan:
            if(descriptive.loc ["Min", ColumnName]<descriptive.loc["Lesser", ColumnName]):
                lesser.append(ColumnName)
            if(descriptive.loc ["Max", ColumnName] > descriptive.loc["Greater", ColumnName]):
                greater.append(ColumnName)
        return lesser,greater
    def replace_in_the_outlayer(dataset,quan):
        central_tendency_per_IQR=central_tendency_percentile.MMM_per_IQR(dataset,quan)
        descriptive=central_tendency_per_IQR 
        lesser, greater =central_tendency_percentile.outlayer_column_names(dataset, quan)
        for ColumnName in lesser:
            dataset[ColumnName] [dataset[ColumnName]<descriptive.loc["Lesser", ColumnName]]=descriptive.loc["Lesser", ColumnName]
        for ColumnName in greater:
            dataset[ColumnName] [dataset[ColumnName]>descriptive.loc["Greater", ColumnName]]=descriptive.loc["Greater", ColumnName]
        return  lesser, greater
      # after checking replaceing with  value to the dataset not to descriptive 
    def freqTable(ColumnName,dataset):
        import pandas as pd
        freqTable=pd.DataFrame(columns=["Unique_Values","Frequencey","Releative_Frequencey","Cusum"])
        freqTable["Unique_Values"]=dataset[ColumnName].value_counts().index
        freqTable["Frequencey"]=dataset[ColumnName].value_counts().values
        freqTable["Releative_Frequencey"]=(freqTable["Frequencey"]/103)
        freqTable["Cusum"]=freqTable["Releative_Frequencey"].cumsum()
        return freqTable

        
                    