#!/usr/bin/python
#inport used librarys
import os
import subprocess 

#create a class
class OperationsAgent:

   def __init__(self, process, action):
      self.process = process
      self.action = action
   
   #execute ovo commands
   def ovo(self):
     cmdovo = '/opt/OV/bin/ovc '
     if action == "start":
       cmd = '/opt/OV/bin/ovc -start'
       os.system(cmd)
       subprocess.Popen([cmdovo, ' -start'], stdout = subprocess.PIPE))
       #do this
       print ("Executing " + process + "and " + action)
     elif action == "stop":
     elif action == "kill":
     elif action == "restart":
     elif action == "status":
     else:
       print("the given argument is incorrect")


      
      
#Call the class and wanted function  
#start de ovo agent
OperationsAgent.ovo("start")


#stop the opcagt agent
OperationsAgent.opcagt("stop")
