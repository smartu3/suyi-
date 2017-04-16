#coding=utf-8


#"可变的"tuple
t =  ('a','b',['a','b'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)