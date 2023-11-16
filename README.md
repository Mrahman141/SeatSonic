# SeatSonic

## Team Members

[Albert Abalian](https://github.com/Bert-Stein)   
[Gazal Garg](https://github.com/Gazal100)   
[Mohammed Aminoor Rahman](https://github.com/Mrahman141)  
[Tatiana Kashcheeva](https://github.com/Amoraa)

## What is SeatSonic

SeatSonic is a concert ticket sales management system designed to assist companies in efficiently handling the process of selling and managing concert tickets. The platform supports multiple venues, each with a unique seating plan, and allows users to place orders for concert tickets. The system is built with an agile product engineering approach, emphasizing adaptability and responsiveness to customer needs.

## Technologies Used

### Backend
```
- Django: A high-level Python web framework that facilitates rapid development and clean, pragmatic design.
- MongoDB: A NoSQL database used for storing and managing dynamic and scalable data related to venues, concerts, pricing, and user accounts.
- Socket-level programming: Implemented for handling concurrent requests from multiple clients.
```

### Frontend

```
- Django Templates: Utilized for rendering dynamic HTML content based on server-side data.
- Bootstrap: Integrated for a responsive and modern user interface design.
- JavaScript: Used for enhancing the interactivity and user experience on the client side.
```

## How it Works

1. **Venue and Concert Setup**: The system supports multiple venues, each with a unique seating plan. Concerts are scheduled for specific dates and venues, with customizable seating configurations.

2. **Order Processing**: Users, including consumers and bulk ticket purchasers (resellers or commercial clients), can place orders via conventional Internet standards. The system processes ticket orders, tracking the number of seats sold and the corresponding revenue.

3. **Multi-language and Currency Support**: While the current implementation assumes English communication and Canadian dollars, the system is designed to easily support other languages and currencies in the future.

4. **Dynamic Updates**: Information about venues, concerts, pricing, and initial account balances can be uploaded and updated by the company hosting the system.

## Back-End Dependencies

```
- Django Bootstrap: Integrates Bootstrap with Django for streamlined frontend development.
- Django Math Filters: Provides mathematical filters and utilities for Django templates.
- Django Rosetta: Enables easy handling of translations in Django projects.
- pymongo: Python driver for MongoDB, used for interacting with the NoSQL database.
```

## Front-End Dependencies

```
- Bootstrap: The latest version of the popular CSS framework for responsive and visually appealing web design.
- jQuery: A fast and feature-rich JavaScript library, enhancing the client-side functionality of the application.
```
