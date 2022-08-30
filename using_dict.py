state_capitals={"Washigntopn":"Olympia","Oregon":"Salem","Califonia":"Saramento"}

# print(state_capitals)

# print(state_capitals["Washigntopn"])

state_capitals["Washigntopn"]="Alberdreon"

# print(state_capitals)

state_capitals["Texas"]="Austin"

# print(state_capitals)

del state_capitals["Washigntopn"]

print(state_capitals)

removed_capitals=state_capitals.pop("Oregon")

print(state_capitals)
print(removed_capitals)


