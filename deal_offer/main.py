from booking import BookingBot as bot
with bot() as bot:
    bot.land_first_page()
    bot.close_pop_up()
    bot.send_props()
    bot.apply_filter()
    bot.find_top_reviewed()
    bot.get_picture()