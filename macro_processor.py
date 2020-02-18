# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
macroList = []

class Macro:
    def __init__(self, name, args, body):
        self.name = name
        self.args = args
        self.body = body

def searchMacro(src):
    srcCode = src.split()
    print("The splitted code is:")
    print(srcCode)
    for i in range(len(srcCode)):
        if(srcCode[i] == '#define'):
           if(srcCode[i+2].isalnum()):
               print('True')
           macroList.append(Macro(srcCode[i+1],srcCode[i+2],srcCode[i+3]))
           
       
def expandMacro(src):
    srcCode = src.split()
    for i in range(len(srcCode)):
        #print(macroList)
        if(srcCode[i-1] != '#define'):
           for macro in macroList:
               if(srcCode[i] == macro.name):
                    arg = srcCode[i+1]
                    print(arg[1])
                    block = macro.body.replace(macro.args[1],arg[1])
                    print(block)
                    srcCode[i] = block
                    #print(srcCode[i])
                    srcCode[i+1] = ''
                    
    print(' '.join(srcCode))            

#srcCode = "#define SUB (X) X=X-15 #define DIV (Y) Y=Y/5 #include<stdio.h> #include<conio.h> int main() { int a = 10 ; int b = 20 ; SUB (a) ;  DIV (b) ; return 0 ;}"
srcCode=input("Enter the source code in C: \n")
print("\n")
searchMacro(srcCode)    
expandMacro(srcCode)

'''#define SUB (X) X=X-Y 
   #define DIV (Y) Y=X/Y 
   #include<stdio.h> 
   #include<conio.h>
   int main() 
   { 
    int a = 10 ; 
    int b = 20 ;
    SUB (a) ;
    DIV (b) ;
    return 0 ;
    }'''
   
    
    
'''macroList = []

class Macro:
    def __init__(self, name, args, body):
        self.name = name
        self.args = args
        self.body = body

def searchMacro(src):
    srcCode = src.split()
    for i in range(len(srcCode)):
        if(srcCode[i] == '#define'):
           if(srcCode[i+2].isalnum()):
               print('Ture')
           macroList.append(Macro(srcCode[i+1], srcCode[i+2], srcCode[i+3]))
           
def expandMacro(src):
    srcCode = src.split()
    for i in range(len(srcCode)):
        if(srcCode[i-1] != '#define'):
            for macro in macroList:
                if(srcCode[i] == macro.name):
                    arg = srcCode[i+1]
                    #print(arg[1])
                    block = macro.body.replace(macro.args[1],arg[1])
                    srcCode[i] = block
                    srcCode[i+1] = ''
                    
    print(' '.join(srcCode))                

srcCode = input("Enter the C program: \n")
print("\n")
print(srcCode)
searchMacro(srcCode)    
# print('Macros', macroList[0].name)
expandMacro(srcCode)'''
