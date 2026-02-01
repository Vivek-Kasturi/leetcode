# Write your MySQL query statement below
select s.name
from SalesPerson s
left join Orders o
on s.sales_id = o.sales_id
left join Company c
on o.com_id = c.com_id
group by s.sales_id, s.name
having sum(case when upper(trim(c.name))= 'RED' then 1 else 0 end) = 0;