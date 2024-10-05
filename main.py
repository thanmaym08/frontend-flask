from flask import Flask, render_template,jsonify

app = Flask(__name__)
PLACES = [
{
    'id':1,
    'type':'Desert Photography',
    'location': 'Rajasthan,India',
    'salary': 'Rs.10,00,000'
    
},
    {
        'id':2,
        'type':'Ocean Photography',
        'location': 'Lakshadweep island,India',
        'salary': 'Rs.1,00,000'

    },
{
    'id':3,
    'type':'Documentary Photography',
    'location': 'Gujarat,India',
    'salary': 'Rs.15,00,000'

},
{
    'id':4,
    'type':'Astro Photography',
    'location': 'Tamilnadu,India',
    'salary': 'Rs.24,00,000'

}
    
]


@app.route('/')
def index():
    return render_template('index.html',places=PLACES)

@app.route("/api/places")
def list_places():
    return jsonify(PLACES)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
