from flask import Flask, flash, redirect, render_template, request, session, abort
from google_images_download import google_images_download   #importing the library

from random import randint
#from icrawler import crawl
import crawl
import random
app = Flask(__name__)
response = google_images_download.googleimagesdownload()   #class instantiation
arguments = {"keywords":"cat","no_download":"no_download", "limit":10}   #creating list of arguments

@app.route("/",methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		text = request.form['text']
		if text=="":
			text="cat"
		arguments["keywords"]=text
	paths, img_list = response.download(arguments)  # passing the arguments to the function
	rand_img = random.choice(img_list)
	arguments["similar_images"] = rand_img
	arguments["keywords"] = ""
	
	return render_template('index.html')

@app.route("/img",methods=['GET', 'POST'])
def img():
	#res=render_template('test.html')
	paths, img_list = response.download(arguments)  # passing the arguments to the function
	arguments["similar_images"] = random.choice(img_list)
	
	return update_content(img_list)

def img_get(img_list):
	f = open("saving_the_urls.txt", "r").read().splitlines()
	img_url =random.choice(f)
	return img_url

def update_content(img_list):
	#random.choice(img_list)
	imgs = random.sample(img_list,3)
	#print(img1)
	 
	return render_template('test.html',name1 = imgs[0],name2 = imgs[1], name3=imgs[2])

if __name__ == "__main__":
	app.run()#host='0.0.0.0', port=80)


