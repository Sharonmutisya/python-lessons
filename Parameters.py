# Parameters(giving the function information).
# A parameter is a variable inside the brackets that lets you send info in.
def greet(name):
    print(f"Bonjour, {name}!")
greet("Maria")
greet("Chacha")
greet("Mwangi")

# More than one parameters.
def mic_cheque(chequer_name, chequer_niche, chequer_age):
    print(f"{chequer_name} at {chequer_age}years old is the {chequer_niche} podcaster.")
mic_cheque("Mwangi", "funny", 30)
mic_cheque("Chacha", "master mind", 32)