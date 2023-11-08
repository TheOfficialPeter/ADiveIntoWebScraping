---
title: "A Dive into Web Scraping"
layout: post
---

> Skill level: Python beginner

### Hello 👋

Welcome to the new version of my Web Scraping blog post. In this remake I will be more precise and promise to keep things **simple**.

You probably noticed a lot of Web Scraping jobs on freelancing sites and now you are surfing the web trying to figure out what the heck web scraping is all about.

**Look no further 👀**

I'm not good at promoting stuff but I am sure you will find what you need here. To make things simple I have broken it down into steps. You might hate doing steps and want to skip to the advanced stuff. Please don't 😕


**Let's jump in 🏃‍♂️**

## Table of Contents

#### Basic

1. Installing Python + libraries
    1. Installing VsCode and configuring Python
2. Introduction to Requests
    1. Example of Requests
3. Introduction to Beautiful Soup
    1. Example of Beautiful Soup

#### Advanced

4. What is lazy-loading and how to overcome it.
5. Introduction to Selenium
    1. Example of Selenium
6. Introduction to MatplotLib
    1. Displaying information using PyPlot

#### Web Scraping with NodeJS

7. Getting started with NodeJS
      1. What is NodeJS?
      2. Why use NodeJS?
      3. Installing NodeJS
      4. Installing NodeJS modules
8. Introduction to Puppeteer
    1. Example of Puppeteer

#### Browser Automation

9. What is Browser Automation
10. Introduction to browser automation with Selenium
    1. Example of browser automation with Selenium
11. Final thoughts and conclusions

## Installing Pyton

