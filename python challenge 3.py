Name = input('Name: ')
print("Hello " + Name + 
      "! We are going to find out how long you have been alive!")
Age = int(input('How old are you? '))
print('You are ' + str(age) + ' years old.')
Months = age * 12
#12 is the number of months in a year
Days = age * 365
#365 is the number of days in a year
print(Name + ' has been alive for about: ' +
      str(Months) + 'months or' + str(Days) + 'days!')
