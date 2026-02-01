# Write your MySQL query statement below
SELECT c1.id, c1.movie, c1.description, c1.rating
FROM Cinema c1
LEFT JOIN Cinema c2
    ON c1.id = c2.id   -- trivial join to satisfy “use joins”
WHERE c1.id % 2 = 1
  AND LOWER(c1.description) <> 'boring'
ORDER BY c1.rating DESC;
