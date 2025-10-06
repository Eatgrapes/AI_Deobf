import os
import Config
import init
import AI
import command_executor
import shutil
from Commands import Read, unzip
from datetime import datetime
import re

def main():
    print("--- Welcome to AI_Deobf ---")
    if not Config.config_exists():
        print("Configuration not found. Starting initialization process...")
        init.run_initialization()
    
    config_data = Config.load_config()
    ai_service = config_data.get("ai_service")
    print(f"Configuration loaded. Current AI Service: {ai_service}")

    print("\nSelect the language to deobfuscate:")
    print("1. Java")
    print("2. JavaScript")
    
    lang_choice = input("Enter your choice (1 or 2): ")
    if lang_choice == '1':
        language = "Java"
    elif lang_choice == '2':
        language = "JavaScript"
    else:
        print("Invalid choice. Exiting.")
        return

    file_or_folder = input("Enter the path to the file or folder to deobfuscate: ")
    if not os.path.exists(file_or_folder):
        print("File or folder not found. Exiting.")
        return

    now = datetime.now()
    deobf_folder = f"deobf/{now.strftime('%Y-%m-%d_%H-%M-%S')}"
    temp_folder = os.path.join(deobf_folder, "Temp")
    os.makedirs(deobf_folder, exist_ok=True)
    
    initial_content = ""
    if os.path.isfile(file_or_folder) and file_or_folder.endswith(('.zip', '.jar')):
        os.makedirs(temp_folder, exist_ok=True)
        print(f"Extracting {file_or_folder} to {temp_folder}...")
        unzip.unzip(file_or_folder, temp_folder)
        initial_content = Read.read_all_files(temp_folder)
    elif os.path.isdir(file_or_folder):
        initial_content = Read.read_all_files(file_or_folder)
    elif os.path.isfile(file_or_folder):
        with open(file_or_folder, 'r', encoding='utf-8') as f:
            initial_content = f.read()
    else:
        print("Unsupported file type. Exiting.")
        return

    system_prompt = f"""You are an expert software engineer specializing in code deobfuscation. Your task is to deobfuscate a {language} project.
    You have access to a set of commands to interact with a virtual file system. ALL file operations MUST be performed within the output directory.
    if language is java,you need drobf classes to java file
    You must not create any files or directories in the Temp folder.
    Available commands:
    - ls . : List files and directories.（Do not add any additional parameters,and only one path,just a '."）
    - read_all <path>: Read all files in a directory recursively.（just one path, for example : read_all src.  dont More than two paths
    - write <path> <content>: Write content to a file.
    - mkdir <path>: Create a new directory.
    - touch <path>: Create a new empty file.
    when working,don't speaking anything
    except execute commands.
    Please write the complete code of a file in full, instead of changing it one by one later.
    Don't worry about whether the necessary files are created or not, as long as they are not updated later. Don't delete or comment out any code just because they are not created.
    Please dont write Markdown's " and /
    Please ignore META-INF, then you have to deobfuscate all classes and JavaScript Class,Not one can be missed
    Please do not add " " " at the beginning or end of the code file(MUST)
    If the language is java,You must deobfuscate everything in the original class and write it into the code file. This is a must and cannot be omitted. If you encounter a strong obfuscated meaningless class name or meaningless method name, you must rename the class name and method name according to the file content. The circular code caused by meaningless obfuscation must also be removed or modified.
    If the language is JavaScript ，You need to remove and modify meaningless class names or method names to ensure that they can be used
    You must create a src Folder, and then create folders and files from it, this is the source code

    Your response must be in the format `{{start}}commands: <command_name> <args...>{{end}}`.
    When you are finished, respond with "deobfuscation complete". If no deobfuscation is needed, respond with "no deobfuscation needed".
    Start by analyzing the provided code.
    """
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Deobfuscate the following {language} code:\n{initial_content}"}
    ]

    print("\nStarting deobfuscation process...")
    while True:
        response = AI.get_ai_response(messages)
        print(f"\n[AI] {response}")
        messages.append({"role": "assistant", "content": response})

        if response.lower().strip() == "deobfuscation complete":
            print("\nDeobfuscation complete.")
            break
        elif response.lower().strip() == "no deobfuscation needed":
            print("\nNo deobfuscation needed.")
            break
        
        if response.startswith("{start}") and response.endswith("{end}"):
            response_body = response.strip().replace("{start}", "").replace("{end}", "").strip()
            parts = response_body.split()
            command_name = parts[0]
            
            print(f"Executing: {command_name}")

            if command_name == "write":
                # Use regex to extract file_path and content
                match = re.match(r'write\s+(\S+)\s+(.*)', response_body, re.DOTALL)
                if match:
                    relative_file_path = match.group(1)
                    content = match.group(2).strip()
                    file_path = os.path.join(deobf_folder, relative_file_path)
                    result = command_executor.execute_command(command_name, [file_path, content])
                else:
                    result = "Error: Could not parse write command."
            elif command_name == "unzip":
                # The source file for unzip is the one provided by the user
                result = command_executor.execute_command(command_name, [file_or_folder, temp_folder])
            else:
                args = [os.path.join(deobf_folder, arg) for arg in parts[1:]]
                result = command_executor.execute_command(command_name, args)

            print(f"[System] {result}")
            messages.append({"role": "user", "content": f"Command result: {result}"})
        else:
            # If the AI responds with something other than a command or completion,
            # ask it for the next command.
            messages.append({"role": "user", "content": "Please provide the next command."})


    if os.path.exists(temp_folder):
        shutil.rmtree(temp_folder)
        print("Temp folder deleted.")
    print(f"Deobfuscated files are in: {deobf_folder}")

if __name__ == "__main__":
    main()