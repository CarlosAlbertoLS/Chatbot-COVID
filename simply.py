import aiml

kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

print("Hello, I'm Esimibot")
while True:
    input_text = input(">Human: ")
    response = kernel.respond(input_text)
    print("Esimibot> " + response)