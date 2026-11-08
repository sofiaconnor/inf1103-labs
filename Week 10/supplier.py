class Supplier:

    def __init__(self, supplier_id: str, name: str, contact_email: str) -> None: # None here means that this method will return no value (None)
                                                                                 # use str for supplier_id since they include letters e.g. "S001"
        self.__supplier_id: str = supplier_id
        self.__name: str = name
        self.__email: str = contact_email

    def display_information(self) -> None:
        print("Supplier Id:", self.__supplier_id)
        print("Name:", self.__name)
        print("Email:", self.__email)