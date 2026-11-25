ideas = ["branding", "podcasting", "coding"]
ideas.append("OOTD")
print(f"I have {len(ideas)} ideas")
for index, idea in enumerate(ideas):
    print(f"{index + 1}. {idea}")
    ideas.remove("podcasting")
    print(ideas)
    new_idea = input("get ready:")
    ideas.append(new_idea)
    print(ideas)
