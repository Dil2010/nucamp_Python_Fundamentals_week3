state_capitals={"Washigntopn":"Olympia","Oregon":"Salem","Califonia":"Saramento"}

# for sta in state_capitals:
#     print(sta)

# print(" ")
# for city in state_capitals.values():
#     print(city)
# print(" ")
# for state in state_capitals.keys():
#     print(state)

for state in state_capitals:
    print(state_capitals[state],"is the capital of",state)
print("")
for state,city in state_capitals.items():
    print(city,"is the capital of",state)
   