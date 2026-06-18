def validate_customer_fields(customer_name, address, cphone_no):
    customer_name_check = len(customer_name) != 0 and customer_name.isalpha() and len(customer_name) > 2
    address_check = len(address) != 0 and (address.isalpha())
    cphone_no_check = len(cphone_no) != 0 and cphone_no.isdigit() and 9 <= len(str(cphone_no)) <= 15
    return customer_name_check, address_check, cphone_no_check
