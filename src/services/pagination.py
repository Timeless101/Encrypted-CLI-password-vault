import math

class Pagination():
    def __init__(self, total_cred):

        self.total_cred = total_cred
        self.current_page: int = 1
        self.page_size: int = 5
        self.offset: int = 0

        self.total_pages: int = math.ceil(total_cred / self.page_size)
        self.pages: int = (self.current_page - 1) * self.page_size
        self.howed_items: int = self.pages + self.page_size
        self.showing_items_start: int = (self.current_page * self.page_size) - 4
        self.showing_items_end: int = min(self.current_page * self.page_size, total_cred)
        self.pages: int = (self.current_page - 1) * self.page_size
        self.showed_items: int = self.pages + self.page_size

    def next_page(self):
        if self.showed_items < self.total_cred:
            self.current_page += 1
            self.offset += self.page_size
        else:
            pass

    def previous_page(self):
        if self.showed_items > self.page_size:
            self.current_page -= 1
            self.offset -= self.page_size
        else:
            pass