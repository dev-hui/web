import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from selenium import webdriver
import twitter
import tweepy

twitter_consumer_key = "RC1Da2IWF3d3RrjjuAMsgIZhu"
twitter_consumer_secret = "yeMmgMHHLWq67PmIha21sfo1ErDZMCdcfk6TWIXdL7HZtC4PxL"  
twitter_access_token = "2965836421-7b8crBaWXyWoZCNByETv6hSwEfSAO38xPBfAhpy"
twitter_access_secret = "Fk2vLTRDl5ErdUPclBaoZn2XyVOc7vGePDnVk0YU7AAEx"

twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                      consumer_secret=twitter_consumer_secret, 
                      access_token_key=twitter_access_token, 
                      access_token_secret=twitter_access_secret)

app = Flask(__name__)
 
@app.route('/')
def index():
  return render_template('index.html')
  
@app.route('/index')
def homepage():
  return render_template('index.html') 

@app.route('/work')
def work():
  return render_template('work.html')   
  
@app.route('/another')
def another():
  return render_template('another.html')   
  
@app.route('/blah')
def blah():
    return render_template('blah.html')  

@app.route('/favorite')
def favorite():    
  return render_template('favorite.html')
  
@app.route('/news')
def news():    
  return render_template('news.html')

@app.route('/news_result', methods=['POST'])
def result():
    if request.method == 'POST':
        keyword = request.form['input1']
        page    = request.form['input2']
        
        daum_news_list = []
        
        for i in range(1, int(page)+1) : 
            resp = requests.get('https://search.daum.net/search?w=news&q=' + keyword + '&p=' + str(i))
            soup = BeautifulSoup(resp.text, 'html.parser')
            
            for i in soup.find_all("a", class_="f_link_b") :
                daum_news_list.append(i.text)

        return render_template("news_result.html", daum_list = daum_news_list)

@app.route('/shopping')
def shopping():    
  return render_template('shopping.html')

@app.route('/shopping_result', methods=['POST'])
def naver_shopping():        
    search  = request.form['input3']
    search_list = []
    search_list_src = []

    driver = webdriver.Chrome()
    driver.implicitly_wait(3)

    driver.get("https://search.shopping.naver.com/search/all_search.nhn?query=" + search)

    import time 

    y = 1000
    for timer in range(0, 10):
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        y += 1000
        time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    for i in soup.select("div.search_list.basis > ul > li") :
        search_list_src.append(i.find("img", class_="_productLazyImg")["src"])
        search_list.append(i.find("a", class_="link").text)

    driver.close()
        
    return render_template('shopping_result.html',
                           search_list = search_list,
                           search_list_src = search_list_src,
                           len = len(search_list))
        

@app.route('/horoscope')
def horoscope() :
  return render_template('horoscope.html')



