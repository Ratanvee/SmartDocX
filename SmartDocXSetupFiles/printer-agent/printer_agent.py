# import time
# import requests
# import win32api
# import win32print
# import os
# import json

# def load_shop_id():
#     path = "printer-agent/config.json"
#     with open(path, "r") as f:
#         return json.load(f).get("shop_id")

# def print_file(file_path):
#     win32api.ShellExecute(0, "print", file_path, None, ".", 0)

# def main():
#     shop_id = load_shop_id()
#     while True:
#         try:
#             # response = requests.get(f"https://yourwebsite.com/api/get-jobs/{shop_id}")
#             response = requests.get(f" http://127.0.0.1:8000")
#             jobs = response.json().get("jobs", [])

#             for job in jobs:
#                 file_url = job["file_url"]
#                 file_name = os.path.basename(file_url)
#                 local_path = os.path.join("C:\\PrintEase\\queue", file_name)

#                 r = requests.get(file_url)
#                 with open(local_path, "wb") as f:
#                     f.write(r.content)

#                 print_file(local_path)

#                 # requests.post(f"https://yourwebsite.com/api/update-job-status/{job['id']}",
#                 requests.post(f" http://127.0.0.1:8000",
#                               json={"status": "completed"})
#         except Exception as e:
#             print("Error:", e)

#         time.sleep(10)

# if __name__ == "__main__":
#     main()



# ==============================
# Step 1: printer_agent.py (background agent that checks for print jobs)
# ==============================
import time
import requests
import win32api
import win32print
import os
import json

def load_shop_id():
    path = r"C:\\Program Files\\SmartDocX\\printer-agent\\config.json"
    with open(path, "r") as f:
        return json.load(f).get("shop_id")

def print_file(file_path):
    win32api.ShellExecute(0, "print", file_path, None, ".", 0)

def download_file(url, local_path):
    r = requests.get(url)
    with open(local_path, "wb") as f:
        f.write(r.content)
    return local_path

def main():
    shop_id = load_shop_id()
    while True:
        try:
            response = requests.get(f"http://127.0.0.1:8000/api/get-pending-jobs/{shop_id}")
            jobs = response.json().get("jobs", [])

            for job in jobs:
                file_url = job["file_url"]
                file_name = os.path.basename(file_url)
                local_path = os.path.join("C:\\SmartDocX\\queue", file_name)

                download_file(file_url, local_path)
                print_file(local_path)

                requests.post(f"http://127.0.0.1:8000/api/update-job-status/{job['id']}/", json={"status": "printed"})
        except Exception as e:
            print("Error:", e)

        time.sleep(10)

if __name__ == "__main__":
    main()

