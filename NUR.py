class Page:
    def __init__(self, page_number):
        self.page_number = page_number
        self.referenced = False
        self.modified = False


class NURPageReplacement:
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
            evict_page = self.select_page_to_evict()
            del self.page_table[evict_page.page_number]
            frame = Page(page_number)
            self.frames[self.frames.index(evict_page)] = frame
            self.page_table[page_number] = frame

    def select_page_to_evict(self):
        # Primeira chance: procurar por páginas que não foram referenciadas
        for frame in self.frames:
            if not frame.referenced:
                return frame

        # Segunda chance: procurar por páginas que não foram modificadas
        for frame in self.frames:
            if not frame.modified:
                return frame

        # Terceira chance: todas as páginas foram referenciadas e modificadas, escolher a primeira
        return self.frames[0]


# Exemplo de uso
nur = NURPageReplacement(3)

# Simulando acesso às páginas
nur.access_page(1)
nur.access_page(2)
nur.access_page(3)
nur.access_page(4)
nur.access_page(2)
nur.access_page(5)
nur.access_page(6)
nur.access_page(2)

# Imprimindo o estado final dos quadros
for frame in nur.frames:
    print(f"Quadro {frame.page_number}: Referenciada={frame.referenced}, Modificada={frame.modified}")
