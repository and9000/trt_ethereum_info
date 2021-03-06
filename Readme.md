<h1 align="center">TheRockTrading.com Ethereum Info</h1>
<h3 align="center">Display Ethereum value from TheRockTrading.com</h3>
<br>

[GNOME Shell extension](https://extensions.gnome.org/) displaying Ethereum to Euro (configurable) cryptocurrency value. It's a simple python script, it works thank to [Argos](https://github.com/p-e-w/argos).  

<p align=center>
    <a href="https://github.com/and9000/trt_ethereum_info">
        <img src="https://user-images.githubusercontent.com/6862031/28545449-4a2a4d7c-70c7-11e7-820a-161e04acb62f.png" />
    </a>
</p>

### What?

I'm growing an interest for [cryptocurrencies](https://en.wikipedia.org/wiki/Cryptocurrency), specially for [Ethereum](https://en.wikipedia.org/wiki/Ethereum).
 
I use linux and GNOME, I've an account on [therocktrading.com](https://www.therocktrading.com/) and I want to keep an eye on Ethereum value.  

### Installation

Install and enable [Argos](https://github.com/p-e-w/argos) then clone the repo, install requirements, copy and make it executable **trt_ethereum_info.py**.

```
git clone https://github.com/and9000/trt_ethereum_info.git
cd trt_ethereum_info
pip install -r requirements.txt
cp trt_ethereum_info.py ~/.config/argos/trt_ethereum_info.r.10s.py
chmod +x ~/.config/argos/trt_ethereum_info.r.10s.py
```
Funny extension means it will dock on the `r`ight side and it will update every `10s`econds.

### Configuration

`trt_ethereum_info` is customizable, you can choose to change:
 * `fundId` to show another exchange
 * `defaultKey` to show another index 
 * `printOrder`to modify the opening tab order
  
### Thanks to

[Argos](https://github.com/p-e-w/argos) project.

### Note

This is not even an alpha release. Well it works for me, maybe I will improve it, please be nice. :)

### License

Copyright &copy; 2017 Andrea Lorenzetti (<andrea@lorenzetti.me>)

Released under the terms of the [GNU General Public License, version 3](https://gnu.org/licenses/gpl.html)

