from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

animals = [
    {'id': 1, 'name': 'Lion'},
    {'id': 2, 'name': 'Elephant'},
    {'id': 3, 'name': 'Giraffe'}
]

@app.route('/')
def index():
    return render_template('index.html', animals=animals)

@app.route('/add_animal', methods=['POST'])
def add_animal():
    data = request.get_json()
    new_animal = {'id': len(animals) + 1, 'name': data['name']}
    animals.append(new_animal)
    return jsonify(new_animal)

@app.route('/delete_animal/<int:id>', methods=['DELETE'])
def delete_animal(id):
    deleted_animal = [animal for animal in animals if animal['id'] == id][0]
    animals.remove(deleted_animal)
    return jsonify(deleted_animal)

if __name__ == '__main__':
    app.run(debug=True)
