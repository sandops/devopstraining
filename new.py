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
