# Django Feature Flags Prototype

## Overview
This project is a prototype implementation of a Feature Flag System for Django. It is designed to enable controlled activation and deactivation of experimental features within a Django application, allowing safer testing, gradual rollouts, and improved development flexibility.

The goal of this project is to explore how a native feature flag system can be integrated into Django to support scalable and maintainable feature experimentation.

---

## Features
- Centralized feature flag registry  
- Enable/disable features dynamically  
- Django settings integration  
- Simple runtime API for checking flags  
- Extendable for user-based or environment-based flags  

---

## Project Structure
```bash
django-feature-flags/
│── feature_flags/
│   │── __init__.py
│   │── registry.py
│   │── utils.py
│   │── middleware.py
│── examples/
│── tests/
│── README.md
```

---

## Installation
```bash
git clone https://github.com/your-username/django-feature-flags-prototype.git
cd django-feature-flags-prototype
pip install -r requirements.txt
```

---

## Usage

### 1. Define Feature Flags
```python
FEATURE_FLAGS = {
    "new_dashboard": True,
    "beta_feature": False,
}
```

---

### 2. Use in Code
```python
from feature_flags.utils import is_enabled

if is_enabled("new_dashboard"):
    # New feature logic
    pass
else:
    # Old feature logic
    pass
```

---

### 3. Middleware (Optional)
```python
MIDDLEWARE = [
    "feature_flags.middleware.FeatureFlagMiddleware",
]
```

---

## Future Improvements
- Django Admin integration for UI-based control  
- Database-backed feature flags  
- User/group-based targeting  
- A/B testing support  
- Performance optimization  

---

## Tech Stack
Python, Django, Django ORM, Middleware, SQLite/PostgreSQL, Git

---

## Contribution
This project is currently a prototype developed as part of preparation for Google Summer of Code (GSoC) with Django Software Foundation.

Contributions, suggestions, and feedback are welcome.

---

## Author
Lakshay Kaushik  
GitHub: https://github.com/lakshaykaushik1

---

## License
This project is open-source and available under the MIT License.
