def create_shopping_list():
  """
  Skapar shopping listan 
  """
  return ["Kurslitteratur", "Anteckningsblock", "Penna"]

def shopping_list(slist):
  """
  Listar artiklar i shoppinglistan
  """
  position = 1
  for item in slist:
    print(str(position) +". " + item) 
    position = position +1

def shopping_add(slist):
  """
  Lägg till artiklar i shoppinglistan
  """
  item_name = input("Vad ska läggas till i listan? ")
  slist.append(item_name)

def shopping_remove(slist):
  """
  Radera artiklar ur shoppinglistan 
  """
  try:
    item = int(input("Vilken sak vill du ta bort ur listan? "))
    slist.pop(item -1)
  except: 
    print('Fel: måste vara ett numreriskt värde som finns i listan!')
  
def shopping_edit(slist):
  """
  Editera artiklar i shoppinglistan
  """
  try:
    item = int(input("Vilken sak vill du ändra på ? "))
    text = input("Vad vill du att det skall stå istället för '" + slist[item -1] + "'? ")
    slist[item -1] = text
  except:
    print('Fel: måste vara ett numreriskt värde som finns med i listan!')
