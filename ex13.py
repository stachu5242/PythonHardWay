from sys import argv

script, user_name = argv
prompt ='> '

print("Hi :"+user_name+ ", i'm the "+ script +" script")
print("I'd like to ask u a few questions.")
print("Do u like me "+user_name)
likes = raw_input(prompt)

print("Where do u live "+user_name)
lives = raw_input(prompt)

print(likes,lives)
