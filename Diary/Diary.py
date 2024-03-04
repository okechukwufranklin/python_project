class diary:
    def __init__(self, Id, body, title):
        self.Id = Id
        self.body = body
        self.title = title

    def get_id(self):
        return self.Id

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def set_body(self, body):
        self.body = body

    def set_title(self, title):
        self.title = title


def is_locked():
    return True


class Diary:
    def __init__(self, username, password):
        self.password = password
        self.username = username
        self.entries = []
        self.is_locked = bool

    def lock_diary(self):
        self.is_locked = True


    def unlock_diary(self, password):
        if self.password == password:
            self.is_locked = False

    def create_entry(self, title, body):
        id = len(self.entries) + 1
        entry = diary(id, body, title)
        self.entries.append(entry)

    def size_of_entries(self):
        return len(self.entries)

    def find_entry_by_id(self, Id):
        for entry in self.entries:
            if Id == entry.get_id():
                return entry
        return None

    def set_password(self, password):
        self.password = password

    def validate_password(self, password):
        return password == self.password

    def delete_entry(self, Id):
        entry = self.find_entry_by_id(Id)
        if entry:
            self.entries.remove(entry)

    def update_entry(self, Id, title, body):
        entry = self.find_entry_by_id(Id)
        if entry:
            entry.set_title(title)
            entry.set_body(body)
