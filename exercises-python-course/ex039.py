from datetime import date
born_year = int(input('Which year do you born?'))
year = date.today().year
age = year - born_year
print('YOURE {} YEARS OLD'.format(age))
y1 =
y2 =
if age < 18:
    print('YOU ARE NOT YET OF AGE TO ENLIST! STILL {} YEARS TO ENLIST'.format(y1))
elif age == 18:
    print('ITS TIME TO ENLIST!')
else:
    print('YOU PASSED {} OF THE TIME TO ENLIST!')
