from xml.dom.minidom import parse

# Caminho para o arquivo XML
file_path = "C:/Users/20211181110021/Desktop/atividades-pos-2024/teste/biblioteca.xml"

try:
    # Carrega o documento XML
    dom = parse(file_path)
    print("Arquivo XML carregado com sucesso.")
    
    # Obtém o elemento 'livros' do XML
    livros = dom.getElementsByTagName('livro')
    
    # Acessa as informações de cada livro
    for livro in livros:
        categoria = livro.getAttribute('categoria')
        elemento_titulo = livro.getElementsByTagName('título')[0]
        titulo = elemento_titulo.firstChild.nodeValue
        elemento_autor = livro.getElementsByTagName('autor')[0]
        origem = elemento_autor.getAttribute('origem')
        autor = elemento_autor.firstChild.nodeValue
        elemento_ano = livro.getElementsByTagName('ano')[0]
        ano = elemento_ano.firstChild.nodeValue

        print("Categoria:", categoria)
        print("Título:", titulo)
        print(f'Autor: {autor} ({origem})')
        print("Ano:", ano)
        print("---\n")

except FileNotFoundError:
    print(f"Arquivo não encontrado: {file_path}")
except Exception as e:
    print(f"Erro ao carregar o arquivo XML: {e}")