class Page:
    def __init__(self, page_number):
        self.page_number = page_number
        self.referenced = False


class ClockPageReplacement:
    def __init__(self, num_frames):
        self.num_frames = num_frames
        self.frames = []
        self.page_table = {}
        self.hand = 0

    def access_page(self, page_number):
        if page_number not in self.page_table:
            self.handle_page_fault(page_number)

        page = self.page_table[page_number]
        page.referenced = True

    def handle_page_fault(self, page_number):
        if len(self.frames) < self.num_frames:
            frame = Page(page_number)
            self.frames.append(frame)
            self.page_table[page_number] = frame
        else:
            while True:
                frame = self.frames[self.hand]
                if frame.referenced:
                    frame.referenced = False
                    self.hand = (self.hand + 1) % self.num_frames
                else:
                    del self.page_table[frame.page_number]
                    new_frame = Page(page_number)
                    self.frames[self.hand] = new_frame
                    self.page_table[page_number] = new_frame
                    self.hand = (self.hand + 1) % self.num_frames
                    break


# Exemplo de uso
clock = ClockPageReplacement(3)

# Simulando acesso às páginas
clock.access_page(1)
clock.access_page(2)
clock.access_page(3)
clock.access_page(4)
clock.access_page(2)
clock.access_page(5)
clock.access_page(6)
clock.access_page(2)

# Imprimindo o estado final dos quadros
for frame in clock.frames:
    print(f"Quadro {frame.page_number}")
