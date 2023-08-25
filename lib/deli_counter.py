import ipdb

katz_deli = [1,2,3,4,5]

def line(queue_list):
    if not queue_list:
        print("The line is currently empty.")
    else:
        line_order = "The line is currently:"
        for index in range(len(queue_list)):
            line_order += f" {index+1}. {queue_list[index]}"        
        print(line_order)

def take_a_number(queue_list, customer):
    queue_list.append(customer)
    print(f"Welcome, {customer}. You are number {len(queue_list)} in line.")  

def now_serving(queue_list):
    if not queue_list:
        print("There is nobody waiting to be served!")
    else:
        current_customer = queue_list.pop(0)
        print(f"Currently serving {current_customer}.")


