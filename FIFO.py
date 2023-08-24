class Page:
    def __init__(self, page_number):
        self.page_number = page_number


class FIFOPageReplacement:
    def __init__(self, num_frames):
        self.num_frames = num_frames
        self.frames = []
        self.page_table = {}

    def access_page(self, page_number):
        if page_number not in self.page_table:
            self.handle_page_fault(page_number)

    def handle_page_fault(self, page_number):
        if len(self.frames) < self.num_frames:
            frame = Page(page_number)
            self.frames.append(frame)
            self.page_table[page_number] = frame
        else:
            evict_page = self.frames[0]
            del self.page_table[evict_page.page_number]
            frame = Page(page_number)
            self.frames.pop(0)
            self.frames.append(frame)
            self.page_table[page_number] = frame


# Exemplo de uso
fifo = FIFOPageReplacement(3)

# Simulando acesso às páginas
fifo.access_page(1)
fifo.access_page(2)
fifo.access_page(3)
fifo.access_page(4)
fifo.access_page(2)
fifo.access_page(5)
fifo.access_page(6)
fifo.access_page(2)

# Imprimindo o estado final dos quadros
for frame in fifo.frames:
    print(f"Quadro {frame.page_number}")


