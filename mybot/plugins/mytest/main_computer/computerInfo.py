import psutil
import os
class computerInfo():
    def __init__(self) -> None:
        pass
    def getPidByName(self,process_name):
        pid_byname = ""
        try:
            for proc in psutil.process_iter():
                if proc.name() != process_name:
                    continue
                pid_byname = str(proc.pid)
        except Exception as e:
            print(e)
        return pid_byname

    def MemInfo(self):
        Mem_Info = psutil.virtual_memory()
        used = round(Mem_Info[3]/1024/1024/1024,2)
        free = round(Mem_Info[4]/1024/1024/1024,2)

        return used,free

    def killProcess(self,process_name):
        pid = self.getPidByName(process_name)
        if pid:
            kill_msg = "taskkill /f /pid {}".format(pid)
            os.system(kill_msg)
            return True
        return False
       