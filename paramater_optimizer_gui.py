import time
import tkinter as tk
from tkinter import ttk
import main as optimizer
from selenium.common.exceptions import NoSuchWindowException, WebDriverException

root = tk.Tk()
root.title("TRADINGVIEW OTT OPTIMIZER")

canvas = tk.Canvas(root, width=400, height=250, relief='raised')
canvas.pack()

# box label create
shareName_Label = tk.Label(root, text="Stock")
shareName_Label.config(font=('helvetica', 10))
canvas.create_window(100, 25, window=shareName_Label)

shareName_Label_2 = tk.Label(root, text="Stock-2")
shareName_Label_2.config(font=('helvetica', 10))
canvas.create_window(100, 50, window=shareName_Label_2)

shareName_Label_3 = tk.Label(root, text="Stock-3")
shareName_Label_3.config(font=('helvetica', 10))
canvas.create_window(100, 75, window=shareName_Label_3)

periodStart_Label = tk.Label(root, text="Period Start")
periodStart_Label.config(font=('helvetica', 10))
canvas.create_window(100, 110, window=periodStart_Label)

periodEnd_Label = tk.Label(root, text="Period End")
periodEnd_Label.config(font=('helvetica', 10))
canvas.create_window(100, 135, window=periodEnd_Label)

percent_Label = tk.Label(root, text="Percent")
percent_Label.config(font=('helvetica', 10))
canvas.create_window(100, 170, window=percent_Label)


# entry box create
entry_share_name = ttk.Entry(root)
entry_share_name.insert(0, "KRDMD")
canvas.create_window(250, 25, window=entry_share_name)

entry_share_name_2 = ttk.Entry(root)
entry_share_name_2.insert(0, "")
canvas.create_window(250, 50, window=entry_share_name_2)

entry_share_name_3 = ttk.Entry(root)
entry_share_name_3.insert(0, "")
canvas.create_window(250, 75, window=entry_share_name_3)

entry_period_first = tk.Entry(root)
entry_period_first.insert(0, 1)
canvas.create_window(250, 110, window=entry_period_first)

entry_period_last = tk.Entry(root)
entry_period_last.insert(0, 60)
canvas.create_window(250, 135, window=entry_period_last)

entry_percent = tk.Entry(root)
entry_percent.insert(0, 4.0)
canvas.create_window(250, 170, window=entry_percent)


def gui():
    while True:
        try:
            share = entry_share_name.get()
            share_2 = entry_share_name_2.get()
            share_3 = entry_share_name_3.get()
            period_first = entry_period_first.get()
            period_last = entry_period_last.get()
            percent = entry_percent.get()

            # search 1 stock
            if share_2 == "":
                if share_3 == "":
                    optimizer.main(
                        share=share,
                        period_first=int(period_first),
                        period_last=int(period_last),
                        percent=float(percent)
                                   )
            # search 2 stock
            if share_2 != "":
                if share_3 == "":
                    optimizer.main(
                        share=share,
                        period_first=int(period_first),
                        period_last=int(period_last),
                        percent=float(percent)
                                   )

                    time.sleep(15)

                    optimizer.main(
                        share=share_2,
                        period_first=int(period_first),
                        period_last=int(period_last),
                        percent=float(percent)
                                   )
            # search 3 stock
            if share_2 != "":
                if share_3 != "":
                    optimizer.main(
                        share=share,
                        period_first=int(period_first),
                        period_last=int(period_last),
                        percent=float(percent)
                                   )
                    time.sleep(15)

                    optimizer.main(
                        share=share_2,
                        period_first=int(period_first),
                        period_last=int(period_last),
                        percent=float(percent)
                                   )
                    time.sleep(15)

                    optimizer.main(
                        share=share_3,
                        period_first=int(period_first),
                        period_last=int(period_last),
                        percent=float(percent)
                                   )

        except NoSuchWindowException:
            pass

        except WebDriverException:
            pass

        break


button = tk.Button(text='SCAN', command=gui, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas.create_window(250, 210, window=button)

root.mainloop()

