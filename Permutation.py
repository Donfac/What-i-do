#from itertools import permutations

#my_list = [1,2,3]

#list_of_permutations = permutations(my_list)
#cnt = 0
#for permutation in list_of_permutations:
    #cnt += 1
   # print(permutation)
#print(len(my_list), cnt)


#2
#import cProfile

#def faculty(n):
 #   if n<= 1:
  #      return n
   # else:
    #    return faculty(n-1)*n

#def counter(n):
 #   cnt = 0
  #  for i in range(n):
   #     cnt += 1
    #return cnt
#cProfile.run("counter(faculty(11))")


#3
import random
def generate_key():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cletters = list(letters)
    key = {}
    for c in letters:
        key[c] = cletters.pop(random.randint(0, len(cletters) - 1))
    return key




def encrypt(key, message):
    cipher =""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher

def get_decrypt_key(key): 
    dkey = {}
    for k in key:
        dkey[key[k]] = k
    return dkey    

key = generate_key()
print(key)
message = "I LOVE YOU"
cipher = encrypt(key, message)
print(cipher)   
dkey = get_decrypt_key(key)
message = encrypt(dkey, cipher)
print(message)













