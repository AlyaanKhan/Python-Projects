import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_classes():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL")
        return
    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Request Error", f"An error occurred: {e}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    classes = set()
    
    for tag in soup.find_all(True):
        if 'class' in tag.attrs:
            classes.update(tag['class'])
    
    if classes:
        class_listbox.delete(0, tk.END)
        for cls in sorted(classes):
            class_listbox.insert(tk.END, cls)
        messagebox.showinfo("Success", "Classes fetched! Please select a class to scrape its content.")
    else:
        messagebox.showinfo("No Data", "No classes found on the website.")

def scrape_website():
    selected_class = class_listbox.get(tk.ACTIVE)
    url = url_entry.get()
    
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL")
        return
    if not selected_class:
        messagebox.showwarning("Input Error", "Please select a CSS class")
        return
    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Request Error", f"An error occurred: {e}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(class_=selected_class)
    
    data = []
    for element in elements:
        data.append(element.get_text(strip=True))
    
    if data:
        global scraped_data
        scraped_data = pd.DataFrame(data, columns=['Content'])
        messagebox.showinfo("Success", "Scraping complete! You can now export the data.")
    else:
        messagebox.showinfo("No Data", "No content found with the specified class.")

def export_csv():
    if scraped_data is None:
        messagebox.showwarning("Export Error", "No data to export")
        return
    
    file = filedialog.asksaveasfilename(defaultextension='.csv', 
                                        filetypes=[("CSV files", "*.csv")])
    if file:
        scraped_data.to_csv(file, index=False)
        messagebox.showinfo("Export Success", "Data exported successfully as CSV")

def export_excel():
    if scraped_data is None:
        messagebox.showwarning("Export Error", "No data to export")
        return
    
    file = filedialog.asksaveasfilename(defaultextension='.xlsx', 
                                        filetypes=[("Excel files", "*.xlsx")])
    if file:
        scraped_data.to_excel(file, index=False, engine='openpyxl')
        messagebox.showinfo("Export Success", "Data exported successfully as Excel")

root = tk.Tk()
root.title("Web Scraper")
root.geometry("500x600")
root.resizable(False, False)

bg_color = "#f0f4f7"
button_color = "#4CAF50"
button_text_color = "black"
label_color = "#333333"
entry_bg_color = "#FFFFFF"
entry_text_color = "#333333"
listbox_bg_color = "#FFFFFF"
listbox_text_color = "#333333"

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12), background=bg_color, foreground=label_color)
style.configure("TButton", font=("Arial", 12), padding=10)
style.configure("TEntry", font=("Arial", 12), padding=10, fieldbackground=entry_bg_color, foreground=entry_text_color)

main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.pack(fill=tk.BOTH, expand=True)

root.configure(bg=bg_color)

url_label = ttk.Label(main_frame, text="Enter URL:", style="TLabel")
url_label.pack(anchor=tk.W)

url_entry = ttk.Entry(main_frame, width=50, style="TEntry")
url_entry.pack(fill=tk.X, pady=5)

fetch_classes_button = ttk.Button(main_frame, text="Fetch Classes", command=fetch_classes)
fetch_classes_button.pack(pady=10)

class_label = ttk.Label(main_frame, text="Select CSS Class:", style="TLabel")
class_label.pack(anchor=tk.W)

class_listbox = tk.Listbox(main_frame, width=50, height=10, bg=listbox_bg_color, fg=listbox_text_color)
class_listbox.pack(fill=tk.BOTH, pady=5)

scrape_button = ttk.Button(main_frame, text="Scrape", command=scrape_website)
scrape_button.pack(pady=10)

export_frame = ttk.Frame(main_frame, padding="10 10 10 10")
export_frame.pack(fill=tk.BOTH, expand=True)

export_csv_button = tk.Button(export_frame, text="Export as CSV", command=export_csv, bg=button_color, fg=button_text_color, font=("Arial", 12))
export_csv_button.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.X)

export_excel_button = tk.Button(export_frame, text="Export as Excel", command=export_excel, bg=button_color, fg=button_text_color, font=("Arial", 12))
export_excel_button.pack(side=tk.RIGHT, padx=10, pady=10, expand=True, fill=tk.X)

scraped_data = None

root.mainloop()
