SELECT categories.name, COUNT(*) as num FROM book_categories
INNER JOIN books
ON book_categories.book_id = books.id 
INNER JOIN categories
ON book_categories.category_id = categories.id
GROUP BY categories.name
ORDER BY num DESC, name ASC
LIMIT 3;
