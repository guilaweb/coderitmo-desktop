## Estrutura da GUI

A interface gráfica do Coderitmo Desktop é construída usando a biblioteca Python **CustomTkinter**.

*   **Janela Principal:** Definida na classe `CoderitmoApp` no arquivo `main.py`, que herda de `customtkinter.CTk`.
*   **Configurações Iniciais:**
    *   Título: "Coderitmo - Editor de Pseudocódigo Pythonico"
    *   Tamanho Inicial: 1100x700 pixels (pode ser ajustado)
    *   Tamanho Mínimo: 800x500 pixels
    *   Aparência: Baseada no sistema (Claro/Escuro)
    *   Tema de Cor: Azul (padrão do CustomTkinter)

*(Esta seção será expandida conforme adicionarmos os painéis de editor, saída e controles).*

## Como Executar

1.  Certifique-se de ter o Python 3.x instalado.
2.  Clone o repositório (se aplicável).
3.  Navegue até a pasta raiz do projeto (`coderitmo-desktop`).
4.  Crie e ative um ambiente virtual:
    ```bash
    python -m venv .venv
    # Windows:
    .\.venv\Scripts\activate
    # Linux/macOS:
    source .venv/bin/activate
    ```
5.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
    *(Nota: Ainda não criamos o `requirements.txt`, por enquanto instale manualmente: `pip install customtkinter`)*
6.  Execute a aplicação:
    ```bash
    python main.py
    ```