command=input("Enter e to encode, d to decode, q to quit:")

while command!='q':

    new_message=''
    message=input("Enter your secret message: ")
    key=int(input("Enter key between 1-25: "))
    ALPHABET="abcdefghijklmnopqrstuvwxyz"


    while key<1 or key>25:     #checking whether the key is between 1 and 25

        print("Enter valid key")
        key=input("Enter key between 1-25: ")

    if command=='e':

        for mes in message:       #taking each character in the user message individualy
            if mes in ALPHABET:   #checking whether that individual character is in ALPHABET
                position=ALPHABET.index(mes)   #taking the character position in ALPHABET
                new_position=ALPHABET.index(mes)+key  #adding the key value to that position
                if new_position>25:        #checking whether the newposition(value after adding the key)is higher that 25
                    new_position=new_position-25        #minus 25 from newposition so it will arrange in a circle
                new_message=list(new_message)       #converting the new_message into a list

                new_message.append(ALPHABET[new_position])    #adding the newposition characters to the new_message list one by one

                new_message=''.join(new_message)        #converting that list to text
            else:
                new_message+=mes       #if not in ALPHABET straightaway add to new_message
        print(new_message)

    elif command=='d':

        for mes in message:       #taking each character in the user message individualy
            if mes in ALPHABET:   #checking whether that individual character is in ALPHABET
                position=ALPHABET.index(mes)   #taking the character position in ALPHABET
                new_position=ALPHABET.index(mes)-key  #minus the key value to that position
                if new_position>25:        #checking whether the newposition(value after adding the key)is higher that 25
                    new_position=new_position-25        #minus 25 from newposition so it will arrange in a circle
                new_message=list(new_message)       #converting the new_message into a list

                new_message.append(ALPHABET[new_position])    #adding the newposition characters to the new_message list one by one

                new_message=''.join(new_message)        #converting that list to text
            else:
                new_message+=mes       #if not in ALPHABET straightaway add to new_message
        print(new_message)
    else:

        print("Invalid command re enter")


    command=input("Enter e to encode, d to decode, q to quit:")