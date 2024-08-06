import subprocess
import sys

def install_requirements(requirements_file='requirements.txt'):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_file])
        print("Packages installed successfully.")
    except subprocess.CalledProcessError as e:
        print("An error occurred while installing packages.")
        print(e)

if __name__ == "__main__":
    install_requirements()