#!/usr/bin/python
#Mr.KaitoX
 
def kaito():
     
    code = raw_input(" Encode: ")
    
    sc = "\\x" + "\\x".join("{0:x}".format(ord(code)) 
    
    for code in code)
    
    print "\n shellcode =('" + sc + "'); exec(shellcode)"; kaito();
    
kaito()