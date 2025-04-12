import customtkinter

# --- Configurações Globais de Aparência ---
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# --- Classe Principal da Aplicação ---
class CoderitmoApp(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # --- Configuração da Janela Principal ---
        self.title("Coderitmo - Editor de Pseudocódigo Pythonico")
        initial_width = 1100
        initial_height = 700
        self.geometry(f"{initial_width}x{initial_height}")
        self.minsize(800, 500)

        # --- Configurar o Layout da Grade Principal (2 colunas, 3 linhas) ---
        # A coluna 0 (editor) vai expandir mais que a coluna 1 (variáveis)
        self.grid_columnconfigure(0, weight=3) # Coluna do editor/output
        self.grid_columnconfigure(1, weight=1) # Coluna das variáveis
        # A linha 1 (editor/variáveis) vai expandir mais que as outras
        self.grid_rowconfigure(0, weight=0) # Linha dos controles (altura fixa)
        self.grid_rowconfigure(1, weight=3) # Linha do editor/variáveis
        self.grid_rowconfigure(2, weight=1) # Linha da saída

        # --- Criar os Frames para cada Seção ---
        self._criar_frames()

        # --- Criar os Widgets dentro dos Frames ---
        self._criar_widgets()

        print("Layout com frames e widgets básicos criado.")


    def _criar_frames(self):
        # Frame para os Controles (Linha 0, Colunas 0 e 1)
        self.controles_frame = customtkinter.CTkFrame(self, height=50) # Altura definida
        self.controles_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 5), sticky="new") # Norte, Leste, Oeste

        # Frame Principal da Área Central (Linha 1) - vai conter Editor e Variáveis lado a lado
        self.central_frame = customtkinter.CTkFrame(self)
        self.central_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="nsew") # Todas as direções
        # Configurar grid dentro do frame central
        self.central_frame.grid_columnconfigure(0, weight=3) # Editor
        self.central_frame.grid_columnconfigure(1, weight=1) # Variáveis
        self.central_frame.grid_rowconfigure(0, weight=1) # Linha única expande

        # Frame para a Saída (Linha 2, Colunas 0 e 1)
        self.saida_frame = customtkinter.CTkFrame(self)
        self.saida_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=(5, 10), sticky="nsew")
        # Configurar grid dentro do frame de saída para o textbox expandir
        self.saida_frame.grid_columnconfigure(0, weight=1)
        self.saida_frame.grid_rowconfigure(0, weight=1)


    def _criar_widgets(self):
        # --- Widgets no Frame de Controles ---
        self.botao_executar = customtkinter.CTkButton(self.controles_frame, text="Executar")
        self.botao_executar.pack(side="left", padx=5, pady=10) # Usando pack para simplicidade aqui

        self.botao_passo = customtkinter.CTkButton(self.controles_frame, text="Passo", state="disabled")
        self.botao_passo.pack(side="left", padx=5, pady=10)

        self.botao_parar = customtkinter.CTkButton(self.controles_frame, text="Parar", state="disabled")
        self.botao_parar.pack(side="left", padx=5, pady=10)

        # --- Widgets no Frame Central ---
        # Frame Esquerdo (Editor) dentro do Central Frame
        self.editor_container_frame = customtkinter.CTkFrame(self.central_frame)
        self.editor_container_frame.grid(row=0, column=0, padx=(0, 5), pady=0, sticky="nsew")
        self.editor_container_frame.grid_columnconfigure(0, weight=1)
        self.editor_container_frame.grid_rowconfigure(0, weight=1)

        self.editor_textbox = customtkinter.CTkTextbox(self.editor_container_frame, wrap="none", font=("Consolas", 12)) # 'none' desabilita quebra de linha automática
        self.editor_textbox.grid(row=0, column=0, sticky="nsew")
        self.editor_textbox.insert("0.0", '# Exemplo Coderitmo-Lang (ainda não funcional)\n\nalgoritmo "Soma Simples"\n\nvar\n    num1: inteiro\n    num2: inteiro\n    soma: inteiro\n\ninicio\n    escreva_saida("Digite o primeiro número:")\n    leia_entrada(num1)\n\n    escreva_saida("Digite o segundo número:")\n    leia_entrada(num2)\n\n    soma = num1 + num2\n\n    escreva_saida("A soma é: ", soma)\n\nfim_algoritmo\n')

        # Frame Direito (Variáveis) dentro do Central Frame
        self.variaveis_frame = customtkinter.CTkFrame(self.central_frame, width=200) # Largura sugerida
        self.variaveis_frame.grid(row=0, column=1, padx=(5, 0), pady=0, sticky="nsew")
        self.variaveis_frame.grid_propagate(False) # Impede que o frame encolha/expanda com o conteúdo interno
        self.variaveis_frame.grid_columnconfigure(0, weight=1)
        # Adiciona um Label temporário
        label_vars = customtkinter.CTkLabel(self.variaveis_frame, text="Variáveis", font=customtkinter.CTkFont(size=14, weight="bold"))
        label_vars.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
        # Aqui virá um Textbox, Treeview ou similar para mostrar as variáveis

        # --- Widgets no Frame de Saída ---
        self.saida_textbox = customtkinter.CTkTextbox(self.saida_frame, wrap="word", state="disabled", font=("Consolas", 12)) # Habilita quebra de linha
        self.saida_textbox.grid(row=0, column=0, sticky="nsew")
        # Exemplo de como adicionar texto (habilitando/desabilitando)
        self.saida_textbox.configure(state="normal") # Habilita para escrita
        self.saida_textbox.insert("0.0", "Bem-vindo ao Coderitmo!\n")
        self.saida_textbox.configure(state="disabled") # Desabilita novamente (read-only)


# --- Ponto de Entrada da Aplicação ---
if __name__ == "__main__":
    app = CoderitmoApp()
    app.mainloop()