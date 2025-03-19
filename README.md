# 🍽️ Django Food Menu App  

A **Django-based food menu application** that allows users to browse, add, and manage food items with user authentication features. This project is designed to demonstrate core Django functionalities, including CRUD operations, user authentication, and database management.  

## 🚀 Features  

- **Food Menu Display** – Browse food items with images, descriptions, and prices.  
- **Detailed View** – Click on any item to view its full details.  
- **User Authentication** – Register, log in, and log out functionality.  
- **Add Food Items** – Logged-in users can add new food items with an image, name, description, and price.  
- **Delete Food Items** – Users can delete food items with confirmation.  
- **User-Specific Entries** – Each food item displays the user who added it.  

## 🛠️ Tech Stack  

- **Backend:** Django (Python)  
- **Database:** SQLite (Default Django DB) 
- **Frontend:** HTML, CSS (Bootstrap for styling)  

## 🛠️ Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/DS-Vijayapala/Food-Menu-App.git
   cd django-food-menu
   ```
2. Create a virtual environment and activate it:  
   ```bash
   python -m venv venv  
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:  
   ```bash
   python manage.py migrate
   ```
5. Create a superuser (for admin access):  
   ```bash
   python manage.py createsuperuser
   ```
6. Start the development server:  
   ```bash
   python manage.py runserver
   ```
7. Open your browser and visit:  
   ```
   http://127.0.0.1:8000/
   ```

## 📸 Screenshots  

Click This Url For ScreenShots - 

## 🏗️ Future Improvements  

- Implement a **shopping cart** feature.  
- Add **category filtering** for food items.  
- Improve UI with modern styling.  

## 🐝 License  

This project is licensed under the **MIT License**.  


