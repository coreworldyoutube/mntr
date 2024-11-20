import subprocess

def run_python_code(code: str):
    """Pythonコードを実行"""
    exec(code)

def run_java_code(code: str):
    """Javaコードをファイルに書き出して実行"""
    with open("TempProgram.java", "w") as file:
        file.write("public class TempProgram { public static void main(String[] args) { " + code + " } }")
    
    # Javaコンパイルと実行
    subprocess.run(["javac", "TempProgram.java"])
    subprocess.run(["java", "TempProgram"])

def execute_mntr_file(file_path: str):
    """.mntrファイルを読み込み、順番にプログラムを実行"""
    with open(file_path, "r") as f:
        lines = f.readlines()
    
    if lines[0].strip() != "MNTR01":
        raise ValueError("不正な形式です！")

    current_language = None
    program_code = ""

    for line in lines[1:]:
        line = line.strip()

        if line == "PYTHON":
            if current_language == "PYTHON":
                run_python_code(program_code)
            current_language = "PYTHON"
            program_code = ""
        elif line == "JAVA":
            if current_language == "PYTHON":
                run_python_code(program_code)
            current_language = "JAVA"
            program_code = ""
        else:
            program_code += line + "\n"

    # 最後のプログラムを実行
    if current_language == "PYTHON":
        run_python_code(program_code)
    elif current_language == "JAVA":
        run_java_code(program_code)

# 実行
execute_mntr_file("example.mntr")
