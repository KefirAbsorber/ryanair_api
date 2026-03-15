import configparser

config = configparser.ConfigParser()
# full request is: frm, to, date_from, date_to (date format yyyy-mm-dd)
while True:
    config.read("settings.ini")
    mode = input("Choose mode: \n0. Check tracking \n1. Add tracking \n2. Delete tracking \n3. Update tracking \n4. Exit\n")
    match mode:
        case "0": #check
            print("Entries in settings.ini:\n id frm  to  date_from  date_to")
            queries = config.sections()

            if not queries:
                print("No entries found, nothing to display")
                continue

            for query in queries:
                print(str(config[query])[9:], config[query]["frm"], config[query]["to"], config[query]["date_from"],
                      config[query]["date_to"])

        case "1":  # add
            # grab next index or set to 1
            num = config.sections()
            if num:
                num = str(int(num[-1]) + 1)
            else:
                num = "1"

            # setup section with flight details
            config.add_section(num)
            config[num]["frm"] = input("Enter departure airport code: ").upper()
            config[num]["to"] = input("Enter destination airport code: ").upper()
            config[num]["date_from"] = input("Enter starting date (in format yyyy-mm-dd): ")
            config[num]["date_to"] = input("Enter ending date (in format yyyy-mm-dd): ")

        case "2":  # delete
            print("Entries in settings.ini:\n id frm  to  date_from  date_to")
            queries = config.sections()

            if not queries:
                print("No entries found, nothing to delete")
                continue

            for query in queries:
                print(str(config[query])[9:], config[query]["frm"], config[query]["to"], config[query]["date_from"],
                      config[query]["date_to"])

            while True:
                rm = input("Input the number of query you wish to remove, or 0 to cancel: ")
                if rm.isdigit():
                    break

            if rm == "0":
                continue

            config.remove_section(rm)

        case "3":  # update
            pass
        case "4":  # exit
            print("Exit")
            break
    with open('settings.ini', 'w') as configfile:
        config.write(configfile)