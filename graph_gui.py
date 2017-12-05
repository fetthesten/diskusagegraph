import pickle
import tkinter as tk
from tkinter import messagebox as msgbox
from diskusagegraph import DiskUsageGraph

class DiskUsageGui:

    def __init__(self, graph = None):
        if graph:
            self.graph = self.load_graph(graph)

        self.current_dir = 'c:\\'
        
        self.layouts = {}
        self.styles = {}

        self.init_styles()
        self.init_layouts()
        
        self.window = self.init_window()

        #self.layouts['main']['dir_entry']['item'].insert(0, self.current_dir)
        
        self.window.mainloop()

    def load_graph(self, graph):
        return graph

    def init_window(self):
        root = tk.Tk()
        root.title('disk usage graph')
        root.geometry('1024x768')
        # root.wm_attributes('-fullscreen','true')

        root.configure(background = 'white')
        root.columnconfigure(2, weight = 1)
        self.load_layout(root)

        root.focus_set()
        
        return root

    def test(self):
        msgbox.showinfo('klikkosaurus', 'heyo')

    def quit_window(self):
        self.window.destroy()

    def load_layout(self, root, layout=None, style=None):
        #todo: clear old layout
        if not layout:
            layout = 'main'
        if not style:
            style = 'default'
        current_style = self.styles[style]
        for n, el in self.layouts[layout].items():
            
            s = {}
            s.update(current_style[el['style']])
            tk_args = {}
            tk_args.update(current_style[el['style']])
            if 'font' in s:
                tk_args['font'] = current_style[s['font']]
            if 'background' in s:
                tk_args['background'] = current_style[s['background']]
            if 'foreground' in s:
                tk_args['foreground'] = current_style[s['foreground']]
            if 'bd' in s:
                tk_args['bd'] = s['bd']
            tk_args['text'] = None if 'text' not in el else el['text']
            tk_args['command'] = None if 'command' not in el else el['command']
            tk_args['highlightbackground'] = None if 'highlightbackground' not in s else current_style[s['highlightbackground']]
            tk_args['highlightforeground'] = None if 'highlightforeground' not in s else current_style[s['highlightforeground']]
            tk_args['activebackground'] = None if 'activebackground' not in s else current_style[s['activebackground']]
            tk_args['activeforeground'] = None if 'activeforeground' not in s else current_style[s['activeforeground']]
            print(tk_args)
            default_grid_args = {
                'column': 0,
                'row': 0,
                'columnspan': 1,
                'rowspan': 1,
                'sticky': 'w'
                }
            grid_args = {}
            for kw, default_value in default_grid_args.items():
                grid_args[kw] = default_value if kw not in el else el[kw]
                   
            meth = getattr(tk, el['element'])
            self.layouts[layout][n]['item'] = meth(root, **tk_args).grid(**grid_args)

    def init_layouts(self):
        self.layouts['main'] = {
            'heading': {
                'element': 'Label',
                'text': 'a disk usage graph fam',
                'style': 'h1',
                'column': 0,
                'row': 0,
                'columnspan': 3,
                'sticky': 'W'
                },
            'dir_entry': {
                'element': 'Entry',
                'style': 'entry_dir',
                'column': 0,
                'row': 1,
                'sticky': 'EWNS',
                'columnspan': 3,
                },
            'filler': {
                'element': 'Frame',
                'style': 'menu_filler',
                'column': 0,
                'row': 2,
                'sticky': 'EWNS',
                'columnspan': 3
                },
            'button_load': {
                'element': 'Button',
                'text': 'load dir',
                'style': 'button_regular',
                'command': 'test',
                'column': 1,
                'row': 2,
                'sticky': 'W'
                },
            'button_reset': {
                'element': 'Button',
                'text': 'reset graph',
                'style': 'button_regular',
                'command': self.test,
                'column': 2,
                'row': 2,
                'sticky': 'W'
                },
            }
        
    def init_styles(self):
        self.styles = pickle.load(open('styles.dat', 'rb'))
        
if __name__ == '__main__':
    g = DiskUsageGui()
