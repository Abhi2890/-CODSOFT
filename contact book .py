import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        self.contacts = []

        self.create_interface()

    def create_interface(self):
        # Labels
        tk.Label(self.root, text="Name:", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Label(self.root, text="Phone:", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tk.Label(self.root, text="Email:", font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
        tk.Label(self.root, text="Address:", font=("Helvetica", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="w")

        # Entry widgets
        self.name_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        self.phone_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)
        self.email_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
        self.address_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        tk.Button(self.root, text="Add Contact", command=self.add_contact, font=("Helvetica", 12)).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="View Contacts", command=self.view_contacts, font=("Helvetica", 12)).grid(row=5, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Error", "Name and Phone are required fields.")

    def view_contacts(self):
        contacts_window = tk.Toplevel(self.root)
        contacts_window.title("Contact List")

        tk.Label(contacts_window, text="Contact List", font=("Helvetica", 16)).pack(pady=10)

        for contact in self.contacts:
            contact_info = f"Name: {contact['Name']}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}\n"
            tk.Label(contacts_window, text=contact_info, relief="solid", borderwidth=1, padx=10, pady=5, font=("Helvetica", 12)).pack(pady=5)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
