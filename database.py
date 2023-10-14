import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('credentials.json')
firebase_admin.initialize_app(cred, {"databaseURL": "https://dfootball-3b007-default-rtdb.firebaseio.com/"})


# Function to add score and winner to the database
def add_score(winner, username, final_score):
    ref = db.reference('scores')  # Assuming 'scores' is the root node for storing scores
    new_score = ref.push({
        'winner': winner,
        'username': username,
        'final_score': final_score
    })

# Function to fetch scores and winners from the database
def fetch_scores():
    ref = db.reference('/scores')
    return ref.get()
