import model
import view


def main():
    mode = view.mode()
    if mode == '1':
        new_contact = view.import_contact()
        model.import_contact(new_contact)
        view.good_result()
    else:
        get_name = view.get_contact()
        model.export_contact(get_name.capitalize())