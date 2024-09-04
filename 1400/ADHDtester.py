"""
Programer: Saurav Pokharel
Date: 09/03/2024
Description:ADHD Tester. 
"""

#default point set to 0
point = 0 

print('Rate the following activities on a scale from 1 to 5 on how your child does with the given activities, 5 being the very well and 1 being not well at all.')

organize = int (input('How well do you manage your time on a scale of 1-5? '))
point += organize

homework = int(input('How punctual are you with homework deadlines on a scale of 1-5? '))
point += homework

task = int(input('How well do you manage sequential tasks on a scale of 1-5? '))
point += task

room = int(input('How well do you keep your room organized on a scale of 1-5? '))
point += room

detail = int(input('On a scale of 1-5, how would you rate your attention to detail? '))
point += detail

print('You have scored total points of', point)