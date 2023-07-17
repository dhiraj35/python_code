from src.config.database import *

 cursor = db.connect('fin')
        updateStatus = 0
        errMsg = 'Something Went Wrong'
        try:
            masterCountQry = "SELECT * FROM db_finance.tbl_corporate_child where master_id='"+str(masterId)+"' and  child_parentid='"+str(accContractID)+"' and child_datasrc='"+str(data_src)+"' "
            cursor.execute(masterCountQry)
            masterCountData = cursor.fetchone()
            if (masterCountData != None):
