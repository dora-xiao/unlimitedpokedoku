# # import pokebase as pb
# import requests

# d = {}
# # Region
# d["generation-i"] = []
# d["generation-ii"] = []
# d["generation-iii"] = []
# d["generation-iv"] = []
# d["generation-v"] = []
# d["generation-vi"] = []
# d["generation-vii"] = []
# d["generation-viii"] = []
# d["generation-ix"] = []
# d["hisui"] = []
# # Type
# d["normal"] = []
# d["fire"] = []
# d["water"] = []
# d["electric"] = []
# d["grass"] = []
# d["ice"] = []
# d["fighting"] = []
# d["poison"] = []
# d["ground"] = []
# d["flying"] = []
# d["psychic"] = []
# d["bug"] = []
# d["rock"] = []
# d["ghost"] = []
# d["dragon"] = []
# d["dark"] = []
# d["steel"] = []
# d["fairy"] = []
# # Color
# d["red"] = []
# d["blue"] = []
# d["yellow"] = []
# d["green"] = []
# d["black"] = []
# d["brown"] = []
# d["purple"] = []
# d["gray"] = []
# d["white"] = []
# d["pink"] = []

# d["dual"] = []
# d["mono"] = []

# d["mythical"] = []
# d["legendary"] = []
# d["baby"] = []

# d["hasform"] = [] # only counts the base species (ex: rotom has form but you can't put rotom-heat)

# d["hasgenderdifferences"] = []
# d["genderless"] = []

# # quag is height 14 and weight 750
# d["taller"] = []
# d["shorter"] = []
# d["heavier"] = []
# d["lighter"] = []

# d["mega"] = []

# # EVOLUTION CHAIN API ENDPOINT IS REALLY MESSY - TODO LATER
# # noevo = []
# # firstoftwo = []
# # firstofthree = []
# # secondoftwo = []
# # secondofthree = []
# # thirdofthree = []
# # splitevo = []
# # evolvesbyitem = []
# # evolvesbyfriendship = []

# # TODO: add ultra beasts

# # base species (1 to 1025) and forms (10001 to 10277)
# idtoname = [""]*1026
# formidtoname = [""]*278
# idtoimg = [""]*1026
# formidtoimg = [""]*278

# # iterate through 1025 base species but add all forms as well
# for i in range(1025):
#     print(i)
#     data = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{i+1}').json()
#     varieties = data["varieties"]

#     for v in varieties:
#         formdata = requests.get(v["pokemon"]["url"]).json()

#         id = formdata["id"]
#         if(id > 10000): # form
#             formidtoname[id-10000] = formdata["name"]
#             formidtoimg[id-10000] = formdata["sprites"]["other"]["official-artwork"]["front_default"]
#         else: # basic species
#             idtoname[id] = formdata["name"]
#             idtoimg[id] = formdata["sprites"]["other"]["official-artwork"]["front_default"]
#             d[data["color"]["name"]].append(id)
#             if(len(varieties) > 1): d["hasform"].append(id)
        
#         if(data["is_baby"]): d["baby"].append(id)
#         if(data["is_mythical"]): d["mythical"].append(id)
#         if(data["is_legendary"]): d["legendary"].append(id)
#         if(data["gender_rate"] == -1): d["genderless"].append(id)
#         if(data["has_gender_differences"]): d["hasgenderdifferences"].append(id)
#         if("mega" in formdata["name"]): d["mega"].append(id)

#         if("alola" in formdata["name"]): 
#             d["generation-vii"].append(id)
#         elif("galar" in formdata["name"]): 
#             d["generation-viii"].append(id)
#         elif("hisui" in formdata["name"]): 
#             d["hisui"].append(id)
#         elif("paldea" in formdata["name"]): 
#             d["generation-ix"].append(id)
#         else:
#             d[data["generation"]["name"]].append(id)
        
#         if(formdata["weight"] > 750):
#              d["heavier"].append(id)
#         else: 
#              d["lighter"].append(id)

#         if(formdata["height"] > 14):
#              d["taller"].append(id)
#         else: 
#              d["shorter"].append(id)

#         types = formdata["types"]
#         if(len(types) == 1): 
#             d["mono"].append(id)
#             d[types[0]["type"]["name"]].append(id)
#         else:
#             d["dual"].append(id)
#             d[types[0]["type"]["name"]].append(id)
#             d[types[1]["type"]["name"]].append(id)

#         # evodata = requests.get(data["evolution_chain"]["url"]).json()["chain"]
#         # level = 1
#         # if(len(evodata["evolves_to"]))
        
#         # noevo = []
#         # firstoftwo = []
#         # firstofthree = []
#         # secondoftwo = []
#         # secondofthree = []
#         # thirdofthree = []
#         # splitevo
#         # evolvesbyitem = []
#         # evolvesbyfriendship = []
            

# # Save to file
# f = open("data.txt", "w")
# result = ""

# gentoname = {"generation-i": "kanto", "generation-ii": "johto", "generation-iii": "hoenn", "generation-iv": "sinnoh", "generation-v": "unova", "generation-vi": "kalos", "generation-vii": "alola", "generation-viii": "galar", "generation-ix": "paldea"}

# for k,v in d.items():
#     if(k in gentoname.keys()): 
#         result += (f"const {gentoname[k]} = {str(v)}\n")
#     else:
#         result += (f"const {k} = {str(v)}\n")

# result += f"const base = {str(list(zip(idtoname, idtoimg)))}\n"
# result += f"const form = {str(list(zip(formidtoname, formidtoimg)))}\n"

# f.write(result)
# f.close()

# # print(d)
# # print(idtoname)
# # print(formidtoname)


searchresults = "";
for i in range(1, len(basename)):
    displayname = " ".join(map(lambda s: s.capitalize(), basename[i].replace("-", " ").split(" ")))
    searchresults += "<li id='search-"+str(i)+"' style='display:none;'><img src='"+baseimg[i]+"'><p>"+displayname+"</p><button onclick='guess("+str(i)+")'>SELECT</button></li>\n"
    
for i in range(1, len(formname)):  
    displayname = " ".join(map(lambda s: s.capitalize(), formname[i].replace("-", " ").split(" ")))
    searchresults += "<li id='search-"+str(10000+i)+"' style='display:none;'><img src='"+formimg[i]+"'><p>"+displayname+"</p><button onclick='guess("+str(10000+i)+")'>SELECT</button></li>\n"


f = open("temp.txt", "w")
f.write(searchresults)
f.close()