# 💰 FinanceMate API

FinanceMate is a personal finance tracking API built with Django Rest Framework. It allows users to manage their expenses, income, budgets, and savings goals in a secure and organized way.

---

## 🚀 Authentication Endpoints

These endpoints handle user registration and login using JWT.

- `POST /api/accounts/register/` — Register a new user
- `POST /api/accounts/login/` — Log in to get access & refresh tokens
- `POST /api/accounts/token/refresh/` — Refresh your access token using the refresh token

🔐 **JWT Tokens**
- **Access Token**: Short-lived; used for authenticated requests.
- **Refresh Token**: Used to get a new access token without re-logging in.

---

## 🌐 Core API Root

- `GET /api/core/` — Welcome endpoint with a simple greeting

---

## 📂 Categories

Organize your transactions using custom categories.

- `GET /api/core/categories/` — List all categories
- `POST /api/core/categories/` — Create a new category
- `GET /api/core/categories/<id>/` — Retrieve a single category
- `PUT /api/core/categories/<id>/` — Update a category
- `PATCH /api/core/categories/<id>/` — Partially update a category
- `DELETE /api/core/categories/<id>/` — Delete a category

---

## 💸 Transactions

Track income and expenses.

- `GET /api/core/transactions/` — List all transactions
- `POST /api/core/transactions/` — Create a new transaction
- `GET /api/core/transactions/<id>/` — Retrieve a single transaction
- `PUT /api/core/transactions/<id>/` — Update a transaction
- `PATCH /api/core/transactions/<id>/` — Partially update a transaction
- `DELETE /api/core/transactions/<id>/` — Delete a transaction

---

## 📊 Budgets

Set monthly spending limits per category.

- `GET /api/core/budgets/` — List all budgets
- `POST /api/core/budgets/` — Create a new budget
- `GET /api/core/budgets/<id>/` — Retrieve a single budget
- `PUT /api/core/budgets/<id>/` — Update a budget
- `PATCH /api/core/budgets/<id>/` — Partially update a budget
- `DELETE /api/core/budgets/<id>/` — Delete a budget

---

## 🎯 Savings Goals

Track progress toward your financial goals.

- `GET /api/core/goals/` — List all goals
- `POST /api/core/goals/` — Create a new savings goal
- `GET /api/core/goals/<id>/` — Retrieve a specific goal
- `PUT /api/core/goals/<id>/` — Update a goal
- `PATCH /api/core/goals/<id>/` — Partially update a goal
- `DELETE /api/core/goals/<id>/` — Delete a goal

---

## 🧠 Tech Stack

- Django & Django REST Framework
- JWT Authentication
- MySQL or PostgreSQL

---

## 📌 Notes

- All endpoints (except registration/login) require JWT authentication.
- Use your **access token** in the `Authorization` header like this:
    Authorization: Bearer <access_token>