# Write your MySQL query statement below
SELECT id, movie,description, rating
FROM Cinema 
where id%2=1
and lower(description)<>'boring'
and id in(select id from Cinema)
order by rating desc