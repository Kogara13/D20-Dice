#!/usr/bin/python

import random 

#Change the color of the dice by changing the text at the beginning of the print statements
# \033[1;30m (Black)
# \033[1;31m (Red)
# \033[1;32m (Green)
# \033[1;33m (Yellow)
# \033[1;34m (Blue)
# \033[1;35m (Purple)

#For additional formating options, see: https://stackabuse.com/how-to-print-colored-text-in-python/

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
            ':,:' 
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
            ':,:' 
""".format(Rn))
if Rn == 20:
    print('NAT 20!')
