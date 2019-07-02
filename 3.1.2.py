def lucky_ticket(ticket_number):
    ticket_number1 = list(str(ticket_number))
    halfticket1 = int(ticket_number1[0]) + int(ticket_number1[1]) + int(ticket_number1[2])
    halfticket2 = int(ticket_number1[3]) + int(ticket_number1[4]) + int(ticket_number1[5])
    if halfticket1 == halfticket2:
        return '%s счастливый' %ticket_number
    else:
        return '%s несчастливый' %ticket_number

number = 123123
print(lucky_ticket(number))