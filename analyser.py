import os
import pandas as pd
print(os.listdir("./opinions"))
print(*[filename.split(".")[0] for filename in os.listdir("./opinions")],sep="\n")

product_code = input("Podaj kod produktu: ")

opinions = pd.read_json(f"./opinions/{product_code}.json")

print(opinions)

opinions_count = len(opinions.index) #opinions.shape[0]
pros_count = sum([False if len(p)==0 else True for p in opinions.pros])
cons_count = sum([False if len(c)==0 else True for c in opinions.cons])
average_score =0
print(opinions["pros"])
