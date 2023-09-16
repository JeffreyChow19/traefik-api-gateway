from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "The only way to do great work is to love what you do. -Steve Jobs",
    "In the middle of every difficulty lies opportunity. -Albert Einstein",
    "Success is not the key to happiness. Happiness is the key to success. -Albert Schweitzer",
    "Believe you can and you're halfway there. -Theodore Roosevelt",
    "Don't watch the clock; do what it does. Keep going. -Sam Levenson",
    "A creative man is motivated by the desire to achieve, not by the desire to beat others. -Ayn Rand",
    "The future belongs to those who believe in the beauty of their dreams. -Eleanor Roosevelt",
    "The secret of getting ahead is getting started. -Mark Twain",
    "The only limit to our realization of tomorrow will be our doubts of today. -Franklin D. Roosevelt",
    "The purpose of our lives is to be happy. -Dalai Lama",
    "Life is what happens when you're busy making other plans. -John Lennon",
    "Love the life you live. Live the life you love. -Bob Marley",
    "In three words I can sum up everything I've learned about life: it goes on. -Robert Frost",
    "Life is either a daring adventure or nothing at all. -Helen Keller",
    "Many of life's failures are people who did not realize how close they were to success when they gave up. -Thomas A. Edison",
    "You have within you right now, everything you need to deal with whatever the world can throw at you. -Brian Tracy",
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. -Christian D. Larson",
    "The best way to predict your future is to create it. -Peter Drucker",
    "You are never too old to set another goal or to dream a new dream. -C.S. Lewis",
    "Your time is limited, don't waste it living someone else's life. -Steve Jobs"
]

@app.route('/', methods=['GET'])
def home():
    return "Hello from Quotes... Use GET /quote to get a quote"

@app.route('/quote', methods=['GET'])
def get_quote():
    return jsonify(random.choice(quotes))

if __name__ == '__main__':
    app.run(debug=True)