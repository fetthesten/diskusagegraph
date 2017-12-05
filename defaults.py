import pickle

class defaults:
    def __init__(self):
        self.styles = {}
        self.styles['default'] = {
            'font_heading': ('Segoe UI Light', 24),
            'font_button_regular': ('Segoe UI', 16),
            'font_button_thicc': ('Segoe UI Semibold', 16),
            'font_entry': ('Segoe UI', 12),
            'color_background_main': '#ffffff',
            'color_background_entry': '#333333',
            'color_background_button': '#ff6e00',
            'color_background_button_highlight': '#aa3b00',
            'color_background_button_quit': '#ff3900',
            'color_background_button_quit_highlight': '#aa0b00',
            'color_foreground_button': '#ffffff',
            'color_foreground_main': '#333333',
            'h1': {
                'font': 'font_heading',
                'justify': 'left',
                'anchor': 'w',
                'background': 'color_background_main',
                'foreground': 'color_foreground_main',
                'height': 1,
                'width': 0,
                'padx': 2,
                'pady': 4
            },
            'button_regular': {
                'font': 'font_button_regular',
                'justify': 'left',
                'anchor': 'w',
                'background': 'color_background_button',
                'foreground': 'color_foreground_button',
                'relief': 'flat',
                'height': 1,
                'width': 16,
                'padx': 2,
                'pady': 1,
                'borderwidth': 0,
                'activeforeground': 'color_foreground_button',
                'activebackground': 'color_background_button_highlight'
            },
            'button_quit': {
                'font': 'font_button_thicc',
                'justify': 'center',
                'anchor': 'center',
                'background': 'color_background_button_quit',
                'foreground': 'color_foreground_button',
                'relief': 'flat',
                'height': 0,
                'width': 3,
                'padx': 2,
                'pady': 1,
                'borderwidth': 0,
                'activeforeground': 'color_foreground_button',
                'activebackground': 'color_background_button_quit_highlight'
            },
            'menu_filler': {
                'background': 'color_background_button',
            },
            'entry_dir': {
                'background': 'color_background_entry',
                'font': 'font_entry',
                'foreground': 'color_background_main',
                'relief': 'flat',
                'bd': 2,
            },
        }

    def styles(self):
        return self.styles;

    def save(self):
        pickle.dump(self.styles, open('styles.dat', 'wb'))

if __name__ == '__main__':
    d = defaults()
    d.save()
