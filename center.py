from classs import Team
teams = []
members = []
objects = []

def add_teams(team, members):
    if len(team) == 0:
        for c in range(1, 4):
            team = input(f'Digite o nome do {c}º time: ')
            aux = input(f'Digite os nomes dos membros separando por espaço\n')

            member = aux.split(' ')

            teams.append(team)
            members.append(member)
    else:
        for c in range(len(members) + 1, 4):
            team = input(f'Digite o nome do {c}º time: ')
            aux = input(f'Digite os nomes dos membros separando por espaço\n')

            member = aux.split(' ')

            teams.append(team)
            members.append(member)
    
    add_to_class(teams, members)
    return teams,members

def add_to_class(team, members):
    for c in team:
        c = Team(c, members[team.index(c)])
        objects.append(c)

print('Olá bem vindo ao programa de pontuação de treinos de e-sports')

while True:
    opction = input('''Escolha uma das opções abaixo digitando o número correspondente:
[1] Ver tabela
[2] Novo Treino 
[3] Sair\n''')

    if opction == '1':
        print(objects)
        for c in objects:
            print(c.name)
            print(c.members)
            print(c.kills)
    if opction == '2':
        if len(teams) > 0:
            print(teams)

            opction2 = input('[1]Continuar com os times\n[2]Mudar times\n')
            if opction2 == '1':
                add_to_class(teams, members)

            elif opction2 == '2':

                opction3 = input('[1]Apagar todos\n[2]Excluir alguns\n')
                if opction3 == '1':
                    teams = []
                    members = []
                    teams,members = add_teams(teams, members)
                
                elif opction3 == '2':
                    opction4 = input('Digite a(s) equipes que deseja excluir de acordo com a sua posição previamente mostrada(separe por um espaço)\n')
                    del_teams = list(map(int, opction4.split(' ')))

                    del teams[max(del_teams) - 1]
                    del_teams.remove(max(del_teams))

                    for c in del_teams:
                        del teams[c - 1]
                        del members[c - 1]
            print(teams)
            print(members)

        else:
            teams,members = add_teams(teams, members)
            print(teams)
            print(members)
    
    if opction == '3':
        break