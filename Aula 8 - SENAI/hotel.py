print('--------------------------RESERVAS DO HOTEL------------------------------------')

print(f'''  
      -----------------------------REGRAS DE CONCLUSÃO DE CADASTRO------------------------
      1. SER MAIOR DE IDADE (18 ANOS).
      EM CASO DE MENORES DE IDADE, ESTAR COM RESPONSÁVEL PARA ELE REALIZAR O CADASTRO.
      \n''')



print('----------------CADASTRO------------------------')

nome1 = input('Digite o seu nome completo para concluir o cadastro no hotel: ')
idade1 = int(input('Digite a sua idade para concluir o cadastro no hotel: '))
if idade1 >= 18:
    print('Cadastro concluído! ☑️')

    print('\n------------------RESERVA DE QUARTOS---------------')
    quartos = ['','QUARTO SIMPLES','QUARTO DUPLO','QUARTO LUXO']
    valores = [0,100.00,150.00,250.00]

    escolha_quartos = int(input(f'''
        1- {quartos[1]}: R$ {valores[1]}
        2- {quartos[2]}: R$ {valores[2]}
        3- {quartos[3]}: R$ {valores[3]}

    ESCOLHA O SEU QUARTO: '''))
    if escolha_quartos == 1:
        print(f'Você escolheu o quarto simples! Aproveite a sua viagem.')
    elif escolha_quartos == 2:
        print(f"Você escolheu o quarto duplo! Aproveite a sua viagem.")
    elif escolha_quartos == 3:
        print(f"Você escolheu o quarto luxo! Aproveite a sua viagem.")
    else:
        print(f"Ops.. Quarto inválido, digite o número corretamente do quarto desejado!")


    print('\n----------------ESTADIA----------------------------')
    dias = int(input('Quantos dias você deseja ficar? '))

    #acessa o valor que foi escolhido no input escolha_quartos
    calculo = valores[escolha_quartos] * dias

    print('-------------------TOTAL------------------------------')
    total = print(f"O total é: {calculo}")

    print('\n----------------------FORMA DE PAGAMENTO--------------')
    list_form_pag = ['','PIX','CARTÃO DE DÉBITO','CARTÃO DE CRÉDITO']
    index_list_form_pag = [0,1,2,3]
    form_pag = int(input(f'''
        {list_form_pag[1]} - {index_list_form_pag[1]}
        {list_form_pag[2]} - {index_list_form_pag[2]}
        {list_form_pag[3]} - {index_list_form_pag[3]}
    \nDIGITE A FORMA DE PAGAMENTO:  '''))

    if form_pag == 1:
        print('\n Compra concluída! Obrigada, volte sempre!')
    elif form_pag == 2:
        print('\n Compra concluída! Obrigada, volte sempre!')
    elif form_pag == 3:
        print('\n Compra concluída! Obrigada, volte sempre!')
    else: 
        print('Ops.. Digite uma forma de pagamento válida.')

else:
    print('''Ops.. Você não pode concluir o cadastro!✖️
            Apenas maiores de idade podêm concluir o cadastro.
            Peça o seu responsável legal para fazer o seu cadastro e reservar os quartos.
          ''')