from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/spell')
def cast_spell():
    spell_name = request.args.get('name', 'unknown')
    return jsonify({
        'spell': spell_name,
        'effect': f"{spell_name.capitalize()} spell has been cast!"
    })

if __name__ == '__main__':
    app.run(debug=True)
