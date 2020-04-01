# Simple COVID-19 Exponential Growth Simulator V 0.4b -- 03/31/20 -- 11:59PM
import time
num_infected = 0
day = 0

print('The number of people infected doubles every six days approximately.')

time.sleep(2)
num_infected = int(input('How many people are currently infected?  Type a number without commas.  Then press enter.'))
ttl_day = int(input('How many days do you want to simulate?  Type a number without commas.  Then press enter.'))
print(f'There are currently {num_infected} people.  This simulation will calculate {day} days of data.')
while day <= ttl_day:
    
    num_infected += num_infected
    num_dead = round(0.023 * num_infected)
    print(f'On day {day} there are {num_infected:,} infected people.')
    print(f'Approximately {num_dead:,} of the infected people have died or will die.\n')
    day += 6 
    time.sleep(2)

print(f'After {day} days there are approximately {num_infected:,} infected people and {num_dead:,} dead people.')

    
    
    
