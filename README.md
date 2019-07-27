# crypto-R2

This is a crypto bot made entirely with python. Using the `ccxt` library, we were able to create
an automated bot that will buy and sell given specific filters. We make sure before buying, that 
1. The current price is below the weekly average 
2. The buying price is below the initial bought price
3. The slope of the last 6 hours transitions from negative to positive

And before selling:
1. The current price is above the weekly average
2. The selling price is above the initial bought price
3. The slope of the last 6 hours transitions from positive to negative

This will ensure some form of stability in such a volitile exchange system. The goal of this project
was actually to get my friends and I more involved with python projects, (two of which, this was there
first python program ever)! There are many bugs in this program, and we still work on it here and there, 
but we were just having fun and trying something a little out of our comfort zone :) 

## Getting Started

Here are the steps for cloning and running this project. 

### Prerequisites and Installing

To install all dependencies:

```
git clone https://github.com/BrandontMitchell/crypto-b0t.git 
cd crypto
pip install -r requirements.txt
python -m crypto.interface.main
```
## Built With

* [ccxt](https://github.com/ccxt/ccxt) - Crypto api library
* [Matplotlib](https://matplotlib.org/) - Graphing
* [PyQt5](https://pypi.org/project/PyQt5/) - GUI framework

## Authors

* **Brandon Mitchell** - [Github](https://github.com/brandontmitchell)
* **Fadel Shtiui** - [Github](https://github.com/fadelshtiui)
* **Maksim Vengrovski** - [Github](https://github.com/vilnius1998)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
