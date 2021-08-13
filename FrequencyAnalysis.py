cipher = """lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt
  wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb""" 

# a class to restructure the code
class Attack:
    def __init__(self):
            self.alphabet = "abcdefghijklmnopqrstuvwxyz"
            self.freq = {}
    def calculate_freq(self, cypher):
            for c in self.alphabet:
                self.freq[c] = 0        # set the freq of the character to zero
            letter_count =0 #how many characters are there

            for c in cipher: #count the freq of each letter
                if c in self.freq:
                    self.freq[c] += 1
                    letter_count += 1
            for c in self.freq:
                self.freq[c]= round(self.freq[c]/letter_count,4)
    def print_freq(self):
        new_line_count = 0
        for c in self.freq:
            print(c,  ':', self.freq[c], ' ' , end='')
            if new_line_count % 3 == 2:
             print()
            new_line_count += 1
attack = Attack()
attack.calculate.freq(cipher)
attack.print_freq()





