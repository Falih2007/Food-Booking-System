def create_customers_table_query():
    return '''CREATE TABLE IF NOT EXISTS customers (
                        customer_id int(10),
                        customer_name VARCHAR(50),
                        address VARCHAR(100),
                        customer_phoneno INT(15),
                        date_of_order date,
                        time varchar(50),
                        BUTTER_CHICKEN FLOAT(5),
                        PIZZA FLOAT(5),
                        BURGER FLOAT(5),
                        GRILLED_CHICKEN_WRAP FLOAT(5),
                        TEA FLOAT(5),
                        COFFEE FLOAT(5),
                        CHOCOLATE_MILKSHAKE FLOAT(5),
                        WATERMELON_JUICE FLOAT(5),
                        ICE_CREAM FLOAT(5),
                        GULAB_JAMUN  FLOAT(5),
                        CHEESE_CAKE  FLOAT(5),
                        KUNAFA FLOAT(5)
                    )'''


def max_customer_id_query():
    return 'SELECT MAX(customer_id) FROM customers'


def insert_customer_query(customer_id, customer_name, address, cphone_no):
    return f'''INSERT INTO customers(customer_id,customer_name, address, customer_phoneno) VALUES({customer_id},'{customer_name}', '{address}', {int(cphone_no)})'''


def update_customer_summary_query(customer_name, address, cphone_no, chicken, pizza, burger, grilled_chicken, tea, coffee, chocolate_milkshake, watermelon_juice, icecream, gulab_jamun, cheese_cake, kunafa, customer_id):
    return f'''update customers set customer_name='{customer_name}',
                             address='{address}',
                             customer_phoneno={int(cphone_no)},
                             BUTTER_CHICKEN={chicken},
                             PIZZA={pizza},
                             BURGER={burger},
                             GRILLED_CHICKEN_WRAP={grilled_chicken},
                             TEA={tea},COFFEE={coffee},
                             CHOCOLATE_MILKSHAKE={chocolate_milkshake},
                             WATERMELON_JUICE={watermelon_juice},
                             ICE_CREAM={icecream},
                             GULAB_JAMUN={gulab_jamun},
                             CHEESE_CAKE={cheese_cake},
                             KUNAFA={kunafa} where customer_id={customer_id}'''
