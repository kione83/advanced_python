import openpyxl as xl

wb = xl.load_workbook('schedule.xlsx')
sheet = wb['Sheet1']

sheet['A1'] = 'Monday'
sheet['C1'] = 'Tuesday'
sheet['E1'] = 'Wednesday'
sheet['G1'] = 'Thursday'
sheet['I1'] = 'Friday'

sheet['B1'] = 'Notes of the day'
sheet['D1'] = 'Notes of the day'
sheet['F1'] = 'Notes of the day'
sheet['H1'] = 'Notes of the day'
sheet['J1'] = 'Notes of the day'

wb.save('schedule.xlsx')