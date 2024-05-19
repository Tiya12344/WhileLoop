number = int(input("Please enter a number "))

i = 0
FirstValue = 0
SecondValue = 1

while i < number:
    if i <= 1:
        Next = i
    else:
        Next = FirstValue + SecondValue
        FirstValue = SecondValue
        SecondValue = Next
    print(Next)
    i = i + 1