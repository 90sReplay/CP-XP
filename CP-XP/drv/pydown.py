import requests

print("NOTICE: If you don't have requests pip-installed, then this will crash!")
print("        Press enter to continue.")
input()

def download_file(url, name):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(f"C:\\CP-XP\\drv\\{name}", "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print("File downloaded...")
    except requests.exceptions.RequestException as e:
        print("?Syntax Error")

print("Return the URL of the file.")
url = input()
print("Return the Name of the file.")
name = input()

download_file(url, name)
