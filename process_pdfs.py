import subprocess

if __name__ == "__main__":
    print("Starting PDF batch processing")
    subprocess.run(["python", "main_runner.py"])
    print("Completed PDF batch processing")