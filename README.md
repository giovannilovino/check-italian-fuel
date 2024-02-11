# Check FUEL: Monitoring Fuel Prices in Italy

This Python script utilizes the *BeautifulSoup (bs4)* and *Requests* libraries to **scrape average monthly and weekly fuel and energy prices in Italy** from the Ministry of Environment and Energy Security.

[![](https://dgsaie.mise.gov.it/images/stella.png?wmfmt=1669622364)](https://dgsaie.mise.gov.it/)

We hope that Check FUEL proves to be a useful tool for monitoring fuel prices in Italy. Please refer to the **README.md** file for further instructions on script installation and usage.


## Getting Started

To get started with the code on this repo, you need to either *clone* or *download* this repo into your machine as shown below;

```bash
git clone https://github.com/giovannilovino/check-italian-fuel
```

## Dependencies

Before you begin playing with the source code, you might need to install dependencies just as shown below;

```bash
pip3 install -r requirements.txt
```

## Running the App

To execute the script, no special requirements are needed. After installing the necessary libraries from **requirements.txt**, you just need to run one of the two scripts, **Check_Monthly_FUEL.py** or **Check_Weekly_FUEL.py**. The script will automatically perform web scraping.

## Explore it 

Explore it and twist it to your own use case.

## Main Usage
The primary goal of Check FUEL is to provide a simple and reliable way to track fuel prices, using both monthly and weekly data directly from the Italian government's website. This can be particularly useful for businesses managing logistics and transportation, enabling them to monitor costs and invoices on a monthly and weekly basis.

## Resilient to Site Changes
The scraping approach adopted is designed to be robust to small layout changes on the site. However, if the site undergoes significant modifications, the script should be adapted accordingly.

## Possible Future Implementations (Not Included by Default)
Automated Emails: An automated email service can be implemented to send results regularly, enabling more proactive monitoring.

Difference Comparison: Please note that only **Check_Weekly_FUEL.py** will generate a *.txt* file with the output. Libraries like **difflib** can be implemented to compare weekly .txt files and identify significant price variations.

## Issues
In the last two years, the Ministry of Environment and Energy Security website has remained largely unchanged, but it is advisable to check for any alterations and adjust the scripts accordingly.
If the site undergoes significant changes, the scripts may require adaptation to maintain their efficiency.

In case you have any difficulties or issues while trying to run the script
you can raise an issue. 

## Pull Requests

If you have something to add, I welcome pull requests on improvement; your helpful contribution will be merged as soon as possible.

## Give it a Star

If you find this repo useful, give it a star so that many people can get to know it.

## Credits

All the credit goes to [Giovanni Lovino](https://github.com/giovannilovino).