Installing python is really simple. Just visit [the official python site](https://www.python.org/downloads/) and download the latest version and open the installer. During installation please make sure you have checked the box that **adds python to the PATH**. If you don't see the checkbox, add it manually. [Here](https://medium.com/@omoshalewa/why-you-should-add-python-to-path-and-how-58693c17c443) is an example. If this link is broken just google 'How to add python to PATH'.<br/>

### Installing VsCode

Time to get a text editor. We will be using [VsCode](https://code.visualstudio.com) ( beginner friendly ) After installing [Vscode](https://code.visualstudio.com) from the website, open it up and you should be greeted with a fancy looking UI. Now we are going to connect Python with Vscode otherwise we our text editor (Vscode) is useless. I will be explaining how to install the extension, but if you find it difficult to follow you can also visit the official tutorial [here](https://code.visualstudio.com/docs/languages/python). Upon being greeted with the main User Interface, navigate to the extensions tab. (Picture below of the extensions tab icon)

![image](https://user-images.githubusercontent.com/57006688/205931750-ab716e71-84f6-41e6-9bcc-a2d2c559923d.png)

Search python in the textbox then install the first one. It might take some time to install.

![image](https://user-images.githubusercontent.com/57006688/205932087-fcbac426-c45c-453e-bcf0-bd330eb8e027.png)

After installed press `ctrl+shift+p` (You can also go the the <b>View</b> tab and select <b>Open command palette</b>). A window from the top should appear, type in `Python: Select Interpreter` and press Enter or Click on that option.

![group js - Chat - Visual Studio Code 12_6_2022 10_36_50 PM](https://user-images.githubusercontent.com/57006688/206017893-3617bf8b-402a-4e85-b831-8f0d47e52d68.png)

Then select the **recommended one**. Great! Now we have Python connected to Vscode.<br/>

**Let's keep going :running_man:**

## Requests

The Requests library is a pre-installed ( meaning you don't have to do anything to get it ) python library. If you don't have the library installed or just want to make sure do the following:<br/>

1. Open windows command prompt or your default terminal.
2. Type in `pip install requests`
3. Look at what the output says. It will state whether the requirements are already met (already installed) or not. Either way it should be installed.

Requests is used to make HTTP requests to web pages / ip addresses to be able to retrieve or send data. We use this library only for basic web scraping that doesn't involve the need for advanced methods of scraping. You would also **need to know how to work with strings** to use this library as your preferred choice of scraping since Requests fetches the web page's front-end code as a whole string. ( So everything you see on the web page's screen as text ). The string formatting has to be done manually when using Requests. When we reach <b>4. Introduction to Beautiful Soup</b> you'll see how we as programmers work around this tedious problem.

### Example of Requests

We can start of by creating a new python folder called "Python" and then create a file inside of it and then open it in Vscode and call it something similar to <b>main.py</b> or <b>test.py</b>. 

![image](https://user-images.githubusercontent.com/57006688/206842513-27afffc6-5ef5-4bc9-9a02-ab255a2d4e8d.png)

![test py - Python - Visual Studio Code 12_10_2022 11_08_15 AM](https://user-images.githubusercontent.com/57006688/206842598-d726bb0d-2c91-4ee8-bf37-a4bf206f5b1a.png)

After opening the folder in VsCode we can create a file using the create file button ( image below ):

![image](https://user-images.githubusercontent.com/57006688/206842604-ee109fed-cc06-4baf-8612-05bbe102a19d.png)

We will be naming the file `test.py` as below:

![image](https://user-images.githubusercontent.com/57006688/206842611-4794a625-d821-4513-90b1-76f85af50ca6.png)

Now let's open the file and firstly import the modules/libraries we need for web scraping in this case we are using Requests. The first line of code should look like this:

```python
import requests

results = request.get('https://books.toscrape.com')
```

To run this python file click the **triangle play** icon 

![image](https://github.com/TheOfficialPeter/ADiveIntoWebScraping/assets/57006688/38c23c22-1f6b-45cc-afbc-87a27159236f)

In the above image we are making a `HTTP GET` request using the `requests.get(url)` function to fetch the web page data of the url which we are storing in a variable called `results`. If we were to print the html source code of the web page we would do so as follows:

```python
print(results.text)
```

This will print out all the source code of the web page.

Alright let's think about this. Web scraping **requires you to know** what you want to achieve. This is my thought process when it comes to scraping.
- I look through the website and all it has to offer.
- I start to look for **unique, important** as well as **repeating values**. Both can be used in different use cases.

Below is my analysis of the website we are currently testing.

![image](https://user-images.githubusercontent.com/57006688/206375541-986bbc31-7338-4b6a-8e25-cd391ac35219.png)

I outline possible features we might want a bot to fetch without needing any input from us.

The items circled in `red` are repeating values. The items circled in `blue` are important values. In this scenario we can use the important values to monitor the results of the books and use the repeating values to store the information about it. To be honest this scenario doesn't really have a great "important value", but we will use it anyways. You will be seeing better ones as we progress to different websites to scrape.

For this example we will only be scraping the `import value` since scraping all of the `repeating values` is a super tedious process which you **should not** be using. Further in this blog I will talk about using other libraries to make this process easier.

First we start by opening up the browsers `inspect-element` tool usually you can do this by right-clicking on the web page and selectring `inspect-element`. A sidebar will open up show the html source code of the currently opened web page.

![image](https://user-images.githubusercontent.com/57006688/206644544-876f25ed-85f0-47e1-8ee1-5b770722aaa8.png)

You can look in the inspect element tool and you will find that the `important value` is actually a `<strong>1000</strong>`. This is the html source code for the component. 

We will fetch this using the python program as follows:

```python
begin = results.text.find('<strong>', 0)
end = results.text.find('</strong>', begin)
```

Let me explain what's happening here. We are using the source code text for the web page and searching for string of text inside of the huge block of text. We want to "cut" out only the part that we need which in this case is the `important value`. We will do so by grabbing the positions of the `important value` text inside of the big text ( code example above ) and then "cutting" it out ( code example below ).

```python
important_value = results.text[begin+len("<strong>"):end]
print(important_value)
```

The reason for using `begin+len('<strong>')` is to ensure we only capture the **1000** value and not the **strong** as well. Now run the program and you should see this:

```txt
1000
```

This means the program has worked 🎉. Well done. You are learning the basics of Web Scraping.

## Beautiful Soup

What is Beautiful Soup? Its a 3rd party python library ( someone else's code ) that we can use to extract information from web page source code ( html ) quicker and with ease.

### Example of Beautiful Soup

To start using Beautiful Soup we first have to install it on our device. We can do so by opening up comamnd prompt and installing the library using `pip` as follows:

```bash
pip install beautifulsoup4
```

Wait for it to finish install then go back to your python file. Now we will continue in the same file as before. Let's add Beautiful Soup to our current python file by putting in this line at the top of the file:

```python
from bs4 import BeautifulSoup as bs
```

We are using the `as` keyword to tell python we want to use a shorter version of BeautifulSoup. So we can reference BeautifulSoup as `bs`. Now let's add more code to extract `repeating values` from the web page.

This is what you should have in your python file right now:

```python
from bs4 import BeautifulSoup as bs
import requests

results = requests.get('https://books.toscrape.com')
```

Now we first have Beautiful Soup parse ( make it readable for itself ) the html source code for the web page by using this line:

```python
soup = bs(results.text, 'html.parse')
```

Now we can use the `soup` variable to do all kinds of operation on the source code. We will use the `find_all` function to get all website components with a certain characteristic ( something that makes them the same ). After that we loop through all of the found components and print their text values.

```python
for bookName in soup.find_all('h3'):
    print(bookName.text)
```

We are using the `h3` tag on `find_all` since all of the `repeating values` are h3 tags when you look in the `inspect-element` tool. Notice how we are using `bookName.text` since using `bookName` will print the element with its tag and everything as you would see it in `inspect-element` where we actually only want and need the value of the component.

The result of the code should look similar to this:

```txt
A Light in the ...
Tipping the Velvet
Soumission
Sharp Objects
Sapiens: A Brief History ...
The Requiem Red
The Dirty Little Secrets ...
The Coming Woman: A ...
The Boys in the ...
The Black Maria
Starving Hearts (Triangular Trade ...
Shakespeare's Sonnets
Set Me Free
Scott Pilgrim's Precious Little ...
Rip it Up and ...
Our Band Could Be ...
Olio
Mesaerion: The Best Science ...
Libertarianism for Beginners
It's Only the Himalayas
```

Great job 👍 You are doing really well if you have come so far.

> Next up: Avanced Section

## What is Lazy Loading?

Lazy Loading occurs when you encounter a website that doesn't have all components loaded in yet. **Youtube** is a greate example. Videos on youtube load in as you are scrolling through them. If they wanted to load in all vidoes your device would break, becuase there are so many thus they only load in the ones needed for your view.

This means that the web page's source code isn't the same. It changes when new components gets loaded in. So if we wanted to get a video's information like its title or author we won't be able to use the methods we have learned about so far.

This is where tools like Selenium come in.

**Let's keep the flow flowin'🌊**

## Selenium

Selenium is a webdriver tool used to scrape information from sites by automating a browser instance. Explained simply Selenium will act like a human using a browser and that gives it the ability to wait for components to load in ( overcome lazy loading ) and do a lot of other automation.

### Example of Selenium

#### Requirements
First we have to install the required tools for Selenium to work. For this we will need to install its library for python using `pip`. Open up the terminal and execute this `pip` command:

```bash
pip install selenium
```

Wait for installation to complete. Then create a new python file called someting like: `selenium_test.py`.

Selenium pushed a new update since my previous blog post which automatically installed the webdriver for you. A webdriver is needed to open up a browser instance and start interacting with the browser programmatically. We will be using the **Chrome WebDriver** for this example. Feel free to use any other option.

Let's quickly write some code to automically download the latest Chrome WebDriver version and use it in our code:

```bash
pip install webdriver_manager
```

After installing these tools we will now open up the file  `selenium_test.py` and import the selenium library like this:

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
```

Now we have all the libraries we need imported. Now we want to define some options before starting the chrome webriver and selenium. For this example we won't change the options, but usually after finishing a project it might be preferable to use the `headless` option for selenium which doesn't open up the browser when it visits and fetches information from web pages.

Let's define the default option for the Web Driver

```python
options = webdriver.ChromeOptions()
```

Now we will initialize selenium and put the main object in a variable called `driver`

```python
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
```

Now we can use the `driver` object to do all kinds of website related actions. For this example I am going to use **Youtube** as an example of a site using Lazy Loading.

First we have to open up the chrome browser and redirect it to **Youtube**s mainpage.

```python
driver.get("https://www.youtube.com")
```

Now the browser will navigate to **Youtube**s main page.

Before continuing let's break down what a URL is and what it is made of.

A URL (Uniform Resource Locator) is a string of text that specifies the location of a resource on the internet. It is like an address that specifies where something is located. URLs are used to access web pages, but they can also be used to access other types of resources, such as images and videos.

There are several parts that make up a URL:

**Protocol**: This specifies the type of resource that the URL is pointing to. The most common protocol is http, which stands for HyperText Transfer Protocol. Other protocols include https, ftp, file, and mailto.

**Domain**: This is the main part of the URL and specifies the name of the website that the resource is located on. For example, the domain for Google is google.com.

**Path**: This specifies the location of the resource within the website. It is like a file path on a computer, and it can include subdirectories and individual files.

**Query String**: This is a set of key-value pairs that are appended to the end of the URL and are used to pass additional information to the server. They are usually separated from the rest of the URL by a ? character, and each key-value pair is separated by a & character.

**Fragment**: This is an optional part of the URL that specifies a specific location within a resource. It is separated from the rest of the URL by a # character.

Here is an example of a complete URL:

`https://www.example.com/path/to/resource?key1=value1&key2=value2#fragment`

**In this example**:

The protocol is `https`
The domain is `www.example.com`
The path is `/path/to/resource`
The query string is `key1=value1&key2=value2`
The fragment is `fragment`

We can use this information to construct a URL to make the selenium ( aks browser ) search for Youtube videos. This is the final URL we will be using to search for the Youtube term **"tiny train models"**. So change the previous code snippet to the one below:

```python
driver.get("https://www.youtube.com/results?search_query=tiny+train+models")
```

> "+" symbols represent spaces in a URL

After reaching the web page with the results loading in we can either wait for all of the results to load in. To make Selenium wait for results you can set the following options:

```python
options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
```

Overwrite the code snippet you have for initializing the browser object with the one above which will set the page load strategy to `normal`. This means it will wait for all page content to load before doing anything.

Now we can use our own browser to look on the Youtube page with the given URL from earlier: https://www.youtube.com/results?search_query=tiny+train+models

Once the page finished loading open up `inspect-element` tool again and look for the component in the source code for the **video titles**.

Once the page finished loading, open up `inspect-element` tool again and look for the components in the source code for the **video titles**.https://www.youtube.com/results?search_query=tiny+train+models

This is what I found 

![image](https://github.com/TheOfficialPeter/ADiveIntoWebScraping/assets/57006688/4d4bde31-a6f1-4773-82bd-fab57e1b7d59)

First we will add another class to the python file called **By**. We will use this to define what attribute we want to look for. Import this class as follows by inserting this snippet at the beginning of the file.

```python
from selenium.webdriver.common.by import By
```

Now as you can see we have a repeating component attribute in the source code for the components. We will be fetching all the website components that have this repeating attribute.

```python
results = driver.find_elements(By.ID, 'video-title')
```

Let's break down the code in the snippet above. This will search through the currently loaded web page for the attribute video-title on all the components/elements to find the ones we want.

Let's loop through all the results from the fetching to see what it has found.

```python
for videoTitle in results:
    print(videoTitle.text)
```

We use the `.text` otherwise it will return all the components with their attributes, but we only want the text from those components ( video title text ). 

We should end up with a result like this:

```txt
Miniatur Wunderland: Largest Model Train Set - Guinness World Records
WHY ARE THESE MODEL TRAINS SO TINY?! Fun Toy Trains !
Learn Math While Playing Games with Your Favorite Characters & Monsters
Brio trains: wooden locomotives, steam train, trucks, cars, brio train railway
Simon's Trains visits Peter Spoerer's White Horse Railway - gauge 1 live steam in the garden!
How Can Trains This Small Even Work?
Toy Trains Galore 4!
Building a Realistic Imaginary Mountain Model Railroad
I was Sent the Smallest Model Train - Z Scale Unboxing and More!
London Underground model railway build 14 - building a road and embankments
Trains vs Deep Water – BeamNG.Drive - Railking kereta api - Railfans Live - Drama kereta api
0027 A tiny distraction - T gauge
Plochingen dampfspektakel 2017
NANO TRAINS - World’s Smallest Working Train 1:1000 Scale
SMALLEST WORKING TRAIN-SET IN THE WORLD!!!
THE WORLDS SMALLEST MODEL TRAIN SET.. (AND IT WORKS)
Miniature Steam Train You Can Actually Ride
Building A Realistic Imaginary Desert Railroad
Firing up the Allen Models Fitchburg Northern Live Steam Locomotive
Riding the WORLD'S LONGEST Model Train Track!
Neat Train Layouts In Small Spaces | Fall Model Railroad Show 2022
Awesome Model Trains with Steam Locomotives!
This model train layout may be bigger than your house - KING 5 Evening
The Livi B. Railroad - Tiny backyard railroad around a house!
```

If you see a bunch of **video titles** you have succeeded. Well done!

## Matplotlib

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. Mostly used for visualizing data and it comes handy when scraping websites since you can visually see the data and use it to make predictions on the data forecast.

### Examples of Matplotlib

I've decided to use a different website than Youtube for this example. I want to make it easy to understand why we would want to use **Matplotlib** alongside web scraping and how it could be benificial.

First we install the library and import it into our projects. Run the following line in your terminal:

```bash
pip install matplotlib
```

Wait for it to finish then go to your python file and add the following snippet at the beginning:

```python
import matplotlib.pyplot as plt
```

Now we have a ton of functions for showing us statistical graphs and such, but for these graphs we first need data to show. So let's use a website that will fit out purpose. We will be using **A Spotify charts website** Which shows the daily charts for global songs with their amount of streams. We will plot these songs on a bar chart with their amount of streams.

First let's modify out Selenium driver `get()` to change the web page since we are not using Youtube anymore. Change it to this:

```python
driver.get("https://kworb.net/spotify/country/global_daily.html")
```

Now let's open up the web page ourselves and open up `inspect-element` to look for what the repeating elements have in common inside of the html source code.

We only want the Song titles and the amount of streams. Let's first focus on the song titles. We can see that it used the classname `text mp`

![image](https://github.com/TheOfficialPeter/ADiveIntoWebScraping/assets/57006688/267d6922-eea9-44a4-9def-544da6667a80)

Now let's have Selenium look for all components with that classname. Since we have two classname ( seperated by space ) we have to the the CSS Selector option with the method as follows:

```python
results = driver.find_elements(By.CSS_SELECTOR, ".text.mp")
```

Now let's loop through all the results and save them in an array called `songTitles`.

```python
songTitles = []

for songTitle in results:
    songTitles.append(songTitle.text)
```

Now we have finished part 1 of the process. Now we need the amount of streams for each song. Let's see what the attributes are for these components using `inspect-element`.

![image](https://github.com/TheOfficialPeter/ADiveIntoWebScraping/assets/57006688/986ba707-78f9-41d6-9e45-d517cf901b21)

Notice how there is no attribute that is unique to this component which we can use. So this is where more advanced techniques come into play and where I teach you how to utilize different methods and approaches for getting what you want. **All the tools you need already exists, you just need to know how to use them**. Notice how the component we want is part of a list ( image below )? We can say that the component we want is **7th** in the list.

![image](https://github.com/TheOfficialPeter/ADiveIntoWebScraping/assets/57006688/c52c8dfa-e676-43c7-a3a5-07d3fb43a313)

Go to the second most streamed song in the list and you will notice it's also the **7th** component in its list.

This can also be considered as a unique repeating attribute for all of these total streams components. We just need to know how to extract it. We can do so by using `XPath` ( XPath is a path that you have to go down along the html source code to get to a specific component or multiple components ). The XPath in this case would be `//*[@id="spotifydaily"]/tbody/tr[1]`. How did I get this?

All the components are in a list, right? So just the pick the list they are in and right click -> copy -> copy xpath

![image](https://github.com/TheOfficialPeter/ADiveIntoWebScraping/assets/57006688/1483c663-66ed-4c2b-be40-eb715423fc6f)

Now the XPath will have a `[1]` at the end indicating that its the first one, but we don't want only the first one we want all of these list components. So let's do so by remove the one at the end: 

`//*[@id="spotifydaily"]/tbody/tr`

This is perfect.

Selenium has a method for search using XPath too. So let's use that to get all list components:

```python
results = driver.find_elements(By.XPATH, "//*[@id='spotifydaily']/tbody/tr")
```

We are allowed to overwrite the results variable since we aren't using it anymore. Now let's loop through our results:

```python
for list in results:
    print(list)
```

But now we have a problem. We don't want the list, we want the streams inside of these list components. We can get them by looking for the **7th** component within them. For this we will use `CSS Selectors` again, but use `n-th child` selector to get the **7th** component within each list.

```python
for list in results:
    print(list.find_element(By.CSS_SELECTOR, ":nth-child(7)").text)
```

Now we have all the stream values, let's save them in an array. Add this snippet before the loop:

```python
songStreams = []
```

And then change the loop we have as follows:

```python
for list in results:
    songStreams.append(list.find_element(By.CSS_SELECTOR, ":nth-child(7)").text)
```

Now we have the song titls and the song streams. Now we will plot our results on a Bar chart. Song Titles being the X variable and Stream being the Y.

```python
plt.bar(songTitles, songStreams)
plt.xlabel('Song Titles')
plt.ylabel('Total Streams')

plt.show()
```

If you see a bar chart that means it worked. If you get an error saying `Mismatch is between arg 0 with shape (201,) and arg 1 with shape (200,).` or something similar then it means there were more song titles and streams or more stream than song titles so the program couldn't match the two together. If this is so you can use just put a limit on how many rows you want to fetch by modifying the two loops:

Song title loop modified:

```python
for i in range(20):
    songTitles.append(results[i].text)
```

Song Streams loop modified:

```python
for i in range(20):
    songStreams.append(results[i].find_element(By.CSS_SELECTOR, ":nth-child(7)").text)
```

Now we only fetch the top 20 rows. Now your bar chart should show up when running the program otherwise open up a github issue. You might not be able to read the song titles since they are all overlapping, but hovering your mouse over a certain bar on the chart will display the song title on bottom right side of screen.

## NodeJS

### What is NodeJS?

NodeJS is a javascript runtime used for creating web server. Thanks to a huge community of developer supporting the framework it has grown exponentially over the years with tons of integrations and libraries to make it super extensible in usage.

### Why use NodeJS?

I've been using NodeJS since I started making web server a few years ago, but it can be used in a similar fashion for a huge variety of different web related tasks and web scraping is no exception.

### NodeJS Installation

NodeJS has an installation process similar to that of Python. When visiting the web site ( https://nodejs.org ) you will be greeted with two big green buttons. **LTS** and **Current**. If you broken experimental features like me use the **LTS** version.

Download and run the installer that does all the installation work for you. After you are done using the installer you can check if you installed it corectly by opening command prompt and running the following command:

```bash
node -v
```

If its working you would see the version isntalled. Next check if you have `npm` installed by running this in command prompt:

```bash
npm -v
```

It should also output the version if it worked otherwise you can check installtion instructions [here](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).

### Installing NodeJS Modules

NodeJS modules similar to Python libraries add extensibility to your application and allows more functionality while providing a smoother coding experience.

We will be using `npm` to install nodejs moduels/packages. Installation a module is also done in the terminal / command prompt with the following format:

```bash
npm install MODULENAME
```

## Puppeteer

You could easily think of puppeteer being a nodejs alternative for selenium. I would consider it to be personal preference since they are almost the same. It's good to have a module like Puppeteer which was specifically made for using in NodeJS, if you are working in NodeJS.

#### Installation

You can install puppeteer using `npm`

```bash
npm i puppeteer
```

This will install Puppeteer in your current project directory for usage. It also automatically install the Chrome Driver so you can start using the module right away.

### Example of Puppeteer

For this example we will be using a more realistic example like an online shop when you might want to grab all the deals. We'll be using **Amazon** and their "Today's deals" page and scrape all the products and their prices.

First we start off by create a new file named: `scrape.js` and open it. Now we will import Puppeteer into the file:

```js
// Import puppeteer
import puppeteer from 'puppeteer';
```

Then we redirect Puppeteer to go to the Amazon Today's deals page

```js
const browser = await puppeteer.launch();
const page = await browser.newPage();
await page.goto('https://www.amazon.com/gp/goldbox');
```

Then we open up `inspect-element` again and look for the attribute of the repearing elements ( the products and their info ). We notice that all of the components we want like the **price** and **item name** is placed in a `a-link-normal _discount-asin-shoveler_style_link__1FS9h` class. So let's fetch all the web components/elements with this class. We also know that the price's class is `_discount-asin-shoveler_style_priceContainer__3lkqa` and the product name's class is `a-color-base _discount-asin-shoveler_style_title__3k8Rn`. This might change and yours might be different since different versions of amazon website.

```js
const deals = await page.evaluate(() => {
    const dealElements = document.querySelectorAll('.a-link-normal _discount-asin-shoveler_style_link__1FS9h');
    let deals = [];

    for (const dealElement of dealElements) {
      const title = dealElement.querySelector('');
      const price = dealElement.querySelector('._discount-asin-shoveler_style_priceContainer__3lkqa');

      deals.push({ title, image, price });
    }

    return deals;
})
```

In the above example we place the whole snippet in a evaluate() which will return a promise that will be resolved when it has finished searching for all the deals. It first look for the product card and then extract info like price and name.