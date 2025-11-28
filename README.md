# TASK #1_DATA

## Description
Solution for TASK #1_DATA (DATA group).  
Load book data from JSON into a relational database and create a summary table by publication year.

## Repository Contents
- `task1_d.json` / `task1_valid.json` – original and fixed JSON files  
- `convert.py` – optional script to fix the JSON  
- `create_books.sql` – SQL to create `books` table  
- `create_summary.sql` – SQL to create `books_summary` table  
- `insert.py` – Python script to load data into the database  

## Tables

**books** – raw book data from JSON  
**books_summary** – aggregated data by publication year:  
- `publication_year`  
- `book_count`  
- `average_price` (in USD, rounded to cents, €1 = $1.2)  

## Usage

1. Load data into `books` table:

```bash
python insert.py
