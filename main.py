import management
from spartan import Spartan
from flask import Flask, request, jsonify
import json

flask_object = Flask(__name__)

#   http://127.0.0.1:5000
@flask_object.route('/', methods = ["GET"])
def home_page():
    return "Welcome to the home page, API allow application to interact with external data resources"
""""
method: GET, route: /spartan/<spartan_id>
  Get certain employee using the spartan_id. An error message should be returned if the spartan_id doesn't exist in the system. The data should be returned as string
"""
@flask_object.route('/spartan_add', methods=['POST'])  # allows user to add sparta data by passing json file
def add_employee():
    management.load_from_json()
    # management.json_load()
    sparta_data = request.json  #
    spartan_id = sparta_data['spartan_id']
    first_name = sparta_data['first_name']
    last_name = sparta_data['last_name']
    birth_year = sparta_data['birth_year']
    birth_month = sparta_data['birth_month']
    birth_day = sparta_data['birth_day']
    course = sparta_data['course']
    stream = sparta_data['stream']

    # call the method that will create the employee record
    sparta_object = Spartan(spartan_id, first_name, last_name, birth_year, birth_month, birth_day, course, stream)
    sparta_object.print_spartan_data()
    management.save_to_json()
    return f"The employee ({spartan_id}: {first_name} {last_name} {birth_year} {birth_month} {birth_day} {course} {stream})"

# http://127.0.0.1:5000//spartan/<spartan_id> get certain employee data, return error message if id doesnt exists in system, return as string@flask_object.route('/spartan/<spartan_id>', methods=["GET"])
@flask_object.route('/spartan/<spartan_id>', methods=["GET"])
def sparta_id_getter(spartan_id):
    # Check the database, read from a file, etc
    data = jsonify(id=spartan_id, name="Test", position="Data")
    return data


# #http://127.0.0.1:5000/spartan/remove?id=sparta_id   This API should allow the user to remove a spartan from the system by passing the sparta_id in the query_string@flask_object.route('/spartan/remove', methods=['POST'])
def remove():
    id_to_remove = request.args.get("id")
    return f"User would like to remove: {id_to_remove}"



@flask_object.route('/spartan', methods=["GET"])
def list_all():
    return "User would like to list the Spartans as one JSON object"


a




if __name__ == "__main__":
    #all_sparta_dict = {}
    #v_dict = all_sparta_dict
    flask_object.run()
    #flask_object.run(debug=True)