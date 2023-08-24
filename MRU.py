class Page:
    def __init__(self, page_number):
        self.page_number = page_number
        self.last_used = 0


class MRUPageReplacement:
    def __init__(self, num_frames):
        self.num_frames = num_frames
        self.frames = []
        self.page_table = {}
        self.time = 0

    def access_page(self, page_number):
        if page_number not in self.page_table:
            self.handle_page_fault(page_number)

        page = self.page_table[page_number]
        page.last_used = self.time
        self.time += 1

    def handle_page_fault(self, page_number):
        if len(self.frames) < self.num_frames:
            frame = Page(page_number)
            self.frames.append(frame)
            self.page_table[page_number] = frame
        else:
            frame = max(self.frames, key=lambda f: f.last_used)
            del self.page_table[frame.page_number]
            new_frame = Page(page_number)
            self.frames[self.frames.index(frame)] = new_frame
            self.page_table[page_number] = new_frame


# Exemplo de uso
mru = MRUPageReplacement(3)

# Simulando acesso às páginas
mru.access_page(1)
mru.access_page(2)
mru.access_page(3)
mru.access_page(4)
mru.access_page(2)
mru.access_page(5)
mru.access_page(6)
mru.access_page(2)

# Imprimindo o estado final dos quadros
for frame in mru.frames:
    print(f"Quadro {frame.page_number}")
