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
class central_tendency_Univariate():
    def mean_median_mode(dataset,quan):
        import pandas as pd
        descriptive=pd.DataFrame(index=["Mean","Median","Mode"],columns=quan)
        for ColumnName in quan:
            # descriptive[ColumnName]["Mean"]=dataset[ColumnName].mean()
            # descriptive[ColumnName]["Median"]=dataset[ColumnName].median()
            # descriptive[ColumnName]["Mode"]=dataset[ColumnName].mode()[0]
             descriptive.loc ["Mean",ColumnName]=dataset[ColumnName].mean()
             descriptive.loc ["Median",ColumnName]=dataset[ColumnName].median()
             descriptive.loc ["Mode",ColumnName]=dataset[ColumnName].mode()[0]
        return descriptive
            