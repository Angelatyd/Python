# Python调用VBA
import win32com.client
import os.path

xlApp = win32com.client.Dispatch('Excel.Application')
xlsPath = os.path.expanduser(r'C:\Users\atian1\PycharmProjects\PythonTools\test.xlsm')
wb = xlApp.Workbooks.Open(Filename=xlsPath)
xlApp.Run('Format')
wb.Save()
xlApp.Quit()
print("Macro ran successfully!")