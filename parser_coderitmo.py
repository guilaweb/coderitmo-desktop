import pathlib
from lark import Lark, exceptions

# --- Constantes ---
# Determina o caminho absoluto para o arquivo da gramática
# Isso garante que funcione independentemente de onde o script é executado
GRAMMAR_FILE = pathlib.Path(__file__).parent / "coderitmo_lang.lark"

# --- Classe do Parser ---
class CoderitmoParser:
    """
    Encapsula o parser Lark para a linguagem Coderitmo-Lang.

    Carrega a gramática de um arquivo .lark e fornece um método
    para analisar o código fonte.
    """
    def __init__(self, grammar_path=GRAMMAR_FILE):
        """
        Inicializa o parser carregando a gramática.

        Args:
            grammar_path (pathlib.Path or str): O caminho para o arquivo .lark da gramática.
        """
        try:
            with open(grammar_path, "r", encoding="utf-8") as f:
                grammar_content = f.read()

            # Cria a instância do parser Lark
            # parser='lalr' -> Algoritmo de parsing (bom padrão)
            # lexer='contextual' -> ESSENCIAL para gramáticas baseadas em indentação!
            # propagate_positions=True -> Inclui informações de linha/coluna na AST (muito útil!)
            # start='start' -> Define a regra raiz da gramática
            self.parser = Lark(
                grammar_content,
                parser='lalr',
                lexer='contextual',
                propagate_positions=True,
                start='start'
            )
            print(f"Gramática carregada com sucesso de: {grammar_path}")

        except FileNotFoundError:
            print(f"ERRO CRÍTICO: Arquivo da gramática não encontrado em: {grammar_path}")
            # Em uma aplicação real, talvez queira levantar uma exceção ou tratar de forma diferente
            self.parser = None
        except Exception as e:
            print(f"ERRO CRÍTICO: Falha ao carregar ou inicializar o parser Lark: {e}")
            self.parser = None

    def parse(self, source_code: str):
        """
        Analisa (parse) uma string de código fonte Coderitmo-Lang.

        Args:
            source_code (str): O código a ser analisado.

        Returns:
            lark.Tree: A Árvore de Sintaxe Abstrata (AST) se o parsing for bem-sucedido.
            None: Se o parsing falhar ou se o parser não foi inicializado corretamente.
                  (Imprime informações do erro no console).
        """
        if not self.parser:
            print("Erro: Parser não inicializado corretamente.")
            return None

        try:
            # Adiciona uma nova linha no final se não houver,
            # pois o lexer de indentação do Lark funciona melhor com isso.
            if not source_code.endswith('\n'):
                source_code += '\n'

            ast = self.parser.parse(source_code)
            return ast

        except exceptions.UnexpectedToken as e:
            print(f"\n--- Erro de Sintaxe ---")
            print(f"Token inesperado: '{e.token}' na linha {e.line}, coluna {e.column}.")
            print(f"Esperava um de: {e.expected}")
            # print(f"Contexto:\n{e.get_context(source_code, 20)}") # Mostra trecho do código
            return None
        except exceptions.UnexpectedCharacters as e:
            print(f"\n--- Erro Léxico ---")
            print(f"Caractere(s) inesperado(s) na linha {e.line}, coluna {e.column}.")
            print(f"Contexto próximo: '{source_code[e.pos_in_stream-10:e.pos_in_stream+10]}'")
            return None
        except Exception as e: # Outros erros inesperados do Lark ou gerais
            print(f"\n--- Erro Inesperado no Parsing ---")
            print(f"Erro: {e}")
            return None


# --- Bloco de Teste Simples (Executado apenas se rodar este script diretamente) ---
if __name__ == "__main__":
    print("--- Testando o CoderitmoParser ---")

    # Código de exemplo para teste
    test_code = """
algoritmo "Teste Simples"

var
    nome: texto
    idade: inteiro

inicio
    escreva_saida("Digite seu nome:")
    # leia_entrada(nome) # Comando leia ainda não implementado na gramática/parser

    idade = 10 + 5 # Atribuição simples (expressão ainda não parseada em detalhes)
    escreva_saida("Idade calculada: ", idade)

    # Linha vazia abaixo

    # Outro comentário
    escreva_saida("Fim do teste")
fim

fim_algoritmo
"""

    parser_instance = CoderitmoParser()

    if parser_instance.parser: # Verifica se o parser carregou
        print("\n--- Código a ser Analisado ---")
        print(test_code)
        print("----------------------------")

        ast_result = parser_instance.parse(test_code)

        if ast_result:
            print("\n--- Parsing Bem-Sucedido! ---")
            print("Árvore de Sintaxe Abstrata (AST):")
            # O método pretty() formata a árvore para melhor visualização
            print(ast_result.pretty())
        else:
            print("\n--- Parsing Falhou. Verifique os erros acima. ---")

    print("\n--- Fim do Teste ---")