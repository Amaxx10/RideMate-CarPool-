# HitchRide - Carpool Management System

## Overview
HitchRide is a **Car-Pooling Management System (CMS)** designed to facilitate ride-sharing among users traveling on the same route. Users can either offer a ride as a **Driver** or request a ride as a **Rider**. The system is built using the **Django framework** and integrates **Google Maps API** for location services.

## Features
### Implemented Features:
- **Web Application** for users (Drivers & Riders) to manage ride-sharing.
- **User Authentication** through a login & registration system.
- **Google Maps API Integration** for location suggestions and routing.
- **Driver Dashboard**:
  - Add destinations and view available riders.
  - Accept ride requests and manage bookings.
- **Rider Dashboard**:
  - Request rides by entering pickup & destination points.
  - View driver details upon ride confirmation.
- **Real-Time Ride Tracking**:
  - Directions to pickup points via Google Maps API.
  - Estimated time to reach the destination.
- **Ride Fare Calculation** upon ride completion.

### Pending Features:
- **User Feedback System** for rating drivers and riders.
- **Ride History Management** to track past bookings.

## Technology Stack
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite/PostgreSQL
- **APIs Used**:
  - Google Maps API (Geolocation, Places, Directions)

## Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/HitchRide.git
   cd HitchRide
   ```
2. Set up a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations & start the server:
   ```sh
   python manage.py migrate
   python manage.py runserver
   ```
5. Access the application at `http://127.0.0.1:8000/`

## Screenshots
- **Login & Registration Page**
- **Driver Dashboard**: View & accept ride requests
- **Rider Dashboard**: Request & track rides

(Screenshots can be added in the repository)

## Testing
We followed **Agile development** and used various testing methodologies:
- **Unit Testing** using Python's `unittest`.
- **Integration Testing** to ensure API & module interactions.
- **Performance Testing** using load & stress tests.
- **Compatibility Testing** across OS (Ubuntu, Windows, macOS) & browsers (Chrome, Firefox, Safari).

## License
This project is licensed under the MIT License.

## Acknowledgments
- Google Maps API for location-based services.
- Django framework for backend development.
- Open-source libraries & tools for web development.

---
For more details, refer to the [Project Documentation](https://drive.google.com/file/d/1UBQuHQhfoLH1jlxuSLgsvAu6gZslmhD4/view?usp=sharing).

