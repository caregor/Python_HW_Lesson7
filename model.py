import csv


def import_contact(person):
    with open('contacts.csv', 'a', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'phone', 'description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(person)


def export_contact(key_value):
    with open('contacts.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if key_value == row.get('last_name'):
                print(row['first_name'], row['last_name'], row['phone'], row['description'])


def preparing_data(contact_data):
    new_item = ''
    count = 0
    result = []
    if len(contact_data) > 3:
        for i in range(3,len(contact_data)):
            new_item = new_item + ' ' + contact_data[i]
            count += 1
        for i in range(count):
            contact_data.pop()
    contact_data.append(new_item)
    result.extend(contact_data)
    return result

