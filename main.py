import requests

VERSION = "1.0.0"
LATEST_VERSION_URL = "https://raw.githubusercontent.com/zouzef/version_project/main/latest_version.txt"
def check_for_update():
    try:
        response = requests.get(LATEST_VERSION_URL, timeout=5)
        if response.status_code == 200:
            latest_version = response.text.strip()
            if latest_version != VERSION:
                print(f"A new version ({latest_version}) is available! You are running {VERSION}.")
            else:
                print("You are running the latest version.")
        else:
            print("Could not check for updates (HTTP error).")
    except Exception as e:
        print(f"Could not check for updates: {e}")

def main():
    check_for_update()
    print("Hello, this is your main program.")

if __name__ == "__main__":
    main()
