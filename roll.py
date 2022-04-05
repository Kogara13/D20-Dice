#!/usr/bin/python

import sys 
import random

#Change the color of the dice by changing the text at the beginning of the print statements
# \033[1;30m (Black)
# \033[1;31m (Red)
# \033[1;32m (Green)
# \033[1;33m (Yellow)
# \033[1;34m (Blue)
# \033[1;35m (Purple)

#For additional formating options, see: https://stackabuse.com/how-to-print-colored-text-in-python/

def roll4():
    Rn = random.randint(1,4)
    print("""\033[1;32m
          ;;
        ,;  ;,
       ,;    ;,
      ,;      ;,
     ,;        ;,
    ,;          ;, 
   ,;            ;,
  ,;              ;,
 ,;                ;, 
,;        {}         ;,
::::::::::::::::::::::
    """.format(Rn))

def roll6():
    Rn = random.randint(1,6)
    print("""\033[1;32m
 ::::::::::::::
 ::          ::  
 ::          ::
 ::    {}     ::
 ::          ::
 ::          ::                
 :::::::::::::: 

    """.format(Rn))

def double6():
    Rn = random.randint(1,6)
    Rm = random.randint(1,6)
    print("""\033[1;32m
 ::::::::::::::   ::::::::::::::
 ::          ::   ::          ::
 ::          ::   ::          ::
 ::    {}     ::   ::     {}    ::
 ::          ::   ::          ::
 ::          ::   ::          ::             
 ::::::::::::::   ::::::::::::::

    """.format(Rn, Rm))
    Rn2 = random.randint(1,6)

def roll20():
    Rn = random.randint(1,20)
    #Account for single and double digit numbers moving parts of the dice
    if Rn > 9:
        print("""\033[1;32m             
            ,:::,
       ,,,:;  :  ;:,,, 
   ,,,:       :       :,,, 
,,;...........:...........;,,
; ;          ;';          ; ;
;  ;        ;   ;        ;  ;
;   ;      ;     ;      ;   ;
;    ;    ;       ;    ;    ;
;     ;  ;   {}    ;  ;     ;
;      ;:...........:;      ;
;     , ;           ; ,     ;
;   ,'   ;         ;   ',   ;
'';'      ;       ;      ';''
   ''';    ;     ;    ;'''         
       ''':;;   ;;:'''
            ':::' 
    """.format(Rn))
        
    else: 
        print("""\033[1;32m             
            ,:::,
       ,,,:;  :  ;:,,, 
   ,,,:       :       :,,, 
,,;...........:...........;,,
; ;          ;';          ; ;
;  ;        ;   ;        ;  ;
;   ;      ;     ;      ;   ;
;    ;    ;       ;    ;    ;
;     ;  ;    {}    ;  ;     ;
;      ;:...........:;      ;
;     , ;           ; ,     ;
;   ,'   ;         ;   ',   ;
'';'      ;       ;      ';''
   ''';    ;     ;    ;'''         
       ''':;;   ;;:'''
            ':::' 
    """.format(Rn))
    if Rn == 20:
        print('NAT 20!')

try:
    if sys.argv[1] == "-4":
        roll4()
    elif sys.argv[1] == "-6":
        roll6()
    elif sys.argv[1] == "-d6":
        double6()
    elif sys.argv[1] == "-20":
        roll20()
except:
    print('error')
