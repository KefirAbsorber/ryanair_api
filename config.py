import configparser

config = configparser.ConfigParser()
# full request is: frm, to, date_from, date_to (date format yyyy-mm-dd)
while True:
    mode = input("Choose mode: \n1. Add tracking \n2. Delete tracking \n3. Update tracking \n4. Exit\n")
    match mode:
        case "1":  # add
            # grab next index or set to 1
            config.read("settings.ini")
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

            # save
            with open('settings.ini', 'w') as configfile:
                config.write(configfile)

        case "2":  # delete
            pass
        case "3":  # update
            pass
        case "4":  # exit
            break
