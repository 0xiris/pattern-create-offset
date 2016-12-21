import Tkinter as tk
import pattern_create_offset as pco

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.generate_label = tk.Label(self, text = "Pattern Length:")
        self.offset_label = tk.Label(self, text = "Offset:")


        vcmd = (self.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        vcmd_hex = (self.register(self.validate_hex),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')


        self.generate_entry = tk.Entry(self, validate = 'key', validatecommand = vcmd)
        self.offset_entry = tk.Entry(self, validate = 'key', validatecommand = vcmd_hex)

        self.generate_button = tk.Button(self, text="Generate", command = lambda: self.gen_button(self.generate_entry.get()))
        self.offset_button = tk.Button(self, text="Find Buffer Size", command = lambda: self.off_button(self.offset_entry.get()))

        self.generate_text = tk.Text(self)
        self.offset_text = tk.Text(self)


        self.generate_label.grid(row=0, column = 0)
        self.generate_button.grid(row=0, column = 2)
        self.generate_entry.grid(row=0, column = 1)
        self.generate_text.grid(row = 0, column = 3)

        self.offset_label.grid(row=1, column = 0)
        self.offset_entry.grid(row=1, column = 1)
        self.offset_button.grid(row = 1, column = 2)
        self.offset_text.grid(row=1, column = 3)


    def gen_button(self, string):

        string = int(string)
        self.pattern = pco.create_pattern(string)
        self.generate_text.delete('1.0', tk.END)
        self.generate_text.insert('1.0', self.pattern)


    def off_button(self, string):

        self.index = pco.find_offset(string)
        self.offset_text.delete('1.0', tk.END)
        self.offset_text.insert('1.0', self.index)


    def validate(self, action, index, value_if_allowed,
                 prior_value, text, validation_type, trigger_type, widget_name):

        if text in '0123456789':
            try:
                return True

            except ValueError:
                return False

        else:
            return False

    def validate_hex(self, action, index, value_if_allowed,
                 prior_value, text, validation_type, trigger_type, widget_name):

        if text in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789':
            try:
                return True

            except ValueError:
                return False

        else:
            return False

app = SampleApp()
app.mainloop()