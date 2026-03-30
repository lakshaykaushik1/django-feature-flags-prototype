# Django Feature Flags Prototype

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-Framework-green)
![GSoC](https://img.shields.io/badge/GSoC-2026-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## Overview
This project is a prototype implementation of a Feature Flag System for Django. It enables controlled activation and deactivation of experimental features, allowing safer testing, gradual rollouts, and improved development flexibility.

The goal is to explore how a native feature flag system can be integrated into Django to support scalable and maintainable feature experimentation.

---

## Features
- Centralized feature flag registry  
- Dynamic enable/disable functionality  
- Django settings integration  
- Lightweight runtime API  
- Middleware support for request-based toggling  
- Extendable for user-based and environment-based flags  

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

### Define Feature Flags
```python
FEATURE_FLAGS = {
    "new_dashboard": True,
    "beta_feature": False,
}
```

---

### Use in Code
```python
from feature_flags.utils import is_enabled

if is_enabled("new_dashboard"):
    # New feature logic
    pass
else:
    # Fallback logic
    pass
```

---

### Middleware Setup (Optional)
```python
MIDDLEWARE = [
    "feature_flags.middleware.FeatureFlagMiddleware",
]
```

---

## Future Improvements
- Django Admin interface for real-time flag control  
- Database-backed feature flags  
- User/group-based targeting  
- A/B testing support  
- Performance optimizations  

---

## Tech Stack
Python, Django, Django ORM, Middleware, SQLite/PostgreSQL, Git, GitHub

---

## Contribution
This project is developed as part of preparation for Google Summer of Code (GSoC) with the Django Software Foundation.

Contributions, suggestions, and feedback are welcome.

---

## Author
Lakshay Kaushik  
GitHub: https://github.com/your-username

---

## License
This project is open-source and available under the MIT License.
