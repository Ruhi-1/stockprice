# README

## How to setup this project using python and django.
1. This app is made using Python, Django, HTML and CSS.
2. Firstly you will need to download and install Python.
3. Then you can open your favorite code editor. I use VSCode. 
4. Once you have opened the code editor, then you need to open the terminal and install Django. The command for this is:
 ```
 pip install django
 ```

5. Next create Django project within this project using:
```
django-admin startproject <'name of the project'>
```
6. Then run:
``` 
manage.py runserver
``` 
to make sure your server is running.
7. Now you can start coding your app.

## How to build Cryptocurrency App for Bitcoin and Ethereum using 2 exchanges.
1. To create Cryptocurrency website, you will need to get Api from whichever exchange you decide to use. In this project I have used Coinbase and Gemini. To get the Api for Coinbase and Gemini you will need to go to https://developers.coinbase.com/api/v2#prices and https://docs.gemini.com/rest-api/#ticker respectively.
2. Once you get the api from these link you will need to get the data which is needed in this project. From the coinbase api I have used 2 endpoints to get the buying and selling prices. From gemini api 1 endpoint returns the 'bid' and 'ask' which is the selling and buying price respectively.
3. After that you will need to apply logic to recommend the best price to the user. The recommended buying price will be the lower buy price. The recommended selling price will be the higher sell price.
4. Then you display the values and recommended prices to the user. For this project I have used Bootstrap and CSS on the frontend. Your project should be ready to go.


[Heroku]()


