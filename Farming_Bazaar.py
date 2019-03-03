import pyautogui as pya
import imagesearch as imgs
import time as t
import random as r

# Images
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
empower_lowest_price = "empower_lowest_price.png"

    # Treasure cards

        # Fire
tc_fiery_giant = "tc_fiery_giant.png"
tc_firezilla = "tc_firezilla.png"
tc_fire_beetle = "tc_fire_beetle.png"
tc_fire_wall = "tc_fire_wall.png"
tc_hephaestus = "tc_hephaestus.png"
tc_mutate_elf = "tc_mutate_elf.png"
tc_raging_kraken = "tc_raging_kraken.png"

        # Ice
tc_abominable_weaver = "tc_abominable_weaver.png"
tc_angry_snowpig = "tc_angry_snowpig.png"
tc_articzilla = "tc_articzilla.png"
tc_chinook_genie = "tc_chinook_genie.png"
tc_freeze = "tc_freeze.png"
tc_glacial_wall = "tc_glacial_wall.png"
tc_ice_bird = "tc_ice_bird.png"
tc_ice_guardian = "tc_ice_guardian.png"
tc_icezilla = "tc_icezilla.png"
tc_legion_shield = "tc_legion_shield.png"  # Not searched tcs as I am not sure I need as much
tc_reindeer_knight = "tc_reindeer_knight.png"
tc_tundra_lord = "tc_tundra_lord.png"

        # Storm
tc_cloud_wall = "tc_cloud_wall.png"
tc_healing_current = "tc_healing_current.png"
tc_lighting_elf = "tc_lighting_elf.png"
tc_lord_of_the_squall = "tc_lord_of_the_squall.png"
tc_queen_calypso = "tc_queen_calypso.png"
tc_storm_beetle = "tc_storm_beetle.png"

        # Myth
tc_aftershock = "tc_aftershock.png"
tc_athena_battle_sight = "tc_athena_battle_sight.png"
tc_fable_lord = "tc_fable_lord.png"
tc_myth_banshee = "tc_myth_banshee.png"
tc_reflective_wall = "tc_reflective_wall.png"
tc_shift = "tc_shift.png"
tc_stun = "tc_stun.png"

        # Life
tc_brown_spider = "tc_brown_spider.png"
tc_brulee_sucre = "tc_brulee_sucre.png"
tc_energy_wall = "tc_energy_wall.png"
tc_mass_triage = "tc_mass_triage.png"
tc_triage = "tc_triage.png"

        # Death
tc_bonetree_lord = "tc_bonetree_lord.png"
tc_colossafrog = "tc_colossafrog.png"
tc_deadly_minotaur = "tc_deadly_minotaur.png"
tc_death_bat = "tc_death_bat.png"
tc_deer_knight = "tc_deer_knight.png"
tc_empower = "tc_empower.png"
tc_headless_horseman = "tc_headless_horseman.png"  # deprecated
tc_red_ghost = "tc_red_ghost.png"
tc_silencing_wall = "tc_silencing_wall.png"

    # Balance
tc_balanceblade = "tc_balanceblade.png"
tc_dragonblade = "tc_dragonblade.png"
tc_loremaster = "tc_loremaster.png"
tc_ninja_piglets = "tc_ninja_piglets.png"
tc_shield_wall = "tc_shield_wall.png"
tc_sirocco_djinni = "tc_sirocco_djinni.png"
tc_stone_wall = "tc_stone_wall.png"

    # Symbols
fire_symbol = "fire_symbol.png"
fire_symbol_selected = "fire_symbol_selected.png"
ice_symbol = "ice_symbol.png"
storm_symbol = "storm_symbol.png"
myth_symbol = "myth_symbol.png"
life_symbol = "life_symbol.png"
death_symbol = "death_symbol.png"
balance_symbol = "balance_symbol.png"
astral_symbol = "astral_symbol.png"


