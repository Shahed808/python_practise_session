''' print statements '''

# print("python programming")                                                                           # python programming


''' ways to print the output in python'''
# coding

# print('coding')                                                                                             # coding
# print("coding")                                                                                             # coding
# print('''coding''')                                                                                         # coding
# print("""coding""")                                                                                         # coding

"hel'lo wor'ld"

# print("hel'lo wor'ld")                                                                                      # hel'lo wor'ld
# print('hel\'lo wor\'ld')                                                                                    # hel'lo wor'ld
# print("hel\'lo wor\'ld")                                                                                    # hel'lo wor'ld
# print('''hel'lo wor'ld''')                                                                                   # hel'lo wor'ld
# print("""hel'lo wor'ld""")                                                                                    # hel'lo wor'ld


''' getting the o/p in two or mutiple lines'''

# print("I am a \                                                                                               # I am a programmer
# \
# programmer")

# print(''' I am a                                                                                              # I am a programmer
# programmer''')

# print(""" I am a                                                                                              # I am a programmer
# programmer""")

''' we can multiply the str with numbers aswell'''

# print("Welcome! to my world " * 5)                                                                            # Welcome! to my world   .....

''' comments 
   comments are used to help the better understanding of the code and it doesn't execute in the program
   There are two types of comments in python (single line comment and multi line comment) '''


''' variables in python
A variable can start with alphabet and _ but it cannot start with number '''

# a = "intezer"
# print(a)                                                                                                          # intezer
# print('%s' %a)                                                                                                     # intezer


''' to check variable is valid or not '''

# print('.a'.isidentifier())                                                                                         # False
# print('A_a'.isidentifier())                                                                                         # True
# print('895_a'.isidentifier())                                                                                       # False
# print('+xjd'.isidentifier())                                                                                        # False
# print('Up'.isidentifier())                                                                                           # True


''' ways to assign a variable '''

# p = 256                                                           
# q = 52.326
# s = 'welcome!'

# print(p,q,s)                                                                                                  # 256 52.326 welcome!
# print(p)                                                                                                       # 256
# print(q)                                                                                                       # 52.36
# print(s)                                                                                                       # welcome!

# a=b=c = 'Hello!'; d = 'world'
# print(a,b,c,d)                                                                                             # Hello! Hello! Hello! world

# p,q,r = 12,56,23,56.5
# print(p,q,r)                                                                                               # ValueError : too many values to unpack


# x,y,z,t,e = 23.6,12,45,0
# print(x,y,z,t,e)                                                                                           # ValueError : not enough values to unpack

''' Data Types in python - string'''



# name = "Shahed."
# age = 23
# job = "hacker!."

# print("My name is ",name,"My age is ",age, ".I am an ",job)                                                 # My name is Shahed. My age is 23. I am an hacker!



# n = "Hello!"
# m = 23
# z = "to my world🤞😎"           


# print(n+str(m)+z)                                                                                                # Hello! 23 to my world
# print(n,m,z)                                                                                                     # Hello! 23 to my world



# print(type(''))                                                                                                    # class str
# print(type('.'))                                                                                                   # class str
# print(type(','))                                                                                                   # class str
# print(type('!'))                                                                                                   # class str
# print(type(56.23))                                                                                                 # class float
# print(type(56))                                                                                                    # class int


# s = 256
# print(s)                                                                                                          # 256
# print('%d' %s)                                                                                                       # 256


# s = " Hello!"
# print('%s' %s)                                                                                                      # Hello!


# d = 23.65
# print('%f' %d)                                                                                                     # 23.650000
# print('%.2f' %d)                                                                                                    # 23.65
# print('%.3f' %d)                                                                                                     # 23.650


''' conversions methods in python '''

# a = 256                                                                                                            # converting int to str and float
# print(float(a))                                                                                                       # 256.0
# print(str(a))                                                                                                         # '256'


# x = 25.652                                                                                                         # converting float to str and int
# print(int(x),type(int(x)))                                                                                         # 25 class int                                                           
# print(str(x),type(str(x)))                                                                                          # 25 class str



