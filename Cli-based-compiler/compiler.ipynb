import subprocess
import re

def get_code_from_user():
    print("Enter your code (type 'EOF' on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == 'EOF':
            break
        lines.append(line)
    return '\n'.join(lines)

def highlight_syntax(code, language):
    keywords = {
        'python': ['def', 'class', 'import', 'from', 'return', 'if', 'else', 'elif'],
        'java': ['public', 'class', 'static', 'void', 'main', 'if', 'else', 'return']
    }
    keyword_format = '\033[94m' 
    reset_format = '\033[0m'

    for keyword in keywords[language]:
        code = re.sub(f'\\b{keyword}\\b', f'{keyword_format}{keyword}{reset_format}', code)
    return code

def execute_python(code):
    try:
        exec(code)
    except Exception as e:
        return str(e)
    return "Python code executed successfully."

def execute_java(code, filename='Main.java'):
    with open(filename, 'w') as file:
        file.write(code)

    compile_process = subprocess.run(['javac', filename], capture_output=True, text=True)
    if compile_process.returncode != 0:
        return compile_process.stderr

    run_process = subprocess.run(['java', filename.split('.')[0]], capture_output=True, text=True)
    if run_process.returncode != 0:
        return run_process.stderr

    return run_process.stdout

def main():
    print("Welcome to MultiCode CLI IDE!")
    print("Select the language (python/java):")
    language = input().strip().lower()

    code = get_code_from_user()
    highlighted_code = highlight_syntax(code, language)

    print("\nYour code with syntax highlighting:")
    print(highlighted_code)

    if language == 'python':
        output = execute_python(code)
    elif language == 'java':
        output = execute_java(code)
    else:
        output = "Unsupported language."

    print("\nExecution Output:")
    print(output)

if __name__ == '__main__':
    main()
