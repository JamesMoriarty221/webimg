from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

#arguments = {"keywords":"Polar bears","limit":20,"print_urls":True,"no_download":""}   #creating list of arguments
arguments = {"keywords":"pussy creampie","no_download":"no_download", "limit":10}   #creating list of arguments
paths,img_list = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths ofcccccccccccccccc the downloaded images
print(img_list)