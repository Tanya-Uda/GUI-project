import tkinter as tk
from tkinter import messagebox

class RadiobuttonDemo(tk.Tk):
    """Allows the user to place a book order from a set of options"""
    
    def __init__(self):
        """Sets up the window and widgets"""
        super().__init__()
        self.title("BookDemo")
        
        # Labels
        self.label = tk.Label(self, text="Choose the book option")
        self.label.grid(row=0, column=0)  
        
        # Radiobutton group
        self.book_var = tk.StringVar(value="Just the book")  # Default option
        
        self.rb1 = tk.Radiobutton(self, text="Just the book", variable=self.book_var, value="Just the book")
        self.rb1.grid(row=1, column=0)          
        self.rb2 = tk.Radiobutton(self, text="Full package", variable=self.book_var, value="Full package")
        self.rb2.grid(row=2, column=0)          
        
        # Add the "Next" button
        self.next_button = tk.Button(self, text="Next", command=self.placeOrder)
        self.next_button.grid(row=3, column=0, columnspan=2)
        
        # Creating the total price option
        self.total_price = 0.0

    def placeOrder(self):
        selected_option = self.book_var.get()

        if selected_option == "Just the book":
            self.showBookOptions()
        elif selected_option == "Full package":
            self.showPackageOptions()

    def showBookOptions(self):
        """Show more options for books"""
        self.label.config(text="Choose your perfect book:")

        self.formst_prices = {
            "hardcover": 15.00,
            "paperback": 10.00,
        }
        self.package_prices = {
            "kraft": 5.00,
            "metallic": 5.00
        }
        
        # Reset previous widgets
        self.clear_widgets()

        # Book options
        self.book_var = tk.StringVar(value="paperback")
        
        self.book_label = tk.Label(self, text="Book")
        self.book_label.grid(row=0, column=0)
        
        self.rb1 = tk.Radiobutton(self, text="Paperback(10.00)", variable=self.book_var, value="paperback")
        self.rb1.grid(row=1, column=0)
        self.rb2 = tk.Radiobutton(self, text="Hardcover(15.00)", variable=self.book_var, value="hardcover")
        self.rb2.grid(row=2, column=0)
        
        # Genre options
        self.genre_var = tk.StringVar(value="romance")

        self.genre_label = tk.Label(self, text="Genre")
        self.genre_label.grid(row=0, column=1)
        
        self.rb1 = tk.Radiobutton(self, text="Romance", variable=self.genre_var, value="Romance")
        self.rb1.grid(row=1, column=1)
        self.rb2 = tk.Radiobutton(self, text="Fantasy", variable=self.genre_var, value="Fantasy")
        self.rb2.grid(row=2, column=1)
        self.rb3 = tk.Radiobutton(self, text="Fiction", variable=self.genre_var, value="Fiction")
        self.rb3.grid(row=3, column=1)
        self.rb4 = tk.Radiobutton(self, text="Detective", variable=self.genre_var, value="Detective")
        self.rb4.grid(row=4, column=1)
        self.rb5 = tk.Radiobutton(self, text="Horror", variable=self.genre_var, value="Horror")
        self.rb5.grid(row=5, column=1)
        
        # Paper options
        self.paper_var = tk.StringVar(value="paper")

        self.paper_label = tk.Label(self, text="Wrap paper")
        self.paper_label.grid(row=0, column=2)
        
        self.rb1 = tk.Radiobutton(self, text="Paper", variable=self.paper_var, value="paper")
        self.rb1.grid(row=1, column=2)
        self.rb2 = tk.Radiobutton(self, text="Kraft(5.00)", variable=self.paper_var, value="kraft")
        self.rb2.grid(row=2, column=2)
        self.rb3 = tk.Radiobutton(self, text="Metallic(5.00)", variable=self.paper_var, value="metallic")
        self.rb3.grid(row=3, column=2)

        self.confirm_button = tk.Button(self, text="Confirm Order", command=self.confirmOrder)
        self.confirm_button.grid(row=6, column=0, columnspan=2)

    def showPackageOptions(self):
        """Show options for a full package."""
        self.label.config(text="Choose your perfect package:")
        
        self.package_prices = {
            "hardcover": 15.00,
            "paperback": 10.00,
            "metal mark": 2.50,
            "magnetic": 5.00,
            "gel pen": 1.00,
            "stylus pen": 3.50,
            "fountain pen": 7.50,
            "vinyl stickers": 3.00,
            "holographic": 4.00,
            "clear": 3.50,
            "kraft": 5.00,
            "metallic": 5.00
        }

        # Reset previous widgets
        self.clear_widgets()

        # Book options
        self.book_var = tk.StringVar(value="paperback")
        
        self.book_label = tk.Label(self, text="Book")
        self.book_label.grid(row=0, column=0)
        
        self.rb1 = tk.Radiobutton(self, text="Paperback(10.00)", variable=self.book_var, value="paperback")
        self.rb1.grid(row=1, column=0)
        self.rb2 = tk.Radiobutton(self, text="Hardcover(15.00)", variable=self.book_var, value="hardcover")
        self.rb2.grid(row=2, column=0)

        self.genre_var = tk.StringVar(value="romance")

        self.genre_label = tk.Label(self, text="Genre")
        self.genre_label.grid(row=0, column=1)
        
        self.rb1 = tk.Radiobutton(self, text="Romance", variable=self.genre_var, value="Romance")
        self.rb1.grid(row=1, column=1)
        self.rb2 = tk.Radiobutton(self, text="Fantasy", variable=self.genre_var, value="Fantasy")
        self.rb2.grid(row=2, column=1)
        self.rb2 = tk.Radiobutton(self, text="Detective", variable=self.genre_var, value="Fantasy")
        self.rb2.grid(row=3, column=1)
        self.rb2 = tk.Radiobutton(self, text="Horror", variable=self.genre_var, value="Fantasy")
        self.rb2.grid(row=4, column=1)
        self.rb2 = tk.Radiobutton(self, text="Fiction", variable=self.genre_var, value="Fantasy")
        self.rb2.grid(row=5, column=1)

        # Pen options
        self.pen_var = tk.StringVar(value="ballpoint pen")

        self.pen_label = tk.Label(self, text="Pen")
        self.pen_label.grid(row=0, column=2)
        
        self.rb1 = tk.Radiobutton(self, text="Ballpoint pen", variable=self.pen_var, value="ballpoint")
        self.rb1.grid(row=1, column=2)
        self.rb2 = tk.Radiobutton(self, text="Gel pen(1.00)", variable=self.pen_var, value="gel pen")
        self.rb2.grid(row=2, column=2)
        
        self.sticker_var = tk.StringVar(value="paperstick")

        self.sticker_label = tk.Label(self, text="Stickers")
        self.sticker_label.grid(row=0, column=3)
        
        self.rb1 = tk.Radiobutton(self, text="Paper stickers", variable=self.sticker_var, value="paperstick")
        self.rb1.grid(row=1, column=3)
        self.rb2 = tk.Radiobutton(self, text="Vinyl stickers(3.00)", variable=self.sticker_var, value="vinyl stickers")
        self.rb2.grid(row=2, column=3)

        self.confirm_button = tk.Button(self, text="Confirm Order", command=self.confirmOrder)
        self.confirm_button.grid(row=6, column=0, columnspan=2)

    def clear_widgets(self):
        """Clear the previous options/widgets."""
        for widget in self.winfo_children():
            widget.grid_forget()

    def confirmOrder(self):
        """Display the final confirmation with the total price on the app"""
        selected_book = self.book_var.get()
        selected_genre = self.genre_var.get()
        selected_paper = self.paper_var.get()
        selected_pen = self.pen_var.get()
        selected_sticker = self.sticker_var.get()
        
        
        self.total_price = 0.0
        selected_items = []

        #Show what was selected after the price 
        if selected_book in self.formst_prices:
            self.total_price += self.formst_prices[selected_book]
            selected_items.append(f"Book: {selected_book} (${self.formst_prices[selected_book]:.2f})")
        if selected_genre:
            selected_items.append(f"Genre: {selected_genre}")
        if selected_paper in self.package_prices:
            self.total_price += self.package_prices[selected_paper]
            selected_items.append(f"Paper: {selected_paper} (${self.package_prices[selected_paper]:.2f})")
        if selected_pen in self.package_prices:
            self.total_price += self.package_prices[selected_pen]
            selected_item.append(f"Pen: {selected_pen} (${self.package_prices[selected_pen]:.2f})")
        if selected_sticker in self.package_prices:
            self.total_price += self.package_prices[selected_sticker]
            selected_item.append(f"Stickers: {selected_sticker} (${self.package_prices[selected_sticker]:.2f})")
        
        
        # Update the total price label with the final total

        self.total_price_label = tk.Label(self, text=f"Total Price: ${self.total_price:.2f}")
        self.total_price_label.grid(row=7, column=0, columnspan=2)
        
        # Show the user's selected items under the total price
        
        selected_items_text = "\n".join(selected_items)
        self.selected_items_label = tk.Label(self, text="You selected:\n" + selected_items_text)
        self.selected_items_label.grid(row=8, column=0, columnspan=2)
    
        # Show confirmation message
        self.confirmation_label = tk.Label(self, text=f"Your order has been confirmed! Total Price: ${self.total_price:.2f}")
        self.confirmation_label.grid(row=9, column=0, columnspan=2)

        # Disable further input and show quit button
        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.grid(row=10, column=0, columnspan=2)
        
        # Display confirmation message box
        messagebox.showinfo("Confirmation", f"Your order has been confirmed!\nTotal price: ${self.total_price:.2f}")
        
    def quit(self):
        """Method to close the application"""
        self.destroy()


if __name__ == "__main__":
    app = RadiobuttonDemo()
    app.mainloop()
