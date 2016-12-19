import time
def record(patient_id, first_name, last_name, address, gender, contact, age):
    fw = open("patient_info.txt", "a")
    fw.write("%1s%20s%20s%20s%20s%20s%20s\n" %(patient_id, first_name, last_name, address, gender, contact, age))
    fw.close()

def append(patient_id, treatment_id, invoice_id, bill_amount):
    fw = open("invoicing.txt", "a")
    fw.write("%1s%20s%20s%20s\n" % (patient_id, treatment_id, invoice_id, bill_amount))
    fw.close()

def appoint(patient_id, appointment_id, specialist, status):
    fw = open("appointment_plan.txt", "a")
    fw.write("%1s%20s%20s%20s\n" % (patient_id, appointment_id, specialist, status))
    fw.close()

def treatment_plan(patient_id, treatment_id, complaint, treatment):
    fw = open("treatment_plan.txt", "a")
    fw.write("%1s%20s%20s%50s\n" % (patient_id, treatment_id, complaint, treatment))
    fw.close()

def payment(patient_id, treatment_id, total_cash):
    fw = open("payment.txt", "a")
    fw.write("%1s%20s%20s\n" % (patient_id, treatment_id, total_cash))
    fw.close()

def appointment():
    patient_id = input("\nEnter the patient ID:")
    appointment_id = input("Enter the appointment ID:")
    specialist = input("Enter the name of the specialist for checkup:")
    status = input("Enter the status:")
    appoint(patient_id, appointment_id, specialist, status)

def patient_treatment_plan():
    patient_id = input("\nEnter the patient ID:")
    treatment_id = input("Enter the treatment ID:")
    complaint = input("Enter the complaint of the patient:")
    treatment = input("Enter the suggested treatment to the patient:")
    treatment_plan(patient_id, treatment_id, complaint, treatment)

def entry():
    patient_id = input("\nEnter the Patient ID:")
    first_name = input("Enter the First Name:")
    last_name = input("Enter the Last Name:")
    address = input("Enter the Address:")
    gender = input("Enter the Gender:")
    contact = input("Enter the Contact:")
    age = input("Enter the age:")
    record(patient_id, first_name, last_name, address, gender, contact, age)

def invoicing():
    patient_id = input("\nEnter patient ID:")
    treatment_id = input("Enter treatment ID:")
    invoice_id = input("Enter invoice ID:")
    bill_amount = input("Enter bill amount:")
    append(patient_id, treatment_id, invoice_id, bill_amount)
    print("Invoicing done for patient of patient id", patient_id)

def write_payment():
    patient_id = input("\nEnter patient ID:")
    treatment_id = input("Enter treatment ID:")
    total_cash = input("Enter total cash:")
    payment(patient_id, treatment_id, total_cash)
    print("Payment recieved by patient of patient_id", patient_id)

def logout():
    print("\nWe are glad to help you, Thank you!!!\n")

print("Welcome to Prudent Healthcare Service\n")
while True:
    print("What type of login do you want?\n1. Reception Login\n2. Physician Login\n3. Accountant Login\n4. Logout\n")

    option = input("Choose your login type:")
    choose = int(option)

    if (choose == 1):
        username = input("\nEnter your username:")
        password = input("Enter your password:")

        if (username, password) == ("user1", "password"):
            print("\nWelcome to PMS", username, "You have logged in as a reception.\n")
        else:
            print("\nUsername and password does not match\n")
            continue

        while True:
            print("\n1. Record the patient information\n2. Search the patient information\n3. Exit\n")
            menu = input("Choose any option from the menu:")
            choose = int(menu)

            if (choose == 1):
                entry()
                time.sleep(1)
            elif (choose == 2):
                read_again = open("patient_info.txt")
                enter = input("\nPlease input patient ID:")
                for each_line in read_again:
                    (patient_id, first_name, last_name, address, gender, contact, age) = each_line.split()

                if patient_id == enter:
                    print(patient_id, first_name, last_name, address, gender, contact, age)
                else:
                    print("There is no patient of this patient ID")
                read_again.close()
                time.sleep(1)
            elif (choose == 3):
                logout()
                time.sleep(1)
                break
            else:
                print("\nThe selected option is not in the menu\n")
                time.sleep(1)
                continue

    elif (choose == 2):
        username = input("\nEnter your username:")
        password = input("Enter your password:")

        if (username, password) == ("user2", "password"):
            print("\nWelcome to PMS", username, "You have logged in as a physician.\n")
        else:
            print("\nUsername and password does not match\n")
            continue

        while True:
            print("\n1. Appointments management\n2. Patient Treatment Plan\n3. Extract Appointments management detail\n4. Extract Patient Treatment Plan detail\n5. Exit\n")
            menu = input("Choose any option from the menu:")
            choose = int(menu)

            if (choose == 1):
                appointment()
                time.sleep(1)

            elif (choose == 2):
                patient_treatment_plan()
                time.sleep(1)

            elif (choose == 3):
                read_again1 = open("appointment_plan.txt")
                extract = input("\nPlease input patient ID:")
                for each_line in read_again1:
                    (patient_id, appointment_id, specialist, status) = each_line.split()

                if patient_id == extract:
                    print(patient_id, appointment_id, specialist, status)
                else:
                    print("There is no patient of this patient ID")
                read_again1.close()
                time.sleep(1)

            elif (choose == 4):
                read1 = open("treatment_plan.txt")
                enter = input("\nPlease input patient ID:")
                for each_line in read1:
                    (patient_id, treatment_id, complaint, treatment) = each_line.split()

                if patient_id == enter:
                    print(patient_id, treatment_id, complaint, treatment)
                else:
                    print("There is no patient of this patient ID")
                read1.close()
                time.sleep(1)

            elif(choose == 5):
                logout()
                time.sleep(1)
                break

            else:
                print("\nThe selected option is not in the menu")
                time.sleep(1)
                break
    elif (choose == 3):
        username = input("\nEnter your username:")
        password = input("Enter your password:")

        if (username, password) == ("user3", "password"):
            print("\nWelcome to PMS", username, "You have logged in as an accountant.")
        else:
            print("\nUsername and password does not match\n")
            continue
        while True:
            print("\n1. Recieve payment\n2. Invoicing\n3. Extract received payment history\n4. Extract invoice history\n5. Exit")
            menu = input("Choose any option from the menu:")
            choose = int(menu)

            if (choose == 1):
                write_payment()
                time.sleep(1)
            elif (choose == 2):
                invoicing()
                time.sleep(1)
            elif (choose == 3):
                read_payment = open("payment.txt")
                enter = input("\nPlease input patient ID:")
                for each_line in read_payment:
                    (patient_id, treatment_id, total_cash) = each_line.split()

                if patient_id == enter:
                    print(patient_id, treatment_id, total_cash)
                else:
                    print("There is no patient of this patient ID")
                    read_payment.close()
                time.sleep(1)

            elif (choose == 4):
                read = open("invoicing.txt")
                enter = input("\nPlease input patient ID:")
                for each_line in read:
                    (patient_id, treatment_id, invoice_id, bill_amount) = each_line.split()

                if patient_id == enter:
                    print(patient_id, treatment_id, invoice_id, bill_amount)
                else:
                    print("There is no patient of this patient ID")
                read.close()
                time.sleep(1)

            elif (choose == 5):
                logout()
                time.sleep(1)
                break
            else:
                print("\nThe selected option is not in the menu\n")
                time.sleep(1)

    elif (choose == 4):
        print("\nThank you!!")
        break

    else:
        print("\nSelected login type do not exist\n")
        time.sleep(1)


