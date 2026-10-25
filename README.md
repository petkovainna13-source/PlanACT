# PlanACT 🎲

**Think it. Plan it. Do it.**

PlanACT is a Django web application for organizing activities and discovering things to do based on budget, distance, environment, and personal preferences.

## Features

- **Activities:** Create, view, edit, and delete activities with descriptions, locations, budgets, distances, images, and pet-friendly options.
- **Categories:** Organize activities into categories with full CRUD functionality.
- **Vibes:** Assign multiple vibes to activities, with full CRUD functionality.
- **Filtering and Sorting:** Find activities by budget, distance, environment, and pet-friendliness. Sort by name, budget, or distance.
- **Random Picker:** Get a random activity suggestion based on selected preferences.
- **Additional Features:** Form validation, deletion confirmations, custom template tags and filters, and a custom 404 page.

## Technologies

- Python 3.11
- Django 5.2
- SQLite
- HTML and CSS

## Project Structure

The project contains four Django apps:

| App | Purpose |
|---|---|
| `activities` | Activity management, filtering, and sorting |
| `categories` | Category management |
| `vibes` | Vibe management |
| `planner` | Random activity picker |

### Database Relationships

- **Category → Activity:** One-to-many relationship.
- **Activity ↔ Vibe:** Many-to-many relationship.

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/petkovainna13-source/PlanACT.git
cd PlanACT
```

**2. Create and activate a virtual environment**

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Apply migrations**

```bash
python manage.py migrate
```

**5. Start the server**

```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

## Getting Started

The application works with an empty SQLite database. No preloaded data or Django admin access is required.

1. Create a category through the **Categories** page.
2. Create one or more vibes through the **Vibes** page.
3. Add activities through the **Activities** page.
4. Browse, filter, or use the **Random Picker**.

No external services, environment variables, or credentials are required for local setup.

## About

Developed as an individual project for the **SoftUni Django Basics Regular Exam — October 2026**.