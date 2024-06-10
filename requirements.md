# Online Pig Health Management and Feeding Advisory System (OPHMFAS)

## 📜 Requirements Analysis

The system's goal is to assist small-scale pig farmers in Kenya by providing:

-   Disease Diagnosis Assistance
-   Feed Ration Management
-   Pig Health Record-Keeping
-   Report Generation

## 📝 Pseudocode Plan

### 1. System Overview

-   Purpose: Assist farmers with disease diagnosis, feeding strategies, and record-keeping.
-   Target Users: Small-scale pig farmers with basic computer literacy and access to internet-enabled devices.

### 2. Architecture

-   Frontend: HTML, CSS, JavaScript
-   Backend: Python/Java
-   Database: MySQL
-   Communication: HTTP for client-server interactions

### 3. Modules

-   User Interface Module

    -   Login and registration
    -   Input forms for health records and feed management
    -   Display diagnosis results and reports

-   Business Logic Module

    -   Validate user inputs
    -   Process disease diagnosis based on symptoms
    -   Calculate feed rations
    -   Generate reports

-   Data Access Module

    -   CRUD operations for health records and feed data
    -   Query disease information

-   Security Module

    -   User authentication
    -   Data protection and access control

-   Reporting Module

    -   Generate health and feed reports

## 🖥️ System Design

### 1. Database Design

Tables: Users, Pigs, HealthRecords, FeedRecords, Diseases
Relationships:

-   One user can have many pigs
-   Each pig can have multiple health records
-   Each pig can have multiple feed records

### 2. User Interface (UI)

Forms:

-   Login/Registration
-   Add/Edit Pig Information
-   Record Symptoms and Treatment
-   Input Feed Data

Views:

-   Dashboard showing pig health and feed summary
-   Detailed report views
