import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

class BookOrderApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Blind date with a Book")

        #Shows the picture it the main window
        icon = PhotoImage(file="books.png")
        self.iconphoto(False, icon)
        

        # Color for background
        self.configure(bg="#acd0f2")
        
        # Variables to track user selection
        self.selected_book = ""
        self.selected_pen = ""
        self.selected_paper = ""
        self.selected_mark = ""
        self.selected_comment = ""
        self.total_price = 0.0
        self.user_name = ""

        # Create frames for each window
        self.frame1 = tk.Frame(self, bg="#acd0f2")
        self.frame2 = tk.Frame(self, bg="#acd0f2")
        self.frame3 = tk.Frame(self, bg="#acd0f2")
        self.frame4 = tk.Frame(self, bg="#acd0f2")
        
        self.show_frame1()

        
    #Clean frame from old widgets before showing the new ones
    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def show_frame1(self):
        """First window where user inputs their name"""
        self.clear_frame(self.frame2)
        self.clear_frame(self.frame3)
        self.clear_frame(self.frame4)

        self.frame1.grid(row=0, column=0, padx=20, pady=20)

        # Labels for Frame 1
        label1 = tk.Label(self.frame1, text="We are glad to see you!", bg="#acd0f2")
        label1.grid(row=1, column=0, columnspan=2)

        label2 = tk.Label(self.frame1, text="Here you can find your perfect Blind date with a book!", bg="#acd0f2")
        label2.grid(row=2, column=0, columnspan=2)

        label3 = tk.Label(self.frame1, text="Please enter a name, who you make this order for:", bg="#acd0f2")
        label3.grid(row=3, column=0, columnspan=2)

        # Display an image in the first window
        try:
            self.image = tk.PhotoImage(file="bookdate.png")  # Replace with your image path
            self.image_label = tk.Label(self.frame1, image=self.image)
            self.image_label.grid(row=0, column=0, columnspan=2)
        except tk.TclError:
            print("Image file not found. Please check the image path.")

        # Entry for User Name
        self.name_entry = tk.Entry(self.frame1, font=("Arial", 12))
        self.name_entry.grid(row=4, column=0, columnspan=2)

        # Buttons
        self.about_button = tk.Button(self.frame1, text="About Us", command=self.about_us, bg="#e2c3f7", fg="#003366", font=("Arial", 12))
        self.about_button.grid(row=5, column=0, padx=10, pady=10, sticky="ew")
        
        self.next_button = tk.Button(self.frame1, text="Next", command=self.on_next_from_frame1, bg="#e2c3f7", fg="#003366", font=("Arial", 12))
        self.next_button.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

        self.quit_button = tk.Button(self.frame1, text="Quit", command=self.quit, bg="#e2c3f7", fg="#003366", font=("Arial", 12))
        self.quit_button.grid(row=5, column=2,padx=10, pady=10, sticky="ew")

    def about_us(self):
            messagebox.showinfo("Blind Date with a Book", "We are giving a unique opportunity to people\n to read the book they would never buy in store.\n Our goal is to create a positive experience for\n our customers, and it can be a great gift for your\n friends! Choose your package and enter your comments\n about what you want to see in the package!")

    def on_next_from_frame1(self):
        """Callback for the next button on the first window"""
        self.user_name = self.name_entry.get()
        if not self.user_name:
            messagebox.showerror("Error", "Name cannot be empty!")
            return
        self.show_frame2()

    def show_frame2(self):
        """Second window for selecting the book"""
        self.clear_frame(self.frame1)
        self.clear_frame(self.frame3)
        self.clear_frame(self.frame4)

        self.frame2.grid(row=0, column=0, padx=20, pady=20)

        # Labels for Frame 2
        label1 = tk.Label(self.frame2, text="Select a book type below!", bg="#acd0f2", fg="#003366", font=("Arial", 12))
        label1.grid(row=1, column=0, columnspan=2)

        # Display the book picture 
        try:
            self.book_image = tk.PhotoImage(file="book.png")  # Add an image here
            self.book_label = tk.Label(self.frame2, image=self.book_image)
            self.book_label.grid(row=0, column=0, columnspan=2)
        except tk.TclError:
            print("Image file not found. Please check the image path.")

        # Radiobuttons
        self.book_var = tk.StringVar(value="paperback")
        
        self.rb1 = tk.Radiobutton(self.frame2, text="Paperback(10.00)", variable=self.book_var, value="paperback", bg="#acd0f2")
        self.rb1.grid(row=2, column=0,columnspan=2)
        self.rb2 = tk.Radiobutton(self.frame2, text="Hardcover(15.00)", variable=self.book_var, value="hardcover", bg="#acd0f2")
        self.rb2.grid(row=3, column=0, columnspan=2)

        # Buttons
        self.back_button = tk.Button(self.frame2, text="Back", command=self.on_back_from_frame2, bg="#e2c3f7", fg="#003366", font=("Arial", 12))
        self.back_button.grid(row=4, column=0, columnspan=1)

        self.next_button = tk.Button(self.frame2, text="Next", command=self.on_next_from_frame2, bg="#e2c3f7", fg="#003366", font=("Arial", 12))
        self.next_button.grid(row=4, column=1,columnspan=1)

    def on_back_from_frame2(self):
        """Callback for the back button on the second window"""
        self.clear_frame(self.frame2)
        self.show_frame1()

    def on_next_from_frame2(self):
        """Callback for the next button on the second window"""
        if self.book_var.get() == "paperback":
            self.total_price += 10.00
        else:
            self.total_price += 15.00
        self.show_frame3()

    def show_frame3(self):
        """Third window for selecting other items"""
        self.clear_frame(self.frame1)
        self.clear_frame(self.frame2)
        self.clear_frame(self.frame4)

        self.frame3.grid(row=0, column=0, padx=20, pady=20)

        # Labels for Frame 3
        label1 = tk.Label(self.frame3, text="Please, select items for your package:", bg="#acd0f2", fg="#003366", font=("Arial", 14))
        label1.grid(row=1, column=0, columnspan=2)

        # Pen selection (Radiobuttons)
        self.pen_var = tk.StringVar(value="ballpoint")

        label2 = tk.Label(self.frame3, text="Select a pen", bg="#acd0f2", fg="#003366", font=("Arial", 12))
        label2.grid(row=2, column=0, columnspan=2)
        
        self.rb1 = tk.Radiobutton(self.frame3, text="Ballpoint pen", variable=self.pen_var, value="ballpoint", bg="#acd0f2")
        self.rb1.grid(row=3, column=0)
        self.rb2 = tk.Radiobutton(self.frame3, text="Gel pen (3.00)", variable=self.pen_var, value="gel", bg="#acd0f2")
        self.rb2.grid(row=3, column=1)

        # Bookmark selection (Radiobuttons)
        self.mark_var = tk.StringVar(value="paper")

        label3 = tk.Label(self.frame3, text="Select a bookmark", bg="#acd0f2", fg="#003366", font=("Arial", 12))
        label3.grid(row=4, column=0, columnspan=2)
        
        self.rb1 = tk.Radiobutton(self.frame3, text="Paper", variable=self.mark_var, value="paper", bg="#acd0f2")
        self.rb1.grid(row=5, column=0)
        self.rb2 = tk.Radiobutton(self.frame3, text="Magnetic (5.00)", variable=self.mark_var, value="magnetic", bg="#acd0f2")
        self.rb2.grid(row=5, column=1)

        # Wrap paper selection (Radiobuttons)
        self.paper_var = tk.StringVar(value="wrap")

        label4 = tk.Label(self.frame3, text="Select a wrap paper", bg="#acd0f2", fg="#003366", font=("Arial", 12))
        label4.grid(row=6, column=0, columnspan=2)
        
        self.rb1 = tk.Radiobutton(self.frame3, text="Regular wrap", variable=self.paper_var, value="wrap", bg="#acd0f2")
        self.rb1.grid(row=7, column=0)
        self.rb2 = tk.Radiobutton(self.frame3, text="Kraft (5.00)", variable=self.paper_var, value="kraft", bg="#acd0f2")
        self.rb2.grid(row=7, column=1)

        # Buttons
        self.back_button = tk.Button(self.frame3, text="Back", command=self.on_back_from_frame3, bg="#e2c3f7", fg="#003366", font=("Arial", 12))
        self.back_button.grid(row=10, column=0)

        self.next_button = tk.Button(self.frame3, text="Next", command=self.on_next_from_frame3, bg="#e2c3f7", fg="#003366", font=("Arial", 12))
        self.next_button.grid(row=10, column=1)

    def on_back_from_frame3(self):
        """Callback for the back button on the third window"""
        self.clear_frame(self.frame3)
        self.show_frame2()

    def on_next_from_frame3(self):
        # Add the selected pen, bookmark, and paper prices to total
        if self.pen_var.get() == "gel":
            self.total_price += 3.00
        else:
            self.total_price += 0.00

        if self.mark_var.get() == "magnetic":
            self.total_price += 5.00
        else:
            self.total_price += 0.00

        if self.paper_var.get() == "kraft":
            self.total_price += 5.00
        else:
            self.total_price += 0.00

        self.show_frame4()

    def show_frame4(self):
        """Fourth window for adding comments and confirming the order"""
        self.clear_frame(self.frame1)
        self.clear_frame(self.frame2)
        self.clear_frame(self.frame3)

        self.frame4.grid(row=0, column=0, padx=20, pady=20)

        # Labels for Frame 4
        label1 = tk.Label(self.frame4, text="Review Your Selection!", bg="#acd0f2", fg="#003366", font=("Arial", 12))
        label1.grid(row=0, column=0, columnspan=2)

        # Display selected items and prices
        label_book = tk.Label(self.frame4, text=f"Book: {self.selected_book}", bg="#acd0f2", fg="#003366", font=("Arial", 12))
        label_book.grid(row=1, column=0, columnspan=2)

        label_pen = tk.Label(self.frame4, text=f"Pen: {self.pen_var.get()}", bg="#acd0f2", fg="#003366", font=("Arial", 12))
        label_pen.grid(row=2, column=0, columnspan=2)

        label_mark = tk.Label(self.frame4, text=f"Bookmark: {self.mark_var.get()}", bg="#acd0f2", fg="#003366", font=("Arial", 12))
        label_mark.grid(row=3, column=0, columnspan=2)

        label_paper = tk.Label(self.frame4, text=f"Wrapping paper: {self.paper_var.get()}", bg="#acd0f2", fg="#003366", font=("Arial", 12))
        label_paper.grid(row=4, column=0, columnspan=2)

        label_total = tk.Label(self.frame4, text=f"Total Price: ${self.total_price:.2f}", bg="#acd0f2", fg="#003366", font=("Arial", 12))
        label_total.grid(row=5, column=0, columnspan=2)

        # Comment input box
        comment_label = tk.Label(self.frame4, text="Please enter your wishes for the package: book genre, package color, etc", bg="#acd0f2", fg="#003366", font=("Arial", 12))
        comment_label.grid(row=6, column=0, columnspan=2)
        
        self.comment_box = tk.Text(self.frame4, height=4, width=40, font=("Arial", 12))
        self.comment_box.grid(row=7, column=0, columnspan=2)

        # Buttons

        self.back_button = tk.Button(self.frame4, text="Back", command=self.on_back_from_frame4, bg="#e2c3f7", fg="#003366", font=("Arial", 12))
        self.back_button.grid(row=8, column=0,  padx=10, pady=10, sticky="ew")
        
        self.confirm_button = tk.Button(self.frame4, text="Confirm", command=self.on_confirm, bg="#e2c3f7", fg="#003366", font=("Arial", 12))
        self.confirm_button.grid(row=8, column=1, padx=10, pady=10, sticky="ew")
                                     
        self.quit_button = tk.Button(self.frame4, text="Quit", command=self.quit, bg="#e2c3f7", fg="#003366", font=("Arial", 12))
        self.quit_button.grid(row=8, column=2,  padx=10, pady=10, sticky="ew")

    def on_back_from_frame4(self):
        """Callback for the back button on the third window"""
        self.clear_frame(self.frame4)
        self.show_frame3()

    def on_confirm(self):
        """Final confirmation"""
        self.selected_comment = self.comment_box.get("1.0", tk.END).strip()
        # Show final summary
        summary = f"Thank you for ordering this book for {self.user_name}!\n They will have amazing Blind Date with a Book!\n Your package contains:\n {self.book_var.get()} book\n {self.pen_var.get()} pen\n {self.mark_var.get()} bookmark\n {self.paper_var.get()} paper\n Your wishes: {self.selected_comment} \n Your total price: ${self.total_price:.2f}"
        messagebox.showinfo("Order Confirmation", summary)
        self.quit()

        
    def show_frame5(self):
        self.clear_frame(self.frame5)
        self.frame5.grid(row=0, column=0, padx=20, pady=20)

        label = tk.Label(self.frame5, text="Your order has been completed successfully!", font=("Arial", 12))
        label.grid(row=0, column=0)

        self.quit_button = tk.Button(self.frame5, text="Quit", command=self.root.quit, font=("Arial", 12))
        self.quit_button.grid(row=1, column=0, pady=10)

        self.selected_comment = self.comment_box.get("1.0", tk.END).strip()
        # Show final summary
        summary = f"Thank you for your order, {self.user_name}!\nTotal price: ${self.total_price:.2f}\nComments: {self.selected_comment}"
        messagebox.showinfo("Order Confirmation", summary)
        self.quit()

    def quit(self):
        """Method to close the application"""
        self.destroy()

if __name__ == "__main__":
    app = BookOrderApp()
    app.mainloop()
