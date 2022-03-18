from spartan import Spartan
import json

def read_option():
    while True:
        user_option = input("This is a list of your options: \nadd: Add a spartan, \nremove: Remove a spartan, \nlist: List the spartan , \nview: View by id \nsave: Save to JSON, \nload: Load from JSON, \nexit: Exit the app")
        user_option = user_option.strip()

        if user_option in ["add", "remove",  "list", "view", "save", "load", "exit"]:
            return user_option
        else:
            print("Error, You should select one of the options in the list")


def read_sparta_id():
    while True:
        id_str = input("Please Enter the spartan's ID:")
        id_str = id_str.strip()

        if id_str.isdigit():
            sparta_id = int(id_str)
            if sparta_id > 0 :
                return sparta_id
            else:
                print("Error, The sparta ID should be positive number")
        else:
            print("Error, The sparta ID should be a number")


def read_first_name():
    while True:
        first_name = input("Please Enter The spartan's First Name:")
        first_name = first_name.strip()

        if len(first_name) >= 2:
            return first_name
        else:
            print("Error, The  First Name should be at least 2 Characters")


def read_last_name():
    while True:
        last_name = input("Please Enter The spartan's Last Name:")
        last_name = last_name.strip()

        if len(last_name) >= 2:
            return last_name
        else:
            print("Error, The Employee Last Name should be at least 2 Characters")


def read_year():
    while True:
        year_str = input("Please Enter the  Birth Year:")
        year_str = year_str.strip()

        if year_str.isdigit():
            year = int(year_str)
            if (year >= 1900) and (year <= 2004):
                return year
            else:
                print("Error, The  Birth Year should be between 1900 and 2004")
        else:
            print("Error, The  Birth Year should be a number")


def read_month():
    while True:
        month_str = input("Please Enter the  Birth Month:")
        month_str = month_str.strip()

        if month_str.isdigit():
            month = int(month_str)
            if (month >= 1) and (month <= 12):
                return month
            else:
                print("Error, The  Birth Month should be between 1 and 12")
        else:
            print("Error, The  Birth Month should be a number")


def read_day():
    while True:
        day_str = input("Please Enter the  Birth Day:")
        day_str = day_str.strip()

        if day_str.isdigit():
            day = int(day_str)
            if (day >= 1) and (day <= 31):
                return day
            else:
                print("Error, The  Birth Day should be between 1 and 31")
        else:
            print("Error, The  Birth Day should be a number")


def read_course():
    while True:
        course = input("Please Enter The course:")
        course = course.strip()
        if len(course) >= 2:
            return course
        else:
            print("Error, The spartan course should be valid")


def read_stream():
    while True:
        stream = input("Please Enter The stream:")
        stream = stream.strip()
        if len(stream) >= 2:
            return stream
        else:
            print("Error, The spartan course should be valid")

def read_view_spartan_id():
    while True:
        view_id_str = input("Enter the id of spartan you would like to view? ")
        if view_id_str.isdigit():
            view_id = int(view_id_str)
            return view_id
        else:
            print("WARNING: Enter a Valid Spartan ID")


"""
def find_employee():
    spartan_id = input(f"Please Enter Employee Id  :")
    if spartan_id in all_sparta_dict:
        print(all_sparta_dict[spartan_id])
    else:
        print("Employee Id is not valid")
"""


def save_to_json():
    #all_sparta_dict ={}
    temp_dict_of_dict = {}
    for spartan_id in all_sparta_dict:
        sparta_object = all_sparta_dict[spartan_id]
        sparta_dict = sparta_object.__dict__
        temp_dict_of_dict[spartan_id] = sparta_dict

    with open("data.json", "w") as data_file:
        json.dump(temp_dict_of_dict, data_file)


def load_from_json():
    global all_sparta_dict
    all_sparta_dict = {}
    temp_dict_of_dict = {}
    try:
        with open("data.json", "r") as data_file:
            temp_dict_of_dict = json.load(data_file)

    except:
        print("The file data.json doesn't exist")

    print(temp_dict_of_dict)

    for sparta_id_key in temp_dict_of_dict:
        spartan_id = temp_dict_of_dict[sparta_id_key]['spartan_id']
        first_name = temp_dict_of_dict[sparta_id_key]['first_name']
        last_name = temp_dict_of_dict[sparta_id_key]['last_name']
        birth_year = temp_dict_of_dict[sparta_id_key]['birth_year']
        birth_month = temp_dict_of_dict[sparta_id_key]['birth_month']
        birth_day = temp_dict_of_dict[sparta_id_key]['birth_day']
        course = temp_dict_of_dict[sparta_id_key]['course']
        stream = temp_dict_of_dict[sparta_id_key]['stream']

        sparta_object = Spartan(spartan_id, first_name, last_name, birth_year, birth_month, birth_day, course, stream, )
        all_sparta_dict[spartan_id] = sparta_object


if __name__ == "__main__":
    all_sparta_dict = {}
    load_from_json()
    while True:
        option = read_option()

        if option == "add":
            print("The user wants to add a spartan")
            spartan_id = read_sparta_id()
            first_name = read_first_name()
            last_name = read_last_name()
            birth_year = read_year()
            birth_month = read_month()
            birth_day = read_day()
            course = read_course()
            stream = read_stream()
            sparta_object = Spartan(spartan_id, first_name, last_name, birth_year, birth_month, birth_day, course,
                                    stream, )
            all_sparta_dict[spartan_id] = sparta_object
            save_to_json()
            print(all_sparta_dict)
        elif option == "remove":
            print("The user wants to remove a spartan")
            spartan_id = read_sparta_id()
            del all_sparta_dict[spartan_id]
            save_to_json()

        elif option == "list":
            print("The user wants a list of the spartans")
            for spartan_id in all_sparta_dict:
                sparta_object = all_sparta_dict[spartan_id]
                print(sparta_object)
                save_to_json()
        elif option == "view":
            while True:
                spartan_id_view = read_view_spartan_id()
                if spartan_id_view in all_sparta_dict.keys():
                    print(f"The details of the Spartan, with Spartan ID {spartan_id_view}, can be found below:")
                    all_sparta_dict[spartan_id_view].print_spartan_data()
                    break
                else:
                    print("WARNING: Spartan ID entered doesn't exist in the system")
        elif option == "save":
            print("The data will ba saved to JSON file")
            save_to_json()

        elif option == "load":
            print("The data will be loaded from a JSON file")
            load_from_json()

        elif option == "exit":
            print("Thanks, see you later")
            break
        else:
            print("invalid option")