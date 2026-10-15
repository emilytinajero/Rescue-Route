# Rescue Route

Surplus Food Matching & Pickup Planner

---

## Project Overview

RescueRoute is an explainable surplus-food matching and pickup-planning system devloped for CPSC 335.

The system matches time-sensitive food donations with compatible recipient
organizations and volunteer drivers while providing human-readable explanations
for every decision.

The project compares two scheduling strategies:

1. FIFO (First-In-First-Out) Scheduling
2. Greedy Urgency-First Scheduling

The goal is to maximize food rescue while prioritizing donations that are closest to expiration.

---

# Problem Statement

Restaurants, grocery stores, campus events, and caterers often have surplus
food that must be distributed before it expires. At the same time, community
organizations have different capacity limits, food acceptance rules, operating hours, and location constraints.

RescueRoute answers the following question:

> How can time-sensitive food donations be assigned to compatible recipients and volunteers in a way that is efficient, transparent, and easy to explain

---

# System Architecture

## Repository Structure

```text
data/
|-- sample_input.json
|-- empty_input.json
|__ invalid_inputs.json

src/
|-- data_loader.py
|-- validation.py
|-- matching.py
|-- lookup.py
|-- scheduler.py
|-- metrics.py
|__ main.py

tests/
|-- test_matching.py
|-- test_validation.py
|__ test_sample_inputs.py
```

---

## data/

Contains all JSON datasets used by the project.

### sample_input.json

Primary dataset containing all donations, recipients, and volunteers.

### empty_input.json

Used to test empty datasets and edge cases.

### invalid_inputs.json

Contains intentionally invalid records used to verify validation logic by testing all edge cases and testing every validation rule

---

## src/

Contains all application source code.

### data_loader.py

Loads the donation, recipient, and volunteer data from JSON files.

### validations.py

Validates:

- Required fields
- Unique IDs
- Positive quantities and capacities
- Time formats
- Dataset integrity
- Accepted Food Types
- Availabilities

### matching.py

Determines whether a donation-recipient-volunteer combination is feasible.

Checks:

- Food compatibility
- Capacity constraints
- Location compatibility
- Time-Window overlap
- Volunteer pickup limits

Provides:

- Defered Message
- Rejection Reasons

### lookup.py

Creates dictionary-based lookup tables for:

- Donations
- Recipients
- Volunteers

### scheduler.py

Implements the scheduling algorithms and finds the first match

### FIFO Scheduler

Processes donations in arrival order and assigns the first feasible recipient-volunteer pair.

Creates assignment records and explanation messages.

### Greedy Scheduler

Prioritizes donations with earlier expiration times.

Creates assignment records and explanation messages.

### metrics.py

Calculates all project metrics and comparison statistics

### main.py

Provides the command-line user interface and integrates all project components. 



























