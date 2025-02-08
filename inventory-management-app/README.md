# Inventory Management App

This is a Django-based inventory management application designed to manage warehouse outputs. The application allows users to track product quantities and dates, providing a responsive and modern interface.

## Features

- **Product Management**: Add, edit, and delete products from the inventory.
- **Quantity Tracking**: Record the quantity of products and the date of the transaction without the time.
- **Dropdown Selection**: Easily select products from a dropdown list when registering a new output.
- **Summation of Entries**: If a product is registered multiple times, the quantities will be summed instead of creating new entries.
- **Responsive Design**: The application is designed to be mobile-friendly and responsive.
- **Modern UI**: The app features a modern design with a background image for an enhanced user experience.

## Technologies Used

- Django: A high-level Python web framework for building web applications.
- Supabase: A backend-as-a-service platform that provides a PostgreSQL database for storing product data.
- HTML/CSS: For structuring and styling the web pages.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/inventory-management-app.git
   cd inventory-management-app
   ```

2. **Install Dependencies**:
   Make sure you have Python and pip installed. Then, run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Database**:
   Update the `settings.py` file with your Supabase database credentials.

4. **Run Migrations**:
   Apply the database migrations:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   Start the Django development server:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Deployment

To deploy the application on Vercel, ensure that your `vercel.json` file is correctly configured with the necessary build settings and routes.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.