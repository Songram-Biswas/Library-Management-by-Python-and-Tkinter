import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import os
from datetime import datetime, timedelta

DATA_FILE = "library_data.txt"

class Book:
    def __init__(self, bookID, title, author, isIssued=False, issuedTo="", issueDate="", returnDate=""):
        self.bookID = int(bookID)
        self.title = title
        self.author = author
        self.isIssued = bool(int(isIssued)) if isinstance(isIssued, str) else isIssued
        self.issuedTo = issuedTo
        self.issueDate = issueDate
        self.returnDate = returnDate

    def to_line(self):
        return f"{self.bookID}|{self.title}|{self.author}|{int(self.isIssued)}|{self.issuedTo}|{self.issueDate}|{self.returnDate}"

    @staticmethod
    def from_line(line):
        parts = line.strip().split('|')
        while len(parts) < 7:
            parts.append("")  # Fill missing fields
        return Book(*parts)

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.books = self.load_books()
        self.print_all_books()

        # Treeview
        self.tree = ttk.Treeview(root, columns=("ID", "Title", "Author", "Status", "IssuedTo", "IssueDate", "ReturnDate"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=130)
        self.tree.pack(fill="both", expand=True, pady=10)

        self.refresh_table()

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add Book", command=self.add_book).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Issue Book (By ID)", command=self.issue_book).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Return Book", command=self.return_book).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Search Book", command=self.search_book).grid(row=0, column=3, padx=5)
        tk.Button(btn_frame, text="Browse & Issue Book", command=self.browse_and_issue).grid(row=0, column=4, padx=5)
        tk.Button(btn_frame, text="Show All", command=self.refresh_table).grid(row=0, column=5, padx=5)

    def print_all_books(self):
        print("All books loaded:")
        for book in self.books:
            print(f"ID: {book.bookID}, Title: {book.title}, Author: {book.author}, Issued: {book.isIssued}")

    def load_books(self):
        books = []
        if not os.path.exists(DATA_FILE):
            return books
        seen_ids = set()
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                book = Book.from_line(line)
                if book.bookID not in seen_ids:
                    books.append(book)
                    seen_ids.add(book.bookID)
        return books

    def save_books(self):
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            for book in self.books:
                f.write(book.to_line() + "\n")

    def refresh_table(self, books=None):
        self.tree.delete(*self.tree.get_children())
        for book in books if books else self.books:
            self.tree.insert("", "end", values=(
                book.bookID, book.title, book.author,
                "Issued" if book.isIssued else "Available",
                book.issuedTo, book.issueDate, book.returnDate))

    def add_book(self):
        try:
            bookID = int(simpledialog.askstring("Input", "Enter Book ID:"))
            if any(b.bookID == bookID for b in self.books):
                messagebox.showwarning("Warning", "Book ID already exists.")
                return
            title = simpledialog.askstring("Input", "Enter Book Title:")
            author = simpledialog.askstring("Input", "Enter Author Name:")
            self.books.append(Book(bookID, title, author))
            self.save_books()
            self.refresh_table()
            messagebox.showinfo("Success", "Book added successfully.")
        except:
            messagebox.showerror("Error", "Invalid input.")

    def issue_book(self):
        try:
            bookID = int(simpledialog.askstring("Input", "Enter Book ID to Issue:"))
            student = simpledialog.askstring("Input", "Enter Student Roll Number:")
            for book in self.books:
                if book.bookID == bookID:
                    if book.isIssued:
                        messagebox.showwarning("Warning", "Book already issued.")
                        return
                    book.isIssued = True
                    book.issuedTo = student
                    book.issueDate = datetime.today().strftime("%Y-%m-%d")
                    book.returnDate = (datetime.today() + timedelta(days=30)).strftime("%Y-%m-%d")
                    self.save_books()
                    self.refresh_table()
                    messagebox.showinfo("Issued", f"Issued to {student}. Return by {book.returnDate}")
                    return
            messagebox.showerror("Error", "Book not found.")
        except:
            messagebox.showerror("Error", "Invalid input.")

    def return_book(self):
        try:
            bookID = int(simpledialog.askstring("Input", "Enter Book ID to Return:"))
            for book in self.books:
                if book.bookID == bookID:
                    if not book.isIssued:
                        messagebox.showinfo("Info", "Book is not issued.")
                        return
                    book.isIssued = False
                    book.issuedTo = ""
                    book.issueDate = ""
                    book.returnDate = ""
                    self.save_books()
                    self.refresh_table()
                    messagebox.showinfo("Returned", "Book returned successfully.")
                    return
            messagebox.showerror("Error", "Book not found.")
        except:
            messagebox.showerror("Error", "Invalid input.")

    def search_book(self):
        query = simpledialog.askstring("Search", "Enter Title or Author to search:")
        if not query:
            return
        query = query.lower()
        found = [b for b in self.books if query in b.title.lower() or query in b.author.lower()]
        if not found:
            messagebox.showinfo("Search", "No books found.")
        self.refresh_table(found)

    def browse_and_issue(self):
        win = tk.Toplevel(self.root)
        win.title("Browse & Issue Book")
        win.geometry("950x450")

        search_var = tk.StringVar()

        search_entry = tk.Entry(win, textvariable=search_var, width=50)
        search_entry.pack(pady=5)

        book_tree = ttk.Treeview(win, columns=("ID", "Title", "Author", "Status"), show="headings", height=15)
        for col in book_tree["columns"]:
            book_tree.heading(col, text=col)
            book_tree.column(col, width=200)
        book_tree.pack(fill="both", expand=True, pady=5)

        def refresh_browse(books):
            book_tree.delete(*book_tree.get_children())
            for book in books:
                book_tree.insert("", "end", values=(book.bookID, book.title, book.author,
                                                    "Issued" if book.isIssued else "Available"))

        def filter_books(*args):
            q = search_var.get().lower()
            filtered = [b for b in self.books if q in b.title.lower() or q in b.author.lower()]
            refresh_browse(filtered)

        def issue_selected():
            selected = book_tree.selection()
            if not selected:
                messagebox.showwarning("Select", "Please select a book to issue.")
                return
            bookID = int(book_tree.item(selected[0])['values'][0])
            for book in self.books:
                if book.bookID == bookID:
                    if book.isIssued:
                        messagebox.showwarning("Issued", "This book is already issued.")
                        return
                    student = simpledialog.askstring("Student", "Enter Student Roll Number:")
                    if not student:
                        return
                    book.isIssued = True
                    book.issuedTo = student
                    book.issueDate = datetime.today().strftime("%Y-%m-%d")
                    book.returnDate = (datetime.today() + timedelta(days=30)).strftime("%Y-%m-%d")
                    self.save_books()
                    self.refresh_table()
                    refresh_browse(self.books)
                    messagebox.showinfo("Issued", f"Book issued to {student}. Return by {book.returnDate}")
                    return

        search_var.trace_add("write", filter_books)
        tk.Button(win, text="Issue Selected Book", command=issue_selected).pack(pady=5)
        refresh_browse(self.books)

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.geometry("1050x600")
    root.mainloop()
