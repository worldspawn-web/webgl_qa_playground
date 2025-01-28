import asyncio
from airtest.core.api import *
import logging
from utils import (
    random_touch,
    multiple_touches,
    close_window,
    assert_and_touch,
    inter_check,
    clear_console
)

auto_setup(__file__)

def tutorials_checker():
    # Conditions Check
    if not exists(Template(r"tpl1737993406297.png", record_pos=(-0.354, 0.163), resolution=(2400, 1080))):
        clear_console()
        logging.warning('Incorrect Test Start! Check starting conditions.')
    
    # Tutorial Assertions
    clear_console()
    logging.info('Starting Tutorial Assertions..')
    ## Step 1
    tutorial_item_1 = Template(r"tpl1737993438369.png", record_pos=(-0.051, -0.029), resolution=(2400, 1080))
    assert_exists(tutorial_item_1, "First Merge Item.")
    assert_exists(Template(r"tpl1737993502355.png", record_pos=(0.281, -0.163), resolution=(2400, 1080)), "Volume Toggler.")
    swipe(tutorial_item_1, (0.541, 0.333))
    
    ## Step 2
    assert_exists(Template(r"tpl1737993671000.png", record_pos=(-0.185, -0.066), resolution=(2400, 1080)), "Locked Location.")
    assert_exists(Template(r"tpl1737993684689.png", record_pos=(-0.352, 0.166), resolution=(2400, 1080)), "Mascot Dialog Avatar.")
    tutorial_mascot_1 = Template(r"tpl1737993710117.png", threshold=0.6, record_pos=(-0.053, -0.028), resolution=(2400, 1080))
    assert_exists(tutorial_mascot_1, "Mascot on Merge Field.")
    touch(tutorial_mascot_1)
    sleep(2.0)
    
    ## Modal Tutorial Window
    mascot_dialog_img = Template(r"tpl1737993833687.png", record_pos=(-0.293, 0.018), resolution=(2400, 1080))
    assert_exists(mascot_dialog_img, "Mascot Image.")
    assert_exists(Template(r"tpl1737993852018.png", record_pos=(0.056, 0.058), resolution=(2400, 1080)), "Tutorial 'HowTo' Scheme.")
    assert_exists(Template(r"tpl1737993859304.png", record_pos=(0.053, -0.07), resolution=(2400, 1080)), "Tutorial Window Text.")
    random_touch()
    
    ## Step 3
    multiple_touches(4)
    
    tutorial_crate = Template(r"tpl1737993953422.png", record_pos=(-0.007, -0.072), resolution=(2400, 1080))
    wait(tutorial_crate)
    touch(tutorial_crate)
    sleep(2.0)
    assert_exists(Template(r"tpl1737994040356.png", record_pos=(-0.04, -0.029), resolution=(2400, 1080)), "A Bunch of Items Appeared.")
    
    multiple_touches(2)
    assert_exists(Template(r"tpl1737994202528.png", record_pos=(-0.065, -0.028), resolution=(2400, 1080)), "New Items Faded.")
    
    ## Step 4
    ## Hardcoded with swipes :(
    swipe((0.541, 0.336), (0.498, 0.289))
    sleep(2.0)
    assert_exists(Template(r"tpl1737994318578.png", record_pos=(-0.006, -0.132), resolution=(2400, 1080)), "New Item Appeared.")
    swipe((0.498, 0.289),(0.406, 0.388))
    sleep(1.0)
    swipe((0.409, 0.488),(0.451, 0.549))
    sleep(1.0)
    swipe((0.451, 0.549),(0.497, 0.59))
    sleep(1.0)
    swipe((0.406, 0.388),(0.545, 0.549))
    sleep(1.0)
    swipe((0.497, 0.59),(0.545, 0.549))
    sleep(1.0)
    
    ## Step 5 - Quest & LevelUp Messages
    assert_exists(Template(r"tpl1737994581262.png", record_pos=(-0.05, -0.028), resolution=(2400, 1080)), "New Quest Message.")
    assert_exists(Template(r"tpl1737994587064.png", record_pos=(-0.357, -0.004), resolution=(2400, 1080)), "New Quest Icon.")
    random_touch()
    assert_exists(Template(r"tpl1737994639565.png", record_pos=(-0.046, -0.025), resolution=(2400, 1080)), "Mission Complete Message.")
    assert_exists(Template(r"tpl1737994645466.png", record_pos=(-0.051, 0.132), resolution=(2400, 1080)), "Mission Rewards Message.")
    random_touch()
    assert_exists(Template(r"tpl1737994701679.png", record_pos=(-0.048, 0.024), resolution=(2400, 1080)), "New Level Rewards.")
    assert_exists(Template(r"tpl1737994708326.png", record_pos=(-0.052, -0.092), resolution=(2400, 1080)), "New Level Icon.")
    touch((0.65, 0.65))
    sleep(3.0)
    assert_exists(Template(r"tpl1737994753154.png", record_pos=(-0.052, -0.026), resolution=(2400, 1080)), "New Quest (no image).")
    random_touch()
    assert_exists(Template(r"tpl1737994786486.png", record_pos=(-0.048, 0.004), resolution=(2400, 1080)), "Receipt - Level #2.")
    close_window()
    
    ## Step 6 - Wheat
    multiple_touches(3)
    tutorial_item_2 = Template(r"tpl1737995104741.png", target_pos=8, record_pos=(-0.05, -0.066), resolution=(2400, 1080))
    wait(tutorial_item_2)
    touch(tutorial_item_2)
    assert_exists(Template(r"tpl1737995211826.png", record_pos=(-0.051, -0.041), resolution=(2400, 1080)), "A lot of Items Appeared.")
    touch(Template(r"tpl1737995241154.png", record_pos=(-0.138, -0.083), resolution=(2400, 1080)))
    
    ## Step 7 - Cooking
    tutorial_mascot_2 = Template(r"tpl1737995271620.png", target_pos=8, record_pos=(-0.057, -0.094), resolution=(2400, 1080))
    assert_exists(tutorial_mascot_2, "New Quest for Mascot.")
    touch(tutorial_mascot_2)
    wait(Template(r"tpl1737995359467.png", record_pos=(-0.047, -0.001), resolution=(2400, 1080)))
    assert_exists(Template(r"tpl1737995380063.png", record_pos=(-0.116, -0.05), resolution=(2400, 1080)), "Ingredients Full.")
    assert_exists(Template(r"tpl1737995399158.png", record_pos=(-0.244, 0.082), resolution=(2400, 1080)), "Cookie Icon.")
    assert_exists(Template(r"tpl1737995410877.png", record_pos=(-0.209, 0.014), resolution=(2400, 1080)), "Rewards.")
    assert_exists(Template(r"tpl1737995424135.png", record_pos=(-0.049, -0.125), resolution=(2400, 1080)), "Different Window Tabs.")
    cook_btn = Template(r"tpl1737995452481.png", rgb=True, record_pos=(0.123, 0.013), resolution=(2400, 1080))
    cooking_btn = Template(r"tpl1737997802366.png", rgb=True, record_pos=(0.123, 0.015), resolution=(2400, 1080))
    collect_btn = Template(r"tpl1737995566113.png", rgb=True, record_pos=(0.122, 0.012), resolution=(2400, 1080))
    assert_exists(cook_btn, "Cook Button.")
    touch(cook_btn)
    assert_exists(cooking_btn, "Cooking...")
    sleep(12.0) # waiting for cookies to get cooked
    assert_exists(collect_btn, "Collect Button.")
    touch(collect_btn)
    assert_exists(Template(r"tpl1737995821724.png", record_pos=(-0.046, -0.026), resolution=(2400, 1080)), "Cooking Quest Completed.")
    assert_exists(Template(r"tpl1737995834581.png", record_pos=(-0.048, 0.13), resolution=(2400, 1080)), "Cooking Quest Rewards.")
    random_touch()
    
    ## Step 8 - Feeding an Owl (and getting a key)
    assert_and_touch(Template(r"tpl1737995880500.png", record_pos=(-0.048, -0.026), resolution=(2400, 1080)), "Faded Cookie.")
    wait(mascot_dialog_img)
    multiple_touches(3)
    assert_and_touch(Template(r"tpl1737996003308.png", record_pos=(-0.05, -0.03), resolution=(2400, 1080)), "Faded Key.")
    sleep(3.0)
    random_touch()
    assert_and_touch(Template(r"tpl1737996261704.png", target_pos=8, record_pos=(-0.05, -0.114), resolution=(2400, 1080)), "Collect 5 Keys Button")
    assert_and_touch(Template(r"tpl1737996425099.png", target_pos=8, record_pos=(-0.047, -0.08), resolution=(2400, 1080)), "Open Location with Keys")
    
    ## Step 9 - Gnomes
    multiple_touches(3)
    sleep(2.0)
    assert_exists(Template(r"tpl1737996488502.png", record_pos=(-0.064, -0.028), resolution=(2400, 1080)), "Faded mushrooms.")
    swipe((0.356, 0.537), (0.403, 0.476))
    sleep(3.0)
    assert_exists(Template(r"tpl1737996576042.png", record_pos=(0.189, -0.023), resolution=(2400, 1080)), "Gnomes Dialog Image.")
    assert_exists(mascot_dialog_img)
    multiple_touches(6)
    random_touch()
    assert_exists(Template(r"tpl1737996638139.png", record_pos=(-0.047, -0.026), resolution=(2400, 1080)), "Gnome Quest Completed.")
    multiple_touches(2)
    inter_check()
        
    ## Step 10 - Generators
    for i in range(2):
        touch((0.537, 0.537))
        assert_and_touch(Template(r"tpl1737997095676.png", target_pos=8, record_pos=(0.041, -0.072), resolution=(2400, 1080)), "Generator Window")
        sleep(3.0)
        touch((0.537, 0.537))
    
    touch((0.544, 0.432))
    assert_and_touch(Template(r"tpl1737997095676.png", target_pos=8, record_pos=(0.041, -0.072), resolution=(2400, 1080)), "Generator Window")
    sleep(3.0)
    touch((0.544, 0.432))
    sleep(2.0)
    assert_exists(Template(r"tpl1737997345748.png", record_pos=(-0.051, -0.025), resolution=(2400, 1080)), "Books Quest Completed.")
    random_touch()
    touch((0.66, 0.66))
    inter_check()
    
    assert_exists(mascot_dialog_img)
    multiple_touches(2)
    
    touch((0.544, 0.432))
    assert_and_touch(Template(r"tpl1737997095676.png", target_pos=8, record_pos=(0.041, -0.072), resolution=(2400, 1080)), "Generator Window")
    
    assert_exists(Template(r"tpl1737997475594.png", record_pos=(-0.049, -0.025), resolution=(2400, 1080)), "Please fill in the test point.")
    random_touch()
    touch((0.544, 0.432))
    
    ## Step 11 - Cooking Again
    touch(tutorial_mascot_2)
    sleep(2.0)
    touch(cook_btn)
    assert_exists(cooking_btn, "Cooking...")
    sleep(10.0)
    touch(collect_btn)
    inter_check()
    touch(Template(r"tpl1737998492570.png", record_pos=(-0.052, -0.027), resolution=(2400, 1080)))
    sleep(2.0)
    touch(Template(r"tpl1737998505034.png", record_pos=(-0.009, -0.007), resolution=(2400, 1080)))
    sleep(2.0)
    touch(Template(r"tpl1737996261704.png", target_pos=8, record_pos=(-0.05, -0.114), resolution=(2400, 1080)))
    sleep(2.0)
    assert_exists(Template(r"tpl1737998555273.png", record_pos=(-0.047, 0.003), resolution=(2400, 1080)), "Location is Ready to be Unlocked.")
    touch(Template(r"tpl1737998599491.png", target_pos=8, record_pos=(-0.051, -0.081), resolution=(2400, 1080)))
    
    # Everyday Rewards Window
    assert_exists(Template(r"tpl1737998701896.png", record_pos=(-0.054, 0.002), resolution=(2400, 1080)), "Everyday Rewards Modal Window.")
    assert_exists(Template(r"tpl1737998712344.png", record_pos=(-0.237, -0.046), resolution=(2400, 1080)), "Reward of the First Day.")
    assert_exists(Template(r"tpl1737998740108.png", record_pos=(-0.115, -0.05), resolution=(2400, 1080)), "Hidden Icon.")
    random_touch()
    
