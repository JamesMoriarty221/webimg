from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
#from icrawler import crawl
import crawl
import random
app = Flask(__name__)
 
@app.route("/",methods=['GET', 'POST'])
def index():
	crawl.run("cat")
	return render_template('index.html')
	#return "What do you like?"

@app.route("/img",methods=['GET', 'POST'])
def img():

	if request.method == "POST":
		text = request.form['text']
		crawl.run(text)
	res = update_content()
	return res

def img_get():
	f = open("saving_the_urls.txt", "r").read().splitlines()
	img_url =random.choice(f)
	return img_url

def update_content():
	img1 = img_get()
	img2 = img_get()
	img3 = img_get()
	print(img1)
	 
	return render_template('test.html',name1 = img1,name2 = img2, name3=img3)

if __name__ == "__main__":
	app.run()#host='0.0.0.0', port=80)


