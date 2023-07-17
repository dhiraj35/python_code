import mysql.connector
import socket
import configparser
hostname = socket.gethostname() #get socket server address.
import os
from dotenv import load_dotenv
class Database:

    def __init__(self):
        pass

    def connect(self, conn):

        global conn_Centralise,conn_IDC
        config = configparser.ConfigParser()
        load_dotenv()

        # if (hostname[0:2] == '40' or hostname[0:2] == '64'):
        #     config.read('daemon_dev.ini')
        #     sso_url = "http://192.168.20.237:8080/api/fetch_employee_info.php"
        # elif (hostname[0:2] == '17'):
        #     config.read('daemon.ini')
        #     sso_url = "http://192.168.20.237:8080/api/fetch_employee_info.php"
        # else:
        #     print("Invalid argument passed")
        #     exit()
        #config.read('src/config/'+str(os.getenv('DBFILE')))
        #config.read('src/config/daemon_dev.ini')
        config.read('src/config/'+str(os.getenv('DBFILE')))

        if (conn=='fin'):
            try:
                print(config['pan_india']['host_fin_master'],config['host_fin_master']['us'])
                conn_Centralise = mysql.connector.connect(host= config['pan_india']['host_fin_master'], port= config['host_fin_master']['pt'],user= config['host_fin_master']['us'],password= config['host_fin_master']['ps'])
                curs_Centralise = conn_Centralise.cursor(named_tuple=True,buffered=True)
                return curs_Centralise
            except Exception as error:
                print(error)
                exit()

        elif(conn=='idc') :
            try:
                conn_IDC= mysql.connector.connect(host= config['mumbai']['host_idc'], port= config['host_idc']['pt'],user= config['host_idc']['us'],password= config['host_idc']['ps'])
                curs_IDC = conn_IDC.cursor(named_tuple=True,buffered=True)  
                return curs_IDC
            except Exception as error:
                print("Error in connection", str(error), config['mumbai']['host_idc'])
                exit()

    def disconnect(self,conn): 
        if (conn=='fin') :
            conn_Centralise.close()
        elif(conn=='idc') :   
            conn_IDC.close()

    def isDevelopServer():

        if (hostname[0:2] == '40' or hostname[0:2] == '64'):
            return 1
        elif (hostname[0:2] == '17'):
            return 0
        else:
            print("Invalid argument passed")
            exit()

    def dataSrcs():
        dataSrcArr = ["mumbai", "delhi", "chennai", "kolkata", "bangalore", "ahmedabad", "pune", "hyderabad", "remotecity"]
        return dataSrcArr

    # def executeQuery(query, fin_conn): 
    #     try:    
    #         result_query = fin_conn.execute(query)
    #         data = fin_conn.fetchall()
    #         return data
    #     except Exception as err:
    #         print('error in execution ->', str(err), query) 
    
    def commit(self,conn): 
        if (conn=='fin') :
            conn_Centralise.commit()
        elif(conn=='idc') :   
            conn_IDC.commit()
    
    def CentralCities(self):
        central_cities = {"mumbai":3,"delhi":3,"kolkata":3,"bangalore":3,"chennai":3,"pune":3,"hyderabad":3,"ahmedabad":3,"remotecity":3,"remote_city":3,"remote_cities":3}
        return central_cities        
