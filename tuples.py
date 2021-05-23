'''
Task
Given an integer,n, and n space-separated integers as input, create a tuple,t, of those n integers. Then compute and print the result of hash(t)
Title     : Tuples
Subdomain : Data Types
Domain    : Python
Author    : Samuel Bennett
Created   : 23 May 2021
'''
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))
