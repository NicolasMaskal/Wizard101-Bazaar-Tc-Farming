# Wizard101-Bazaar-Tc-Farming
### Some Background
I was in a desperate need of some rare/uncommon treasure cards so I could maintain my pvp career(lol). So while I was manually clicking refresh and looking for treasure cards I need, it hit me that I could create a bot to do it for me. Eventually, I had more than enough tc's so I decided to look for a way to make a profit out of this. I found a discord server for trading where I "sold" my treasure cards for empower(which were traded for crowns items in the same server). At that time I wasn't even playing the game I was just trading to get more empowers to buy crown items from players(because let's face it, crowns are expensive). I stopped playing the game about 6 months ago because I realized that it was a huge time killer and all I had been doing was trading. Recently. I've decided to start uploading my bots  to see if someone's interested. This is the first bot I've decided to upload and they are many more to come. Feel free to contact me about anything.

## If your monitor isn't 1920x1080 the bot won't work
There are 12 images that are crucial to the bot all of other ones are optional
Crucial ones:
```
house_items = "house_items.png"
next_page = "next_page.png"
buy = "buy.png"
buy_yes = "buy_yes.png"
buy_more = "buy_more.png"
buy_more_arrow = "buy_more_arrow.png"
buy_more_buy = "buy_more_buy.png"
gold_0 = "0_gold.png"
ok = "ok.png"
no = "no.png"
sort_by_amount = "sort_by_amount.png"
pick_colors = "pick_colors.png"
selected_school = "selected_school.png"
```

## Notes
I uploaded 79 treasure cards that are/were valuable to a pvp-er or collecter. I imagine you don't want the bot to buy every tc I uploaded, to fix this just delete the ones you don't want.

#### Example:
```
fire_tcs = [tc_fiery_giant, tc_firezilla, tc_fire_beetle, tc_fire_wall,tc_hephaestus, tc_raging_kraken]
```
I don't want the bot to buy fiery giants so I just delete it. I don't delete the file(because I may want it at some point) I just remove it from this list
```
fire_tcs = [tc_firezilla, tc_fire_beetle, tc_fire_wall,tc_hephaestus, tc_raging_kraken]
```

I couldn't get OCR to work correctly so I had to **manually** crop evey single image you see here. This bot 

# Steps to get the bot running if your monitor is 1920x1080

1. pip3 install -r requirements.txt

2. Open wizard101 and go vist our friend Elrik(Bazaar).

3. Start "Farming_Bazaar.py"

4. Profit!

Imagesearch.py is my modified version of https://github.com/drov0/python-imagesearch.
