# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#players who scored
score_1='Ruud Gullit '
score_2='Marco van Basten '

#Minute of the match that a goal was scored
goal_0=32
goal_1=54

#part 1.3
scorer1=score_1 + str(goal_0)
scorer2=score_2 + str(goal_1)
scorers= scorer1 + ', '+scorer2
print(scorers)

#part 1.4
report_a=(score_1 + 'scored in the ' + str(goal_0) + 'nd '+ 'minute')
report_b=(score_2 + 'scored in the ' + str(goal_1) + 'th '+ 'minute')
report= (report_a + '\n'+ report_b)
print(report)

#part 2.1 
player='Erwin koeman'
#first_name='Erwin'
#last_name='Koeman' 

#part 2.2
is_space = player.find(' ')
first_name = player[:is_space]
last_name = player[is_space+1:]
print(first_name)

#part 2.3
last_name_len=len(last_name)
print(last_name_len)

#part 2.4
Player_names=player.split()
First_letter=Player_names[0][0]
name_short= First_letter + '. '+ Player_names[1]
print(name_short)

#part 2.5
times= len(first_name)
name= f'{first_name}!' 
chant= (name + " ") * (len(first_name) -1) + name
print(chant)

#part 2.6
chant_check = chant[-1]
good_chant = chant_check != ' '
print(good_chant)

