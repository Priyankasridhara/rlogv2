#import pandas as pd
#df=pd.read_csv("Mandate.csv")
#u=df.iloc[:, 0:17]
#for k in range(0,17):
    #u[k]=df.iloc[:,k]
    #print(u[k])

 #mydict = {'ID':u[0], 'Job_ID':u[1],'Company Name':u[2],'Job Categroy':u[4],'Job Sub Category':u[5],
# 'HR Name':u[6],'Job Role':u[7], 'skills Required': u[8],'Creation Date':u[9], 'End Date':u[10],
#'Number_of_openings':u[11],'Job Location':u[12],'Designation_of_job':u[13],'ctc':u[14],'Min Exp':u[15],
#'Max Exp':u[16], 'CompanyID':u[1]}

#columns = ', '.join(str(x).replace('/', '_') for x in mydict.keys())
#values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in mydict.values())
#sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('mandate', columns, values)
#print(sql)