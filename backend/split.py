import subprocess

def separate_audio(input_file):
    output_dir = "output_directory"  # Specify your output directory
    subprocess.run(["umx", input_file, "-o", output_dir])
