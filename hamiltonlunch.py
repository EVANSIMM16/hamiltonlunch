
import tkinter as tk
from tkinter import messagebox

class HamiltonLunchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hamilton Lunch")

        self.student_name_var = tk.StringVar()
        self.order_var = tk.StringVar()


        self.drink_var = tk.StringVar()
        self.entree_var = tk.StringVar()
        self.side_var = tk.StringVar()
        self.fruit_var = tk.StringVar()
        self.extra_var = tk.StringVar()

 
        self.payment_var = tk.StringVar()

        self.create_main_window()

    def create_main_window(self):
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack()

        tk.Label(main_frame, text="Welcome to Hamilton Lunch", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(main_frame, text="Student Name and Lunch Period:").grid(row=1, column=0, pady=5, sticky=tk.W)
        tk.Entry(main_frame, textvariable=self.student_name_var).grid(row=1, column=1, pady=5)

 
        self.create_menu_dropdown(main_frame, "Select your drink:", self.drink_var, ["Chocolate Milk", "Strawberry Milk", "2% Milk", "Apple Juice", "Cranberry Juice", "Water"])
        self.create_menu_dropdown(main_frame, "Select your entree:", self.entree_var, ["Taco Triangles", "Country Baked Steak", "Cheese Pizza", "Sausage Pizza", "Pepperoni Pizza", "Chicken Sandwich"])
        self.create_menu_dropdown(main_frame, "Select your side:", self.side_var, ["Green Beans", "Carrots", "Baked Potato", "Salad", "French Fries", "Corn"])
        self.create_menu_dropdown(main_frame, "Select your fruit:", self.fruit_var, ["Green Apple", "Red Apple", "Orange", "Banana", "Bundle of Grapes"])
        self.create_menu_dropdown(main_frame, "Select your extra:", self.extra_var, ["Lays Chips (Original)", "Lays Chips (Sour Cream)", "Cheetos", "Doritos (Nacho Cheese)", "Rice Krispy Treat", "Raisins", "Cookie", "Coke Zero", "Fanta Zero", "Mello Yello Zero"])

 
        payment_options = ["Discover", "Apple Pay", "Mastercard", "Venmo", "PayPal", "Visa", "American Express"]
        self.create_menu_dropdown(main_frame, "Select your payment method:", self.payment_var, payment_options)

        tk.Button(main_frame, text="Order Lunch", command=self.order_lunch).grid(row=7, column=0, pady=10)
        tk.Button(main_frame, text="View Menu", command=self.view_menu).grid(row=7, column=1, pady=10)
        tk.Button(main_frame, text="Exit", command=self.root.destroy).grid(row=8, column=0, columnspan=2, pady=10)

    def create_menu_dropdown(self, frame, label_text, variable, options):
        tk.Label(frame, text=label_text).grid(sticky=tk.W)
        tk.OptionMenu(frame, variable, *options).grid(sticky=tk.W)

    def order_lunch(self):
        student_name = self.student_name_var.get()
        drink = self.drink_var.get()
        entree = self.entree_var.get()
        side = self.side_var.get()
        fruit = self.fruit_var.get()
        extra = self.extra_var.get()
        payment_method = self.payment_var.get()

 
        order_items = [item for item in [drink, entree, side, fruit, extra] if item]
        order_summary = f"Order for {student_name}: {', '.join(order_items)}"

        if payment_method:
            order_summary += f"\nPayment Method: {payment_method}"

        if not student_name or not order_items:
            messagebox.showerror("Error", "Please enter both student name and select at least one item.")
        else:
            messagebox.showinfo("Success", order_summary)

    def view_menu(self):
        menu_window = tk.Toplevel(self.root)
        menu_window.title("Lunch Menu")


        menu_text = """
        Drinks: Chocolate Milk, Strawberry Milk, 2% Milk, Apple Juice, Cranberry Juice, Water
        Entrees: Taco Triangles, Country Baked Steak, Cheese Pizza, Sausage Pizza, Pepperoni Pizza, Chicken Sandwich
        Sides: Green Beans, Carrots, Baked Potato, Salad, French Fries, Corn
        Fruits: Green Apple, Red Apple, Orange, Banana, Bundle of Grapes
        Extras: Lays Chips (Original), Lays Chips (Sour Cream), Cheetos, Doritos (Nacho Cheese), Rice Krispy Treat, Raisins, Cookie, Coke Zero, Fanta Zero, Mello Yello Zero
        """
        tk.Label(menu_window, text=menu_text).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = HamiltonLunchApp(root)
    root.mainloop()
