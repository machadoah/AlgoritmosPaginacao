class Page:
    def __init__(self, page_number):
        self.page_number = page_number
        self.referenced = False


class SCPageReplacement:
    def __init__(self, num_frames):
        self.num_frames = num_frames
        self.frames = []
        self.page_table = {}

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
                frame = self.frames.pop(0)
                if frame.referenced:
                    frame.referenced = False
                    self.frames.append(frame)
                else:
                    del self.page_table[frame.page_number]
                    new_frame = Page(page_number)
                    self.frames.append(new_frame)
                    self.page_table[page_number] = new_frame
                    break


# Exemplo de uso
sc = SCPageReplacement(3)

# Simulando acesso às páginas
sc.access_page(1)
sc.access_page(2)
sc.access_page(3)
sc.access_page(4)
sc.access_page(2)
sc.access_page(5)
sc.access_page(6)
sc.access_page(2)

# Imprimindo o estado final dos quadros
for frame in sc.frames:
    print(f"Quadro {frame.page_number}")
