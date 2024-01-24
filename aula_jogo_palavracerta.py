import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import random

class JogoDaForca:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo Palavra Secreta")
        self.root.geometry("600x400")

        self.palavras = ['perfume', 'computador', 'python', 'desenvolvimento', 'programacao', 'inteligencia', 'artificial', 'tecnologia', 'aprendizado', 'criptografia']
        self.palavra_secreta = random.choice(self.palavras)
        self.letras_acertadas = ''
        self.numero_tentativas = 0

        self.init_ui()

    def init_ui(self):
        # Frame principal com gradiente cinza escuro
        main_frame = tk.Frame(self.root, bg="#363636")
        main_frame.place(relwidth=1, relheight=1)

        # Label para a palavra
        self.label_palavra = tk.Label(main_frame, text='Bem vindo ao jogo da Palavra Secreta: ', font=("Arial", 16), fg="white", bg="#363636")
        self.label_palavra.pack(pady=20)

        self.label_palavra = tk.Label(main_frame, text='Descubra a palavra secreta com a menor quantidade de tentativas: ', font=("Arial", 10), fg="white", bg="red")
        self.label_palavra.pack(pady=20)


        self.label_palavra = tk.Label(main_frame, text='Palavra: ' + '*' * len(self.palavra_secreta), font=("Arial", 14), fg="white", bg="#363636")
        self.label_palavra.pack(pady=20)

        # Label para tentativas
        self.label_tentativas = tk.Label(main_frame, text='Tentativas: 0', font=("Arial", 12), fg="white", bg="#363636")
        self.label_tentativas.pack(pady=10)

        # Entrada de letra
        self.entrada_letra = tk.Entry(main_frame, font=("Arial", 12), width=5)
        self.entrada_letra.pack(pady=10)

        # Botão Verificar
        botao_verificar = tk.Button(main_frame, text='Verificar', font=("Arial", 12), command=self.verificar_letra)
        botao_verificar.pack(pady=10)

        # Carregar e exibir imagem à direita
        img_path = "aulas\jogo.png"  # Substitua pelo caminho real da sua imagem
        if os.path.exists(img_path):
            img = Image.open(img_path)
            img.thumbnail((150, 300), Image.ANTIALIAS)  # Use thumbnail para redimensionar com antialiasing
            img = ImageTk.PhotoImage(img)

            img_label = tk.Label(main_frame, image=img, bg="black")
            img_label.image = img
            img_label.place(relx=0.75, rely=0.5, anchor='center')

    def verificar_letra(self):
        letra_digitada = self.entrada_letra.get()
        self.entrada_letra.delete(0, tk.END)

        if letra_digitada in self.palavra_secreta:
            self.letras_acertadas += letra_digitada
        palavra_formada = ''
        for letra_secreta in self.palavra_secreta:
            if letra_secreta in self.letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*'
        self.label_palavra.config(text='Palavra: ' + palavra_formada)

        if palavra_formada == self.palavra_secreta:
            messagebox.showinfo('Parabéns!', f'Você ganhou!\nA palavra era {self.palavra_secreta}')
            self.reiniciar_jogo()

        self.numero_tentativas += 1
        self.label_tentativas.config(text=f'Tentativas: {self.numero_tentativas}')

        if self.numero_tentativas >= 10:
            messagebox.showinfo('Game Over', f'Que pena, muitas tentativas.\nA palavra era {self.palavra_secreta}')
            self.reiniciar_jogo()

    def reiniciar_jogo(self):
        self.letras_acertadas = ''
        self.numero_tentativas = 0
        self.palavra_secreta = random.choice(self.palavras)
        self.label_palavra.config(text='Palavra: ' + '*' * len(self.palavra_secreta))
        self.label_tentativas.config(text='Tentativas: 0')


if __name__ == '__main__':
    root = tk.Tk()
    jogo_da_forca = JogoDaForca(root)
    root.mainloop()
