# Wizard101-Bazaar-Tc-Farming
### Some Background
I was in a desperate need of some rare/uncommon treasure cards so I could maintain my pvp career(lol). So while I was manually clicking refresh and looking for treasure cards I need, it hit me that I could create a bot to do it for me. Eventually, I had more than enough tc's so I decided to look for a way to make a profit out of this. I found a discord server for trading where I "sold" my treasure cards for empower(which were traded for crowns items in the same server). At that time I wasn't even playing the game I was just trading to get more empowers to buy crown items from players(because let's face it, crowns are expensive). I stopped playing the game about 6 months ago because I realized that it was a huge time killer and all I had been doing was trading. Recently. I've decided to start uploading my bots  to see if someone's interested. This is the first bot I've decided to upload and they are many more to come. Feel free to contact me about anything.

## If your monitor isn't 1920x1080 the bot won't work(skip if you can switch to 1920x1080)
There are 20 images that are crucial to the bot all of other ones are optional(Well you must have atleast one treasure card, otherwise the bot is useless).

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

fire_symbol = "fire_symbol.png"
fire_symbol_selected = "fire_symbol_selected.png"
ice_symbol = "ice_symbol.png"
storm_symbol = "storm_symbol.png"
myth_symbol = "myth_symbol.png"
life_symbol = "life_symbol.png"
death_symbol = "death_symbol.png"
balance_symbol = "balance_symbol.png"
astral_symbol = "astral_symbol.png"
```
So these are the first ones you should retake. Also edit the x,y positions of `imgs.moving_clicking_on_positions_x_y((1126, 390))` where your '#' symbol is in the bazaar.

## Notes
* I uploaded 79 treasure cards that are/were valuable to a pvp-er or collecter. I imagine you don't want the bot to buy every single tc  I uploaded, to fix this just delete the ones you don't want.

#### Example:
```
fire_tcs = [tc_fiery_giant, tc_firezilla, tc_fire_beetle, tc_fire_wall,tc_hephaestus, tc_raging_kraken]
```
I don't want the bot to buy fiery giants so I just delete it. I don't delete the file(because I may want it at some point) I just remove it from this list.
```
fire_tcs = [tc_firezilla, tc_fire_beetle, tc_fire_wall,tc_hephaestus, tc_raging_kraken]
```
* I had an almost infinite amount of gold(due to my halfang bot, which will also be uploaded in the near future) and I decided it was worth it to buy empowers if they are for 3200 gold each. I recommend you starting at near max gold if you want the bot to buy empowers, If you don't then don't forget to remove tc_empower from the list.

* The bot looks at the first 6 pages(death school 11 pages because of the empower logic). If you're not buying empower switch to 6. Change `searching_for_tcs_in_one_school(death_tcs, 11)` to `searching_for_tcs_in_one_school(death_tcs, 6)`

* I couldn't get OCR to work correctly so I had to **manually** crop evey single image you see here. If someone can get OCR to work with this bot, that would be much appreciated.

* This bot isn't very fast, searching for so many images at a time is time consuming. But on the positive side I haven't had any warnings from kingsisle, so the bot is safe to use. **On the off chance you get banned for using my bot, I take no responsibility, it is/was your decision to use my bot**

* English Isn't My First Language, feel free to correct grammar.

* Video of the bot working will be uploaded in the near future

# Steps to get the bot running

1. pip3 install -r requirements.txt

2. Open wizard101 and go vist our friend Elrik(Bazaar).

3. Start "Farming_Bazaar.py"

4. Profit! (Well, kinda)

Imagesearch.py is my modified version of [@drov0's](https://github.com/drov0/python-imagesearch). He has a blog series about botting which I reccommend to [read](https://steemit.com/python/@howo/image-recognition-for-automation-with-python).