@app.route('/horoscope_result', methods=['POST'])
def horoscope_result() :

    if request.method == 'POST' : 
        month = int(request.form['month'])
        day  = int(request.form['day'])
        
        if month == 3:
            if day >= 21 and day <= 31:
                birth = "양자리"
        else:
            pass
        if month == 4:
            if day >= 1 and day <= 19:
                birth = "양자리"
        else:
            pass
        if month == 4:
            if day >= 20 and day <= 30:
                birth = "황소자리"
        else:
            pass
        if month == 5:
            if day >= 1 and day <= 20:
                birth = "황소자리"
        else:
            pass
        if month == 5:
            if day >= 21 and day <= 31:
                birth = "쌍둥이자리"
        else:
            pass
        if month == 6:
            if day >= 1 and day <= 20:
                birth = "쌍둥이자리"
        else:
            pass
        if month == 6:
            if day >= 21 and day <= 30:
                birth = "게자리"
        else:
            pass
        if month == 7:
            if day >= 1 and day <= 22:
                birth = "게자리"
        else:
            pass
        if month == 7:
            if day >= 23 and day <= 31:
                birth = "사자자리"
        else:
            pass
        if month == 8:
            if day >= 1 and day <= 22:
                birth = "사자자리"
        else:
            pass
        if month == 8:
            if day >= 23 and day <= 31:
                birth = "처녀자리"
        else:
            pass
        if month == 9:
            if day >= 1 and day <= 22:
                birth = "처녀자리"
        else:
            pass
        if month == 9:
            if day >= 23 and day <= 30:
                birth = "천칭자리"
        else:
            pass
        if month == 10:
            if day >= 1 and day <= 22:
                birth = "천칭자리"
        else:
            pass
        if month == 10:
            if day >= 23 and day <= 31:
                birth = "전갈자리"
        else:
            pass
        if month == 11:
            if day >= 1 and day <= 21:
                birth = "전갈자리"
        else:
            pass
        if month == 11:
            if day >= 22 and day <= 30:
                birth = "사수자리"
        else:
            pass
        if month == 12:
            if day >= 1 and day <= 21:
                birth = "사수자리"
        else:
            pass
        if month == 12:
            if day >= 22 and day <= 31:
                birth = "염소자리"
        else:
            pass
        if month == 1:
            if day >= 1 and day <= 19:
                birth = "염소자리"
        else:
            pass
        if month == 1:
            if day >= 20 and day <= 31:
                birth = "물병자리"
        else:
            pass
        if month == 2:
            if day >= 1 and day <= 18:
                birth = "물병자리"
        else:
            pass
        if month == 2:
            if day >= 19 and day <= 28:
                birth = "물고기자리"
        else:
            pass
        if month == 3:
            if day >= 1 and day <= 20:
                birth = "물고기자리"
        else:
            pass
                        
    browser = webdriver.Chrome()
    browser.get('https://search.naver.com/search.naver?&query=별자리운세')
    import time
    time.sleep(1)
    browser.find_element_by_link_text(birth).click()
    
    ret = browser.page_source
    
    soup = BeautifulSoup(ret, 'html.parser')
    horo1 = "오늘의 운세 : " + soup.find_all("p", class_="text _cs_fortune_text")[0].text
    horo2 = "내일의 운세 : " + soup.find_all("p", class_="text _cs_fortune_text")[1].text
    horo3 = "이번 주의 운세 : " + soup.find_all("p", class_="text _cs_fortune_text")[2].text
    horo4 = "이번 달의 운세 : " + soup.find_all("p", class_="text _cs_fortune_text")[3].text
    
    horo_list = [horo1, horo2, horo3, horo4]
    horo_list
    
    browser.quit()
    

    return render_template('horoscope_result.html', ret_horo_list=horo_list, ret_horo=birth)


@app.route('/astro')
def astro() :
  return render_template('astro.html')
  

@app.route('/astro_result', methods=['POST'])
def astro_result() :

    if request.method == 'POST' : 
        month = request.form['month']
        day  = request.form['day']
        astro_birth =  month + day

        month='01'
        day='01'
        astro_birth=month+day
        astro_birth

    browser = webdriver.Chrome()
    browser.get('https://apod.nasa.gov/apod/archivepix.html')
    import time
    time.sleep(1)

    browser.find_element_by_css_selector("a[href*=astro_birth]").click();
    
    ret = browser.page_source

    soup = BeautifulSoup(ret, 'html.parser')
    astro1 = "title : " + soup.select("center.b")[0].text
    astro2 = soup.select("a.img")

    astro_list = "당신의 날의 우주 : " 
    
    browser.quit()

    return render_template('astro_result.html', ret_astro=astro_list)

@app.route('/twitter')
def twitter() :
  return render_template('twitter.html')
  

@app.route('/twitter_result', methods=['POST'])
def twitter_result() :
                                                    
    if request.method == 'POST' :
        keyword = request.form['input5']
        tw_result = [] 
        
    tweet = twitter_api.GetSearch(term=keyword, count=20)
    for tw in tweet :
        tw_result.append(tw.text)                          

    return render_template('twitter_result.html', ret_tw_result=tw_result)
  
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
