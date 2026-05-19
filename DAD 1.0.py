import os
import sys
import datetime 

print("DAD V0.1")
while True:
    komut = input("DAD> ")
    
    if komut == "lama":
        print("LAMA")
    elif komut == "files":
        print("""
        /space
        /system
        /boot
        /kernel
        /shell
        /drivers 
          """) 
    elif komut == "off":
        sys.exit(0)
    elif komut == "view-space":
    	print("SPACE: EMPTY")
    elif komut =="date":
    	print(datetime.datetime.now( ).strftime("%d/%m/%Y "))
    elif komut =="help":
    	print("""
    	COMMANDS:
    		LAMA: PRİNT LAMA 
    		FİLES: VİEW FİLES 
    		OFF: EXİT
    		VİEW: VİEW FİLES
    		DATE: SHOW DATE
    		HELP: VİEW THİS MENU 
    		    """)
    elif komut =="view-system":
    	print("""
    	*KERNEL.PY
    	        """)
    	
    else:
        print(f"'{komut}' NOT FOUND THIS COMMAND ")