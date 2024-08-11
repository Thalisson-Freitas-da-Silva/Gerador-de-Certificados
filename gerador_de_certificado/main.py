# Gerador de certificados - Thalisson Freitas da Silva
from fpdf import FPDF

# Variáveis 
nome = input("Digite o seu nome: ")
nome_curso = input("Digite o nome do curso concluido: ")
data_inicio = input("Digite a data de inicio: ")
data_termino = input("Digite a data de término: ")

# Início
certificado = FPDF(orientation='L', format="A4")
# O valor padrão para orientation é 'P' (que significa "Portrait", ou vertical).
# Você pode definir como 'L' (que significa "Landscape", ou horizontal).

# Criar uma página
certificado.add_page()

# Utilização da fonte
certificado.set_font("Arial")
certificado.set_font_size(21)
certificado.set_text_color(0,0,0)

# Template do certificado | Largura e Altura
certificado.image("template_certificado.png", x=0,y=0, w=300, h=210)
certificado.image("faculdade_logo.png", x=229, y=25, w=40, h=40)

# Mensagem de texto
certificado.text(110, 84, nome)
certificado.text(140, 107, nome_curso)
certificado.text(195, 117, data_inicio)
certificado.text(55, 127, data_termino)

# Saída de dados
certificado.output("certificado.pdf")
print("Certificado gerado com sucesso!")