def click_buy():
    imgs.clicking_image(buy_more)
    t.sleep(1.5)
    screen = pya.screenshot()
    buy_more_arrow_pos0 = imgs.imagesearch(buy_more_arrow, screenshot=screen)
    buy_more_buy_pos = imgs.imagesearch(buy_more_buy, screenshot=screen)

    buy_more_arrow_pos = (buy_more_arrow_pos0[0] - 15, buy_more_arrow_pos0[1])
    if buy_more_arrow_pos[0] != -1:
        imgs.moving_clicking_on_positions_x_y(buy_more_arrow_pos)
        imgs.moving_clicking_on_positions_x_y(buy_more_arrow_pos0)
        imgs.moving_clicking_on_positions_x_y(buy_more_buy_pos)
    t.sleep(1)
    imgs.clicking_image(ok)
    t.sleep(1)


def buying_empower(gold=15000):
    # Searching for empower
    empower_pos = imgs.imagesearch(tc_empower)

    # If card found
    if empower_pos[0] != -1:

        pos = imgs.imagesearcharea(image=empower_lowest_price, x1=empower_pos[0] + 350, y1=empower_pos[1], width=70, height=17, name="Test.png", precision=0.95)

        # If more than 74 empowers then click on empower
        if pos[0] != -1:
            pya.moveTo(empower_pos[0], empower_pos[1], duration=r.uniform(0.45, 0.75))
            t.sleep(r.uniform(0.05, 0.15))
            pya.click(empower_pos[0], empower_pos[1])

        # Buying until 74 empowers are left
        while pos[0] != -1:
            t.sleep(0.5)
            gold -= 3200
            imgs.clicking_image(buy)
            t.sleep(0.5)
            screen = pya.screenshot()
            ok_pos = imgs.imagesearch(ok, screenshot=screen)
            if ok_pos[0] != -1:
                imgs.moving_clicking_on_positions_x_y(ok_pos)
            else:
                imgs.clicking_image(buy_yes, screenshot=screen)
            t.sleep(0.5)
            pos = imgs.imagesearcharea(image=empower_lowest_price, x1=empower_pos[0] + 350, y1=empower_pos[1], width=70, height=17, name="Test.png", precision=0.95)


def searching_for_tcs_in_one_school(tcs, pages=15):
    # First sort by amount, image recognition is not recommended as somehow the balance school has a different #
    t.sleep(0.5)
    imgs.moving_clicking_on_positions_x_y((1126, 390))

    for _ in range(pages):

        screenshot_of_page = pya.screenshot()

        # Search for all the wanted tcs on one page
        for tc in tcs:
            print(tc)
            tc_pos = imgs.imagesearch(tc, precision=0.9, screenshot=screenshot_of_page)

            if tc_pos[0] != -1:

                if tc == tc_empower:

                    buying_empower()

                else:

                    while tc_pos[0] != -1:
                        tc_pos = (tc_pos[0] + r.randint(1, 35), tc_pos[1])
                        imgs.moving_clicking_on_positions_x_y(tc_pos)
                        t.sleep(r.uniform(0.35, 0.6))
                        click_buy()
                        tc_pos = imgs.imagesearch(tc, precision=0.9)

                        # Logic that when 'pick colors' is detected to restart the function

                        pick_colors_pos = imgs.imagesearch(pick_colors)
                        if pick_colors_pos[0] != -1:
                            # Clicking on selected school to restart function
                            selected_school_pos = imgs.imagesearch(selected_school)
                            selected_school_pos = (selected_school_pos[0], selected_school_pos[1] + 40)
                            imgs.moving_clicking_on_positions_x_y(selected_school_pos)
                            t.sleep(1)
                            searching_for_tcs_in_one_school(tcs, pages)
                            return

                    # Retake new screenshot because when the bought tc disappears the order will be different
                    screenshot_of_page = pya.screenshot()
                    imgs.clicking_image(ok, to_print=False, screenshot=screenshot_of_page)
                    t.sleep(1)


# ----------------------------------------------------------------------------------------------

        t.sleep(r.uniform(0.35, 0.6))
        imgs.clicking_image(next_page)
        t.sleep(r.uniform(0.75, 0.95))

    t.sleep(r.uniform(0.35, 0.6))


