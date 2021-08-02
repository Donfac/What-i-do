def generate_key(n):
    letters = "ABCDEFGHIJKLMNPQRSTUVWXYZ"
    key = {}
    cnt = 0
    for c in letters:
        key[c] = letters[(cnt + n) % len(letters)]
        cnt += 1
    return key 

def get_decryption_key(key):
    dkey ={}
    for c in key:
        dkey[key[c]] = c
        return dkey


def encrypt(key, message):
      cipher = ""
      for c in message:
          if c in key:
              cipher += key[c]
          else:
              cipher += c
      return cipher     


key = generate_key(3)
print(key)
message = "GOD MY ALL"
cipher = encrypt(key,message)
print(cipher)
dkey = get_decryption_key(key)
message = encrypt(dkey , cipher)
print(message)
# encrypting the  cipher JOG QB DPP
# message = encrypt(key , cipher)
# print(message)
