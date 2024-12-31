import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]


def exibir_nome_do_programa():
      print("""
      𝒮𝒶𝒷ℴ𝓇 ℰ𝓍𝓅𝓇ℯ𝓈𝓈
      """)

def exibir_opcoes():
      print('1. Cadastrar restaurante')
      print('2. Listar restaurantes')
      print('3. Alternar estado do restaurante')
      print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app\n')
    
def voltar_ao_menu_principal():
     input('\nDigite uma tecla qualquer para voltar para o menu: ')
     main()

def opcao_invalida():
      print('Opção inválida!\n')
      voltar_ao_menu_principal()

def exibir_subtitulo(texto):  
     os.system('cls') 
     linha = '*' * (len(texto))
     print(linha)
     print(texto)
     print(linha)
     print()
     
def cadastrar_novo_restaurante():
     exibir_subtitulo('Cadastro de novos restaurantes\n')
     nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ') 
     categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
     dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
     restaurantes.append(dados_do_restaurante)
     print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso !')
     voltar_ao_menu_principal()
     main()

def listar_restaurantes():
     exibir_subtitulo('Listando os novos restaurantes\n')

     print(f'-{'Nome do restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | Status')
     for restaurante in restaurantes:
         nome_restaurante = restaurante['nome']
         categoria_do_estabelecimento = restaurante['categoria']
         estado_do_restaurante = 'ativado' if restaurante['ativo'] else 'desativado'
         print(f'- {nome_restaurante.ljust(20)} | {categoria_do_estabelecimento.ljust(20)} | {estado_do_restaurante.ljust(20)}')

     voltar_ao_menu_principal()

def alternar_estado_restaurante():
          exibir_subtitulo('Alterando estado do restaurante')
          nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
          restaurante_encontrado = False

          for restaurante in restaurantes:
               if nome_restaurante == restaurante['nome']:
                  restaurante_encontrado = True
                  restaurante['ativo'] = not restaurante['ativo']
                  mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
                  print(mensagem)

               if not restaurante_encontrado:
                    print('O restaurante não foi encontrado')  


          voltar_ao_menu_principal()
     

def escolher_opcao():
    try:
      opcao_escolhida = int(input('Escolha uma opção:'))

      if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
      elif opcao_escolhida == 2:
           listar_restaurantes()
      elif opcao_escolhida == 3:
            alternar_estado_restaurante()
      elif opcao_escolhida == 4:
            finalizar_app()      
      else:
            opcao_invalida()
    except:
         opcao_invalida()   

def main():
      os.system('cls')
      exibir_nome_do_programa()
      exibir_opcoes()
      escolher_opcao()
      
if __name__ == '__main__':
    main()