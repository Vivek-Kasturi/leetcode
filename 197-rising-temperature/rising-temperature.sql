# Write your MySQL query statement below
select w1.id from Weather w1
where w1.temperature >(
    select w2.temperature 
    from weather w2
    where w2.recordDate = date_sub(w1.recordDate, interval 1 day)
)