import datetime #date e hora
import re # regex para manipular palavras
import webbrowser # manipular e ter acesso a web
from tkinter import * # interface grafica
from PIL import ImageTk, Image # imagem no tkinter
from tkinter import messagebox # mensagem no tkinter
from load_json import  *

#Projeto Projeto Transversal em Redes 1 - henrique oliveira da rocha - 202066910



class Pris:

    def __init__(self):
        self.window = Tk()
        self.window.title('UNB - Projeto transversal')
        self.hoje = datetime.date.today()
        # self.hour = datetime.datetime.today() {self.hour: %H:%M}
        self.ferias = datetime.date(2023, 2, 18)
        self.falta = self.ferias - self.hoje
        self.foto = ImageTk.PhotoImage(Image.open("unbbaaaaaaa.jpg"))
        self.foto2 = ImageTk.PhotoImage(Image.open("IMG-20230119-WA0013.jpg"))
        self.window.resizable(width=True, height=True)
        self.window.configure(width=1000, height=600, bg="#2E2E2E")
        self.Config_aplicativo()
        self.home_page()

    # deixa o app rodando
    def run(self):
        self.window.mainloop()


    def home_page(self):

        # barra de tarefas superior da homepage
        barra_superior_hp = Label(
        self.window,  bg="#000000", fg="#F5F5F5",
        text=f" 🤖\n", font=("Comic Sans MS", "20", "bold"), pady=1)
        barra_superior_hp.place(relwidth=1, rely=0.00004)

        foto_label_hp = Label(image=self.foto2, bg="#000000")
        foto_label_hp.place(relwidth=1,  rely=0.10)

        # barra de tarefas inferior da homepage
        barra_inferior_hp = Label(self.window, text="202066910", bg="#000000", height=120, pady=10)
        barra_inferior_hp.place(relwidth=1, rely=0.800)

        iniciar = Button(text="⏭️\nIniciar Pris", font=("Comic Sans MS", "11", "bold"), bg="#000000", fg="#FFFFB9", command=self.Config_aplicativo)
        iniciar.place(relwidth=0.099, relheight=0.08, rely=0.8, relx=0.32)

        sair = Button(text="⏹️\nSair", font=("Comic Sans MS", "11", "bold"), bg="#000000", fg="#FFFFB9", command= self.sair)
        sair.place(relwidth=0.090, relheight=0.08, rely=0.8, relx=0.59)

        infor = Button(text="   📰️\nProjeto", font=("Comic Sans MS", "11", "bold"), bg="#000000", fg="#FFFFB9",
                      command=self.info)
        infor.place(relwidth=0.090, relheight=0.08, rely=0.8, relx=0.46)

    def sair(self):
        exit()

    def info(self):
        messagebox.showinfo("Sobre o Projeto" , "Universidade de Brasília - Projeto Transversal em Redes\n\n""Ola! beleza ? Um pouco sobre o projeto\n\n" "Este Projeto foi idealizado na Disciplina de Projeto Transversal em Redes 1\n\nA ideia e ajudar discentes de Engenharia na melhor forma possivel, especificamente, calouros(a), no andamento inicial do curso, entretanto, caso seja necessario, este codigo pode ser adaptado para qualquer outro curso.\n\nEspero que este aplicativo seja util! Obrigado!\n\nHenrique Oliveira da Rocha - Eng de Redes - 202066910")

    def respostas(self, s): # respostas do bot
        dividir_resposta = re.split(r'\s+|[,?!.()&@]\s*',s.lower())
        # vai passar pente fino
        lista_pontuacao = []
        for respostas_pris in dicionario_pris:
            pontos_respostas = 0
            pontos_demandados = 0 # quantas palavras estao na tag dentro do json
            palavra_chave = respostas_pris["TAG"] # aqui passa as tags para a respostas_pris
            # na tag pode botar qualquer palavra chave, mas como queremos algo mais direto, botei apenas uma em cada
            # faz uma analise se tem alguma palavra tag
            if palavra_chave:
                for palavra in dividir_resposta:
                    if palavra in palavra_chave:
                        pontos_demandados = pontos_demandados + 1 # vai igualar os pontos_demandados = palavra_chave


            if pontos_demandados == len(palavra_chave): # vai dar um check se pontos_demandados estao iguais o total de itens na palavra_chave (tag)
                for palavra in dividir_resposta: # se for certo, mostra que deu certo e as tags estao nos pontos_demandados
                    # se a palavra esta no dicionario do usuario ele retorna
                    if palavra in respostas_pris["usuario"]: # se a pergunta do usuario esta no dicionario de perguntas
                       pontos_respostas = pontos_respostas + 1 # dependendo se tiver uma lista com outros respostas, ele da pontos pra resposta indicada e ela vai ser selecionada
            lista_pontuacao.append(pontos_respostas) # aqui passa a melhor resposta pra lista de pontuacao

        resposta_adequada = max(lista_pontuacao) # vai olhar na lista a resposta com maior ponto
        respostas_pris_posicao = lista_pontuacao.index(resposta_adequada)
        # se nao tiver uma resposta adequada ele da uma resposta de erro
        if resposta_adequada != 0: # se for diferente de 0 ele da um retorno exata da reposta, caso contrario ele retorna uma msg de erro
            return dicionario_pris[respostas_pris_posicao]["pris"]
        elif s == "tchau": # tchau fecha o programa
            return exit()
        else: # msg de erro
            return "pfv, tente ser mais especifio, nome completo do curso, apenas a sigla em minusculo\n             ou pesquise no botão do google, talvez eu nao tenha tudo =/"

    def Config_aplicativo(self):

        # barra de tarefas superior
        barra_superior = Label(
        self.window,  bg="#2E2E2E", fg="#FFFFFF",
        text=f"🤖 Assistente Virtual Universitario  \nHoje:{self.hoje: %d / %m / %y} | Falta {self.falta.days} Dias para as Ferias", font=("Comic Sans MS", "12", "bold"), pady=1)
        barra_superior.place(relwidth=1, rely=0.0001)

        foto_label = Label(image=self.foto, bg="#2E2E2E")
        foto_label.place(relwidth=0.09,  rely=0.000010)

        # barra de tarefas inferior
        barra_inferior = Label(self.window, bg="#3d6466", height=120, pady=10)
        barra_inferior.place(relwidth=1, rely=0.810)

        # onde o texto aparece
        self.tela_texto = Text(
        self.window, width=20, height=10, bg="#CDCDC9", fg="#000000", # 20   2
        font=("Helvetica", "14"),  padx=5, pady=5) #  5  5
        self.tela_texto.place(relheight=0.745, relwidth=2, rely=0.08)
        self.tela_texto.configure(cursor="arrow", state=DISABLED)

        # caixa de texto
        self.caixa_texto = Entry(barra_inferior, bg="#303030", fg="#F5F5F5", font=("Helvetica", "16"))
        self.caixa_texto.place(relwidth=0.70, relheight=0.05, rely=0.008,  relx=0.011)
        self.caixa_texto.focus()
        self.caixa_texto.bind( "<Return>", self.caixa_enviar_pergunta)

        # botão de enviar
        perguntar = Button(
        barra_inferior, text="Perguntar", font=("Comic Sans MS", "14", "bold"), width=18, bg="#2E2E2E", fg="#F5F5F5", command=lambda: self.caixa_enviar_pergunta(None) )
        perguntar.place(relx=0.72, rely=0.008, relheight=0.05, relwidth=0.16)

        # botão youtube
        pesquisar_b = Button(barra_inferior, text="Youtube\n 🔍", font=("Comic Sans MS", "13", "bold"), width=18, bg="#2E2E2E", fg="#F5F5F5", command= self.youtube)
        pesquisar_b.place(relx=0.89, rely=0.008, relheight=0.05, relwidth=0.10)

        # barra de scroll
        scrollbar = Scrollbar(self.tela_texto)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.tela_texto.yview)

        # botão calouro
        hyperlink = Button(text="🎓\nCalouro(a)", font=("Comic Sans MS", "11", "bold"), bg="#303030", fg="#F5F5F5", command=self.calouro)
        hyperlink.place(relwidth=0.081, relheight=0.07,  rely=0.009, relx=0.11)

        # botão drive
        hyperlink = Button(text="📜\nG.Drive", font=("Comic Sans MS", "11", "bold"), bg="#303030", fg="#F5F5F5",
                           command=self.Drive)
        hyperlink.place(relwidth=0.081, relheight=0.07, rely=0.009, relx=0.21)

        # botão RU
        hyperlink = Button(text="🍲\nRU", font=("Comic Sans MS", "11", "bold"), bg="#303030", fg="#F5F5F5", command=self.RU)
        hyperlink.place(relwidth=0.053, relheight=0.07, rely=0.009, relx=0.85)

        # botão essenciais
        hyperlink = Button(text="📦\nEssenciais", font=("Comic Sans MS", "11", "bold"), bg="#303030", fg="#F5F5F5", command=self.Essenciais)
        hyperlink.place(relwidth=0.090, relheight=0.07, rely=0.009, relx=0.75)

        # botão horarios_onibus
        hyperlink1 = Button(text="🚌\nOnibus", font=("Comic Sans MS", "11", "bold"), bg="#303030", fg="#F5F5F5", command=self.horarios_onibus)
        hyperlink1.place(relwidth=0.087, relheight=0.07, rely=0.009, relx=0.91)
        hyperlink1.bind("<FocusOut>", lambda e: hyperlink1.configure(bg="black", fg="white"))

    def youtube(self):
        webbrowser.open_new("https://www.youtube.com/")
    def horarios_onibus(self):
        webbrowser.open_new("https://www.inforbrasilia.com.br/2016/02/horario-onibus-unb.html")

    def Drive(self):
        webbrowser.open_new("https://drive.google.com/drive/folders/1Hug-531q1HFPvWaKv9KmpIJTdrQI2jpG")

    def Essenciais(self):
        webbrowser.open_new("https://sigaa.unb.br/sigaa/verTelaLogin.do")
        webbrowser.open_new("https://moodle.mat.unb.br/")
        webbrowser.open_new("https://aprender3.unb.br/login/index.php")
        webbrowser.open_new("https://www.microsoft.com/pt-br/microsoft-teams/log-in")


    def calouro(self):
        webbrowser.open_new("https://boasvindas.unb.br/")


    def RU(self):
        webbrowser.open_new("https://ru.unb.br/index.php/cardapio-refeitorio")

    def caixa_enviar_pergunta(self, a):
        msg_usuario = self.caixa_texto.get()
        self.adicionar_mensagem(msg_usuario, ">> 👨‍🎓 | 👩‍🎓")

    def adicionar_mensagem(self, mensagem_pris, enviar):
        if not mensagem_pris:
            return

        self.caixa_texto.delete(0, END)
        usuario = f"{enviar}: {mensagem_pris}\n\n"
        self.tela_texto.configure(state=NORMAL)
        self.tela_texto.insert(END, usuario)
        self.tela_texto.configure(state=NORMAL)

        pris = f">{bot_name}: {self.respostas(mensagem_pris)}\n\n"
        self.tela_texto.configure(state=NORMAL)
        self.tela_texto.insert(END, pris)
        self.tela_texto.configure(state=DISABLED)
        self.tela_texto.see(END)


if __name__ == "__main__":
    app = Pris()
    app.run()
