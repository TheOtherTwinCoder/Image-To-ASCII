# Image-To-ASCII API
An API that converts any image to an ASCII-themed structure, including black-and-white, colored, and AI-generated ASCII art.

# What is ASCII art?
ASCII art is a form of art that utilizes monospaced characters in such a way to mimic the original image! This is done using an algorithm that parses each pixel, allowing it to check its brightness. The brightness can then be coded to a specific character, usually from one of two sets. Then, the character is placed on the canvas. This process is repeated for each pixel, until the final image is created!

# Examples
Original Image: 

<img width="640" height="427" alt="image" src="https://github.com/user-attachments/assets/43cb7267-6844-4bf9-a136-10ee5c427066" />

Black and White (classic):

<img width="1579" height="1017" alt="Screenshot 2026-06-13 at 6 07 44 PM" src="https://github.com/user-attachments/assets/ab95cb36-5615-4023-a14b-c36175aba14a" />


Color:

<img width="1577" height="1048" alt="Screenshot 2026-06-13 at 6 08 24 PM" src="https://github.com/user-attachments/assets/94b974bf-5dd9-4e03-892e-412c85f25f24" />

Pretty cool, huh?

> [!TIP]
> The colored image is shown in a web browser. If you use cURL, for example, you'll get **a bunch** (and I mean a bunch) of html code! 

# How to use it:
Here's the API Link: https://image-to-ascii-2q75.onrender.com

For the docs, check out https://image-to-ascii-2q75.onrender.com/docs.

## However, here's a detailed guide:

The [link](https://image-to-ascii-2q75.onrender.com) has three modes: **Black and White**, **Color**, and **AI generated**. You can also check the **health** of the server. 
To use each mode, follow its respective guide below:

## Black and White
To use black and white, add ```/bnw/``` to the end of the API link (above). Then, you will need to add query parameters: the URL (str), whether to invert the brightness or not (bool), whether or not to use a complex versison of the ASCII art brightness list (bool), and whether or not to output plaintext (bool).



The ```url``` query needs a URL leading to an image that will be converted to ASCII art. For example, [this link](https://i.ibb.co/1Gh7h7pF/wt-Ttc3-KAAU.jpg) is a valid URL. To enter it, simply put ```?url=``` after the ```/bnw/``` and enter the url afterwards. 

The ```invertbrightness``` query allows the user to choose whther or not to invert the image's brightness values. To enter it, enter ```&invertbrightness=``` after the url parameter. It accepts ```true``` and ```false```. 

The ```complex``` query allows the user to choose whether or not to use a complex version of the ASCII art brightness table. To enter it, enter ```&complex=``` after the ```invertbrightness``` parameter. It accepts ```true``` and ```false```.

The ```plaintext``` query allows the user to choose whether the output comes in plaintext format or not. To enter it, enter ```&plaintext=``` after the complex parameter. It accepts ```true``` and ```false```.

**Example: https://image-to-ascii-2q75.onrender.com/bnw/?url=https://i.ibb.co/nMZ6Z6Vx/wt-Ttc3-KAAU.jpg&invertbrightness=false&complex=false&plaintext=true. Try it out!** 


## Colored
To use color, add ```/colored/``` to the end of the API link (above). Then, you will need to add query parameters: the URL (str), whether to invert the brightness or not (bool), whether or not to use a complex versison of the ASCII art brightness list (bool), and whether or not to invert the color (bool).



The ```url``` query needs a URL leading to an image that will be converted to ASCII art. For example, [this link](https://i.ibb.co/1Gh7h7pF/wt-Ttc3-KAAU.jpg) is a valid URL. To enter it, simply put ```?url=``` after the ```/bnw/``` and enter the url afterwards. 

The ```invertbrightness``` query allows the user to choose whther or not to invert the image's brightness values. To enter it, enter ```&invertbrightness=``` after the url parameter. It accepts ```true``` and ```false```. 

The ```complex``` query allows the user to choose whether or not to use a complex version of the ASCII art brightness table. To enter it, enter ```&complex=``` after the ```invertbrightness``` parameter. It accepts ```true``` and ```false```.

The ```invertcolor``` query allows the user to choose whether or not to invert the image's color. To enter it, enter ```&invertcolor=``` after the complex parameter. It accepts ```true``` and ```false```.

**Example: https://image-to-ascii-2q75.onrender.com/colored/?url=https://i.ibb.co/nMZ6Z6Vx/wt-Ttc3-KAAU.jpg&invertbrightness=false&invertcolor=false&complex=false. Try it out!** 

## AI generated
To  AI generate ASCII images, add ```/ai/``` to the end of the API link (above). Then, next to it, enter the character or scene to generate. For example, do not enter ```Generate a dog.``` Instead, just add ```dog```.

**Example: https://image-to-ascii-2q75.onrender.com/ai/fluffy dog/. Try it out!**

## Health
This checks the health of the server. If you want to check it, go to https://image-to-ascii-2q75.onrender.com/health.

> [!IMPORTANT]
> All of the parameters are required. If you try to visit the link without a parameter, you'll get an error!

If you encounter an error 
