#using subquery
SELECT DISTINCT num AS ConsecutiveNums
FROM Logs l1
WHERE 
    num = (
        SELECT l2.num
        FROM Logs l2
        WHERE l2.id = l1.id + 1
    )
    AND num = (
        SELECT l3.num
        FROM Logs l3
        WHERE l3.id = l1.id + 2
    );
