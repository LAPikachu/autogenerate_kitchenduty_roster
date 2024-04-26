#!/usr/bin/env python
# coding: utf-8
import os
import datetime

def find_monday_date(start_day=datetime.date.today()):
    start_day = datetime.date.today()
    #let's find next mondays date; weekday returns 0 for Mon, 1 for Tue, ... etc. 
    start_day = start_day + datetime.timedelta(days=(7 - start_day.weekday())) 
    return start_day  

def make_table(monday_first_week_date = find_monday_date(),
               current_week = 1, max_weeks = 13):
    with open("table.tex", "w") as f:
        f.write('\\begin{table} [htb]\n\\centering\n\\begin{tabular}{p{10cm}c r} \\\\\n')
        monday = monday_first_week_date
        sunday = monday_first_week_date + datetime.timedelta(days=6)
    #     f.write('\\hline\n10 & 11\\\\')
        while current_week <= max_weeks:

            f.write('\\hline \\\\ \n ')
            f.write('{start} - {end}'.format(start=monday.strftime('%d/%m/%Y'), end=sunday.strftime('%d/%m/%Y')))
            f.write('\\\\ \n')
            current_week += 1
            monday = monday + datetime.timedelta(days=7)
            sunday = sunday + datetime.timedelta(days=7)
        f.write('\n\\end{tabular}\n\\end{table}\n')

def main():
    find_monday_date()
    make_table()
    os.system('pdflatex kitchen_duty_roster.tex')
    os.system('pdflatex Küchendienstplan.tex')
if __name__=='__main__':
    main()






