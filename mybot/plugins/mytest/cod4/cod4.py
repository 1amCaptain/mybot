import os
import time
from ..main_computer.computerInfo import computerInfo
COD4_PATH_ROOT = r"H:\cod4\COD4R\COD4"
# COD4_PATH_SERVERCFG = r"main\server.cfg"
COD4_FILE_SERVERBAT = "server.bat"
COD4_EXE = "h1-mod.exe"

class cod4(computerInfo):
    def __init__(self) -> None:
        pass
    def Check_Server(self):
        if self.getPidByName(COD4_EXE):
            return True,"h1-mod.exe已存在"
        return False,"未找到h1-mod.exe进程"

    def Start_Server(self):
        msg= ""
        server_msg = "connect 192.168.0.103:27020;password 1234"
        StartServer = os.path.join(COD4_PATH_ROOT,COD4_FILE_SERVERBAT)
        os.chdir(COD4_PATH_ROOT)
        os.system(StartServer)
        time.sleep(10)
        status,_ = self.Check_Server()
        if status:
            msg = "服务器已开启!!!\n服务器连接信息{}".format(server_msg)
        else:
            msg = "开启服务器失败,或者h1-mod.exe已经开启"
        return status,msg

    def Kill_Server(self):
        msg = ""
        status = self.killProcess(COD4_EXE)
        if status:
            msg = "服务器已关闭"
        else:
            msg = "服务器未正常关闭或者h1-mod.exe已不存在"
        return status,msg

    def Restart_Server(self):
        if self.Check_Server():
            self.killProcess(COD4_EXE)
        status,msg = self.Start_Server()
        return status,msg

    def returnFun(self):
        return dict({"start":"Start_Server",
        "close":"Kill_Server",
        "restart":"Restart_Server",
        "check":"Check_Server"})
    
    def test(self):
        print("ttttttttttttttttt")

    