import os
import sys
import platform

if platform.system().lower() == 'windows':
    sysid='win'
else:
    sysid='unix'

def update_submodule(lib_name):
    os.chdir("./"+lib_name)
    cmd= "git.exe submodule update --progress --init --force"
    print(cmd)
    os.system(cmd)
    os.chdir("./..")
if __name__=='__main__':
    cmd= "git.exe submodule update --progress --init --force"
    print(cmd)
    os.system(cmd)
    # then update submodule for each sub lib
    update_submodule("Research-M")
    update_submodule("Research-V")
    update_submodule("Research-P")
    print("=====================================================================")
    print("=====================Sucessful Setup Library!========================")
    print("=====================================================================")
    print("Now, you can use the ResearchM.cmake in Research-M, ResearchV.cmake in Research-V,ResearchP.cmake in Research-P to help you construct your projects.")
    print()
    print("If you want to use exmaple to see how to use a library, for example, Research-M, you can go to Research-M folder and execute python make_project, and then use the example project in build")