import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DataExplorer:
    def __init__(self, root):
        self.root = root
        self.root.title("Statistics Data Explorer")
        self.df = None

        button_frame = ttk.Frame(root)
        button_frame.pack(side=tk.TOP, fill=tk.X)

        load_button = ttk.Button(button_frame, text="Load Dataset", command=self.load_dataset)
        load_button.pack(side=tk.LEFT, padx=5, pady=5)

        show_data_button = ttk.Button(button_frame, text="Show Dataset", command=self.show_dataset)
        show_data_button.pack(side=tk.LEFT, padx=5, pady=5)

        stats_button = ttk.Button(button_frame, text="Show Statistics", command=self.show_statistics)
        stats_button.pack(side=tk.LEFT, padx=5, pady=5)

        unique_button = ttk.Button(button_frame, text="Count Unique Values", command=self.count_unique_values)
        unique_button.pack(side=tk.LEFT, padx=5, pady=5)

        histogram_button = ttk.Button(button_frame, text="Show Histogram", command=self.show_histogram)
        histogram_button.pack(side=tk.LEFT, padx=5, pady=5)

        bar_chart_button = ttk.Button(button_frame, text="Show Bar Chart", command=self.show_bar_chart)
        bar_chart_button.pack(side=tk.LEFT, padx=5, pady=5)

        scatter_plot_button = ttk.Button(button_frame, text="Show Scatter Plot", command=self.show_scatter_plot)
        scatter_plot_button.pack(side=tk.LEFT, padx=5, pady=5)

        group_button = ttk.Button(button_frame, text="Group Data", command=self.group_data)
        group_button.pack(side=tk.LEFT, padx=5, pady=5)

        aggregate_button = ttk.Button(button_frame, text="Aggregate Time Series", command=self.aggregate_time_series)
        aggregate_button.pack(side=tk.LEFT, padx=5, pady=5)

        
        output_frame = ttk.Frame(root)
        output_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.output_text = tk.Text(output_frame, wrap=tk.WORD, height=15)
        self.output_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.canvas_frame = ttk.Frame(root)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def load_dataset(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.df = pd.read_csv(file_path)
            messagebox.showinfo("Info", "Dataset loaded successfully!")

    def show_dataset(self):
        if self.df is not None:
            self.output_text.delete('1.0', tk.END)
            self.output_text.insert(tk.END, self.df.head().to_string())
        else:
            messagebox.showerror("Error", "Please load a dataset first!")

    def show_statistics(self):
        if self.df is not None:
            stats = self.df.describe()
            self.output_text.delete('1.0', tk.END)
            self.output_text.insert(tk.END, str(stats))
        else:
            messagebox.showerror("Error", "Please load a dataset first!")

    def count_unique_values(self):
        if self.df is not None:
            column = self.ask_for_column()
            if column:
                unique_count = self.df[column].nunique()
                self.output_text.delete('1.0', tk.END)
                self.output_text.insert(tk.END, f"Unique values in {column}: {unique_count}")
        else:
            messagebox.showerror("Error", "Please load a dataset first!")

    def show_histogram(self):
        if self.df is not None:
            column = self.ask_for_column(numerical=True)
            if column:
                self.clear_canvas()
                fig, ax = plt.subplots(figsize=(6, 4))
                self.df[column].plot(kind='hist', ax=ax)
                ax.set_title(f"Histogram of {column}")
                canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
                canvas.draw()
                canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        else:
            messagebox.showerror("Error", "Please load a dataset first!")

    def show_bar_chart(self):
        if self.df is not None:
            column = self.ask_for_column()
            if column:
                self.clear_canvas()
                fig, ax = plt.subplots(figsize=(6, 4))
                self.df[column].value_counts().plot(kind='bar', ax=ax)
                ax.set_title(f"Bar Chart of {column}")
                canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
                canvas.draw()
                canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        else:
            messagebox.showerror("Error", "Please load a dataset first!")

    def show_scatter_plot(self):
        if self.df is not None:
            column_x = self.ask_for_column("Select X-axis column", numerical=True)
            column_y = self.ask_for_column("Select Y-axis column", numerical=True)
            if column_x and column_y:
                self.clear_canvas()
                fig, ax = plt.subplots(figsize=(6, 4))
                self.df.plot(kind='scatter', x=column_x, y=column_y, ax=ax)
                ax.set_title(f"Scatter Plot of {column_x} vs {column_y}")
                canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
                canvas.draw()
                canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        else:
            messagebox.showerror("Error", "Please load a dataset first.")

    def group_data(self):
        if self.df is not None:
            column = self.ask_for_column()
            if column:
                grouped = self.df.groupby(column).mean()
                self.output_text.delete('1.0', tk.END)
                self.output_text.insert(tk.END, str(grouped))
        else:
            messagebox.showerror("Error", "Please load a dataset first.")

    def aggregate_time_series(self):
        if self.df is not None:
            column = self.ask_for_column(date=True)
            if column:
                self.df[column] = self.df[column].apply(self.clean_date)
                try:
                    self.df[column] = pd.to_datetime(self.df[column], errors='coerce')
                    self.df = self.df.dropna(subset=[column])
                    resampled = self.df.resample('M', on=column).mean()
                    self.output_text.delete('1.0', tk.END)
                    self.output_text.insert(tk.END, str(resampled))
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to parse dates: {e}")
        else:
            messagebox.showerror("Error", "Please load a dataset first.")

    def clean_date(self, date_str):
        try:
            if '-' in date_str and len(date_str.split('-')) == 2:
                return f"{date_str.split('-')[0]}-01-01"
            return date_str
        except Exception as e:
            return None

    def ask_for_column(self, prompt="Select a column", numerical=False, date=False):
        if self.df is not None:
            columns = self.df.select_dtypes(include=['number']).columns if numerical else self.df.columns
            if date:
                columns = self.df.select_dtypes(include=['datetime', 'object']).columns
            column = tk.simpledialog.askstring("Input", f"{prompt}:\nOptions: {', '.join(columns)}")
            if column in columns:
                return column
            else:
                messagebox.showerror("Error", "Invalid column selected.")
        else:
            messagebox.showerror("Error", "Please load a dataset first.")
        return None

    def clear_canvas(self):
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DataExplorer(root)
    root.mainloop()
