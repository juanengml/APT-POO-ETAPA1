"""
 Implemente uma classe  na linguagem Java ,  denominada  FolhaPagamento ,   que contenha  apenas  o método  main ,   com os seguintes passos:  

    Lê os dados de n (entre 1 e 100) funcionários fornecidos pela entrada padrão (teclado). 
    Calcula o valor mensal recebido por cada funcionário. 
    Imprime na saída padrão (tela) a relação de n funcionários com os correspondentes valores mensais recebidos, apresentando primeiramente todos os concursados e, em seguida, os temporários. 

Para cada funcionário, devem ser fornecidos os seguintes dados:  

    Código: um valor inteiro (int). 
    Tipo: o valor (int) 1 para funcionário concursado ou o valor 2 para funcionário temporário. 
    Salário-base: um valor real (double). 
    Tempo: um valor inteiro (int) correspondente ao número de anos de contratação para funcionário concursado ou ao número de meses do período de contrato para um funcionário temporário. 

  Por exemplo, considerando  o seguinte conjunto de n = 3 funcionários :  

    Funcionário com código 147, concursado (1), com salário-base de R$ 4.000,00 e 5 anos de contratação. 
    Funcionário com código 304, temporário (2), com salário-base de R$ 1.500,00 e 24 meses de contrato. 
    Funcionário com código 214, concursado (1), com salário-base de R$ 7.200,00 e 10 anos de contratação. 

"""


func_publico = []
func_temporario = []

class  FolhaPagamento(object):
  def __init__(self,ID=None,tipo_funcionario=None,salario_base=None,tempo=None):
    self.ID = ID
    self.tipo_funcionario = tipo_funcionario
    self.salario_base = salario_base
    self.tempo = tempo
    

  def insert(self):  
   if self.tipo_funcionario == 1:
     valores = {
       "id":self.ID, 
       "Funcionario":"Publico",
       "salario_base": self.salario_base,
       "tempo de contrato":self.tempo
     }
     func_publico.append(valores)
   
   if self.tipo_funcionario == 2:
     valores = {
       "id":self.ID, 
       "Funcionario":"Temporario",
       "salario_base": self.salario_base,
       "tempo de contrato":self.tempo
     } 
     func_temporario.append(valores)
     
  def Report(self):   
   db = [func_publico,func_temporario]
   for tabela in db:
     for funcionario in tabela:
       print(funcionario)


def main():
  cadastro = int(input("Numero de empregados: "))
  for empregado in range(cadastro):
     ID = int(input("ID: "))
     Funcionario = int(input("Funcionario: "))
     Salario = int(input("salario: "))
     tempo = int(input("tempo: "))          
     report = FolhaPagamento(ID,Funcionario,Salario,tempo)
     report.insert()
  rp = FolhaPagamento()
  rp.Report()

     
     

if __name__ == "__main__":
  main()