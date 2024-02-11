The Main, python library used in this code is Pillow it is a PIL Fork.
Then a string of characters were creted in decending order. The decending order implies the gradient effect, the one on the starting will be used to represent darker tones of the image where as the one on the ending side will represent lighter areas.
Then resizing of the frame to get a good ratio of the image was done. That the ascii art resembles the image and does not changes the orinetation of the image.
In my first attempt i was unable to get a proper height, as I was leaving the canvas to the math that was new width wih aspect ratio. 
That didn't gave any clean reasults to 1080p images. Thus scraping the idea of leaving it to the math, so the solution I was able to aquire was that, I rather set a fix parameter for height and width and let the program do the ascii. 
Setting fixed parameters made it easier for landscape photos to look decent in ASCII.
Doing So, I made a seperate verision for Portrait.
After the resizing of frame was done, the image was converted to gray scale. As gray scale gives out the comeplete data of the image in black and white thus making it easier to procude the ASCII version.
After assigning all the values and operations, we gave a field that was set to recieve path form the user. 
The Path, will have a .png or any image extension file if the file doesn't have a vaild path or extension, it will not be valid giving out a "is not valid" message.
Then the data of the image will be converted to ASCII farme. 
The format of the image will be changed and format will be changed. Pixel count will ensure the ascii image width, height.
Then we will print the ASCII Image.
And then we made a funtion to save the file in a .txt file format. 
Finalising with calling the main funtion
