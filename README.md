## Estrutura da GUI

A interface gráfica do Coderitmo Desktop é construída usando a biblioteca Python **CustomTkinter**.

*   **Janela Principal:** Definida na classe `CoderitmoApp` no arquivo `main.py`, que herda de `customtkinter.CTk`.
*   **Configurações Iniciais:**
    *   Título: "Coderitmo - Editor de Pseudocódigo Pythonico"
    *   Tamanho Inicial: 1100x700 pixels (pode ser ajustado)
    *   Tamanho Mínimo: 800x500 pixels
    *   Aparência: Baseada no sistema (Claro/Escuro)
    *   Tema de Cor: Azul (padrão do CustomTkinter)
 
![image](https://github.com/user-attachments/assets/beaa4f91-7f83-46bd-b4b9-40cbe748a477)


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

    ## Estrutura da GUI

A interface gráfica do Coderitmo Desktop é construída usando a biblioteca Python **CustomTkinter** e organizada com o gerenciador de layout **grid**.

*   **Janela Principal (`CoderitmoApp`)**: Contém a grade principal (2 colunas, 3 linhas).
    *   Coluna 0 (`weight=3`), Coluna 1 (`weight=1`)
    *   Linha 0 (`weight=0`), Linha 1 (`weight=3`), Linha 2 (`weight=1`)

*   **Frames Principais:**
    *   `controles_frame` (Linha 0, Colunas 0-1): Contém os botões de controle.
    *   `central_frame` (Linha 1, Colunas 0-1): Contém os frames do editor e das variáveis.
        *   Grade Interna: Coluna 0 (Editor, `weight=3`), Coluna 1 (Variáveis, `weight=1`).
    *   `saida_frame` (Linha 2, Colunas 0-1): Contém a caixa de texto de saída.

*   **Widgets Principais:**
    *   **Controles (`controles_frame`):**
        *   `botao_executar`: `CTkButton`
        *   `botao_passo`: `CTkButton` (inicialmente desabilitado)
        *   `botao_parar`: `CTkButton` (inicialmente desabilitado)
    *   **Editor (`central_frame` -> `editor_container_frame`):**
        *   `editor_textbox`: `CTkTextbox` (para entrada do código Coderitmo-Lang).
    *   **Variáveis (`central_frame` -> `variaveis_frame`):**
        *   Placeholder `CTkLabel`. (Será substituído por um visualizador de variáveis).
    *   **Saída (`saida_frame`):**
        *   `saida_textbox`: `CTkTextbox` (somente leitura, para exibir output do programa e mensagens).

*(Screenshots podem ser adicionados aqui para ilustrar o layout).*

## Linguagem Coderitmo e Parser

*   **Linguagem:** A sintaxe da Coderitmo-Lang está sendo definida formalmente no arquivo `coderitmo_lang.lark`. Ela é baseada em indentação e usa palavras-chave inspiradas em Portugol e Python.
*   **Parser:** A análise sintática (parsing) do código Coderitmo-Lang é realizada pela biblioteca **Lark** (`lark-parser`).
*   **Módulo:** A lógica do parser está encapsulada na classe `CoderitmoParser` dentro do arquivo `parser_coderitmo.py`.
    *   Ele carrega a gramática de `coderitmo_lang.lark`.
    *   Utiliza o lexer contextual do Lark para tratar a indentação.
    *   O método `parse(source_code)` recebe o código como string e retorna uma Árvore de Sintaxe Abstrata (AST) da Lark em caso de sucesso, ou `None` em caso de erro (imprimindo detalhes no console).

### Dependências

Adicione `lark-parser` à lista de dependências (ou crie/atualize o `requirements.txt`): 
customtkinter
lark-parser 
Para instalar: `pip install -r requirements.txt` (ou `pip install customtkinter lark-parser`)
