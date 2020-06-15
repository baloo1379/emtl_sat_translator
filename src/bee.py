import subprocess
import shutil
import os


def compile_and_solve(filename):
    """
    Uses BumbleBEE compiler and build-in SAT solver to create solution file
    :param filename: the .bee file which will be solved
    :return: a file with result of solving
    """

    # prepare all file paths
    app_dir = os.getcwd()
    bin_dir = f"{app_dir}/bee_binaries/"
    old_bee_file = f"{app_dir}/{filename}.bee"
    moved_bee_file = f"{bin_dir}/{filename}.bee"
    sol_file = f"{app_dir}/{filename}.sol"

    # later change to shutil.move
    shutil.copy2(old_bee_file, moved_bee_file)

    # change directory to /bee_binaries where compiler is placed
    os.chdir(bin_dir)

    # use compiler
    process = subprocess.Popen(['./BumbleBEE', moved_bee_file],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               universal_newlines=True)
    stdout, stderr = process.communicate()

    # save results to file
    with open(sol_file, 'w') as file:
        file.write(stdout)

    # back to previous directory and clear redundant file
    os.chdir(app_dir)
    os.remove(moved_bee_file)


def compile_and_save(filename):
    """
    Uses BumbleBEE compiler create CTF file
    :param filename: the .bee file which will be solved
    :return: a file with result of compilation
    """

    # prepare all file paths
    app_dir = os.getcwd()
    bin_dir = f"{app_dir}/bee_binaries/"
    old_bee_file = f"{app_dir}/{filename}.bee"
    moved_bee_file = f"{bin_dir}/{filename}.bee"
    sol_file = f"{app_dir}/{filename}.sol"
    ctf_file = f"{app_dir}/{filename}.ctf"
    map_file = f"{app_dir}/{filename}.map"

    # later change to shutil.move
    shutil.copy2(old_bee_file, moved_bee_file)

    # change directory to /bee_binaries where compiler is placed
    os.chdir(bin_dir)

    # use compiler
    process = subprocess.Popen(['./BumbleBEE', moved_bee_file, '-dimacs', ctf_file, map_file],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               universal_newlines=True)
    stdout, stderr = process.communicate()

    # save results to file
    with open(sol_file, 'w') as file:
        file.write(stdout)

    # back to previous directory and clear redundant file
    os.chdir(app_dir)
    os.remove(moved_bee_file)


if __name__ == '__main__':
    os.chdir('../')
    compile_and_solve('test')
