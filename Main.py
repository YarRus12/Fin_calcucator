import Credits as cred

amount = 757786.25
procent = 7.91
end_date = (2029, 1, 15)
start_date = (2022, 4, 16)

credit = cred.Annoy_payment(amount, procent, end_date, start_date)
credit.full_payment()
