# Google Forms Quiz Bot

Python bot built with selenium to automatically open the browser and auto-fill a Google Quiz form based on a pre-filled/pre-scored Google Quiz form. 

Here is when you can use it, 

- You have to fill a Google quiz form. 

- You already have a friend's scored Google quiz form link. 

- You want to transfer the answers, and auto-correct wrong answers based on the form's expected output (if that is enabled in the form)

  

## Quick Demo

![Demo GIF](demo/demo.gif)


## Usage

#### Prerequisites: 

1. Google Chrome Web Driver
2. selenium
3. pyyaml

`Selenium` and `pyyaml` can be easily installed with the requirements.txt file or manually installing them. 

```bash
> pip install -r requirements.txt
```

The google chrome web driver can be obtained from this link - https://chromedriver.chromium.org/downloads. 

**Preferably, put the web driver exe in `C:\Program Files (x86)\chromedriver.exe` folder.**

>  Before you go ahead and install the web driver, make sure to select the correct driver version compatible with you Chrome version from the downloads page. You can check chrome version by pasting this - `chrome://version/` in the top bar. According to your Chrome version download the exact same driver from the above link. 

**If you are using the binaries from the releases page, you may only need to setup the driver.** 



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



Author - [Abhinand](https://github.com/abhinand5)