import os
import random
import json
from termcolor import colored

def carregar_pokemons():
    with open('pokemons.json', 'r') as file:
        return json.load(file)

def carregar_natures():
    with open('natures.json', 'r') as file:
        return json.load(file)

def gerar_poke(h):
    g = 1
    while g != h:
       pokemons = carregar_pokemons()
       natures = carregar_natures()
    
       numero_aleatorio = str(random.randint(1, 145))
       pokemon = pokemons.get(numero_aleatorio)
       if pokemon:
           natureza_aleatoria = random.choice(list(natures.keys()))
           descricao_natureza = natures[natureza_aleatoria]
           print(colored(f'------------------------------------------------------------{g}º Pokémon------------------------------------------------------------', "light_red"))
           print(f'''
     Pokémon: {pokemon['name']} || Tipos: {', '.join(pokemon['types'])} || Nature: {natureza_aleatoria} - {descricao_natureza}"
            ''')
       else:
            print("Pokémon não encontrado.")
       g = g+1

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored(
            '''
        ▄▄▄·       ▄ •▄ ▄▄▄ . ▄▄ • ▄▄▄ . ▐ ▄ ▄▄▄ .▄▄▄   ▄▄▄· ▄▄▄▄▄      ▄▄▄  
        ▐█ ▄█▪     █▌▄▌▪▀▄.▀·▐█ ▀ ▪▀▄.▀·•█▌▐█▀▄.▀·▀▄ █·▐█ ▀█ •██  ▪     ▀▄ █·
        ██▀·  ▄█▀▄ ▐▀▀▄·▐▀▀▪▄▄█ ▀█▄▐▀▀▪▄▐█▐▐▌▐▀▀▪▄▐▀▀▄ ▄█▀▀█  ▐█.▪ ▄█▀▄ ▐▀▀▄ 
        ▐█▪·•▐█▌.▐▌▐█.█▌▐█▄▄▌▐█▄▪▐█▐█▄▄▌██▐█▌▐█▄▄▌▐█•█▌▐█ ▪▐▌ ▐█▌·▐█▌.▐▌▐█•█▌
        .▀    ▀█▄▀▪·▀  ▀ ▀▀▀ ·▀▀▀▀  ▀▀▀ ▀▀ █▪ ▀▀▀ .▀  ▀ ▀  ▀  ▀▀▀  ▀█▄▀▪.▀  ▀
        matheusmrq.github.io/Profile/

        -----------------------------------------------------------------------
            ''', "light_red"))

        print('     Bem-vindo ao PokeGanerator!')
        print('      O que você deseja gerar?')
        print('   [1]Time   [2]Pokemon   [3]Sair')
        opc = int(input('                 '))
        if opc == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(colored(
            '''
        ▄▄▄·       ▄ •▄ ▄▄▄ . ▄▄ • ▄▄▄ . ▐ ▄ ▄▄▄ .▄▄▄   ▄▄▄· ▄▄▄▄▄      ▄▄▄  
        ▐█ ▄█▪     █▌▄▌▪▀▄.▀·▐█ ▀ ▪▀▄.▀·•█▌▐█▀▄.▀·▀▄ █·▐█ ▀█ •██  ▪     ▀▄ █·
        ██▀·  ▄█▀▄ ▐▀▀▄·▐▀▀▪▄▄█ ▀█▄▐▀▀▪▄▐█▐▐▌▐▀▀▪▄▐▀▀▄ ▄█▀▀█  ▐█.▪ ▄█▀▄ ▐▀▀▄ 
        ▐█▪·•▐█▌.▐▌▐█.█▌▐█▄▄▌▐█▄▪▐█▐█▄▄▌██▐█▌▐█▄▄▌▐█•█▌▐█ ▪▐▌ ▐█▌·▐█▌.▐▌▐█•█▌
        .▀    ▀█▄▀▪·▀  ▀ ▀▀▀ ·▀▀▀▀  ▀▀▀ ▀▀ █▪ ▀▀▀ .▀  ▀ ▀  ▀  ▀▀▀  ▀█▄▀▪.▀  ▀
        matheusmrq.github.io/Profile/
            ''', "light_red"))
            print('        \n Gerar-Time Selecionado! Pokémons:')
            gerar_poke(7)
            a = input('Enter...')

        elif opc == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(colored(
            '''
        ▄▄▄·       ▄ •▄ ▄▄▄ . ▄▄ • ▄▄▄ . ▐ ▄ ▄▄▄ .▄▄▄   ▄▄▄· ▄▄▄▄▄      ▄▄▄  
        ▐█ ▄█▪     █▌▄▌▪▀▄.▀·▐█ ▀ ▪▀▄.▀·•█▌▐█▀▄.▀·▀▄ █·▐█ ▀█ •██  ▪     ▀▄ █·
        ██▀·  ▄█▀▄ ▐▀▀▄·▐▀▀▪▄▄█ ▀█▄▐▀▀▪▄▐█▐▐▌▐▀▀▪▄▐▀▀▄ ▄█▀▀█  ▐█.▪ ▄█▀▄ ▐▀▀▄ 
        ▐█▪·•▐█▌.▐▌▐█.█▌▐█▄▄▌▐█▄▪▐█▐█▄▄▌██▐█▌▐█▄▄▌▐█•█▌▐█ ▪▐▌ ▐█▌·▐█▌.▐▌▐█•█▌
        .▀    ▀█▄▀▪·▀  ▀ ▀▀▀ ·▀▀▀▀  ▀▀▀ ▀▀ █▪ ▀▀▀ .▀  ▀ ▀  ▀  ▀▀▀  ▀█▄▀▪.▀  ▀
        matheusmrq.github.io/Profile/
            ''', "light_red"))
            print('        \n Gerar-Pokémon Selecionado! Pokémons:')
            gerar_poke(2)
            a = input('Enter...')
        else:
            break
if __name__ == "__main__":
    main()
