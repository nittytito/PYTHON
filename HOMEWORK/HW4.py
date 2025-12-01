web_devlp = ["Nitty","Soorya","Aarunnya"]
data_science = ["Anjana","Anjanaa","Fousteena"]
ui_ux = ["Anagha","Aleena","Anu"]

all_participants = [web_devlp,data_science,ui_ux]
print("\nAll Participants: \n",all_participants)

web_devlp.append("Miya")
print("\nAdd name: \n",web_devlp)

data_science.insert(1,"Diya")
print("\nInserting Name: \n",data_science)

ui_ux.pop()
print("\nRemoving: \n",ui_ux)

new_data_science = data_science.copy()
data_science.clear()
print("\nNew data science: \n",new_data_science)

participants = web_devlp[:2]
print("\nfirst two participants: \n",participants)

length = [len(name) for name in new_data_science]
print("\nFull Length: \n",length)

check_asha = ("Asha" in web_devlp or "Asha" in new_data_science or "Asha" in ui_ux)
print("\nCheck : \n",check_asha)

tuple_participants = (web_devlp[0],new_data_science[0],ui_ux[0])
print("\nTuple of first participants in all: \n",tuple_participants)