def ui_checker():
    clear_console()
    logging.info('Starting UI Checks...')
    
    inter_check()
    
    # Buttons Definition
    pfp_img = Template(r"tpl1737999306534.png", record_pos=(-0.359, -0.177), resolution=(2400, 1080))
    settings_pfp = Template(r"tpl1737999540207.png", record_pos=(-0.159, -0.07), resolution=(2400, 1080))
    settings_window = Template(r"tpl1737999490394.png", record_pos=(-0.05, -0.013), resolution=(2400, 1080))
    settings_lang = Template(r"tpl1737999606393.png", rgb=True, record_pos=(-0.134, 0.018), resolution=(2400, 1080))
    settings_btn = Template(r"tpl1737999381558.png", record_pos=(0.285, -0.201), resolution=(2400, 1080))
    values_hard = Template(r"tpl1737999359908.png", target_pos=6, record_pos=(0.209, -0.202), scale_step=0.01, resolution=(2400, 1080))
    receipts_btn = Template(r"tpl1737999395816.png", record_pos=(-0.356, 0.177), resolution=(2400, 1080))
    quests_btn = Template(r"tpl1737999419830.png", record_pos=(-0.355, 0.104), resolution=(2400, 1080))
    
    # Assertions
    assert_exists(pfp_img, "Avatar & Progress Bar.")
    assert_exists(Template(r"tpl1737999327073.png", record_pos=(-0.278, -0.189), resolution=(2400, 1080)), "Energy & Gnomes.")
    assert_exists(Template(r"tpl1737999340362.png", record_pos=(-0.006, -0.203), resolution=(2400, 1080)), "Keys Value.")
    assert_exists(Template(r"tpl1737999350365.png", record_pos=(0.099, -0.202), resolution=(2400, 1080)), "Gold Value.")
    assert_exists(values_hard, "Hard Value.")
    assert_exists(settings_btn, "Settings Button.")
    assert_exists(receipts_btn, "Receipts Button.")
    assert_exists(quests_btn, "Quests Button.")
    assert_exists(Template(r"tpl1737999431843.png", record_pos=(0.217, 0.043), resolution=(2400, 1080)), "Location No.4 is Locked.")
    
    touch(pfp_img)
    assert_exists(settings_window, "Settings Window.")
    assert_exists(settings_pfp, "Settings Avatar.")
    assert_exists(Template(r"tpl1737999590012.png", record_pos=(-0.048, 0.106), resolution=(2400, 1080)), "Settings Togglers.")
    assert_exists(settings_lang, "Language Button.")
    assert_exists(Template(r"tpl1737999644348.png", record_pos=(-0.012, -0.069), resolution=(2400, 1080)), "Current Nickname & ID is empty.")
    
    touch(settings_pfp)
    sleep(2.0)
    assert_exists(Template(r"tpl1737999679194.png", record_pos=(-0.052, 0.024), resolution=(2400, 1080)), "Locked Avatars.")
    assert_and_touch(Template(r"tpl1737999700777.png", target_pos=6, record_pos=(-0.056, -0.065), resolution=(2400, 1080)), "Decorations Tab")
    assert_exists(Template(r"tpl1737999744382.png", record_pos=(-0.167, -0.003), resolution=(2400, 1080)), "No Decoratons Available.")
    assert_and_touch(Template(r"tpl1737999789033.png", target_pos=4, record_pos=(-0.048, -0.065), resolution=(2400, 1080)), "Decorations Tab #2")
    
    for i in range(2):
        close_window()

async def check_for_yagames():
    cross = Template(r"tpl1738059416652.png", rgb=True, record_pos=(0.48, 0.152), resolution=(2400, 1080))
    
    while True:
        if exists(cross):
            touch(cross)
        else:
            logging.info("YaGames Banner Not Found.")
        
        await asyncio.sleep(60)
        
async def main_test_flow():
    tutorials_checker()
    ui_checker()
    return True

async def main():
    yagames_task = asyncio.ensure_future(check_for_yagames())
    main_test_task = asyncio.ensure_future(main_test_flow())
    
    main_test_complete = await main_test_task
    
    if main_test_complete:
        yagames_task.cancel()
        try:
            await yagames_task
        except asyncio.CancelledError:
            pass
        
    return True
    
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
