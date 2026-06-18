def create_order_tables_queries():
    return [
        '''create table if not exists pizza(customer_id int(10),s_pizza int(3),m_pizza int(3),l_pizza int(3),s_cost float(3),m_cost float(3),l_cost float(3))''',
        '''create table if not exists burger(customer_id int(10),s_burger int(3),m_burger int(3),l_burger int(3),s_cost float(3),m_cost float(3),l_cost float(3))''',
        '''create table if not exists tikka(customer_id int(10),t_spice int(2),t_cost float(3))''',
        '''create table if not exists wrap(customer_id int(10),w_spice int(2),w_cost float(3))''',
        '''create table if not exists tea(customer_id int(10),karak int(3),black_tea int(3),green_tea int(3),k_cost float(3),b_cost float(3),g_cost float(3))''',
        '''create table if not exists coffee(customer_id int(10),latte int(3),cappuccino int(3),americano int(3),l_cost float(3),c_cost float(3),a_cost float(3))''',
        '''create table if not exists choco(customer_id int(10),s_choco int(3),m_choco int(3),l_choco int(3),s_cost float(3),m_cost float(3),l_cost float(3))''',
        '''create table if not exists watermelon(customer_id int(10),s_watermelon int(3),m_watermelon int(3),l_watermelon int(3),s_cost float(3),m_cost float(3),l_cost float(3))''',
        '''create table if not exists icecream(customer_id int(10),i_cost float(3))''',
        '''create table if not exists gulabjamun(customer_id int(10),g_cost float(3))''',
        '''create table if not exists cheesecake(customer_id int(10),ch_cost float(3))''',
        '''create table if not exists kunafa(customer_id int(10),k_cost float(3))''',
    ]
