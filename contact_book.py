import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactList:
    def __init__(self, root):
        self.root = root
        self.contacts = []

        # Create frames
        self.frame1 = tk.Frame(self.root, bg='#000000')
        self.frame1.pack(pady=5)
        self.frame2 = tk.Frame(self.root, bg='#000000')
        self.frame2.pack(pady=5)
        self.frame3 = tk.Frame(self.root, bg='#000000')
        self.frame3.pack(pady=5)
        self.frame4 = tk.Frame(self.root, bg='#000000')
        self.frame4.pack(pady=5)
        self.frame5 = tk.Frame(self.root, bg='#000000')
        self.frame5.pack(pady=10)

        # Create labels and entries
        tk.Label(self.frame1, text="Name:", font=('Segoe UI', 12, 'bold'), fg='#ffffff', bg='#000000').pack(side=tk.LEFT)
        self.name_entry = tk.Entry(self.frame1, width=30, font=('Segoe UI', 12), fg='#032B44')
        self.name_entry.pack(side=tk.LEFT)
        self.name_entry.bind('<Return>', lambda event: self.add_contact())

        tk.Label(self.frame2, text="Phone:", font=('Segoe UI', 12, 'bold'), fg='#ffffff', bg='#000000').pack(side=tk.LEFT)
        self.phone_entry = tk.Entry(self.frame2, width=30, font=('Segoe UI', 12), fg='#032B44')
        self.phone_entry.pack(side=tk.LEFT)
        self.phone_entry.bind('<KeyRelease>', self.validate_phone_key)

        tk.Label(self.frame3, text="Email:", font=('Segoe UI', 12, 'bold'), fg='#ffffff', bg='#000000').pack(side=tk.LEFT)
        self.email_entry = tk.Entry(self.frame3, width=30, font=('Segoe UI', 12), fg='#032B44')
        self.email_entry.pack(side=tk.LEFT)

        tk.Label(self.frame4, text="Address:", font=('Segoe UI', 12, 'bold'), fg='#ffffff', bg='#000000').pack(side=tk.LEFT)
        self.address_entry = tk.Entry(self.frame4, width=30, font=('Segoe UI', 12), fg='#032B44')
        self.address_entry.pack(side=tk.LEFT)

        # Create buttons
        tk.Button(self.frame5, text="Add", command=self.add_contact, font=('Arial', 12, 'bold'), fg='#ffffff', bg='#008000').pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame5, text="Delete", command=self.delete_contact, font=('Arial', 12, 'bold'), fg='#ffffff', bg='#FF0000').pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame5, text="Update", command=self.update_contact, font=('Arial', 12, 'bold'), fg='#ffffff', bg='#FFA500').pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame5, text="Search", command=self.search_contact, font=('Arial', 12, 'bold'), fg='#ffffff', bg='#0000FF').pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame5, text="Display", command=self.display_contacts, font=('Arial', 12, 'bold'), fg='#ffffff', bg='#03055B').pack(side=tk.LEFT, padx=5)

        # Create listbox
        self.listbox = tk.Listbox(self.root, width=80, font=('Helvetica', 15), fg='#00698f', bg='#ffffff')
        self.listbox.pack(pady=10)

    def validate_phone_key(self, event):
        phone_number = self.phone_entry.get()
        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, ''.join(filter(str.isdigit, phone_number)))

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name and phone:
            contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
            self.contacts.append(contact)
            self.listbox.insert(tk.END, f"{name}: {phone}")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter both name and phone number")

    def delete_contact(self):
        try:
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
            self.contacts.pop(index)
        except:
            messagebox.showerror("Error", "Select a contact to delete")

    def update_contact(self):
        try:
            index = self.listbox.curselection()[0]
            contact = self.contacts[index]

            new_name = simpledialog.askstring("Update Name", "Enter new name:", initialvalue=contact['name'])
            new_phone = simpledialog.askstring("Update Phone", "Enter new phone:", initialvalue=contact['phone'])
            new_email = simpledialog.askstring("Update Email", "Enter new email:", initialvalue=contact['email'])
            new_address = simpledialog.askstring("Update Address", "Enter new address:", initialvalue=contact['address'])

            if new_name and new_phone:
                contact.update({'name': new_name, 'phone': new_phone, 'email': new_email, 'address': new_address})
                self.listbox.delete(index)
                self.listbox.insert(index, f"{new_name}: {new_phone}")
            else:
                messagebox.showerror("Error", "Name and phone cannot be empty")
        except:
            messagebox.showerror("Error", "Select a contact to update")

    def search_contact(self):
        search_term = simpledialog.askstring("Search", "Enter name or phone number to search:")
        if search_term:
            search_results = [f"{c['name']}: {c['phone']}" for c in self.contacts if search_term in c['name'] or search_term in c['phone']]
            if search_results:
                messagebox.showinfo("Search Results", "\n".join(search_results))
            else:
                messagebox.showinfo("No Results", "No contacts found")

    def display_contacts(self):
        if self.contacts:
            messagebox.showinfo("Contacts", "\n".join([f"{c['name']}: {c['phone']}" for c in self.contacts]))
        else:
            messagebox.showinfo("Contacts", "No contacts to display")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Contact List")
root.configure(bg='#000000')
contact_list = ContactList(root)
root.mainloop()
