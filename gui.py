import tkinter as tk
from tkcalendar import Calendar
from autogenerate import  compile_roster, make_table, find_monday_date

def create_gui():
    root = tk.Tk()
    root.title("Kitchen Duty Roster")
    
    date_label = tk.Label(root, text="Select a date:")
    
    root.geometry("400x400")
 
    # Add Calendar
    init_date = find_monday_date()
    cal = Calendar(root, selectmode = 'day',
                   year = init_date.year, month = init_date.month,
                   day = init_date.day)
    
    cal.pack(pady = 20)

    def update_table():
        selected_date = cal._sel_date # as a datetime object
        make_table(selected_date) # update table.tex it needs a datetiem object as input

    get_date_button = tk.Button(root, text="Set Start Date", command= update_table )
    get_date_button.pack()

    compile_button = tk.Button(root, text="Compile", command=compile_roster)
    compile_button.pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()