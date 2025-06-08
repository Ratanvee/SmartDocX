import subprocess
import webbrowser
import os
import json

def load_shop_id():
    config_path = r"C:\Program Files\SmartDocX\printer-agent\config.json"
    if not os.path.exists(config_path):
        print("Shop ID config file not found!")
        return None

    with open(config_path, "r") as f:
        data = json.load(f)
        return data.get("shop_id")

def open_dashboard(shop_id='123'):
    if shop_id:
        url = f"http://127.0.0.1:8000"  # Or your live URL
        webbrowser.open_new_tab(url)
        print("Opened dashboard:", url)
    else:
        print("No shop ID found.")

def start_printer_agent():
    agent_path = r"C:\Program Files\SmartDocX\printer-agent\printer_agent.exe"
    if os.path.exists(agent_path):
        subprocess.Popen([agent_path], creationflags=subprocess.CREATE_NO_WINDOW)
        print("Printer agent started.")
    else:
        print("Printer agent not found!")

if __name__ == "__main__":
    # shop_id = load_shop_id()
    open_dashboard()
    start_printer_agent()
