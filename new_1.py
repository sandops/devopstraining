import json
print(f"This is new world")
name = input(f"Enter your name: ")
print(f"Hello {name} welcome to this spectacular language")
name_file = "/home/ubuntu/gitdemo/json_file"
with open (name_file, 'w') as wr:
    json.dump(name,wr)

with open (name_file , 'r') as f:
   username = json.load(f)
   print(f"Hi {username} welcome back")
print("This is the end of with block")
print("This is end of file")
motorcycles = ['Ducati', 'Suzuki', 'Honda', 'Hero', 'Royal Enfield']
print(f"\nHi {username},please checkout the motorbikes brands you can choose from: \n")
print("\n"+ motorcycles[0]+ "\n")
print("\n"+ motorcycles[1] + "\n")
print('\n'+  motorcycles[2] + '\n')
print('\n'+ motorcycles[3] + '\n')
print('\n' + motorcycles[5] + '\n')

