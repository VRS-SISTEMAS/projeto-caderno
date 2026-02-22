# ==============================================================================
# VRS Soluções - PROJETO CADERNO DIGITAL
# Módulo: cliente_apk.py (Interface Exclusiva do Aluno)
# Desenvolvido por: Gemini (AI) para Vitor Ribeiro
# Descrição: Aplicativo para celular com trava de hardware e anti-print.
# ==============================================================================

import tkinter as tk
from tkinter import messagebox
from seguranca import SegurancaVRS
from validador import ValidadorVRS
from banco_dados import BancoDadosVRS

class AppAlunoVRS:
    def __init__(self, root):
        self.root = root
        self.root.title("VRS Soluções - Caderno Digital")
        self.root.geometry("400x700")
        self.root.configure(bg="#ffffff")
        
        self.db = BancoDadosVRS()
        
        # 1. ATIVA BLINDAGEM NO CELULAR (ANTI-PRINT)
        SegurancaVRS.ativar_protecao_apk(self.root)
        
        self.tela_login()

    def tela_login(self):
        self.container = tk.Frame(self.root, bg="#ffffff")
        self.container.pack(expand=True, fill="both")

        tk.Label(self.container, text="VRS SOLUÇÕES", font=("Helvetica", 20, "bold"), 
                 bg="#ffffff", fg="#007aff").pack(pady=40)

        tk.Label(self.container, text="ACESSO DO ALUNO", font=("Helvetica", 10, "bold"), 
                 bg="#ffffff", fg="#333333").pack()

        tk.Label(self.container, text="\nE-mail cadastrado:", bg="#ffffff").pack()
        self.ent_email = tk.Entry(self.container, font=("Helvetica", 12), width=25, justify="center")
        self.ent_email.pack(pady=10)

        tk.Button(self.container, text="ENTRAR AGORA", font=("Helvetica", 12, "bold"),
                  bg="#007aff", fg="white", width=20, height=2,
                  command=self.autenticar).pack(pady=30)

    def autenticar(self):
        email = self.ent_email.get()
        # O App pergunta ao banco que VOCÊ gerencia no Painel Admin
        sql = "SELECT * FROM alunos WHERE email = ?"
        res = self.db.consultar_dados(sql, (email,))

        if res:
            aluno = {'status': res[0][3], 'expira': res[0][4], 'hw_id': res[0][5], 'nome': res[0][1]}

            # 2. VALIDA SE A MENSALIDADE ESTÁ EM DIA
            if ValidadorVRS.checar_assinatura({'status_pagamento': aluno['status'], 'expira_em': aluno['expira']}):
                
                # 3. VALIDA O CELULAR ÚNICO
                id_celular = SegurancaVRS.obter_id_unico_vrs()
                
                if aluno['hw_id'] is None:
                    self.db.executar_comando("UPDATE alunos SET dispositivo_id = ? WHERE email = ?", (id_celular, email))
                    self.abrir_material(aluno['nome'])
                elif aluno['hw_id'] == id_celular:
                    self.abrir_material(aluno['nome'])
                else:
                    messagebox.showerror("VRS SEGURANÇA", "Acesso negado!\nEste e-mail já está em uso em outro celular.")
        else:
            messagebox.showerror("VRS", "E-mail não encontrado ou assinatura inativa.")

    def abrir_material(self, nome):
        self.container.destroy()
        header = tk.Frame(self.root, bg="#1c1c1e", pady=10)
        header.pack(fill="x")
        tk.Label(header, text=f"Caderno de: {nome}", fg="white", bg="#1c1c1e").pack()

        # ÁREA DOS RESUMOS (TRAVADA CONTRA CÓPIA)
        self.txt_resumo = tk.Text(self.root, font=("Arial", 11), padx=15, pady=15)
        self.txt_resumo.insert("1.0", "BEM-VINDO À SUA ÁREA DE ESTUDOS!\n\nSeu material exclusivo da VRS Soluções aparecerá aqui.\n\n[CONTEÚDO PROTEGIDO]")
        self.txt_resumo.pack(fill="both", expand=True)

        # 4. IMPEDE CÓPIA E COLAGEM
        SegurancaVRS.travar_copia_vrs(self.txt_resumo)

if __name__ == "__main__":
    root = tk.Tk()
    AppAlunoVRS(root)
    root.mainloop()