from Home_work_year_2.Super_store.Super_Classes.SuperStore import SuperStore
from Home_work_year_2.Super_store.Super_functions.Csv_To_List import map_csv
from Home_work_year_2.Super_store.Super_functions import Menu_functions
from time import sleep
from Home_work_year_2.Super_store.Super_functions.Menu_functions import print_menu_np, shirt_max_price, \
    client_order_details
from Home_work_year_2.Super_store.shirt_orders_analysis import shirt_orders_analysis, orders_above_price_avg \
    , orders_clients_dict, orders_per_client_graph


def menu():
    clients, products, shirts, orders = map_csv(["clients.csv", "products_supply.csv", "shirts.csv", "orders.csv"])
    list_of_products = products + shirts
    list_of_clients = clients
    list_of_orders = orders

    super_store = SuperStore(list_of_products, list_of_clients, list_of_orders)
    print("Hello!", '\nThis menu contains several options:')

    while 1 > 0:
        Menu_functions.print_menu()
        user_choice = input("Enter your choice here(1-15):")
        if user_choice != "B":
            while user_choice.isnumeric() != True or int(user_choice) > 19 or int(user_choice) < 1:
                user_choice = input("Wrong input!\nEnter your choice here(1-15 or B):")

            if user_choice == "1":
                Menu_functions.print_products(super_store)

            elif user_choice == "2":
                Menu_functions.print_clients(super_store)

            elif user_choice == "3":
                Menu_functions.add_new_product(super_store)

            elif user_choice == "4":
                Menu_functions.add_new_client(super_store)

            elif user_choice == "5":
                Menu_functions.remove_product(super_store)

            elif user_choice == "6":
                Menu_functions.remove_client(super_store)

            elif user_choice == "7":
                Menu_functions.print_all_under_price(super_store)

            elif user_choice == "8":
                Menu_functions.print_most_expensive(super_store)

            elif user_choice == "9":
                Menu_functions.print_all_phones(super_store)

            elif user_choice == "10":
                Menu_functions.print_all_laptops(super_store)

            elif user_choice == "11":
                Menu_functions.print_avg_phone(super_store)

            elif user_choice == "12":
                Menu_functions.print_largest_screen(super_store)

            elif user_choice == "13":
                Menu_functions.print_most_cam_res(super_store)

            elif user_choice == "14":
                Menu_functions.print_most_popular(super_store)

            elif user_choice == "15":
                Menu_functions.print_shirts(shirts)

            elif user_choice == "16":
                Menu_functions.add_new_order(super_store)

            elif user_choice == "17":
                SuperStore.print_orders(super_store)

            elif user_choice == "18":
                print("the program is restarting\nGood bye!")
                sleep(1)
                menu()
                break

            elif user_choice == "19":
                print("Thank you\nGood bye!")
                break

        else:
            while 1 > 0:
                print_menu_np()
                user_choice_b = input("\nEnter your option:")
                while user_choice_b.isnumeric() != True or int(user_choice_b) > 6 or int(user_choice_b) < 1:
                    user_choice_b = input("\nWrong input!\nEnter your option(1-6):")

                if user_choice_b == "1":
                    shirt_max_price("orders.csv", super_store)

                elif user_choice_b == "2":
                    client_order_details("orders.csv", super_store)

                elif user_choice_b == "3":
                    orders_above_price_avg(shirt_orders_analysis("orders.csv", super_store))

                elif user_choice_b == "4":
                    dict_of_orders = orders_clients_dict(shirt_orders_analysis("orders.csv", super_store)
                                                         , super_store)
                    for client in dict_of_orders:
                        print("Client id:", client, "- Orders:", dict_of_orders[client], "\n")

                elif user_choice_b == "5":
                    orders_per_client_graph(orders_clients_dict(shirt_orders_analysis("orders.csv", super_store)
                                                                , super_store))
                elif user_choice_b == "6":
                    break


menu()