'''But we cannot convert the str into int and float'''

# e = "Hello"
# print(int(e))                                                                                                       # ValueError : invalid literal for int()
# print(float(e))                                                                                                       # ValueError : could not convert str to float


''' but we can convert the str into float and int'''

# h = '23'
# print(float(h))                                                                                                        # 23
# print(int(h))                                                                                                             # 23.0



# s = '23.02'
# print(int(s))                                                                                                  # ValueError : invalid literal for int()
# print(float(s))                                                                                                   # 23.02

# s = '23.02'
# print(float(s))                                                                                                       # 23.02
# z = float(s)
# print(int(z))                                                                                                          # 23


''' string methods'''

# d = "i am A Programmer"                                                                                       
# print(d.capitalize())                                                                                             # I am a programmer


# v = "Today There is no claSS"
# print(v.casefold())                                                                                             # today there is no class




# f = " "
# print(f.isspace())                                                                                              # True
# print('            '.isspace())                                                                                  # True
# print("rtg".isspace())                                                                                            # False 
# print(','.isspace())                                                                                              # False
# print('tv'.isspace())                                                                                              # False


# print('2563'.isnumeric())                                                                                           # True
# print(',123'.isnumeric())                                                                                           # False
# print('asl123'.isnumeric())                                                                                         # False
# print('12.36'.isnumeric())                                                                                          # False


# print('45alpha'.isidentifier())                                                                                         # True
# print('_.236'.isidentifier())                                                                                           # False
# print('code'.isidentifier())                                                                                            # False
# print('!123'.isidentifier())                                                                                            # False


# print('asj123'.isalnum())                                                                                               # True
# print('_asj123'.isalnum())                                                                                              # False
# print('as.j123'.isalnum())                                                                                              # False
# print('asj1,!23'.isalnum())                                                                                             # False
# print('asAS125'.isalnum())                                                                                              # True


# print('12.36'.isalpha())                                                                                                 # False
# print('ASwem'.isalpha())                                                                                                 # True
# print('_12ASW'.isalpha())                                                                                                # False
# print('_AWS'.isalpha())                                                                                                  # False


# r = "I am a developer"
# z = r.index('e')
# print(z)                                                                                                                 # 8


# print("Hello! wor ld.".rindex(' '))                                                                                      # 10


# q = "Wel\tcome\t! to \tcodi\tng wo\trld"
# print(q.expandtabs())                                                                                                   # Wel    come    ! to     codi    ng wo    rld
# print(q.expandtabs(10))                                                                                                  # wel     come    ! to      codi      ng wo      rld
# print(q.expandtabs(2))                                                                                                  # Wel  come  ! to  codi  ng wo  rld


# d = '1,2,3,5,6,2,1,2,1,4,52,1,2,4,6'
# print(d.count('1'))                                                                                                         # 4
# print(d.count('0.23'))                                                                                                      # 0
# print(d.count('52'))                                                                                                         # 1


# b = "I want to be a billionaire"
# print(b.find('a'))                                                                                                              # 3
# print(b.find(' '))                                                                                                              # 1
# print(b.find('i'))                                                                                                              # 16
# print(b.find('.'))                                                                                                              # -1

# b = "I want to be a billionaire"

# print(b.rfind('i'))                                                                                                             # 23
# print(b.rfind(' '))                                                                                                            # 14
# print(b.rfind('e'))                                                                                                             # 25


# w = "I am an hacker!"
# e = w.maketrans('h','j')
# print(w.translate(e))                                                                                                               # I am an jacker


# w = "I'm the  hacker!"
# a = 'cha'
# b = 'cjo'
# z = 'c'
# t = w.maketrans(a,b,z)
# print(w.translate(t))                                                                                                               # I'm tje joker!



# e = "I want to be a programmer"
# x = 'pro'
# r = 'lma'
# z = 'toeba'
# print( e.maketrans(x,r,z))                                                                                                  # {112:108, 114:109, 111: None, 116: None, 101: None, 98: None, 97: None }
# print(e.translate(f))                                                                                                     # I wn lmgmmmm


