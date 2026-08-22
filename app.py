from flask import Flask, render_template, jsonify, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('cards.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/cards', methods=['GET'])
def get_cards():
    category = request.args.get('category')
    conn = get_db_connection()
    
    if category and category != 'All':
        cards = conn.execute('SELECT * FROM cards WHERE category = ?', (category,)).fetchall()
    else:
        cards = conn.execute('SELECT * FROM cards').fetchall()
        
    conn.close()
    return jsonify([dict(card) for card in cards])

@app.route('/api/add', methods=['POST'])
def add_card():
    data = request.json
    korean = data.get('korean')
    english = data.get('english')
    category = data.get('category', 'General')
    
    if not korean or not english:
        return jsonify({'error': 'Both fields are required'}), 400
        
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO cards (korean, english, category) VALUES (?, ?, ?)',
        (korean, english, category)
    )
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Card added successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True)