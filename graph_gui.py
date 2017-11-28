import tkinter as tk
from tkinter import messagebox as msgbox
from diskusagegraph import DiskUsageGraph

class DiskUsageGui:

    def __init__(self, graph = None):
        if graph:
            self.graph = self.load_graph(graph)

        self.layouts = {}
        self.styles = {}

        self.init_styles()
        self.init_layouts()
        
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

        root.focus_set()
        
        return root

    def test(self):
        msgbox.showinfo('rock steady', 'my man')

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
            tk_args['font'] = current_style[s['font']]
            tk_args['background'] = current_style[s['background']]
            tk_args['foreground'] = current_style[s['foreground']]
            tk_args['text'] = None if 'text' not in el else el['text']
            tk_args['command'] = None if 'command' not in el else el['command']
            tk_args['highlightbackground'] = None if 'highlightbackground' not in s else current_style[s['highlightbackground']]
            tk_args['highlightforeground'] = None if 'highlightforeground' not in s else current_style[s['highlightforeground']]
            tk_args['activebackground'] = None if 'activebackground' not in s else current_style[s['activebackground']]
            tk_args['activeforeground'] = None if 'activeforeground' not in s else current_style[s['activeforeground']]

            column = 0 if 'column' not in el else el['column']
            row = 0 if 'row' not in el else el['row']
            sticky = 'w' if 'sticky' not in el else el['sticky']
                   
            meth = getattr(tk, el['element'])
            self.layouts[layout][n]['item'] = meth(root, **tk_args).grid(column=column, row=row, sticky=sticky)

    def init_layouts(self):
        self.layouts['main'] = {
            'heading': {
                'element': 'Label',
                'text': 'a disk usage graph fam',
                'style': 'h1',
                'column': 0,
                'row': 0,
                'sticky': 'W'
                },
            'button1': {
                'element': 'Button',
                'text': 'donkey kong',
                'style': 'button_regular',
                'command': 'test',
                'column': 0,
                'row': 2,
                'sticky': 'W'
                },
            'button2': {
                'element': 'Button',
                'text': 'rocksteady',
                'style': 'button_regular',
                'command': self.test,
                'column': 0,
                'row': 3,
                'sticky': 'W'
                },
            'button_close': {
                'element': 'Button',
                'text': 'x',
                'style': 'button_quit',
                'command': self.quit_window,
                'column': 2,
                'row': 0,
                'sticky': 'E'
                }
            }
        
    def init_styles(self):
        self.styles['default'] = {
            'font_heading': ('Segoe UI Light', 24),
            'font_button_regular': ('Segoe UI', 16),
            'font_button_thicc': ('Segoe UI Semibold', 16),
            'background_main': '#ffffff',
            'background_button': '#ff6e00',
            'background_button_highlight': '#aa3b00',
            'background_button_quit': '#ff3900',
            'background_button_quit_highlight': '#aa0b00',
            'foreground_button': '#ffffff',
            'foreground_main': '#333333',
            'h1': {
                'font': 'font_heading',
                'justify': 'left',
                'anchor': 'w',
                'background': 'background_main',
                'foreground': 'foreground_main',
                'height': 1,
                'width': 0,
                'padx': 2,
                'pady': 4
            },
            'button_regular': {
                'font': 'font_button_regular',
                'justify': 'left',
                'anchor': 'w',
                'background': 'background_button',
                'foreground': 'foreground_button',
                'relief': 'flat',
                'height': 1,
                'width': 16,
                'padx': 2,
                'pady': 1,
                'borderwidth': 0,
                'activeforeground': 'foreground_button',
                'activebackground': 'background_button_highlight'
            },
            'button_quit': {
                'font': 'font_button_thicc',
                'justify': 'center',
                'anchor': 'center',
                'background': 'background_button_quit',
                'foreground': 'foreground_button',
                'relief': 'flat',
                'height': 0,
                'width': 3,
                'padx': 2,
                'pady': 1,
                'borderwidth': 0,
                'activeforeground': 'foreground_button',
                'activebackground': 'background_button_quit_highlight'
            }
        }
        
if __name__ == '__main__':
    g = DiskUsageGui()
