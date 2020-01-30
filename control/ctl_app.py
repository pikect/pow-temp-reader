import sys
import json
import time
import paramiko
import threading
from PyQt5.QtWidgets import QWidget
from views import main_window

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.push_close.clicked.connect(self.closeEvent)
        self.show()
        self.runThread = threading.Thread(target=self.run)
        self.runThread.setDaemon(True)
        self.connectToDevice()



    def connectToDevice(self):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.load_system_host_keys()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        with open("client.json") as jfile:    
            self.file = json.load(jfile)
            self.ip = self.file["ip"]
            
        try:
            self.ssh_client.connect(self.ip, username='root', password='netico987', timeout=10)
            self.sftp_client = self.ssh_client.open_sftp()
            self.runThread.start()

        except Exception as e:
            text = "Connection Error: " + str(e)
            print(text)
            time.sleep(1)
            sys.exit(1)

    def run(self):
        while True:
                try:
                    remote_file = self.sftp_client.open('/tmp/urtu/pow/temperature')
                    try:
                        temperature = remote_file.read()
                        temperature = temperature.decode()
                        self.ui.lcdNumber.setProperty("value", temperature)
                    finally:
                        remote_file.close()
                    time.sleep(5)

                except Exception as e:
                    self.ssh_client.close()
                    print(e)
                    sys.exit(1)

    def closeEvent(self):
        sys.exit(0)
