# 
# Desctiption: Takes inputs relating to a group of Wordpress products and makes csv file for bulk product uploading
# Author: Alexander Powell
# Version: v2.0
# Dependencies: See "requirements.py" file
#


import customtkinter as ctk
from tkinter import filedialog, messagebox
from openpyxl import Workbook
import os
import csv


# Initialize CustomTkinter
ctk.set_appearance_mode("Dark")  # Options: "Dark", "Light"
ctk.set_default_color_theme("blue")  # Default theme


# Define functions
def excel_exporter():
    try:
        def leading_zeros(num):
            return f"{num:03}"  # Ensure numbers are padded to three digits

        # Creating the workbook
        wb = Workbook()
        ws = wb.active
        headings = ['Name', 'Images', 'Regular Price', 'Type', 'Categories', 'Download URL']
        ws.append(headings)

        # User inputs
        photo_num = int(photo_num_inp.get())
        amount = int(amount_num_inp.get())
        amount += photo_num

        original_name = str(photo_name_inp.get())
        original_link = str(link_inp.get())
        price = float(price_inp.get() or 14.99)
        types = str(type_inp.get() or 'Virtual, Downloadable')
        cat = str(cat_inp.get() or "Unknown")

        first_iter = True
        while photo_num < amount:
            current_num = leading_zeros(photo_num)
            current_name = original_name if first_iter else original_name.replace(original_name[-3:], current_num)
            current_link = f"{original_link}/{current_name}"

            ws.append([current_name, current_link, price, types, cat, current_link])
            first_iter = False
            photo_num += 1

        file_name = original_name.replace(original_name[-3:], '')  # Base file name
        dir_name = filedialog.askdirectory()
        os.chdir(dir_name)

        # Save as CSV
        with open(f'{dir_name}/{file_name}.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for row in ws.iter_rows(values_only=True):
                writer.writerow(row)

        messagebox.showinfo("Export Complete", "CSV file has been successfully exported.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please check your entries.")


def quit_program():
    root.destroy()


def clear_form():
    for entry in [photo_num_inp, amount_num_inp, photo_name_inp, link_inp, price_inp, type_inp, cat_inp]:
        entry.delete(0, "end")


# UI
root = ctk.CTk()
root.title("BulkifyWP")
root.geometry("800X800")
root.resizable(False, False)

# Header
header_label = ctk.CTkLabel(root, text="WordPress Bulk Product Automator", font=("Arial", 20, "bold"))
header_label.pack(pady=10)

# Input Frame
input_frame = ctk.CTkFrame(root, corner_radius=10)
input_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Input Fields
fields = [
    ("Number of the first photo:", lambda: messagebox.showinfo("Hint", "Enter the number of the photo without leading zeros.")),
    ("Total number of photos:", lambda: messagebox.showinfo("Hint", "Enter the total number of photos to create.")),
    ("Photo name:", lambda: messagebox.showinfo("Hint", "Enter the name of the first photo (e.g., MESoftballVSVHS0001).")),
    ("Photo link:", lambda: messagebox.showinfo("Hint", "Enter the URL of the photo location.")),
    ("Regular Price:", lambda: messagebox.showinfo("Hint", "Enter the price. Defaults to $14.99 if left blank.")),
    ("Type:", lambda: messagebox.showinfo("Hint", "Enter the product types (e.g., Virtual, Downloadable).")),
    ("Categories:", lambda: messagebox.showinfo("Hint", "Enter the product categories."))
]

inputs = []
for text, hint_function in fields:
    label = ctk.CTkLabel(input_frame, text=text)
    label.pack(anchor="w", padx=10, pady=5)
    frame = ctk.CTkFrame(input_frame, fg_color="transparent")
    frame.pack(fill="x", padx=10)
    entry = ctk.CTkEntry(frame, width=400)
    entry.pack(side="left", padx=5)
    inputs.append(entry)
    hint_button = ctk.CTkButton(frame, text="?", width=30, command=hint_function)
    hint_button.pack(side="left")

# Map inputs to variables
photo_num_inp, amount_num_inp, photo_name_inp, link_inp, price_inp, type_inp, cat_inp = inputs

# Buttons
button_frame = ctk.CTkFrame(root, corner_radius=10)
button_frame.pack(pady=20)

export_button = ctk.CTkButton(button_frame, text="Export to CSV", command=excel_exporter)
export_button.grid(row=0, column=0, padx=10, pady=10)

clear_button = ctk.CTkButton(button_frame, text="Clear Form", command=clear_form)
clear_button.grid(row=0, column=1, padx=10, pady=10)

quit_button = ctk.CTkButton(button_frame, text="Quit", command=quit_program)
quit_button.grid(row=0, column=2, padx=10, pady=10)

# Run the application
root.mainloop()
