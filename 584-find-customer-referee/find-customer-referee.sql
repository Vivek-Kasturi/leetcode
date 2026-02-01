# Write your MySQL query statement below
#self join
SELECT c1.name
FROM Customer c1
LEFT JOIN Customer c2
    ON c1.referee_id = c2.id
WHERE c1.referee_id <> 2 OR c1.referee_id IS NULL;