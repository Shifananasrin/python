A=input("enter the word:").lower()
if A.endswith('ing'):
    word=A[:-3]+'ly'
else:
    word=A+'ing'
print(word)
