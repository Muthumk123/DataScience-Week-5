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
    def mean_median_mode_percentile(dataset,quan):
         import numpy as np
         import pandas as pd
         descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%"],columns=quan)
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
         return descriptive
                
                    