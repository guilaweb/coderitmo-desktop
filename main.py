import customtkinter

# --- Configurações Globais de Aparência (Faça isso antes de criar a janela principal) ---
# Modes: "System" (padrão), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (padrão), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

# --- Classe Principal da Aplicação ---
class CoderitmoApp(customtkinter.CTk): # Herdamos de CTk para que nossa classe seja a janela

    def __init__(self):
        # Chama o construtor da classe pai (CTk)
        super().__init__()

        # --- Configuração da Janela Principal ---
        self.title("Coderitmo - Editor de Pseudocódigo Pythonico")
        # Define um tamanho inicial (Largura x Altura)
        initial_width = 1100
        initial_height = 700
        self.geometry(f"{initial_width}x{initial_height}")
        # Define um tamanho mínimo para evitar que a janela fique muito pequena
        self.minsize(800, 500)

        print("Janela principal do Coderitmo criada.")
        # (Futuramente, aqui chamaremos métodos para criar os widgets internos)
        # self._criar_widgets()


    # (Podemos adicionar métodos aqui depois, como _criar_widgets)
    # def _criar_widgets(self):
    #    # Aqui virá a criação dos painéis, editor, saída, botões...
    #    pass

# --- Ponto de Entrada da Aplicação ---
if __name__ == "__main__":
    # Cria uma instância da nossa aplicação (que é a janela principal)
    app = CoderitmoApp()
    # Inicia o loop de eventos do Tkinter (mantém a janela aberta e responsiva)
    app.mainloop()