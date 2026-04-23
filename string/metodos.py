#strip = remove espacos em brancos da string
#lower = deixa em lowecase (minuscula)
#upper = deixa em highercase (maiuscula)
#replace = substitui uma substring por outra

s = " Just keep swimming "
t = s.strip()
print(t)
t = s.lower()
print(t)
t = s.upper()
print(t)
t = s.replace("swimm", "runn")
print(t)

s = "Every journey begins with a single step"
resultado = "th" in s
print(resultado) #True or False

resultado = s.find("journey")
print(resultado)

resultado = s.find("ep", 36)


