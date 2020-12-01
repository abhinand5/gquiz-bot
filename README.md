# Google Forms Quiz Bot

Python bot built with selenium to automatically open the browser and auto-fill a Google Quiz form based on a pre-filled/pre-scored Google Quiz form. 

Here is when you can use it, 

- You have to fill a Google quiz form. 

- You already have a friend's scored Google quiz form link. 

- You want to transfer the answers, and auto-correct wrong answers based on the form's expected output (if that is enabled in the form)


> **Leave a star ⭐ if you find it useful.** 

## Quick Demo

![Demo GIF](demo/demo.gif)

## Usage

**If you are using the binaries from the [releases](https://github.com/abhinand5/gquiz-bot/releases) page, you may only need to setup the driver and skip straight to configuring section of this readme file. However if you're using the source code make sure to install the required python packages as explained below.**

#### Prerequisites:

1. Google Chrome Web Driver
2. selenium
3. pyyaml

`Selenium` and `pyyaml` can be easily installed with the requirements.txt file or manually installing them. 

```bash
> pip install -r requirements.txt
```

The google chrome web driver can be obtained from this link - https://chromedriver.chromium.org/downloads. 

**Preferably, put the web driver `chromedriver.exe` in `C:\Program Files (x86)\` folder.**

>  Before you go ahead and install the web driver, make sure to select the correct driver version compatible with you Chrome version from the downloads page. You can check chrome version by pasting this - `chrome://version/` in the top bar. According to your Chrome version download the exact same driver from the above link. 



#### Configuring the bot

This step has to be followed no matter you're using source code or the binaries. The fields in the `yaml` file are pretty straight forward, just as what the comment lines say. 

>  Note: Ignore List can be used to ignore certain questions that need to be filled by the user manually. You should edit the ignore list to rightly ignore these form fields otherwise you may run into an error.

```yml
# "driver_path" -->  Web Browser's driver path  
driver_path: C:\Program Files (x86)\chromedriver.exe

# "user_profile" --> Path to Google Chrome user profile data [chrome://version/]
user_profile: C:\Users\abhin\AppData\Local\Google\Chrome\User Data\Default

# "form_url"    -->  Google form you are interested in filling
form_url: https://forms.gle/LpUr7S5s3tW9F63G6

# "filled_form" -->  Pre-filled google form with answers
filled_form: https://docs.google.com/forms/d/e/1FAIpQLScUsrx-rpXax6Hp_IK1gcIkzg8-6K9zE8ul14x_u22QJXww9A/viewscore?viewscore=AE0zAgBcn5wrIIbk8RmSGjHD3-k0NkScYJfsbA7mPF2V-6xmn91D5FSxwlPtclTdXe5lMHk

# List of questions to be ignored
ignore_list: 
  - "name"
  - "class"
  - "section"
  - "reg no"
  - "reg. no"
  - "roll no"
  - "year"
```



#### Running the bot

It is as simple as, 

```bash
> python main.py
```

But before that you have to configure the `config.yml` file which is pretty straight forward. 

However if you're using the binaries in the releases page, you want to run the `.exe` file like this,

```bash
> ./gquiz-bot.exe
```

Setting up the `config.yml` file is mandatory in any case. 

> Note: While running the bot if the prefilled form score is below 80% the bot will ask if you want it to proceed in the console. Only if you respond `y` it will proceed.



Author - [Abhinand](https://github.com/abhinand5)