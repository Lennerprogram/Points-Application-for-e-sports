from tkinter import *
from tkinter import font


class configs:
    def __init__(self):
        root = Tk()
        root.geometry('400x120')
        root.title('Configurações')

        myFont = font.Font(family = 'Helvetica', size = 12)
        def team_player():
            self.team_players = teamPlayers.get()

        def numberteam():
            self.team_numbers = int(teamNumbers.get())
            root.destroy()
        #frames
        frame1 = Frame(root)
        frame1.pack()
        frame2 = Frame(root)
        frame2.pack()
        frame3 = Frame(root)
        frame3.pack(pady=12)

        #variables
        teamPlayers = IntVar()
        self.team_players = 0
        teamNumbers = StringVar()
        self.team_numbers = 0

        #Numbers of player per team
        label = Label(frame1, text='Jogadores por equipe:', font = myFont)
        label.pack(side = LEFT, pady=10)

        onePlayer = Radiobutton(frame1, text='1', variable = teamPlayers, value = 1, command = team_player)
        twoPlayer = Radiobutton(frame1, text='2', variable = teamPlayers, value = 2, command = team_player)
        threePlayer = Radiobutton(frame1, text='3', variable = teamPlayers, value = 3, command = team_player)
        fourPlayer = Radiobutton(frame1, text='4', variable = teamPlayers, value = 4, command = team_player)
        fivePlayer = Radiobutton(frame1, text='5', variable = teamPlayers, value = 5, command = team_player)

        onePlayer.pack(side = LEFT)
        twoPlayer.pack(side = LEFT)
        threePlayer.pack(side = LEFT)
        fourPlayer.pack(side = LEFT)
        fivePlayer.pack(side = LEFT)

        #team Numbers
        label2 = Label(frame2, text='Quantidade de times:', font = myFont)
        label2.pack(side = LEFT)

        numbers = Entry(frame2, textvariable=teamNumbers)
        numbers.pack(side = RIGHT)

        btn = Button(frame3, text='Times', width=10, command = numberteam, font = myFont)
        btn.pack(side = TOP)

        root.mainloop()