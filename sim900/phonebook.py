class Phonebook:
    def __init__(self, sim900):
        self.sim900 = sim900

    def select_storage(self, storage="SM"):
        """
        Select the phonebook memory storage.
        """
        return self.sim900.send_command(f'AT+CPBS="{storage}"')

    def read_entry(self, index):
        """
        Read the phonebook entry at the specified index.
        """
        return self.sim900.send_command(f'AT+CPBR={index}')

    def find_entry(self, name):
        """
        Find phonebook entries matching the given name.
        """
        return self.sim900.send_command(f'AT+CPBF="{name}"')

    def write_entry(self, index, number, name):
        """
        Write a phonebook entry.
        """
        return self.sim900.send_command(f'AT+CPBW={index},"{number}",129,"{name}"')

    def delete_entry(self, index):
        """
        Delete the phonebook entry at the specified index.
        """
        return self.sim900.send_command(f'AT+CPBW={index}')
