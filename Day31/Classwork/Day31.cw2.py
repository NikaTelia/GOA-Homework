Name = '   chocolate   '

print(Name.capitalize())
print(Name.upper())
print(Name.lower())
print(Name.strip())
print(Name.rstrip())
print(Name.lstrip())
print(Name.index('c',2))
print(Name.find('o'))

#capitalize - პირველი ასო ადიდებს
#upper - ასოებს ადიდებს
#lower - ყველა ასოს აპტარავებს
#strip - შლის ცარიელ ადგილს
#lstrip - მარცხნივ შლის ადგილს
#rstrip - მარჯვნივ შლის ადგილს
#index - გამოიტანს ასო სადაც მდებაროებს თუ არ არის ასო შედცომას გამოიტანს
#find - გამოიტანს ინდექს სადაც არის თუ არ არის ასო გამოიტანს -1

# def value - არის შემცვლელი რიხვი თუ არ გვაქცს შემოტანილი რიცხვი 
# მაგ: (num1, num2=1) ცვლადი(3) -- აქ არ წერია მეორე რიცვი მაშინ ეს 1 რაც მითითედ
# მანდ და ჯამს დაემატება ან ა.შ, აუცილებელია!!! თუ მიუთითებდ რიცხვს დაეგნორებს