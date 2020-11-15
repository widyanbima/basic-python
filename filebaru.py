# masukkan input dalam fahrenheit
fh=int(input("Masukkan suhu di dalam fahrenheit: "))
print(fh)
print(type(fh))

# Konverternya
cs=(fh-32)*5.0/9.0
print("Suhu Fahrenheit",fh,"adalah",int(cs))

def toCelcius(fahrenheit):
    cs=(fahrenheit-32) *5.0/9.0
    return cs
toCelcius(fh)
