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
