import subprocess
import os

if __name__ == '__main__':
    # Make a copy of the environment
    subprocess.call(['java', '-jar', '../target/Tesi-1.0-SNAPSHOT.jar','firstArgument','secondArgument'])