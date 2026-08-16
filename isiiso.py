import tkinter as tk
import webbrowser 

janela = tk.Tk()
janela.title("ISO-BR")
janela.geometry("400x300")

texto = tk.Label(janela, text="ISO-BR")
texto.pack(pady=20)



def clique():
    webbrowser.open("https://download2444.mediafire.com/4clqq0r3gjgg1t4D5h9c1DaYJGxpkkIz_AFhLmL5zaTaFHebVqaEl5E4xpcHgwmd6v7uS1JPfrmbay-5Msrf7uHuB7_y-lG0ZXbSKd1Ap8o3Bj8K9JRHKY_36ezQeRjjTi3GL4W-kDk15mTLKrc6MaovLxAO1kQsUneWeWp5Zx54hfg/i3gjydlmg1fe91a/WinPE11_10_8_Sergei_Strelec_x86_x64_2026.07.09_English.rar")  

botao1 = tk.Button(janela, text="Sergei Strelec x86-x64 WinPE11-10-8 (EN)", command=clique)
botao1.pack()

def clique():
    webbrowser.open("https://dn721604.ca.archive.org/0/items/ms-dos-6.22_dvd/MS-DOS%206.22.iso")

botao2 = tk.Button(janela, text="MS-DOS 6.22 (EN)", command=clique)
botao2.pack()

def clique():
    webbrowser.open("https://dl.os.click/OS/NT5.1/2600.5512/Pro/pt-br_windows_xp_professional_with_service_pack_3_x86_cd_x14-80400.iso?md5=l-_r1BWInpYTUAeanFwyAA&expires=1786927816")

botao3 = tk.Button(janela, text="XP PROFESSIONAL (x86-X64) (PT-BR)", command=clique)
botao3.pack()

def clique():
    webbrowser.open("https://dl.os.click/OS/NT6.0/6002.18005/client/Multi/pt_windows_vista_with_sp2_x64_dvd_x15-36319.iso?md5=_nJUCRRio_7trFqrCj79pA&expires=1786928022")

botao4 = tk.Button(janela, text="VISTA x86-64 (64-bit) Multi-Edition (PT-BR)", command=clique)
botao4.pack()

def clique():
    webbrowser.open("https://dl.os.click/OS/NT6.1/7601.17514/client/Ultimate/pt_windows_7_ultimate_with_sp1_x64_dvd_u_677358.iso?md5=igRNA9jRAR1_k6naVl_a1Q&expires=1786924853")

botao5 = tk.Button(janela, text="WINDOWS 7 PROFESSIONAL x86-64 (64-bit) (PT-BR)", command=clique)
botao5.pack()

def clique():
    webbrowser.open("https://dl.os.click/OS/NT6.2/9200.16384/client/en_windows_8_x64_dvd_915440.iso?md5=CvcWAVHhifoWpxfMUymPEw&expires=1786924849")

botao6 = tk.Button(janela, text="WINDOWS 8 Multi-Edition x86-64 (64-bit) (PT-BR)", command=clique)
botao6.pack()

def clique():
    webbrowser.open("https://dl.os.click/OS/NT6.3/9600/16384/client/en_windows_8_1_x64_dvd_2707217.iso?md5=qnNIm2YvwkvvwQDzuluq0A&expires=1786924802")

botao7 = tk.Button(janela, text="WINDOWS 8.1 Multi-Edition x86-64 (64-bit) (PT-BR)", command=clique)
botao7.pack()

def clique():
    webbrowser.open("https://dl.os.click/OS/NT10/2016_LTSB/Enterprise/pt_windows_10_enterprise_2016_ltsb_x64_dvd_9060113.iso?md5=AQbPWM66DImSLCBtJII83A&expires=1786929512")

botao8 = tk.Button(janela, text="WINDOWS 10 Multi-Edition x86-64 (64-bit) (PT-BR)", command=clique)
botao8.pack()

def clique():
    webbrowser.open("https://dl.os.click/OS/NT10/Win11_26100/1742/en-us_windows_11_consumer_editions_version_24h2_x64_dvd_1d5fcad3.iso?md5=dycBh5Dwxkt0a8a3mhb5MA&expires=1786924845")

botao9 = tk.Button(janela, text="WINDOWS 11 Multi-Edition x86-64 (64-bit) (PT-BR)", command=clique)
botao9.pack()

janela.mainloop()
