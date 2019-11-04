from flask import Flask

app = Flask(__name__)

stores = [
    {
        'name': 'My Savage Store',
        'items':
        [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]


@app.route('/')
def home():
    return "Hello World"


# POST /store data: {name: }
@app.route('/store', method=['POST'])
def create_store():
    pass


# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    pass


# GET /store
@app.route('/store/')
def get_stores(name):
    pass


# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', method=['POST'])
def create_item_in_store():
    pass


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass


app.run(port=5000)
