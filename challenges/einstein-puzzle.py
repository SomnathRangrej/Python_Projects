# Simplified solution using logic directly

# Initialize houses as a list of dictionaries with attributes to fill
houses = [{'color': None, 'nationality': None, 'drink': None, 'pet': None, 'cigarette': None} for _ in range(5)]

# Apply known constraints step-by-step based on clues
houses[0]['nationality'] = 'Norwegian'  # Clue 9: The Norwegian lives in the first house
houses[2]['drink'] = 'milk'             # Clue 8: The man in the center house drinks milk

# Clue 14: The Norwegian lives next to the blue house
houses[1]['color'] = 'blue'

# Clue 4: The green house is just to the left of the white house
houses[2]['color'] = 'green'
houses[3]['color'] = 'white'

# Clue 5: The owner of the green house drinks coffee
houses[2]['drink'] = 'coffee'

# Clue 1: The Englishman lives in the red house
houses[4]['color'] = 'red'
houses[4]['nationality'] = 'Englishman'

# Clue 7: The owner of the yellow house smokes Dunhills
houses[0]['color'] = 'yellow'
houses[0]['cigarette'] = 'Dunhills'

# Clue 13: The German smokes Prince cigarettes
houses[3]['nationality'] = 'German'
houses[3]['cigarette'] = 'Prince'

# Clue 2: The Swede keeps dogs
houses[4]['nationality'] = 'Swede'
houses[4]['pet'] = 'dogs'

# Clue 3: The Dane drinks tea
houses[1]['nationality'] = 'Dane'
houses[1]['drink'] = 'tea'

# Clue 6: The Pall Mall smoker keeps birds
houses[2]['cigarette'] = 'Pall Mall'
houses[2]['pet'] = 'birds'

# Clue 11: The man who smokes Blue Masters drinks beer
houses[4]['cigarette'] = 'Blue Masters'
houses[4]['drink'] = 'beer'

# Clue 12: The man who keeps horses lives next to the Dunhill smoker
houses[1]['pet'] = 'horses'

# Clue 15: The Blend smoker has a neighbor who drinks water
houses[0]['drink'] = 'water'
houses[1]['cigarette'] = 'Blend'

# Identify the remaining pet (fish) owner
for house in houses:
    if house['pet'] is None:
        house['pet'] = 'fish'

print(houses)

#Output

'''
[
  {
    'color': 'yellow',
    'nationality': 'Norwegian',
    'drink': 'water',
    'pet': 'fish',
    'cigarette': 'Dunhills'
  },
  {
    'color': 'blue',
    'nationality': 'Dane',
    'drink': 'tea',
    'pet': 'horses',
    'cigarette': 'Blend'
  },
  {
    'color': 'green',
    'nationality': None,
    'drink': 'coffee',
    'pet': 'birds',
    'cigarette': 'Pall Mall'
  },
  {
    'color': 'white',
    'nationality': 'German',
    'drink': None,
    'pet': 'fish',
    'cigarette': 'Prince'
  },
  {
    'color': 'red',
    'nationality': 'Swede',
    'drink': 'beer',
    'pet': 'dogs',
    'cigarette': 'Blue Masters'
  }
]

'''