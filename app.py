from flask import Flask, render_template, request, jsonify
import pyodbc
import os

app = Flask(__name__)

# # Azure SQL Database configuration
# server = 'bdo-testing.database.windows.net'
# database = 'DB_login'
# username = 'bdo-global'
# password = 'dinusha@12'
# driver = '{ODBC Driver 17 for SQL Server}'

# Azure SQL Database configuration
server = os.environ['server']
database = os.environ['database']
username =  os.environ['userN']
password = os.environ['password']
driver = '{ODBC Driver 17 for SQL Server}'

# Establishing the connection
connection = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    input1 = request.form.get('input1')
    input2 = request.form.get('input2')

    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO direct (id, name) VALUES (?, ?)", input1, input2)
        connection.commit()
        return jsonify({'message': 'Data stored successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/details', methods=['GET'])
def data():
    try:
        cursor= connection.cursor()
        cursor.execute("SELECT * FROM direct")
        rows = cursor.fetchall()

        data = []
        for row in rows:
            data.append({
                'id': row.id,
                'name': row.name
            })

        return render_template("details.html",data=data)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
