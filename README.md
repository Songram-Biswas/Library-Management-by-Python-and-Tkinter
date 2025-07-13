# Library-Management-by-Python-and-Tkinter 
1. Project Title 
Library Management System Using Python and Tkinter 
2. Objective 
The main objective of this project is to create a simple, efficient, and user-friendly desktop application 
to manage a library. This system provides functionality to add, issue, return, and search books, 
reducing manual efforts and improving reliability through automation. 
3. Tools and Technologies Used - Programming Language: Python 3.x - GUI Framework: Tkinter - Data Storage: Text file (library_data.txt) - Packaging Tool: PyInstaller (for converting .py to .exe) - IDE: Any (e.g., VS Code) - Platform: Windows 
4. Features Implemented 
4.1 Book Management - Add new books with unique IDs, title, and author. - Stored in library_data.txt using format: 
bookID|title|author|isIssued|issuedTo|issueDate|returnDate 
4.2 Issue & Return System - Issue book to a student using roll number. - Records issue and return dates. - Return process clears associated data. 
4.3 Search Functionality - Search by title or author (case-insensitive). - Displays matching books in the GUI. 
4.4 Browse & Issue Interface - Interactive list view of all books. - Instant filtering and issue option. 
4.5 Data Persistence - All operations are saved to library_data.txt. - Duplicate book entries are prevented. 
5. File Structure 
D:\Projects\library_gui_qt\ 
├── library_ui.py               
# Main GUI application 
├── library_data.txt           
├── dist\                      
│  
 └── library_ui.exe 
└── build\                     
 # Contains book records 
# Folder containing generated .exe 
# Temporary build files 
6. Conversion to Executable (.exe) 
The application is packaged using PyInstaller: 
Steps: 
1. Open Command Prompt. 
2. Navigate to the project directory: 
cd D:\Projects\library_gui_qt 
3. Run: 
pyinstaller --onefile --windowed library_ui.py 
4. Executable will be in the 'dist' folder. 
7. Sample Data 
Pre-filled with 2000+ engineering-related books, e.g.: 
101|Introduction to Mechanical Engineering|R.K. Rajput|0||| 
... 
2000|Advanced Control Systems|Ogata|0||| 
8. Benefits - Lightweight and easy to use. - No external database needed. - Fast search. - Ideal for academic demos. 
9. Limitations - Not suited for multi-user use. - Data stored in plain text. - Slower with very large files. 
10. Future Enhancements - Add login system. - Use SQLite or MySQL. - Add overdue alerts. - Export to PDF/Excel. - Cross-platform GUI (e.g., PyQt or web-based). 
 
 
 
 
 
 
 
 
11. Screenshots 
Include screenshots of: - Main window- 
 
Book addition 
 
- Issue dialog - Browse/Search window 
12. Conclusion 
This Library Management System fulfills basic needs of book management and demonstrates Python 
GUI capabilities. It can be a foundation for more advanced systems.
