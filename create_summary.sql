CREATE TABLE books_summary AS
SELECT
    year AS publication_year,
    COUNT(*) AS book_count,
    ROUND(
        AVG(
            CASE
                WHEN price LIKE '$%' THEN CAST(SUBSTRING(price FROM 2) AS NUMERIC)
                WHEN price LIKE '€%' THEN CAST(SUBSTRING(price FROM 2) AS NUMERIC) * 1.2
            END
        ), 2
    ) AS average_price
FROM books
GROUP BY year
ORDER BY year;