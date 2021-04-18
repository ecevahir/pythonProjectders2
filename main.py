from selenium import webdriver
import ayarlar
chromesur=webdriver.Chrome(executable_path=ayarlar.chromepath)

chromesur.get("http://www.milliyet.com.tr")
chromesur.close()
