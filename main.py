text=input("enter your text:")
shift_number=int(input("enter your shift number:"))

alphabet="abcdefghijklmnopqrstuvwxyz"
result=""

for ch in text:
    if ch . isalpha():
        id=alphabet.find(ch.lower())
        new_ch=alphabet[(id + shift_number) % len(alphabet)]
        if ch . isupper():
            new_ch=new_ch.upper()
        result+=new_ch
    else:
        result+=ch
print(result)