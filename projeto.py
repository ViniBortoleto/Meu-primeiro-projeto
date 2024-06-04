projeto = input("Digite a descricao do projeto: ")
horas_trabalhadas = input("Digite a quantidade de horas previstas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo = input("Digite o prazo estimado: ")
valor_total = int(valor_hora) * int(horas_trabalhadas)

from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial")

pdf.image("template.png", x=0, y=0 )

pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_trabalhadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_total))

pdf.output("Orcamento.pdf")
print("Orcamento gerado com sucesso!")