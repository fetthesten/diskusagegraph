import tkinter as tk
from diskusagegraph import DiskUsageGraph

class DiskUsageGui:

    def __init__(self, graph = None):
        if graph:
            self.graph = self.load_graph(graph)

        self.layouts = {}

        self.layouts['main'] = {
            'heading': {
                'element': 'label',
                'text': 'a disk usage graph fam',
                'font': ('Segoe UI Light', 12)
                },
            'button': {
                'element': 'label',
                'text': 'donkey kong',
                'font': ('Segoe UI Light', 12)
                }
            }
        self.window = self.init_window()

        self.window.mainloop()

    def load_graph(self, graph):
        return graph

    def init_window(self):
        root = tk.Tk()
        root.title('disk usage graph')
        root.geometry('1024x768')

        root.configure(background = 'white')
        
        self.load_layout(root)
            
        return root

    def load_layout(self, root, layout=None):
        #todo: clear old layout
        if not layout:
            layout = 'main'
        for n, el in self.layouts[layout].items():
            print(n, el)
            if el['element'] is 'label':
                self.layouts[layout][n]['item'] = tk.Label(root,
                    text=el['text'],
                    font=el['font'],
                    background='#990099',
                    width=24,
                    height=2,
                    justify='left',
                    padx=4,
                    pady=4).grid(column=0, sticky='W')
                
            
def test():
    g = DiskUsageGui()

if __name__ == '__main__':
    test()
