# Application Tracker

Practice project for while job hunting...

## Problem statement:

I'm looking for a job in a tough job market and I expect to apply to many positions over a long-ish period of time. I would like to:

- keep track of the places & jobs I apply to
- track the phases I go through -- e.g. applied, initial screen, interview(n), offer, acceptance
- keep notes for each job for reference in subsequent stages (e.g. what attracted me to the job)
- track when these events occur so that I can plot statistics over time
- output various metrics -- e.g. total number of first-round interviews I did

## Benefits

By creating this application, I would like to:

- Brush up on both frontend and backend tech skills
- Explore Copilot-based development
- Have a demonstrable project to show potential employers
- Generate topics for my blog, which will help me stand out from other applicants

## Features

- Data entry screen for initial entry of job / company information
- Data edit screen, e.g. to add an event related to an application
- Home page with basic stats - total applied to, total companies applied to, total interviews, etc.
- Stats page with simple graphs and charts

## Tech stack

- Backend:
  - FastAPI / Python backend
  - SQLite data layer
  - Pydantic
  - Alembic
- React frontend
  - ES6 or Typescript tbd

# Models

```
Company
    company_id
    name
    website
    recruiter_name
    recruiter_email
    description (aka what do they do)

JobApplication
    job_app_id
    company_id
    datestamp
    job_title
    source
    source_url
    stage_id

Note
    notes_id
    job_app_id
    datestamp
    notes

Stage
    stage_id
    name
    is_deleted

```
