# AirBnB_clone
AirBnB_clone - The Console

## Project Description
This project aims to build a command-line interpreter for managing AirBnB objects.The command interpreter facilitates the creation, retrieval, updating and deletion of AirBnB objects.

##Command Interpreter Description
The command interpreter can be initiated by running the 'console.py' script. It provides a set of commands for interacing with AirBnB objects.Users can create, retrieve, update, and delete objects through the provided commands.

##How to Start
1. **Clone this repository to your local machine:**
    ```bash
    git clone https://github.com/your-username/airbnb-clone.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd airbnb-clone
    ```

3. **Run the command `./console.py` to start the AirBnB console:**
    ```bash
    ./console.py
    ```

### How to Use

- Upon starting the console, use commands to interact with AirBnB objects.
- Use the `help` command to view the list of available commands and their usage.

### Examples

```bash
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) create User
a1373d34-377e-42d7-9b19-5385577a51f4
(hbnb) show User a1373d34-377e-42d7-9b19-5385577a51f4
[User] (a1373d34-377e-42d7-9b19-5385577a51f4) {'id': 'a1373d34-377e-42d7-9b19-5385577a51f4', 'created_at': '2023-01-01T12:00:00', 'updated_at': '2023-01-01T12:00:00'}

(hbnb) update User a1373d34-377e-42d7-9b19-5385577a51f4 name "John Doe"
(hbnb) show User a1373d34-377e-42d7-9b19-5385577a51f4
[User] (a1373d34-377e-42d7-9b19-5385577a51f4) {'id': 'a1373d34-377e-42d7-9b19-5385577a51f4', 'created_at': '2023-01-01T12:00:00', 'updated_at': '2023-01-01T12:01:00', 'name': 'John Doe'}

(hbnb) quit
$


