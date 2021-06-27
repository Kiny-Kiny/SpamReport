#!/usr/bin/env python
# -*- coding: utf-8 -*-
global R,B,C,Y,G,RT,CY,CO
CO='\033[m';R='\033[1;31m';B='\033[1;34m';C='\033[1;37m';CY='\033[1;36m';Y='\033[1;33m';G='\033[1;32m';RT='\033[;0m';NO_FORMAT="\033[0m";C_GREY89="\033[38;5;254m";C_RED1="\033[48;5;196m"
import smtplib, os, sys, time, ssl
def link():
	os.system("termux-open-url https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4OSggjYOgt8g8HbgSU58LpUqQ5GsD63ipENqa84YegMHionqqvIXMMoc4bqu-C0GH0N--Kal_AFpd5rRJYyO0g-y1AbEQ")

def restart():
    python = sys.executable;os.execl(python, python, *sys.argv)

def clear():
	os.system("clear")
	
try:
	import pyfiglet
except:
	os.system("pip install pyfiglet");restart()
result = pyfiglet.figlet_format("R e q u i e m", font = "cosmic" );clear();print(f'''{C}{G}
{result}
...`
                             .+ss+//oss:`
                         `:oy+-       `:ss+.
                      `/ss/`              -oyo-
                   -+yo:                     `/ys/`
               `:sy+.                           `:sy+.
            `/ss/`                                  -+yo+
           -h/                                         .ys`
          `m-                                        -+ssdo
          -d                                      :sdNNNNNd
          :d                                  `/ymNNNNNNNNd
          :d                               .+hNNNNNNNNNNNNd
          :d                            -odNNNNNNNNNNNNNNNd
          :d                         :sdNNNNNNNNNNNNNNNNNNd
          :d                       +mNNNNNNNNNNNNNNNNNNNNNd
          :d                      sNNNNNNNNNNNNNNNNNNNNNNNd
          :d                      hNNNNNy`yyNNNNNNNNNNNNNNd
          :d                      hNNNNh-.:sNNNNNNNNNNNNNNd
          :d                      hNNNh`+NNNNNNNNNNNNNNNNNd
          -d                      hNNNy  `./mNNNNNNNNNNNNNd
          `m.                     hNNNNdyy- dNNNNNhmNNNNNNs
           :d:                    hNNNNNmh./NNmy/-+mNNNNNy`
            `+ys:`                hNNNh`` yNNNoodNNNNNmy:
               `/yy/.             hNNNNmh/mNNNNNNNNdo-
                  `:syo-          hNNNNNNNNNNNNNh+.
                      .+ys:`      hNNNNNNNNNms/`
                         `/sy+.   yNNNNNNdo-
                             -oyo/+mNmy/.
                                `-:::
{C}\n{C}{G}Coded By:{C} Kiny\n{C}[{R}*{C}] Ative a permissão de baixa segurança e utilize um email por ataque(recomendação)\n{C}Modo: {G}Menu{C}''');link();sus = input(f"\n{C}{Y}O'que deseja fazer?{C}\n{C}[{G}1{C}] Desativar Numero\n{C}[{G}2{C}] Retirar do Contador\n{C}[{G}3{C}] Retirar Banimento{C}[{R}0{C}] Sair\n{C}[{G}Digite a opção{C}]: ")
if sus == '1':
	os.system('python3 spa.py')
elif sus == '2':
	os.system('python3 conta.py')
elif sus == '3':
	os.system('python3 ban.py')
elif sus == '0':
	print(f"{C}{R}Adeus{C}");exit()
else:
	restart()
