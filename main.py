from selenium import webdriver

chromesur=webdriver.Chrome(executable_path="C:\\Users\\emre\\PycharmProjects\\WebSuruculeri\\x86\\chromedriver.exe")

chromesur.get("http://www.milliyet.com.tr")
chromesur.close()
