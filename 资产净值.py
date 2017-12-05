import xdrlib,sys
import xlrd
def open_excel(file='D:\基金公司\数据库-制表符\资产组合-基金公司维度.xlsx'):
    try:
        data=xlrd.open_workbook('D:\基金公司\数据库-制表符\资产组合-基金公司维度.xlsx')
        return data
    except Exception as e:
        print (str(e))
def excel_table_byindex(file='D:\基金公司\数据库-制表符\资产组合-基金公司维度.xlsx',colnameindex=0,by_index=0):
    data=open_excel(file='D:\基金公司\数据库-制表符\资产组合-基金公司维度.xlsx')
    table=data.sheets()[by_index]
    nrows=table.nrows
    ncols=table.ncols
    colnames=table.row_values(colnameindex)
    list=[]
    for rownum in range(1,nrows):
        row=table.row_values(rownum)
        if row:
            app={}
            for i in range(len(colnames)):
                app[colnames[i]]=row[i]
            list.apend(app)
    return list




