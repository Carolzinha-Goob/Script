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
    webbrowser.open("https://dn790002.ca.archive.org/0/items/WinXPProSP3PortugueseBrazilian/pt-br_windows_xp_professional_with_service_pack_3_x86_cd_vl_x14-74137.is")

botao3 = tk.Button(janela, text="XP PROFESSIONAL (x86-X64) (PT-BR)", command=clique)
botao3.pack()

def clique():
    webbrowser.open("https://dn710106.ca.archive.org/0/items/vista_x64/vista_x64.iso")

botao4 = tk.Button(janela, text="VISTA x86-64 (64-bit) Ultimate (PT-BR)", command=clique)
botao4.pack()

def clique():
    webbrowser.open("https://dn721605.ca.archive.org/0/items/Windows7_x86-x64_ptBR_Pack_MSDN/pt_windows_7_professional_with_sp1_x86_dvd_u_677096.iso")

botao5 = tk.Button(janela, text="WINDOWS 7 PROFESSIONAL x86-64 (64-bit) (PT-BR)", command=clique)
botao5.pack()

def clique():
    webbrowser.open("https://dn721505.ca.archive.org/0/items/HRMCCSAX64FREPTBRDV5/HRM_CCSA_X86FRE_PT-BR_DV5.ISO")

botao6 = tk.Button(janela, text="WINDOWS 8 Multi-Edition x86-64 (64-bit) (PT-BR)", command=clique)
botao6.pack()

def clique():
    webbrowser.open("https://dn720708.ca.archive.org/0/items/win-8.1-single-lang-brazilian-portuguese_202301/Win8.1_SingleLang_BrazilianPortuguese_x64.iso")

botao7 = tk.Button(janela, text="WINDOWS 8.1 Multi-Edition x86-64 (64-bit) (PT-BR)", command=clique)
botao7.pack()

def clique():
    webbrowser.open("https://ia600603.us.archive.org/32/items/Win10HomeProTH2PTBR/Win10_1511_2_BrazilianPortuguese_x64.iso")

botao8 = tk.Button(janela, text="WINDOWS 10 Multi-Edition x86-64 (64-bit) (PT-BR)", command=clique)
botao8.pack()

def clique():
    webbrowser.open("https://software.download.prss.microsoft.com/dbazure/Win11_25H2_BrazilianPortuguese_x64_v2.iso?t=68382c8c-5478-4dbc-8f54-60139b7a0272&P1=1787068322&P2=602&P3=2&P4=gy9XjV4oZm5PlMbngilR8yhAgpfIxR%2f4nktqUJpKosmAHjujfFH1PlM4FCF6Wg%2bu5SLPzsVR1SiwXBc3Sxumttbp7AEDkR2oygSlUJaxsghuo6qs5bwiKGV%2bSM8b9odasHmfdIl77lD4NNrKcRSsQskvDbpr%2bqixHOEb%2fd6VbuUc%2bNdicuBhl%2b19PYIaDcthONe5DU0nUf9tKrlT7R7kmbigMpMrJsYeLqNkHZ4kQuo3FhntM%2bRn8cEwZGwdlKzdJ9Zu8ERjBmYJqtvP7NaGm7WT1zhpmlPu7VekYOYEG6m4OnYLnjF%2f9pNzILiw8Sfv5wZbe2RdNGWLT9wUiaePAA%3d%3d")

botao9 = tk.Button(janela, text="WINDOWS 11 Multi-Edition x86-64 (64-bit) (PT-BR)", command=clique)
botao9.pack()

janela.mainloop()
