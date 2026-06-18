def extract_meter_amounts(ch_meter, p_meter, b_meter, gr_meter, t_meter, co_meter, cho_meter, w_meter, ice_meter, g_meter, chs_meter, k_meter):
    chicken = ch_meter.amountusedvar.get()
    pizza = p_meter.amountusedvar.get()
    burger = b_meter.amountusedvar.get()
    grilled_chicken = gr_meter.amountusedvar.get()

    tea = t_meter.amountusedvar.get()
    coffee = co_meter.amountusedvar.get()
    chocolate_milkshake = cho_meter.amountusedvar.get()
    watermelon_juice = w_meter.amountusedvar.get()

    icecream = ice_meter.amountusedvar.get()
    gulab_jamun = g_meter.amountusedvar.get()
    cheese_cake = chs_meter.amountusedvar.get()
    kunafa = k_meter.amountusedvar.get()

    return {
        'chicken': chicken,
        'pizza': pizza,
        'burger': burger,
        'grilled_chicken': grilled_chicken,
        'tea': tea,
        'coffee': coffee,
        'chocolate_milkshake': chocolate_milkshake,
        'watermelon_juice': watermelon_juice,
        'icecream': icecream,
        'gulab_jamun': gulab_jamun,
        'cheese_cake': cheese_cake,
        'kunafa': kunafa,
    }
