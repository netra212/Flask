# Put and Delete-HTTP Verbs. 
# Working with API's -- Json

from flask import Flask, jsonify, request 

app = Flask(__name__)

## Initial Data is my to do list. 
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"},
]

@app.route('/')
def home():
    return "Welcome to the sample To Do List app."

### Get: Retrieve all the items. 
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

## get: Retrieve a specific item by Id. 
@app.route('/items/<int:item_id>', method=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found."})
    return jsonify(item)

## Post: create a new task. 
@app.route('/items', methods['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error": "Item not found."})

    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": resquest.json['name'],
        "description": request.json["description"]
    }

    items.append(new_item)
    return jsonify(new_item)

# Put: Update an existing item. 
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"})
    item["name"] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])

    return jsonify(item)

# DELETE: Delete an item. 
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result": "Item deleted"})

    
if __name__ == '__main':
    app.run(debug=True)


