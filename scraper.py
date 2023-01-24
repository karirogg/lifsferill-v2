import urllib.request
from tqdm import tqdm
imgURL = "https://projecteuler.net/captcha/show_captcha.php"

for i in tqdm(range(1000)):
    urllib.request.urlretrieve(imgURL, f"./img/captcha_{i}.png")