def going_to_tc_screen():
    fire_pos = imgs.imagesearch(fire_symbol_selected)
    if fire_pos[0] == -1:

        t.sleep(r.uniform(0.35, 0.6))
        imgs.pressing_key("x", amount=r.randint(2, 5))
        t.sleep(5)
        imgs.clicking_image(house_items, amount_of_clicks=2, time_between_clicks=0.5)
        t.sleep(r.uniform(2, 3))

    screenshot_of_page = pya.screenshot()
    fire_pos = imgs.imagesearch(fire_symbol_selected, screenshot=screenshot_of_page)
    ice_pos = imgs.imagesearch(ice_symbol, screenshot=screenshot_of_page)
    storm_pos = imgs.imagesearch(storm_symbol, screenshot=screenshot_of_page)
    myth_pos = imgs.imagesearch(myth_symbol, screenshot=screenshot_of_page)
    life_pos = imgs.imagesearch(life_symbol, screenshot=screenshot_of_page)
    death_pos = imgs.imagesearch(death_symbol, screenshot=screenshot_of_page)
    balance_pos = imgs.imagesearch(balance_symbol, screenshot=screenshot_of_page)
    astral_pos = imgs.imagesearch(astral_symbol, screenshot=screenshot_of_page)

    return fire_pos, ice_pos, storm_pos, myth_pos, life_pos, death_pos, balance_pos, astral_pos


fire_tcs = [tc_fiery_giant, tc_firezilla, tc_fire_beetle, tc_fire_wall,tc_hephaestus, tc_raging_kraken]

ice_tcs = [tc_abominable_weaver, tc_angry_snowpig, tc_articzilla, tc_chinook_genie, tc_freeze, tc_glacial_wall, tc_ice_bird,
           tc_ice_guardian, tc_icezilla, tc_reindeer_knight, tc_tundra_lord]

storm_tcs = [tc_cloud_wall, tc_healing_current, tc_lighting_elf, tc_lord_of_the_squall, tc_queen_calypso, tc_storm_beetle]

myth_tcs = [tc_aftershock, tc_athena_battle_sight, tc_myth_banshee, tc_reflective_wall, tc_shift, tc_stun]

life_tcs = [tc_brown_spider, tc_brulee_sucre, tc_energy_wall, tc_mass_triage, tc_triage]

death_tcs = [tc_bonetree_lord, tc_colossafrog, tc_deadly_minotaur, tc_death_bat, tc_deer_knight, tc_empower, tc_red_ghost, tc_silencing_wall]

balance_tcs = [tc_balanceblade, tc_dragonblade, tc_loremaster, tc_ninja_piglets, tc_shield_wall, tc_sirocco_djinni, tc_stone_wall]

astral_tcs = []

fire_pos, ice_pos, storm_pos, myth_pos, life_pos, death_pos, balance_pos, astral_pos = going_to_tc_screen()
print(balance_pos)
while True:

    # Fire
    imgs.moving_clicking_on_positions_x_y(fire_pos)
    t.sleep(r.uniform(1.25, 1.5))
    searching_for_tcs_in_one_school(fire_tcs, 6)

    # Ice
    imgs.moving_clicking_on_positions_x_y(ice_pos)
    t.sleep(r.uniform(1.25, 1.5))
    searching_for_tcs_in_one_school(ice_tcs, 6)

    # Storm
    imgs.moving_clicking_on_positions_x_y(storm_pos)
    t.sleep(r.uniform(1.25, 1.5))
    searching_for_tcs_in_one_school(storm_tcs, 6)

    # Myth
    imgs.moving_clicking_on_positions_x_y(myth_pos)
    t.sleep(r.uniform(1.25, 1.5))
    searching_for_tcs_in_one_school(myth_tcs, 6)

    # Life
    imgs.moving_clicking_on_positions_x_y(life_pos)
    t.sleep(r.uniform(1.25, 1.5))
    searching_for_tcs_in_one_school(life_tcs, 6)

    # Death
    imgs.moving_clicking_on_positions_x_y(death_pos)
    t.sleep(r.uniform(1.25, 1.5))
    searching_for_tcs_in_one_school(death_tcs, 11)

    # Balance
    imgs.moving_clicking_on_positions_x_y(balance_pos)
    t.sleep(r.uniform(1.25, 1.5))
    searching_for_tcs_in_one_school(balance_tcs, 6)





