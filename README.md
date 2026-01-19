# AuditFlow API
AuditFlow is a backend API built with Django Rest Framework to manage audits, findings, and access control.
It is designed as a modular monolith focused on maintainability, security, and clear domain boundaries.

## Architecture
The project follows a modular monolith architecture:

- `user` – authentication and users
- `audits` – audits, audit types, audit findings
- `core` – shared permissions, pagination, utilities

## DB PostgreSQL
Data integrity, complex queries, and structured + semi-structured data.

## Authentication
Authentication is handled using JWT (SimpleJWT).

### Login
#### POST
```http
   /v1/auth/login/
```

Returns access and refresh tokens.

All protected endpoints require:
Authorization: Bearer <access_token>

## Permissions
- Admin (superuser):
  - Full access to all resources

- Auditor:
  - Can create audits
  - Can manage only their own audits
  - Can add and update findings for their audits

Object-level permissions are enforced using custom DRF permission classes.

## Resources

### Audit Types
- Create reference audit categories (e.g. Internal Audit, IT Audit, Compliance Audit,	Internal Audit)

### Audits
- Create and manage audits
- Status lifecycle: draft → in_progress → completed
- Soft delete for data integrity

### Audit Findings
- Findings belong to audits
- Can only be managed by audit owner or admin

## API Flow Example
- 1 Create Audit Type
- 2 Create Audit
- 3 Add Findings to Audit
- 4 Update Audit status

## Example Requests
#### Create Audits
POST /v1/provider/audits/create/
```http
{
  "title": "Q1 Financial Audit",
  "description": "Quarterly internal audit",
  "audit_type": "3",
  "status": "draft"
}
```
#### Update audit details
PATCH v1/provider/audits/<id>/
```http
{
    "title": "Q1 Financial Audit",
    "status": "in_progress",
    "description": "Quarterly internal audit – field work started"
}
```

####  Create findings
POST  /v1/provider/audits/<id>/findings/
```http
{
  "title": "Missing Expense Approvals",
  "description": "Multiple expense records do not contain managerial approval.",
  "severity": "high",
  "evidence": {
    "documents": [
      "expense_jan_2026.pdf",
      "expense_feb_2026.pdf"
    ],
    "notes": "Approval policy not enforced"
  }
}
```

####  Update findings
PATCHT  /v1/provider/audits/<id>/findings/
```http
{
  "severity": "medium",
  "description": "Issue partially resolved after policy update"
}
```

#### Pagination & Filtering
GET /v1/audits/?status=in_progress&page=1

## Tech Stack
- Python
- Django
- Django Rest Framework
- PostgreSQL
- SimpleJWT

## Design Decisions
- Monolithic architecture for simpler deployment and maintenance
- Explicit, domain-specific permission classes
- Nested endpoints for audit findings
- Soft delete strategy for audit records
- PATCH preferred over PUT for partial updates

## Run locally
- python -m venv .venv
- .venv\Scripts\activate
- pip install -r requirements.txt
- python manage.py createsuperuser
- python manage.py collectstatic
- python manage.py makemigrations 
- python manage.py migrate
- python manage.py runserver

## .env
SECRET_KEY=
DEBUG=False
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=5432