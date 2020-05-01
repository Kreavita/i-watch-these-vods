#config
WATCH_TIME = 11 # How many minutes should be watched? 11 Should be enough to get rewards

#script begins
import os, time, sys
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
except:
    proc = subprocess.check_call([sys.executable, "-m", "pip", "install", "selenium"])
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
exe = ""
if os.name == "nt": exe = ".exe"

launch_path = os.path.dirname(os.path.abspath(__file__))

index = 0
vod_list = []


def file_read(path):
    with open(path, "r") as f: lines = [line.strip() for line in f if not line.startswith("#")]
    return lines

def file_write(path, data):
    with open(path, "r") as f:
        lines = [line for line in f if line.startswith("#")]
    with open(path, "w") as f:
        f.writelines(lines)
        f.write(data)
    return True

def inline_prt(s):
    sys.stdout.write(s)
    sys.stdout.flush()
    sys.stdout.write("\b" * (len(s) + 1))

def cinput(text):
    if sys.version_info[0] == 3:
        input(text)
    else:
        raw_input(text)

for line in file_read(os.path.join(launch_path, 'data', 'index')):
    index = int(line.strip())
for line in file_read(os.path.join(launch_path, 'data', 'sources_vods')):
    if len(line) > 4: vod_list.append(line.strip())

try: driver = webdriver.Firefox(executable_path=os.path.join(launch_path, "driver", "geckodriver" + exe))
except Exception as e:
    print("WebDriver: Error occured with Firefox: {0}, forcing Chrome...".format(e))
    driver = webdriver.Chrome(executable_path=os.path.join(launch_path, "driver", "chromedriver" + exe))

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://watch.lolesports.com")
cinput('[{0}] Script loaded, Log in into the League Page to gain Rewards and then press Enter to continue...'.format(time.ctime(time.time())))

for i in range(index, len(vod_list)):
    inline_prt("[{0}] Watching {1} of {2} for {3} Minutes ...".format(time.ctime(time.time()), i + 1, len(vod_list), WATCH_TIME))

    driver.get(vod_list[i])
    
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "video-player-youtube")))

    time.sleep(1)
    
    if WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//video'))).get_attribute("currentTime") == "0":
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Play"]'))).click()
        
    driver.switch_to.default_content()
    
    time.sleep(WATCH_TIME * 60)
    
    driver.get("https://watch.lolesports.com/rewards")
    file_write(os.path.join(launch_path, 'data', 'index'), str(i))

driver.quit()

cinput("[{0}] Watched {1} VODs for {2} total Minutes, Close it or press Enter to End this script ...".format(time.ctime(time.time()), len(vod_list), len(vod_list) * WATCH_TIME))
