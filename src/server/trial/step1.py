import os
import subprocess

# runs files on local computer
def execute_local(file_path):
    # os.path.splitext("/path/to/file.ext") = ("'file','.ext'")
    file_path_without_extension = os.path.splitext(file_path)[0]
    # contains directory part of file_path
    file_dir = os.path.dirname(file_path)
    # lets subprocess run current directory files
    if file_dir == "":
        file_dir = os.path.dirname(__file__)
    print ("file_dir: ",file_dir)
    try:
        # runs the terminal command - compile (gcc name.c -o name)
        process_compile = subprocess.run(["gcc",file_path,"-o", file_path_without_extension],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        # debug statements: 'process_compile' var holds returned process data
        print ("process_compile stdout:",process_compile.stdout)
        print ("\nprocess_compile stderr:\n",process_compile.stderr)

    #if compilation is not clear, then handle it
    except subprocess.CalledProcessError as e:
        print ("\nCompilation Error\n")
        # print(e)
        exit(1)


    #if compilation is clear, try to run the file
    else:
        try:
            # runs terminal command - execute (./name)
            process_exec = subprocess.run([file_dir+file_path_without_extension],check=True,timeout=5,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            # debug statements: 'process_exec' var holds returned process data
            print ("\n\nprocess_exec stdout:",process_exec.stdout)
            print ("\nprocess_exec stderr:",process_exec.stderr)

        #if program execute is unclear, handle it here
        except subprocess.CalledProcessError:
            print ("Execution Error")
            exit(1)

        #if program execution is successful, handle it here
        else:
            print ("Execution Successful")
            exit(0)

    return

# demo function instance as proof of concept
execute_local("hello_world.c")
