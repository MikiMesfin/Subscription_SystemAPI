# SaaS Subscription Management System

A Django-based subscription management system that handles user subscriptions, payments, and business profiles with Stripe integration.

## Features

- User Authentication and Authorization
- Business Profile Management
- Subscription Plans and Management
- Payment Processing with Stripe
- Invoice Generation and Management
- Admin Dashboard
- RESTful API
- Webhook Integration for Stripe Events

## Tech Stack

- Python 3.8+
- Django 5.1
- Django REST Framework
- MySQL Database
- Stripe API
- Celery for Background Tasks
- Redis for Caching



## API Endpoints

### Authentication
- `POST /api/accounts/login/` - User login
- `POST /api/accounts/logout/` - User logout

### User Management
- `GET /api/accounts/dashboard/` - User dashboard
- `GET /api/accounts/users/` - List users (admin only)
- `POST /api/accounts/users/` - Create user
- `GET /api/accounts/business-profiles/` - List business profiles

### Subscriptions
- `GET /api/subscriptions/plans/` - List available plans
- `POST /api/subscriptions/subscriptions/` - Create subscription
- `GET /api/subscriptions/dashboard/` - Subscription dashboard
- `GET /api/subscriptions/analytics/` - Subscription analytics

### Payments
- `GET /api/payments/dashboard/` - Payment dashboard
- `GET /api/payments/billing/` - Billing overview
- `GET /api/payments/invoices/` - List invoices

## Testing

Run the test suite:
```bash
python manage.py test
```

## Background Tasks

Start Celery worker:
```bash
celery -A core worker -l info
```

Start Celery beat for scheduled tasks:
```bash
celery -A core beat -l info
```

## Project Structure

```
saas_subscription_system/
├── accounts/                 # User and business profile management
├── subscriptions/           # Subscription and plan management
├── payments/               # Payment and invoice handling
├── core/                  # Project settings and configuration
├── templates/             # HTML templates
├── static/               # Static files (CSS, JS, images)
├── requirements.txt      # Project dependencies
└── manage.py            # Django management script
```

## Key Components

### Models
- User & BusinessProfile (accounts app)
- Plan & Subscription (subscriptions app)
- Payment & Invoice (payments app)

### Features
1. User Management
   - Custom user model with email authentication
   - Business profile management
   - Role-based access control

2. Subscription Management
   - Multiple subscription plans
   - Trial period support
   - Automatic renewal handling
   - Plan upgrade/downgrade

3. Payment Processing
   - Secure payment handling with Stripe
   - Invoice generation
   - Payment history tracking
   - Automatic payment retry

4. Admin Interface
   - User management
   - Subscription oversight
   - Payment tracking
   - System configuration

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details

