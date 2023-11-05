# A Dive Into Webscraping
###### Author: P e t e r. <br/> Please note: This article assumes that you know the basic python syntax. Also the code is available [here](https://github.com/TheOfficialPeter/webscraping.github.io/).

### Basic

1. Installing Python + libraries.
      1. Installing VsCode and configuring Python
      2. Installing libraries
2. Introduction to Requests.
3. Example of Requests.
4. Introduction to Beautiful Soup.
5. Example of Beautiful Soup.

### Advanced

6. What is lazy-loading and how to overcome it.
7. Introduction to Selenium.
8. Example of Selenium.
9. Displaying information using PyPlot

### Web Scraping with NodeJS

10. Getting started with NodeJS.
      1. What is NodeJS?
      2. Why use NodeJS?
      3. Installing NodeJS.
      4. Installing NodeJS modules
11. Introduction to Puppeteer.
12. Example of Puppeteer.

### Browser Automation

13. What is Browser Automation.
14. Introduction to browser automation with Selenium
15. Example of browser automation with Selenium

## Installing Python + Libraries

Installing python is really simple. Just visit [the official python web page](https://www.python.org/downloads/) and download the latest version and open the installer. During installation please make sure you have checked the box that **adds python to the PATH**. If you don't see the checkbox, add it manually. [Here](https://medium.com/@omoshalewa/why-you-should-add-python-to-path-and-how-58693c17c443) is an example. If this link is broken just google 'How to add python to PATH'.<br/>

### Installing VsCode and configuring Python

The next step for you it to grab your text editor so we can start coding some cool stuff. Personally I prefer using [Vim](https://www.vim.org) or [Vscode](https://code.visualstudio.com). I would recommend you to use VsCode since it is more beginner-friendly. After installing [Vscode](https://code.visualstudio.com) from the website, open it up and you should be greeted with a fancy looking UI. Now we are going to connect Python with Vscode otherwise we our text editor (Vscode) is useless. I will be explaining how to install the extension, but if you find it difficult to follow you can also visit the official tutorial [here](https://code.visualstudio.com/docs/languages/python). Upon being greeted with the main User Interface, navigate to the extensions tab. (Picture below of the extensions tab icon)

![image](https://user-images.githubusercontent.com/57006688/205931750-ab716e71-84f6-41e6-9bcc-a2d2c559923d.png)

Search python in the textbox then install the first one. It might take some time to install.

![image](https://user-images.githubusercontent.com/57006688/205932087-fcbac426-c45c-453e-bcf0-bd330eb8e027.png)

After installed press `ctrl+shift+p` (You can also go the the <b>View</b> tab and select <b>Open command palette</b>). A window from the top should appear, type in `Python: Select Interpreter` and press Enter or Click on that option.

![group js - Chat - Visual Studio Code 12_6_2022 10_36_50 PM](https://user-images.githubusercontent.com/57006688/206017893-3617bf8b-402a-4e85-b831-8f0d47e52d68.png)

Then select the recommended one. Great! Now we have Python installed and connected with Vscode.<br/>
We can now create python files and run them within Vscode.

### Installing libraries

By now you should know what command prompt is. We will be using it to install the required libraries. At the start of each section I will show you how you can install the required libraries. Some might not require installation, but I will state how when it does.

## Introduction to Requests

The Requests library is a pre-installed (sometimes) python library. If you don't have the module installed or just want to make sure do the following:<br/>

1. Open command prompt.
2. Type in `pip install requests`
3. Look at what the output says. It will state whether the requirements are already met (already installed) or not. Either way it should be installed.

Requests is used to make HTTP requests to web pages / ip addresses to be able to retrieve or send data.
We use this library only for basic web scraping that doesn't involve the need for extreme methods of scraping. You would also need to know how to work with strings to use this library as your main method of scraping since Requests grabs the web page's front-end code as a whole string. The string formatting has to be done manually. When we reach <b>4. Introduction to Beautiful Soup</b> you'll see how we work around this tedious problem. 

## Example of Requests

We can start of by creating a new python folder called "Python" and then create a file inside of it and then open it in Vscode and call it something similar to <b>main.py</b> or <b>test.py</b>. 

![image](https://user-images.githubusercontent.com/57006688/206842513-27afffc6-5ef5-4bc9-9a02-ab255a2d4e8d.png)

![test py - Python - Visual Studio Code 12_10_2022 11_08_15 AM](https://user-images.githubusercontent.com/57006688/206842598-d726bb0d-2c91-4ee8-bf37-a4bf206f5b1a.png)

![image](https://user-images.githubusercontent.com/57006688/206842604-ee109fed-cc06-4baf-8612-05bbe102a19d.png)

![image](https://user-images.githubusercontent.com/57006688/206842611-4794a625-d821-4513-90b1-76f85af50ca6.png)

Now let's open the file and firstly import the modules/libraries we need for web scraping in this case we are using Requests. The first line of code should look like this: 

![image](https://user-images.githubusercontent.com/57006688/206243471-9bb0d503-b731-41d1-b696-2f8123cffe0b.png)

We are importing the Requests module (it's basically a python script containing pre-defined functions that you can use almost anywhere).

Now we have a list of functions we can use to do some scraping. We would like to grab a web page's code first so that we can use that information for statistical purposes, marketing research etc.

![image](https://user-images.githubusercontent.com/57006688/206243759-59cfd1cb-7e01-4619-8ec0-f9e241381bdb.png)

In the above image we are using the `HTTP GET` requests using the `requests.get(url)` function to make grab the html source of the url which we are storing in a variable called `r`. If we were to print the variable `r` this is what it will return when we run the file:

![image](https://user-images.githubusercontent.com/57006688/206243942-f54a0b87-2478-4bb0-8678-abb717fea3da.png)

This is the HTML code of the website url we provided to the `GET` request, stored as a string.
Now that we have the data captured from the website we can use it. Also forgot to mention you can run python files by pressing the `run icon` top right.

![image](https://user-images.githubusercontent.com/57006688/206244165-6dd386fc-c046-45f1-a5af-6ed5d7c40e86.png)

Let's go back a few steps. Web scraping requires you to know what you want to achieve. This is my thought process when it comes to scraping.
- I have a deep look into the website and it's mechanics.
- I start to look for <b>unique, important values</b> as well as <b>repeating values</b>. Both can be used in different use cases.
<br/>
Below is my analysis of the website we are currently testing.

![image](https://user-images.githubusercontent.com/57006688/206375541-986bbc31-7338-4b6a-8e25-cd391ac35219.png)

The items circled in `red` are repeating values. The items circled in `blue` are important values. In this scenario we can use the important values to monitor the results of the books and use the repeating values to store the information about it. To be honest this scenario doesn't really have a great "important value", but we will use it anyways. You will be seeing better ones as we progress to different websites to scrape.

Now we will scrape the `important value` instead of the `repeating values` only becuase it's a tedious process to do a lot of complex scraping with manual string methods as I mentioned previously, but I'll do it once.

First start of by grabbing the element's tags beginning index like this:

![image](https://user-images.githubusercontent.com/57006688/206643961-d7dace65-57b6-495c-9255-9a91f7ba2af6.png)

What we do is get the number of the character where the `<strong>` element is first occured, because when you look in your browser's inspector tool (right-click, inspect element)

![image](https://user-images.githubusercontent.com/57006688/206644544-876f25ed-85f0-47e1-8ee1-5b770722aaa8.png)

You'll see that the `important value` has a tag around it called "strong" and you would also notice that it is the first occurance of the tag "strong", but if there were previous occurences of that tag then this wouldn't have worked becuase this code grabs the first occurence. Hopefully I explained it in a way you could understand.

Now we will grab the "strong" closing tag which looks like `</strong>`

![image](https://user-images.githubusercontent.com/57006688/206644713-140e28f1-1285-4b96-bc04-d3b859d16057.png)

Now we have 2 numbers. We know where the element starts and end in the whole string. Now we `cut` the text out like below.

![image](https://user-images.githubusercontent.com/57006688/206644893-db60f43c-7d29-4909-b692-b711c659b5a9.png)

And now if we print the part that we cut out of the main string we get this:

![image](https://user-images.githubusercontent.com/57006688/206644967-8c6586a7-cdee-411c-84c9-950fbf86df1d.png)

The reason I use `+len("<strong>")` is becuase it grabs the number of the starting point of the element's text so when you do it without that part like below:

`stringCut = sourceCode[begin:end]` <br/>
`print(stringCut)`


Then it will output this:

`<strong>1000`

But when you add the length of the word `<strong>` you get:

`1000`

And that's it. This is webscraping in a nutshell. 

## Introduction to Beautiful Soup

"Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work."

To install this library you'll have to open command prompt and type in the following `pip install beautifulsoup4` and then press `Enter`. 

## Example of Beautiful Soup

Now we will add the library to our Python script.

![image](https://user-images.githubusercontent.com/57006688/206842016-22120611-a9e3-41d2-8686-37c06c8de6f9.png)

We say `as bs` just to add our own abbreviation to the class `BeautifulSoup` so now we can just use `bs` everywhere.

Let's continue where we last left off. Since beatiful soup is used to dissasemble a website's source code, it doesn't grab the source code this means that we will still be using the requests library to grab the source code and feed it to beautiful soup. So you should have this as your code currently:

![image](https://user-images.githubusercontent.com/57006688/206841902-34204c0c-0306-458c-a618-61c3bbcf3749.png)

And now we have the variable `soureCode` which stores the code and we will read it in beautiful soup like this:

![image](https://user-images.githubusercontent.com/57006688/206842137-a705c1b0-0835-4666-b933-e9b02f6ad166.png)

Alright. Now let's grab the "repeating values" which are the book names. We will do this by using Beautiful Soup's `find_all()` function which can fetch any tag names etc. Since each name elements has a tag `h3` it will be really easy grabbing them all.

![image](https://user-images.githubusercontent.com/57006688/206853776-0293bc5d-1747-44c6-a2e6-f4136c8c77be.png)

In the image above we use the `bs.find_all()` function with the parameter set as `h3` to find all the h3 tagged elements on the web page. If you don't know how I got `h3` right-click on webpage and open the developer tools (right-click -> Inspect element) and then you will see that the name has an h3 tag. Now we have a loop that will go through all the `elements` that we found. Now we just want the text of those elements, not the element itself. so if we want to print the name of each book we will do this

![image](https://user-images.githubusercontent.com/57006688/206853892-b0ae17cf-7de0-41fc-b2ac-08b344be9eb4.png)

you have to put `.text` becuase otherwise it will print the entire element. You can change it and see the difference. And that's the basics of scraping with Beautiful Soup. You can have a look at `9. Displaying information using PyPlot` if you want to see how we place the fetched information into visual representations and graphs. Again I want to remind you that all the files and code is uploaded to this github repo which you can visit [here](https://github.com/TheOfficialPeter/webscraping.github.io/)

## What is lazy-loading and how to overcome it

You have 2 different types of websites. Static web pages and Dynamic web pages. Static web pages loads all the content that you see using html,css etc. This type of content doesn't require any loading in, because it is pre-loaded if that makes sense. Dynamic web pages has content that need to be loaded in and you'll see web pages like these everywhere YouTube is an example of a dynamic web page, because the videos needs to be loaded in, becuase our computers doesn't have the capacity or power to show every video that exists on the YouTube, it would break. That's why YouTube only loads in the videos that need to be loaded in and thus we call it a dynamic web page. These pages require different methods of scraping since the previous 2 libraries we used can only read `pre-loaded code` from a website and since the videos aren't pre-loaded we can't really fetch their information. The workaroud for this is to either use browser extensions and plugins which can read the content after it is loaded in or by using a browser automating tool such as selenium or puppetteer which are the two ones we'll be using.

## Introduction to Selenium

Selenium is an open source umbrella project for a range of tools and libraries aimed at supporting browser automation. It provides a playback tool for authoring functional tests across most modern web browsers, without the need to learn a test scripting language. We can use this tool to overcome lazy-loading.

## Example of Selenium

Let's start building our first selenium scraper. We can create a new python script for this application called `seleniumScrape.py` or someting similar. Now let's open the file in VsCode. Now as usual let's start importing all the required modules/libraries. Open up your command prompt or terminal or whatever console you use and type in `pip install selenium` and press Enter. Great now we can start building out first advanced scraper!

For this module we will need a webdriver. There's a few you can choose from:
- Chrome
- Edge
- Firefox
- Safari

For this article we will be using the Chrome web driver. You can download and install it [here](https://chromedriver.storage.googleapis.com/index.html?path=108.0.5359.71/)

If you don't know how to install or where to put the .exe file. Go to your boot drive folder (normall called `C:/`) and place the `chromedriver.exe` inside there. Now we can import the modules in the new script we created

![image](https://user-images.githubusercontent.com/57006688/208761770-6173e303-4062-454e-829c-1b0f3756c707.png)

Now we can create a variable called driver which will fetch the installed driver. `Please note that this method of grabbing the webdriver is deprecated. I will update this article when it stops working.`

![image](https://user-images.githubusercontent.com/57006688/210176704-440b15e3-18fd-4b4e-b63b-64d39e4ceb15.png)

Now we can ask selenium to use the webdriver and to open a website and store the result of the website in a variable. For this example we open the web version of youtube as our scraping website. Please note that this is for educational purposes only.

![image](https://user-images.githubusercontent.com/57006688/210176723-a29d7483-1962-484d-ba6a-916d63ef76a0.png)

We have a problem. Since this is the base url and will only give us recommended video results and we want searched results we will have to change the url, but first let's go over what a url is and how it works. This answer was given by ChatGPT btw. I do not have a deep enough understanding to give a simple answer.

### Let's first understand how a URL works and how we can modify a url to give different outputs to our browser window.

A URL (Uniform Resource Locator) is a string of text that specifies the location of a resource on the internet. It is like an address that specifies where something is located. URLs are used to access web pages, but they can also be used to access other types of resources, such as images and videos.

There are several parts that make up a URL:

Protocol: This specifies the type of resource that the URL is pointing to. The most common protocol is http, which stands for HyperText Transfer Protocol. Other protocols include https, ftp, file, and mailto.

Domain: This is the main part of the URL and specifies the name of the website that the resource is located on. For example, the domain for Google is google.com.

Path: This specifies the location of the resource within the website. It is like a file path on a computer, and it can include subdirectories and individual files.

Query string: This is a set of key-value pairs that are appended to the end of the URL and are used to pass additional information to the server. They are usually separated from the rest of the URL by a ? character, and each key-value pair is separated by a & character.

Fragment: This is an optional part of the URL that specifies a specific location within a resource. It is separated from the rest of the URL by a # character.

Here is an example of a complete URL:

```https://www.example.com/path/to/resource?key1=value1&key2=value2#fragment```

In this example:

The protocol is `https`.<br/>
The domain is `www.example.com`.<br/>
The path is `/path/to/resource`.<br/>
The query string is `key1=value1&key2=value2`.<br/>
The fragment is `fragment`.<br/>

Using the information above we will modify the url in our code to search for a specific word or sentence, in this case `cats`. Here's the fixed line of code:

![image](https://user-images.githubusercontent.com/57006688/210654689-5edeefc7-1b2d-41ac-bf71-7a33e3200a01.png)

Now it will grab the source code of the website which contains the video resutls for the term "cats".
Now that selenium has read the site it can find elements that take time to load in (lazy-loaded elements). When looking at youtube we know that videos are one of the main elements that takes time to load in. This included the title of the video, the thumbnail, the video uploader etc. Now we are going to scrape video titles and save them in a .txt file which we can open anytime to look into. Let's start by using our web browsers `inspect element` tool (right-click then choose the inspect element option) and then look for what the element for the video titles look like. 

![image](https://user-images.githubusercontent.com/57006688/210404778-414ac4fd-d8fe-4bbc-8e85-669630beb47c.png)

Looking at the image above if we use the `inspect element` tool on the video title we can see the element has a unique id (so far we think it is unique). So let's scrape all the elements that have the same ID as this one, because then we will be able to scrape all of those video titles from our search.

Now we will ask Selenium to read all the video titles from the web page by doing the following.

First we use the find_elements method from the driver and here we can specify what we want to search for specifically. Don't forget to add the `By` class into the code as well since we will be using it.

![image](https://user-images.githubusercontent.com/57006688/210656276-4db71045-afb7-42fc-bec7-5c88167047a1.png)

Then use the find_elements method.

![image](https://user-images.githubusercontent.com/57006688/210656512-035aba3b-5dd5-4b25-9942-ae98c501237d.png)

This will return a Python list containing all the elements it found. Let's iterate through the list and save all the items in a .txt file for future usage.

![image](https://user-images.githubusercontent.com/57006688/210760793-82d613c7-3a57-4458-b83f-fb50e6b25542.png)

Now if we run this it will give us something similar to this:

![image](https://user-images.githubusercontent.com/57006688/210760868-92964829-f4b3-4e4a-b018-6a307f9f86e6.png)

This is the list of all video titles on that page. Now we will place this into a .txt file. Create a file named `youtubeResults.txt` then go back to your code and change the following. This is what we had. 

![image](https://user-images.githubusercontent.com/57006688/213861443-fcfbae1f-c6d7-456a-a958-badc3c5e4ea8.png)

It printed the results now we change it so that the results are saved.

![image](https://user-images.githubusercontent.com/57006688/213861679-ed160f4e-ee3a-4b7b-8c02-86c5bc7fffd8.png)

If we break this down into multiple steps you would have the first line where you open the file and you would notice the second parameter to the open() function which is `w`. This indicates that we wish to write to the file and add text to it. The next step is where we replace the print function with the `file.write()` function which will place the video titles in the file and then add a `/n` after it. This means that we want the video titles to be place below one another in the text file and not all in one line. Lastly we use the `file.close()` to close the file when we are done using it. Learning this is useful for when clients want a list generated from scraped data so that it can be represented in multiple ways. Also if you got errors in your output it may be because some video title character wasn't able to be written to the file. I'll leave that part for you to figure out.

## Displaying information using PyPlot

The pyplot module is a part of the matplotlib library in Python, which is a popular data visualization library used for creating various types of charts and plots. We use this to represent our scraped data visually. For this example we will be using PyPlot to show the most played game currently out of a few listed ones. We will be scraping information from the website: https://steamdb.info . We will start as follows:

Make sure the matplotlib module is installed by using pip:

![image](https://user-images.githubusercontent.com/57006688/225046481-ce0423ae-7491-4bfd-80f1-3f6edf5d9f6e.png)

Now that we have matplotlib let's import the pyplot library from it

![image](https://user-images.githubusercontent.com/57006688/225046989-e2cc0d50-f928-426b-92c3-459c2f2586dc.png)

We will be using Selenium once again for scraping the information, because as mentioned in the previous section we use this library to scrape `Dynamic web pages`. This website ( https://steamdb.info ) is dynamic because it loads the numbers in automatically. Lets import Selenium and get it running.

![image](https://user-images.githubusercontent.com/57006688/225048322-61267535-0f8d-40a6-829a-1da651b19f5d.png)

We now visit the website ourselfs to use `inspect element` on it. We would like to know what type of element these numbers are:

![image](https://user-images.githubusercontent.com/57006688/225048874-ffee6bf7-43eb-49ec-bd78-a08a504b22c6.png)

Open up `inspect element` ( by right-clicking on the numbers and choosing inspect element ). Now we have a look the the number's code

![image](https://user-images.githubusercontent.com/57006688/225049228-82b28d49-40a2-416e-8c44-0e71b3b35311.png)

We can see that the element has a class attribute which give it a grouping identity. Let's see if the other numbers also have that class

![image](https://user-images.githubusercontent.com/57006688/225049649-f0b7620a-4f1d-4b65-b4af-3ca16f0537a9.png)

Great! They do. Now we know that these are repeating values and they have a repeating attribute (class). We will be using the className to grab all the numbers, but first we need the names of these game too otherwise the numbers are pretty much useless. Using the `inspect element` again we can see that the numbers of the game's currently playing and the name of the game is all wrapped in one html element:

![image](https://user-images.githubusercontent.com/57006688/225050613-ff9562a9-fc79-4d87-aa81-bbcf9ad894b5.png)

So if we grab the element which keeps this information we will have the game's name and currently playing. We will now make a loop to grab all the games and their information using the element's class which is `app`.

![image](https://user-images.githubusercontent.com/57006688/225052449-a883d17a-e194-4f7d-a7d6-8c7ca22f4665.png)

This will grab all the elements with the class `app` and store it in a variable. Now we make the loop and print all the games information:

![image](https://user-images.githubusercontent.com/57006688/225052712-1f6c41fc-170e-4a56-b443-838f77dfab79.png)

Ok great we now get information like: game's name, currently playing and peaked playing. We will now sort this information so that we can use it as input for pyplot.

--- More coming soon ---
--- I need to redo the Selenium installation since it changed ---


