I don't want to write an interface so I asked gemini how I should structure the code for it to make the gui for me using tkinter and it gave me this weird file structure:
```
StudyBites/
├── assets/                 <-- Icons, default images
│   └── icon.ico
├── data/                   <-- Where the user's files/CSV go
│   └── (User files here)
├── src/                    <-- Source Code Package
│   ├── __init__.py         <-- Makes this a Python package
│   ├── model.py            <-- The Logic (CSV, Math, File Scanning)
│   └── view.py             <-- The UI (Tkinter classes)
├── main.py                 <-- The Entry Point (Run this!)
├── README.md
└── requirements.txt
```
I have never done an actual package before... I hope this isn't too hard...