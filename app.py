from flask import Flask, render_template
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://blog'

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/add_players')
def add_players():
    return render_template('add_players.html')

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=8005,
        debug=True
    )



from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Route to display the home page
@app.route('/')
def home():
    # Connect to the SQLite database
    conn = sqlite3.connect('football_transfers.db')
    cursor = conn.cursor()

    # Fetch all player transfer records from the database
    cursor.execute("SELECT * FROM transfers")
    transfers = cursor.fetchall()

    conn.close()

    # Render the HTML page and pass the data to it
    return render_template('home.html', transfers=transfers)


# Route to handle adding new transfers
@app.route('/add', methods=['POST'])
def add_transfer():
    if request.method == 'POST':
        appearance_id = request.form['appearance_id']
        game_id = request.form['game_id']
        player_id = request.form['player_id']
        player_club_id = request.form['player_club_id']
        player_current_club_id = request.form['player_current_club_id']
        date = request.form['date']
        player_name = request.form['player_name']
        competition_id = request.form['competition_id']
        yellow_cards = request.form['yellow_cards']
        red_cards = request.form['red_cards']


        # Connect to the SQLite database
        conn = sqlite3.connect('football_transfers.db')
        cursor = conn.cursor()

        # Insert the new transfer record into the database
        cursor.execute("INSERT INTO transfers (appearance_id, game_id , player_id, player_club_id, player_current_club_id, date, player_name, competition_id, yellow_cards, red_cards) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (appearance_id, game_id , player_id, player_club_id, player_current_club_id, date, player_name, competition_id, yellow_cards, red_cards))
        conn.commit()
        conn.close()

        return home()


# Main entry point to run the Flask app


import sqlite3

def init_db():
    conn = sqlite3.connect('football_transfers.db')
    cursor = conn.cursor()

    # Create the table to store transfers if it doesn't already exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS transfers (
        appearance_id,
        game_id,
        player_id,
        player_club_id,
        player_current_club_id,
        date,
        player_name,
        competition_id,
        yellow_cards,
        red_cards
    )''')

    conn.commit()
    conn.close()

# Call this function to set up the database
init_db()

if __name__ == '__main__':
    app.run(debug=True)