
from Commands import Mkdir, Read, Touch_File, unzip, Write, ls, Read_File

COMMANDS = {
    "mkdir": Mkdir.mkdir,
    "touch": Touch_File.touch,
    "unzip": unzip.unzip,
    "read_all": Read.read_all_files,
    "read_file": Read_File.read_file,
    "ls": ls.ls,
    "write": Write.write_to_file,
}

def execute_command(command_name, args):
    if command_name in COMMANDS:
        return COMMANDS[command_name](*args)
    else:
        return f"Unknown command: {command_name}"
