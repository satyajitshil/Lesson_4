ammount = int(input("How much money do you want to withdraw: "))
note_1 = ammount//100
note_2 = (ammount%100)//50
note_3 = ((ammount%100)%50)// 10
print(note_1, note_2, note_3)
